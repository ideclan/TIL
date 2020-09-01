## Courses

### Crawling with Python

- [파이썬입문과 크롤링기초 부트캠프](https://www.inflearn.com/course/Python-crawling-basic), 인프런, 2019
- [업무 자동화를 위한 파이썬 pyautogui, beautifulsoup 크롤링 기초](https://www.inflearn.com/course/%EC%97%85%EB%AC%B4%EC%9E%90%EB%8F%99%ED%99%94-%ED%8C%8C%EC%9D%B4%EC%8D%AC-pyautogui-%ED%81%AC%EB%A1%A4%EB%A7%81%EA%B8%B0%EC%B4%88#), 인프런, 2019
- [현존 최강 크롤링 기술: Scrapy와 Selenium 정복](https://www.inflearn.com/course/Crawling-Scrapy-Selenium#), 인프런, 2019

## 네이버(Naver) 월/일/주간/주말 별 연극 크롤링

> [TEAMLAB Blog 네이버 연극 크롤링 포스팅 by Jiheon-Lee](https://teamlab.github.io/jekyllDecent/blog/crawling%20with%20python/Selenium으로-네이버-연극-데이터-크롤링하기-with-Python)

![Naver_theater](https://user-images.githubusercontent.com/48443734/72893751-32196780-3d5d-11ea-9ec3-6b5fa24a3409.PNG)

- **Crawling with python Code**

  월/일, 주간, 주말 별 연극 정보 + 연극 이미지

```python
from urllib.parse import quote_plus    # 한글 텍스트를 퍼센트 인코딩으로 변환
from selenium import webdriver    # 라이브러리에서 사용하는 모듈만 호출
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   # 해당 태그를 기다림
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException    # 태그가 없는 예외 처리
import time
import pandas as pd

_input = input('''-월--일, -월, 이번주, 이번주말 중 선택하여 입력해주세요.
                                 (-은 숫자 입력, 이번년도만 가능) : ''')
user_input = quote_plus(_input)

url = f'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query={user_input}%20%EC%97%B0%EA%B7%B9%20%EA%B3%B5%EC%97%B0'
chromedriver = 'C:/Users/LeeJiheon/Desktop/가천대학교/TEAMLAB/2019_winter_study/2주차/crawling/chromedriver'

options = webdriver.ChromeOptions()
options.add_argument('headless')    # 웹 브라우저를 띄우지 않는 headlss chrome 옵션 적용
options.add_argument('disable-gpu')    # GPU 사용 안함
options.add_argument('lang=ko_KR')    # 언어 설정
driver = webdriver.Chrome(chromedriver, options=options)

driver.get(url)

try:    # 정상 처리
    element = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'list_title'))
    )    # 해당 태그 존재 여부를 확인하기까지 3초 기다림
    theater_list = []
    pageNum = int(driver.find_element_by_class_name('_totalCount').text)
    count = 0

    for i in range(1, pageNum):
        theater_data = driver.find_elements_by_class_name('list_title')
        img_data = driver.find_elements_by_class_name('list_thumb')

        for k in theater_data:
            theater_list.append(k.text.split('\n'))

        for j in img_data:
            count += 1
            j.screenshot(f'img/{count}.png')

        driver.find_element_by_xpath("//a[@class='btn_page_next _btnNext on']").click()
        time.sleep(2)

except TimeoutException:    # 예외 처리
    print('해당 페이지에 연극 정보가 존재하지 않습니다.')

finally:    # 정상, 예외 둘 중 하나여도 반드시 실행
    driver.quit()

for i in range(len(theater_list)):
    theater_list[i].append(theater_list[i][1].split('~')[0])
    theater_list[i].append(theater_list[i][1].split('~')[1])

for i in range(len(theater_list)):
    if theater_list[i][4] == '오픈런':
        theater_list[i][4] = '50.01.01.'
        theater_list[i].append('True')
    else:
        theater_list[i].append('False')

theater_df = pd.DataFrame(theater_list,
                          columns=['연극명', '기간', '장소', '개막일', '폐막일', '오픈런'])
theater_df.index = theater_df.index + 1    # 인덱스 초기값 1로 변경
theater_df['개막일'] = pd.to_datetime(theater_df['개막일'], format='%y.%m.%d.')
theater_df['폐막일'] = pd.to_datetime(theater_df['폐막일'], format='%y.%m.%d.')
theater_df.to_csv(f'theater_{_input}_df.csv', mode='w', encoding='utf-8-sig',
                   header=True, index=True)

print('웹 크롤링이 완료되었습니다.')
```

<br>

- **Theater DataFrame**<br>
  ![Theater DataFrame](https://user-images.githubusercontent.com/48443734/72877924-48afc680-3d3d-11ea-8e88-828df67bf9a2.png)

<br>

- **Theater CSV**<br>
  ![Theater CSV](https://user-images.githubusercontent.com/48443734/72878495-6598c980-3d3e-11ea-8628-0617b17d7467.PNG)

<br>

- **Theater IMG**<br>
  ![Theater IMG](https://user-images.githubusercontent.com/48443734/73162391-074e5b00-4131-11ea-9efa-cd26b27ab940.PNG)

<br>

최저가 연극 관람 티켓 구매 정보 크롤링

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

theater_df = pd.read_csv('theater_df.csv')

chromedriver = 'C:/Users/LeeJiheon/Desktop/가천대학교/TEAMLAB/2019_winter_study/2주차/crawling/chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get('https://shopping.naver.com')

search_word = theater_df['연극명'].values.tolist()

shop_list = []
for i in search_word:
    search_input = driver.find_element_by_xpath('//*[@id="autocompleteWrapper"]/input[1]')
    search_input.clear()
    search_input.send_keys(i)
    search_click = driver.find_element_by_xpath('//*[@id="autocompleteWrapper"]/a[2]')
    search_click.send_keys(Keys.RETURN)
    elem = driver.find_element_by_xpath('//*[@id="_search_list"]/div[1]/ul/li[1]/div[2]/div/a')
    purchase_name = elem.text
    purchase_link = elem.get_attribute('href')
    elem = driver.find_element_by_css_selector('#_search_list > div.search_list.basis > ul > li:nth-child(1) > div.info > span.price > em > span.num._price_reload')
    purchase_price = elem.text
    shop_list.append([purchase_name, purchase_price, purchase_link])
    time.sleep(2)

driver.quit()

shop_df = pd.DataFrame(shop_list,
                       columns=['Title', 'Price', 'link'])
shop_df.to_csv('shop_df.csv', mode='w', encoding='utf-8-sig',
               header=True, index=True)

print('웹 크롤링이 완료되었습니다.')
```

<br>

- **Shop DataFrame**<br>
  ![Theater DataFrame](https://user-images.githubusercontent.com/48443734/73162389-061d2e00-4131-11ea-8cfc-e945bce21f35.png)

<br>

User의 최저가 연극 티켓 정보 요청 크롤링

```python
from urllib.parse import quote_plus    # 한글 텍스트를 퍼센트 인코딩으로 변환
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   # 해당 태그를 기다림
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException    # 태그가 없는 예외 처리
import pandas as pd

user_input = quote_plus(input('최저가 연극 관람 티켓을 찾을 검색어를 입력해주세요 : '))
url = f'https://search.shopping.naver.com/search/all.nhn?query={user_input}&cat_id=&frm=NVSHATC'
chromedriver = 'C:/Users/LeeJiheon/Desktop/가천대학교/TEAMLAB/2019_winter_study/2주차/crawling/chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get(url)

try:    # 정상 처리
    element = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, '_itemSection'))
    )    # 해당 태그 존재 여부를 확인하기까지 3초 기다림
    shop_list = []
    elem = driver.find_element_by_xpath('//*[@id="_search_list"]/div[1]/ul/li[1]/div[2]/div/a')
    purchase_name = elem.text
    purchase_link = elem.get_attribute('href')
    elem = driver.find_element_by_css_selector('#_search_list > div.search_list.basis > ul > li:nth-child(1) > div.info > span.price > em > span.num._price_reload')
    purchase_price = elem.text
    shop_list.append([purchase_name, purchase_price, purchase_link])

except TimeoutException:    # 예외 처리
    print('해당 페이지에 최저가 연극 관람 정보가 존재하지 않습니다.')

finally:    # 정상, 예외 둘 중 하나여도 반드시 실행
    driver.quit()

shop_df = pd.DataFrame(shop_list,
                       columns=['Title', 'Price', 'link'])
shop_df.to_csv('req_shop_df.csv', mode='a', encoding='utf-8-sig',
               header=True, index=True)

print('웹 크롤링이 완료되었습니다.')
```

<br>

Theater_Detail_Info 크롤링

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

theater_df = pd.read_csv('theater_df.csv')
search_word = theater_df['연극명'].values.tolist()

chromedriver = '/home/leejiheon/workspace/crawling/chromedriver'
driver = webdriver.Chrome(chromedriver)

driver.get('https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EA%B7%B9%EC%A0%81%EC%9D%B8%ED%95%98%EB%A3%BB%EB%B0%A4')

detail_list = []
for i in search_word:
    search_input = driver.find_element_by_xpath('//*[@id="nx_query"]')
    search_input.clear()
    search_input.send_keys(i)
    search_click = driver.find_element_by_xpath('//*[@id="nx_search_form"]/fieldset/button')
    search_click.send_keys(Keys.RETURN)
    elem = driver.find_element_by_class_name('item_list')
    info = elem.text
    info_list = info.strip().split('\n')
    age = info_list[2]
    time = info_list[4]
    discription = info_list[-1]
    detail_list.append([i, age, time, discription])

driver.quit()

detail_df = pd.DataFrame(detail_list,
                         columns=['연극명', '관람등급', '공연시간', '내용'])
detail_df.to_csv('detail_df.csv', mode='w', encoding='utf-8-sig', header=True, index=True)

print('웹 크롤링이 완료되었습니다.')
```

<br>

- **Theater_Detail DataFrame**<br>
  ![Theater_Detail DataFrame](https://user-images.githubusercontent.com/48443734/73242868-75eeef80-41e9-11ea-8d27-9c4ef4117880.png)

<br>

## 멜론(Melon) 실시간 인기차트 TOP 100 크롤링 (학습용)

![Melon_top100](https://user-images.githubusercontent.com/48443734/72893752-32196780-3d5d-11ea-861d-5ab671010623.PNG)

- **Crawling with python Code**<br>

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd


hdr = {'User-Agent': 'Mozilla/5.0'}
url = 'https://www.melon.com/chart/index.htm'
req = requests.get(url, headers=hdr)
soup = BeautifulSoup(req.content, 'html.parser')
lst_data = soup.select('.lst50, .lst100')

melon_lst = []
for i in lst_data:
    temp = []
    temp.append(i.select_one('.rank').text)
    temp.append(i.select_one('.rank01').a.text)
    temp.append(i.select_one('.rank02').a.text)
    temp.append(i.select_one('.rank03').a.text)
    melon_lst.append(temp)

melon_df = pd.DataFrame(melon_lst,
                        columns=['순위', '노래명', '아티스트', '앨범명'])
melon_df.to_csv('melon_100.csv', mode='w', encoding='utf-8-sig',
                header=True, index=False)
```

<br>

- **Melon DataFrame**<br>
  ![Melon_DataFrame](https://user-images.githubusercontent.com/48443734/72587362-58439f80-3938-11ea-8ee7-644525c76563.png)

<br>

- **Melon CSV**<br>
  ![Melon CSV](https://user-images.githubusercontent.com/48443734/72587352-4bbf4700-3938-11ea-9a58-0019fd5e83da.PNG)
