### Travis CI ?

- Github 에서 진행되는 프로젝트를 위한 지속적인 통합(CI) 위한 도구
- Travis CI 사용 시 테스트, 빌드, 배포를 자동화
- Ruby, JAVA, Node.js, Python, PHP, Go 지원

### Travis Process

![_2020-09-10__11 45 38](https://user-images.githubusercontent.com/48443734/106099259-b9be6100-617d-11eb-862c-ad2281451622.png)


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

![_2020-09-08__10 11 36](https://user-images.githubusercontent.com/48443734/106099305-cba00400-617d-11eb-8ca4-052b7fcf8183.png)

- 테스트 코드가 없거나 실패 했을 때 다음과 같이 빨간색의 Fail Status Image 를 확인 할 수 있습니다.

### Travis Status Image

![_2020-09-08__10 10 42](https://user-images.githubusercontent.com/48443734/106099356-e1152e00-617d-11eb-8fe1-d4bc39eb371a.png)

- Travis CI 홈페이지에서도 빌드, 테스트 상태를 확인 할 수도 있지만 다음과 같이 Status Image 를
GitHub [README.md](http://readme.md) 에 삽입이 가능합니다.

    ![_2020-09-08__10 14 02](https://user-images.githubusercontent.com/48443734/106099363-e3778800-617d-11eb-83c6-fccedb5c27fa.png)

- Travis CI 홈페이지에서 Status Image 를 클릭

### Travis 적용 (Success)

![_2020-09-09__8 57 35](https://user-images.githubusercontent.com/48443734/106099413-f8ecb200-617d-11eb-8d62-212cddd87a95.png)

![_2020-09-09__8 58 48](https://user-images.githubusercontent.com/48443734/106099417-fab67580-617d-11eb-8ed8-2427ed203047.png)

- 테스트 성공 했을 때 다음과 같이 초록색의 Success Status Image 를 확인 할 수 있습니다.
- 또한 빌드와 테스트 진행 내용들을 자세하게 확인이 가능합니다.