### Travis CI ?

- Github 에서 진행되는 프로젝트를 위한 지속적인 통합(CI) 위한 도구
- Travis CI 사용 시 테스트, 빌드, 배포를 자동화
- Ruby, JAVA, Node.js, Python, PHP, Go 지원

### Travis Process

![Travis Process](https://user-images.githubusercontent.com/48443734/93674990-c1db0580-fae6-11ea-8ea2-ba344e8f05b8.png)

- 여러 개발자들이 GitHub 에 Push 할 때 Travis CI 는 이것을 Event 가 발생했다고 감지하여 작동하게 됩니다. (Event 에 정의가 없다면 기본 값은 Push 이며 트리거 변경이 가능합니다)
- Travis CI 는 GitHub Repository 를 Clone 하여 작성했던 .travis.yml 로 빌드, 테스트를 진행하고 성공 실패 여부를 이메일로 돌려줍니다.

### Travis 사용법

- Travis CI 홈페이지에서 GitHub 계정으로 회원가입
- travis 와 GitHub Repository 를 연동
- 프로젝트 최상단 Repository 에 .travis.yml 작성

### .travis.yml 예시

```yaml
language: node_js
node_js: 12
before_install:
	- cd backend/
	- npm install
cache: npm
script:
	- npm run test
```

- 언어는 node.js , 버전은 12 로 지정합니다.
- 빌드 전 종속성을 설치합니다.
  (제가 진행중인 프로젝트의 구조는 최상위 폴더에서 frontend, backend 로 구성되어 이동이 필요했습니다)
- cache 를 적용합니다. (Travis CI 가이드 참고)
- 작성한 테스트 코드를 실행할 스크립트를 작성합니다.

### Travis 적용 (Fail)

![Failed Example](https://user-images.githubusercontent.com/48443734/93675802-01a1ed00-fae7-11ea-88cd-ab1c206797ed.png)

- 테스트 코드가 없거나 실패 했을 때 다음과 같이 빨간색의 Fail Status Image 를 확인 할 수 있습니다.

### Travis Status Image

![Travis Status Image](https://user-images.githubusercontent.com/48443734/93676340-2c8c4100-fae7-11ea-91b5-5258ecdb2a12.png)

- Travis CI 홈페이지에서도 빌드, 테스트 상태를 확인 할 수도 있지만 다음과 같이 Status Image 를 GitHub README.md 에 삽입이 가능합니다.

![Travis CI 홈페이지에서 Status Image 클릭](https://user-images.githubusercontent.com/48443734/93676525-4d549680-fae7-11ea-9192-1e50745e6f1c.png)

- Travis CI 홈페이지에서 Status Image 를 클릭

### Travis 적용 (Success)

![Successed Example](https://user-images.githubusercontent.com/48443734/93676640-7aa14480-fae7-11ea-9bfb-177b3f46250b.png)
![Successed Example Detail](https://user-images.githubusercontent.com/48443734/93676712-7ffe8f00-fae7-11ea-99c7-2e2785f00584.png)
![Terminal](https://user-images.githubusercontent.com/48443734/93676741-8260e900-fae7-11ea-8be7-5c6617f19c9d.png)

- 테스트 성공 했을 때 다음과 같이 초록색의 Success Status Image 를 확인 할 수 있습니다.
- 또한 빌드와 테스트 진행 내용들을 자세하게 확인이 가능합니다.
- 터미널 환경에서 실행했던 결과와 동일한 결과를 확인 할 수 있습니다.
