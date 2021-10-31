# VS Code Extension

- Visual Studio Code의 확장 기능 (=플러그인)
- VS Code 의 Marketplace 에서 확인
- 다양한 확장 기능으로 좀 더 좋은 개발환경 구축

## VS Code Marketplace

- 수많은 Extension 포함
- Extension 검색 가능
- 원하는 기능 Install 하여 사용

### Material Theme

- 테마를 적용하여 가독성 향상
- 여러가지 테마 색상이 있으며 취향에 따라 선택

### Material Icon Theme

- 파일마다 아이콘을 부여하여 어떠한 확장자 파일인지 명확하게 확인이 가능

### Prettier - Code formatter

- 저장 시 정해진 규칙에 따라 강제적으로 정렬
- JS, Vue, CSS, HTML, Mark down, YAML, JSON 등 지원
- 사용자가 규칙을 설정할 수 있음
  - 적용하기 전 필요한 설정 : VS Code 실행 > Ctrl (Command) + Shift + P > user 검색하여 Open User Settings > Format On Save를 검색하여 체크
  - Open User Settings 에서 prettier를 검색하여 들여쓰기, 작은따옴표 등 설정 가능

### Bracket Pair Colorizer 2

- 하나의 괄호끼리 다른 색깔을 부여
- 2는 정확성과 속도 향상된 버전 (권장)

### Indent-rainbow

- 들여쓰기 마다 색깔 부여

### Auto Rename Tag

- HTML Tag 를 변경 시 열거나 닫는 Tag 도 자동으로 변경

### REST Client

- REST api 호출에 대한 결과 response 를 표시
- .http 형식으로 파일을 생성하여 사용
- api 호출 하나씩 ### 으로 구분
  - .http 확장자 파일에서 GET 또는 POST 요청 방식을 적으면 상단에 Send Request 버튼이 생기며 클릭 시 오른쪽에 response 결과를 확인 가능
  - 하단에 Content-Type: ex) application.json 등으로 파일 형식 지정 가능

### CSS Peek

- Ctrl + Shift + F12 : css 파일을 불러와 바로 편집이 가능
- F12 : 선택한 id 나 class가 있는 CSS 파일로 이동
- Ctrl + hover : 선택한 id 나 class 의 style code를 보여줌

### HTML CSS Support

- CSS 파일에서 정의한 class 명을 HTML 파일에서 출력

### Live Sass Compiler

- SASS는 CSS의 단점을 보완한 확장형 (확장자=.scss)
- 하지만 브라우저에 사용하기 위해선 컴파일 작업이 필요
- 이때 쉽게 컴파일을 하도록 도와주는 기능 (오른쪽 하단 눈 표시 버튼 클릭 시 컴파일 진행)

### Live Server

- 파일을 수정하여 저장 시 새로고침 없이 수정사항을 바로 반영한 결과 확인 가능\

### Emmet

- Emmet 은 내장되어 있어 확장 install 필요 X
  - html 파일에서 ! 입력시 HTML 기본 템플릿 제공
  - <> 입력 없이 태그 이름만 입력해도 열고 닫는 태그를 생성
  - ul>li\*4 입력 시 ul 안에 li 태그를 4개 생성 (생성이 필요한 개수가 많을 시 유용)
