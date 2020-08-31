Courses
-------
### Bootstrap Bootcamp
- [Bootstrap 4 & 3 Framework Tutorial](https://www.inflearn.com/course/bootstrap-2#), 인프런, 2018
- [나만의 포트폴리오 웹페이지 만들기](https://www.inflearn.com/course/%ED%8F%AC%ED%8A%B8%ED%8F%B4%EB%A6%AC%EC%98%A4#), 인프런, 2019

Bootstrap 정리
-------
### HTML5 Framework
기본 HTML에서 제공하지 않는 UI를 직접 만들어 쓸 수 있지만 하나하나 직접 다 만들어야 하기 때문에 꽤 힘든 작업이 될 수 밖에 없다. 이에 HTML5, CSS3를 이용한 웹 프레임워크들이 등장하였고 현재 많은 프레임워크들이 제공되고 있다.<br>

### Bootstrap Framework
트위터에서 시작된 jQuery 기반의 HTML5 Web Framework로 다양한 UI 요소들을 제공하고 있다. 트위터에서 사용하던 각종 레이아웃, 버튼, 입력 요소 등 UI 요소들을 누구나 사용할 수 있도록 만들어진 오픈 소스 프레임워크이다. 부트스트랩을 이용하게 되면 디자이너 없이도 Front 개발이 가능하고 소스가 공개되어 있어 기본 UI 요소외에 다른 UI 요소들도 만들어 사용할 수 있다.<br>

### Bootstrap 특징
- 글자, 인용문 등 자잘한 것 뿐만 아니라 메뉴, 버튼, 탭 등 웹 페이지에서 많이 사용하는 UI요소들을 제공하고 있다.
- 반응형 웹 개발을 지원하고 있어 PC, 모바일 동시 지원하는 웹 애플리케이션 개발이 가능하다.
- 라이선스가 자유롭기 때문에 수정해서 사용해도 되고 배포 및 판매도 가능하다.
- 현재 최신 버전은 4이며 3도 있다. Bootstrap 4는 인터넷 익스플로러 10부터 지원하고 있기 때문에 하위 버전까지 지원한다면 Bootstrap 3을 사용해야 한다.<br>

### Bootstrap CDN 적용
- Bootstrap 4.1
```html
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js"></script>
```
Bootstrap 4.1의 HTML Template은 다음과 같다.
```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js"></script>
<title>Bootstrap 4</title>
</head>
<body>
	<div class="container">

	</div>
</body>
</html>
```

<br>

- Bootstrap 3.3.7
```html
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
```
Bootstrap 3.3.7의 HTML Template은 다음과 같다.
```html
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
<title>Bootstrap 3</title>
</head>
<body>
	<div class="container">

	</div>
</body>
</html>
```

<br>

### 그리드
CSS를 통해 가로 길이를 정해주면 그 가로 길이 만큼 공간을 차지하게 된다. Bootstrap은 가로 한 줄을 12등분하여 요소 하나의 비율을 정해 배치할 수 있도록 제공하고 있다.<br>
![Grid](https://user-images.githubusercontent.com/48443734/73048429-753e1c80-3ebc-11ea-863e-f3294e84e524.PNG)

**기본 코드**
```html
<div class="row">
  <div class="col"></div>
  <div class="col"></div>
  <div class="col"></div>
</div>
```
**양식**
<pre>col-scale-{숫자} : 12칸 중 몇 칸을 차지할 것인지 설정
col-{숫자} : 세로 방향으로 배치되지 않는다.(BS3 X)
col-sm-{숫자} : 576px 이하면 세로로 배치된다.
col-md-{숫자} : 768px 이하면 세로로 배치된다.
col-lg-{숫자} : 992px 이하면 세로로 배치된다.
col-xl-{숫자} : 1200px 이하면 세로로 배치된다.</pre><br>

### 문자열 클래스
HTML에서 제공하고 있는 문자열 관련 CSS에 더 세밀하게 꾸밀 수 있도록 다양한 클래스를 제공하고 있다.

Display CSS Class는 해당 태그의 설정되어 있는 글자크기를 무시하고 새로 설정할 수 있다. (문자열을 표시하는 태그는 모두 적용 가능)
```html
<h1 class="display-1">Display 1</h1>
<h1 class="display-2">Display 2</h1>
<h1 class="display-3">Display 3</h1>
<h1 class="display-4">Display 4</h1>
```

<br>

**문자열 관련 태그들**
<pre>small : 설정된 크기보다 조금 작은 크기로 표시
mark : 배경색을 달리하여 강조
abbr : 약어
blockquote : 항목 표시
code : 프로그램 코드 표시
kbd : 키보드 단축키
pre : 태그내의 문자열을 작성한 모양 그대로 출력</pre>

**문자열 관련 CSS Class**
<pre>font-weight-bold : 문자열을 굵게(BS4)
font-italic : 문자열을 기울어지게(BS4)
font-weight-light : 문자열을 가늘게
font-weight-normal : 기본 굵기의 문자열
text-left : 좌측 정렬
text-center : 중앙 정렬
text-right : 우측 정렬
text-{ sm, md, lg, xl }-left(center, right) : 기본은 좌측, 중앙, 우측에 정렬 되지만
브라우저의 가로 길이에 따라 좌측 정렬로 변경(BS4)

text-justify : 영역안에서 문자열을 좌우에 맞춤
text-monospace : 모노 스페이스 글자로 표시(BS4)
text-nowrap : 문자열이 영역을 벗어나더라도 개행되지 않음
text-lowercase : 문자열을 소문자로 표시
text-uppercase : 문자열을 대문자로 표시
text-capitalize : 첫 글자가 소문자일 경우 대무낮로 표시
list-unstyled : ul이나 ol 태그를 사용할 때 스타일을 제거
list-inline : ul이나 ol 태그의 항목을 가로방향으로 배치

dl-horizontal : dl 태그 내부 항목들을 가로 방향으로 배치(BS3)
pre-scrollable : pre 태그에서 스크롤이 되지 않는 상황에서도 스크롤바 영역을 표시</pre>