## create react app

```bash
$ npx create-react-app my-app

# 또는

$ npm install -g create-react-app
$ npm create-react-app my-app
```

### npm과 npx의 차이

- `npm` : Package Manager (관리)
- `npx` : Package Runner (실행)

`$ npm install -g`를 통해 한 번만 설치하면 되는 편리함이 있지만, 변경사항이 자주 일어나는 모듈인 경우 글로벌로 설치한 모듈을 매번 업데이트를 해주어야 한다. 이러한 문제점들을 해결하기 위해 `npm 5.2` 버전부터는 `npx`라는 패키지 실행 도구를 제공하기 시작했다.

`npx`는 모듈을 로컬에 저장하지 않고, 매번 최신 버전의 파일만을 임시로 불러와 실행 시킨 후에, 다시 그 파일을 제거하는 방식이다.

## react app 프로젝트 구조

`public/index.html` 내에 `<div id="root"></div>` 태그안에서 컴포넌트를 사용하고 있는 것을 볼 수 있다.

이는 `src/index.js`에서 `ReactDOM.render()`의 인자로

- `<App />` : 사용자가 정의한 태그인 컴포넌트, `./App` 호출
- `document.getElementById("root")` : id가 root인 태그

```javascript
// src/index.js

import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import reportWebVitals from "./reportWebVitals";

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("root")
);

reportWebVitals();
```

`App` 함수형 컴포넌트와 클래스형 컴포넌트 방식

```javascript
// App.js

// function type
import React from "react";
import "./App.css";

function App() {
  return <div className="App"></div>;
}

// class type
import React, { Component } from "react";
import "./App.css";

class App extends Component {
  render() {
    return <div className="App"></div>;
  }
}
```

전역 스타일과 `App` 컴포넌트에 관련된 스타일

`index.css`는 모든 컴포넌트에 적용하기 위해 정의하며,  
`App.css`는 해당 컴포넌트에서만 적용할 스타일을 정의한다.

```javascript
// index.js

import "./index.css";

// App.js

import "./App.css";
```

## react app 배포

개발 환경에서 실행하여 개발을 진행한 후, 배포하는 과정에서는 불필요한 리소스 제거와 브라우저에 적합한 코드로 변경이 필요하다. 이를 `build`라고 하여 아래와 같이 진행한다.

```bash
$ npm run build
```

프로젝트 루트 경로 내에 `build/`가 생성된다.

빌드된 파일로 서버 실행은

```bash
$ npx serve -s build

# 또는

$ npm install -g serve
$ serve -s build
```

> 크롬 개발자 도구 -> Network에서 캐시 비우기 및 강력 새로고침한 결과  
> 개발 환경에서의 실행한 리소스 용량 `2.2 MB`에서 빌드 후 실행한 리소스 용량 `125 KB`로 많이 줄어든 것을 확인할 수 있다.

## Component 만들기

`header`, `nav`, `article` 태그 부분들을 컴포넌트로 만들어 사용한다.

```html
<html>
  <body>
    <header>
      <h1>WEB</h1>
      world wide web!
    </header>

    <nav>
      <ul>
        <li><a href="1.html">HTML</a></li>
        <li><a href="2.html">CSS</a></li>
        <li><a href="3.html">JavaScript</a></li>
      </ul>
    </nav>

    <article>
      <h2>HTMl</h2>
      HTML is HyperText Markup Language.
    </article>
  </body>
</html>
```

컴포넌트의 사용 방법은 사용자가 정의한 이름인 태그로  
아래 예제에서의 `Subject` 컴포넌트는 `<Subject></Subject>`로 사용한다.

```javascript
// App.js

import React, { Component } from "react";
import "./App.css";

class Subject extends Component {
  render() {
    return (
      <header>
        <h1>WEB</h1>
        world wide web!
      </header>
    );
  }
}

class TOC extends Component {
  render() {
    return (
      <nav>
        <ul>
          <li>
            <a href="1.html">HTML</a>
          </li>
          <li>
            <a href="2.html">CSS</a>
          </li>
          <li>
            <a href="3.html">JavaScript</a>
          </li>
        </ul>
      </nav>
    );
  }
}

class Content extends Component {
  render() {
    return (
      <article>
        <h2>HTML</h2>
        HTML is HyperText Markup Language.
      </article>
    );
  }
}

class App extends Component {
  render() {
    return (
      <div className="App">
        <Subject></Subject>
        <TOC></TOC>
        <Content></Content>
      </div>
    );
  }
}

export default App;
```

## Props

`props`는 properties의 줄임말로, 어떠한 값을 컴포넌트에게 전달해줘야 할 때 사용한다.

`{this.props.속성명}`로 사용자 정의 태그의 속성(attribute) 값을 전달받아 사용할 수 있다.

```javascript
import React, { Component } from "react";
import "./App.css";

class Subject extends Component {
  render() {
    return (
      <header>
        <h1>{this.props.title}</h1>
        {this.props.sub}
      </header>
    );
  }
}

class Content extends Component {
  render() {
    return (
      <article>
        <h2>{this.props.title}</h2>
        {this.props.desc}
      </article>
    );
  }
}

class App extends Component {
  render() {
    return (
      <div className="App">
        <Subject title="WEB" sub="world wide web!"></Subject>
        <Content
          title="HTML"
          desc="HTML is HyperText Markup Language."
        ></Content>
      </div>
    );
  }
}

export default App;
```

## React Developer Tools

- [Chrome Extension - React Developer Tools](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=ko)

## Component 파일로 분리하기

1. `src/` 내에 `components/`를 생성한다.
2. 앞에서의 `Subject` 컴포넌트를 파일로 분리한다고 가정했을 때, `components/Subject.js` 파일을 생성한다.

```javascript
import React, { Component } from "react";

class Subject extends Component {
  render() {
    return (
      <header>
        <h1>{this.props.title}</h1>
        {this.props.sub}
      </header>
    );
  }
}

export default Subject;
```

3. `App.js`에서 파일로 분리한 컴포넌트를 불러온다.

```javascript
import Subject from "./components/Subject";
```

## State

컴포넌트가 실행될 때 `constructor()`를 통해 컴포넌트 초기화를 진행한다. 그리고 state 값을 초기화한다. 이때, `render()`보다 먼저 실행이 되어야 한다.

```javascript
class App extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }
  render() {}
}
```

앞에 예제에서 `Subject`, `Content` 컴포넌트로 `props`를 통해 전달할 값들을 state로 관리한다.

`this.state`를 통해 state 값에 접근이 가능하다.

```javascript
class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      subject: {
        title: "WEB",
        sub: "world wide web!",
      },
      content: {
        title: "HTML",
        desc: "HTML is HyperText Markup Language.",
      },
    };
  }
  render() {
    return (
      <div className="App">
        <Subject
          title={this.state.subject.title}
          sub={this.state.subject.sub}
        ></Subject>
        <TOC></TOC>
        <Content
          title={this.state.content.title}
          desc={this.state.content.desc}
        ></Content>
      </div>
    );
  }
}
```
