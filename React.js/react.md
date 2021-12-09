- [create react app](#create-react-app)
  - [npm과 npx의 차이](#npm과-npx의-차이)
- [react app 프로젝트 구조](#react-app-프로젝트-구조)
- [react app 배포](#react-app-배포)
- [Component 만들기](#component-만들기)
- [Props](#props)
- [React Developer Tools](#react-developer-tools)
- [Component 파일로 분리하기](#component-파일로-분리하기)
- [State](#state)
  - [Key](#key)
- [Event, State, Props and render](#event-state-props-and-render)
  - [Event 설치](#event-설치)
- [Event에서 State 변경하기](#event에서-state-변경하기)
  - [Event bind 함수](#event-bind-함수)
  - [Event setState 함수](#event-setstate-함수)
- [Component Event 만들기](#component-event-만들기)
- [Props VS State](#props-vs-state)
- [CRUD](#crud)
  - [Create 구현](#create-구현)
    - [mode 변경 기능](#mode-변경-기능)
    - [mode 전환 기능](#mode-전환-기능)
    - [form onSubmit Event](#form-onsubmit-event)
    - [Contents 변경](#contents-변경)
    - [shouldComponentUpdate](#shouldcomponentupdate)
    - [Immutable](#immutable)
  - [Update 구현](#update-구현)
    - [form](#form)

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
2. 앞에 예제에서 `Subject` 컴포넌트를 파일로 분리한다고 가정했을 때, `components/Subject.js` 파일을 생성한다.

```javascript
// components/Subject.js

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
// App.js

import Subject from "./components/Subject";
```

## State

컴포넌트가 실행될 때 `constructor()`를 통해 컴포넌트 초기화를 진행한다. 그리고 state 값을 초기화한다. 이때, `render()`보다 먼저 실행이 되어야 한다.

```javascript
// App.js

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }
  render() {}
}
```

앞에 예제에서 `Subject` 컴포넌트로 `props`를 통해 전달할 값들을 state로 관리한다.

`this.state`를 통해 접근이 가능하다.

```javascript
// App.js

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      subject: {
        title: "WEB",
        sub: "world wide web!",
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
          title="HTML"
          desc="HTML is HyperText Markup Language."
        ></Content>
      </div>
    );
  }
}
```

### Key

`this.state`에 `contents`를 추가하여 `TOC` 컴포넌트에 `props`를 통해 `data`로 전달한다.

```javascript
// App.js

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      subject: {
        title: "WEB",
        sub: "world wide web!",
      },
      contents: [
        { id: 1, title: "HTML", desc: "HTML is for information" },
        { id: 2, title: "CSS", desc: "CSS is for design" },
        { id: 3, title: "JavaScript", desc: "JavaScript is for interactive" },
      ],
    };
  }
  render() {
    return (
      <div className="App">
        <Subject
          title={this.state.subject.title}
          sub={this.state.subject.sub}
        ></Subject>
        <TOC data={this.state.contents}></TOC>
        <Content
          title="HTML"
          desc="HTML is HyperText Markup Language."
        ></Content>
      </div>
    );
  }
}
```

전달받은 `data`로 사용할 태그와 함께 `list`를 만든 후 `{tableOfConents}`처럼 사용이 가능하다.

```javascript
// components/TOC.js

import React, { Component } from "react";

class TOC extends Component {
  render() {
    const { data } = this.props;
    const tableOfContents = data.map((content) => (
      <li>
        <a href={`/contents/${content.id}`}>{content.title}</a>
      </li>
    ));

    return (
      <nav>
        <ul>{tableOfContents}</ul>
      </nav>
    );
  }
}

export default TOC;
```

하지만 `Console`에서 다음과 같은 오류가 발생한다.

```
Warning: Each child in a list should have a unique "key" prop.
```

각 항목들은 `key`라는 `props`를 가지고 있어야 한다. 따라서 `<li key={}>`에 식별자를 추가한다.

```javascript
const tableOfContents = data.map((content) => (
  <li key={content.id}>
    <a href={`/contents/${content.id}`}>{content.title}</a>
  </li>
));
```

## Event, State, Props and render

`App` 컴포넌트의 `state`가 변경되면 `props`를 통해 해당 값을 전달하여 동적으로 표현이 가능하다.

`state`가 변경될 때, 해당 컴포넌트가 가진 `render()` 함수가 다시 호출된다. 그리고 하위 컴포넌트의 `render()` 함수 또한 모두 동일하게 다시 호출된다.

따라서 `state` 값에 따라 다르게 표현하기 위해 `render()` 함수 내에 조건문을 사용할 수 있다.

```javascript
class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      mode: "welcome",
      welcome: {
        title: "Welcome",
        desc: "Hello, React!!!",
      },
      subject: {
        title: "WEB",
        sub: "world wide web!",
      },
      contents: [
        { id: 1, title: "HTML", desc: "HTML is for information" },
        { id: 2, title: "CSS", desc: "CSS is for design" },
        { id: 3, title: "JavaScript", desc: "JavaScript is for interactive" },
      ],
    };
  }
  render() {
    let _title, _desc;
    if (this.state.mode === "welcome") {
      _title = this.state.welcome.title;
      _desc = this.state.welcome.desc;
    } else if (this.state.mode === "read") {
      _title = this.state.contents[0].title;
      _desc = this.state.contents[0].desc;
    }
    return (
      <div className="App">
        <Subject
          title={this.state.subject.title}
          sub={this.state.subject.sub}
        ></Subject>
        <TOC data={this.state.contents}></TOC>
        <Content title={_title} desc={_desc}></Content>
      </div>
    );
  }
}
```

`this.state`에 `mode`를 추가하여 해당 값에 따라 다른 `title`과 `desc`를 갖도록 한다.

### Event 설치

JavaScript에서의 Event는 `onclick=""`으로 사용하지만 React에서는 `onClick={}`으로 사용한다.

파라미터 `e`는 이벤트 객체이다.

**이벤트 객체(event object)**

특정 타입의 이벤트와 관련이 있는 객체

- 해당 타입의 이벤트에 대한 상세 정보를 저장
- 모든 이벤트 객체는 이벤트의 타입을 나타내는 `type` 프로퍼티와 이벤트의 대상을 나타내는 `target` 프로퍼티를 가진다.

```javascript
render() {
    return (
      <div className="App">
        <header>
          <h1>
            <a
              href="/"
              onClick={function (e) {
                console.log(e);
                debugger;
              }}
            >
              {this.state.subject.title}
            </a>
          </h1>
          {this.state.subject.sub}
        </header>
      </div>
    );
  }
```

> 크롬 개발자 도구를 사용할 때 코드 내에 `debugger`를 사용하면 해당 부분에서 실행을 멈추고 `Sources` 탭에서 여러 정보를 확인할 수 있다.

```javascript
<a
  href="/"
  onClick={function (e) {
    console.log(e);
    e.preventDefault();
  }}
>
  {this.state.subject.title}
</a>
```

`e.preventDefault()`를 통해 기본적인 태그의 `event`를 막을 수 있다.

## Event에서 State 변경하기

앞에 예제에서 `state`의 `mode`에 따라 다르게 보여지도록 하였으므로 `event`를 통해 해당 `state`를 변경하도록 한다.

```javascript
<a
  href="/"
  onClick={function (e) {
    e.preventDefault();
    this.state.mode = "welcome";
  }}
>
  {this.state.subject.title}
</a>
```

하지만 다음과 같은 에러가 발생한다.

```
TypeError: Cannot read property 'state' of undefined
```

이는 이벤트가 발생할 때의 호출되는 함수에서의 `this`는 컴포넌트 자기 자신을 가리키지 않는다.

따라서 다음과 같이 수정한다.

```javascript
<a
  href="/"
  onClick={function (e) {
    e.preventDefault();
    this.state.mode = "welcome";
  }.bind(this)}
>
  {this.state.subject.title}
</a>
```

`.bind(this)`를 통해 해당 함수 안에서 `this`는 컴포넌트 자기 자신을 가리키게 된다.

하지만 `state`가 변경이 되어도 작동하지 않는다. 이는 React가 `state` 변경을 알아차리지 못하기에 `this.setState()`를 사용해야 한다.

```javascript
<a
  href="/"
  onClick={function (e) {
    e.preventDefault();
    this.setState({
      mode: "welcome",
    });
  }.bind(this)}
>
  {this.state.subject.title}
</a>
```

### Event bind 함수

`render()` 내에서 `this`는 `render()`가 속해있는 컴포넌트 자기 자신을 가르킨다.

하지만 `event` 함수 내에서 `this`는 `undefined`이다.

```javascript
class App extends Component {
  render() {
    console.log("render", this);
    return (
      <a
        href="/"
        onClick={function (e) {
          console.log("event in", this);
          e.preventDefault();
        }}
      >
        {this.state.subject.title}
      </a>
    );
  }
}

// render App {props: {...}, context: {...} ...}
// event in undefined
```

따라서 `bind()`를 통해 `this`를 주입시킬 수 있다.

```javascript
function bindTest() {
  console.log(this.name);
}

const obj = { name: "Jiheon Lee" };

bindTest().bind(obj);

// Jiheon Lee
```

### Event setState 함수

컴포넌트가 생성되는 시점에서 가장 먼저 실행되는 생성자 함수 `constructor()` 내에서 `state`값을 초기화한다.

이미 컴포넌트가 생성된 이후에 동적으로 `state`를 변경할 때 아래와 같은 방식으로 변경하면 `react`는 변경을 알아채지 못한다.

```javascript
this.state.mode = "welcome";
```

화면의 변경도 이루어지지 않으며, 개발자 도구에서도 이를 알아채지 못하고 재실행해야 `state`가 변경되는 것을 볼 수 있다.

따라서 `setState()`를 사용하여 `react`에게 `state` 변경이 이루어졌음을 알려야 한다.

```javascript
this.setState({
  mode: "welcome",
});
```

## Component Event 만들기

`Subject` 컴포넌트에 `onChangePage` 이벤트를 생성한다. 해당 함수는 `props`를 통해 전달되어 `this.props.onChangePage()`로 호출이 가능하다. 따라서 `<a>` 태그 안에 `onClick` 이벤트가 발생할 때 호출하여 `state`를 변경하도록 한다.

```javascript
// App.js

class App extends Component {
  render() {
    return (
      <div className="App">
        <Subject
          title={this.state.subject.title}
          sub={this.state.subject.sub}
          onChangePage={function () {
            this.setState({
              mode: "welcome",
            });
          }.bind(this)}
        ></Subject>
      </div>
    );
  }
}
```

```javascript
// Subject.js

class Subject extends Component {
  render() {
    return (
      <header>
        <h1>
          <a
            href="/"
            onClick={function (e) {
              e.preventDefault();
              this.props.onChangePage();
            }.bind(this)}
          >
            {this.props.title}
          </a>
        </h1>
        {this.props.sub}
      </header>
    );
  }
}
```

목록을 클릭했을 때 이에 해당되는 내용으로 보여지도록 한다.

따라서 앞에 `Subject` 컴포넌트와 동일하게 `TOC` 컴포넌트에서도 `onChangePage` 이벤트를 생성한다.

```javascript
// App.js

class App extends Component {
  render() {
    return (
      <div className="App">
        <TOC
          onChangePage={function () {
            this.setState({
              mode: "read",
            });
          }.bind(this)}
          data={this.state.contents}
        ></TOC>
      </div>
    );
  }
}
```

```javascript
// TOC.js

class TOC extends Component {
  render() {
    const { data } = this.props;
    const tableOfContents = data.map((content) => (
      <li key={content.id}>
        <a
          href={`/contents/${content.id}`}
          onClick={function (e) {
            e.preventDefault();
            this.props.onChangePage();
          }.bind(this)}
        >
          {content.title}
        </a>
      </li>
    ));

    return (
      <nav>
        <ul>{tableOfContents}</ul>
      </nav>
    );
  }
}
```

선택되어 있는 목록을 알고 있어야 하기 때문에 `state`에 `selectedContentId`를 추가한다.

그리고 `mode: 'read'`인 경우 `selectedContentId`를 가진 `index`를 찾아 해당 목록의 내용을 보여주도록 한다.

```javascript
// App.js

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      mode: "read",
      selectedContentId: 2,
      welcome: {
        title: "Welcome",
        desc: "Hello, React!!!",
      },
      subject: {
        title: "WEB",
        sub: "world wide web!",
      },
      contents: [
        { id: 1, title: "HTML", desc: "HTML is for information" },
        { id: 2, title: "CSS", desc: "CSS is for design" },
        { id: 3, title: "JavaScript", desc: "JavaScript is for interactive" },
      ],
    };
  }
  render() {
    let _title, _desc;
    if (this.state.mode === "welcome") {
      _title = this.state.welcome.title;
      _desc = this.state.welcome.desc;
    } else if (this.state.mode === "read") {
      const idx = this.state.contents.findIndex(
        (content) => content.id === this.state.selectedContentId
      );

      _title = this.state.contents[idx].title;
      _desc = this.state.contents[idx].desc;
    }

    return (
      <div className="App">
        <TOC
          onChangePage={function () {
            this.setState({
              mode: "read",
            });
          }.bind(this)}
          data={this.state.contents}
        ></TOC>
        <Content title={_title} desc={_desc}></Content>
      </div>
    );
  }
}
```

다음으로 사용자가 목록을 클릭했을 때 `selectedContentId`를 변경시켜야 한다.

이는 `TOC` 컴포넌트에서 `props`로 전달받은 `onChangePage` 이벤트 함수에 클릭한 요소의 `id`를 인자로 넘겨 변경하면 된다.

방법으로는 2가지가 있다.

1. 태그안에 `data-<name>` 속성을 추가한다. 만약 `data-id`라면 이벤트 함수 내에서 `e.target.dataset.id`로 접근이 가능하다.

2. `bind()`를 사용한다. 예를 들어, `.bind(this, content.id)` 두번째 인자로 넘겼다면 이벤트 함수 내에서 매개변수를 `function (id, e)`처럼 전달받을 수 있다. 이는 매개변수 순서가 이벤트 객체보다 앞에 나와야 한다.

```javascript
// TOC.js

class TOC extends Component {
  render() {
    const { data } = this.props;
    const tableOfContents = data.map((content) => (
      <li key={content.id}>
        <a
          href={`/contents/${content.id}`}
          data-id={content.id}
          onClick={function (e) {
            e.preventDefault();
            this.props.onChangePage(e.target.dataset.id);
          }.bind(this)}
        >
          {content.title}
        </a>
      </li>
    ));

    return (
      <nav>
        <ul>{tableOfContents}</ul>
      </nav>
    );
  }
}
```

`TOC` 이벤트 함수에서 전달받은 인자 `id`는 문자열이므로, 이를 주의하고 숫자 형태로 변경하여 `selectedContentId`를 변경하도록 한다.

```javascript
// App.js

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      mode: "read",
      selectedContentId: 2,
      welcome: {
        title: "Welcome",
        desc: "Hello, React!!!",
      },
      subject: {
        title: "WEB",
        sub: "world wide web!",
      },
      contents: [
        { id: 1, title: "HTML", desc: "HTML is for information" },
        { id: 2, title: "CSS", desc: "CSS is for design" },
        { id: 3, title: "JavaScript", desc: "JavaScript is for interactive" },
      ],
    };
  }
  render() {
    let _title, _desc;
    if (this.state.mode === "welcome") {
      _title = this.state.welcome.title;
      _desc = this.state.welcome.desc;
    } else if (this.state.mode === "read") {
      const idx = this.state.contents.findIndex(
        (content) => content.id === this.state.selectedContentId
      );

      _title = this.state.contents[idx].title;
      _desc = this.state.contents[idx].desc;
    }
    return (
      <div className="App">
        <Subject
          title={this.state.subject.title}
          sub={this.state.subject.sub}
          onChangePage={function () {
            this.setState({
              mode: "welcome",
            });
          }.bind(this)}
        ></Subject>
        <TOC
          onChangePage={function (id) {
            this.setState({
              mode: "read",
              selectedContentId: Number(id),
            });
          }.bind(this)}
          data={this.state.contents}
        ></TOC>
        <Content title={_title} desc={_desc}></Content>
      </div>
    );
  }
}
```

## Props VS State

**Props**

- 읽기 전용(read-only) 이다.
- 수정할 수 없다.
- 상위 컴포넌트에서 하위 컴포넌트로 데이터를 전달하기 위해 사용된다.

**State**

- 상태 변경은 비동기식일 수 있다.
- `this.setState()`를 통해 수정할 수 있다.
- 렌더링 정보를 동적으로 바꿔나가기 위해 해당 컴포넌트에서 선언한다.

상위 컴포넌트는 하위 컴포넌트에게 `props`를 통해 값을 전달해 내부의 `state`를 바꾸기 때문에 컴포넌트 스스로 외부에서 전달되는 `props`를 변경하는 것은 금지되어 있다.

또한 하위 컴포넌트가 상위 컴포넌트를 동작시키면서 `props`를 전달하는 것이 아니라 상위 컴포넌트 안에 이벤트를 심고 그 안에서 `setState()`로 값을 변경해야 한다.

적절한 `props`와 `state` 사용으로 상위 컴포넌트와 하위 컴포넌트간에 상호 작용을 통해 동적으로 렌더링되는 SPA (Single Page Application)를 만들 수 있다.

## CRUD

- Create : form을 통해 목록과 내용을 작성한 후 저장하면 새로운 목록을 추가할 수 있도록 한다.
- Read : 기존과 추가된 목록, 내용들을 보여질 수 있도록 한다.
- Update : 기존 목록과 내용을 수정할 수 있도록 한다.
- Delete : 기존 목록과 내용을 삭제할 수 있도록 한다.

`components/` 내에 `Control.js`를 생성한다.

```javascript
// components/Control.js

import React, { Component } from "react";

class Control extends Component {
  render() {
    return (
      <ul>
        <li>
          <a href="/create">create</a>
        </li>
        <li>
          <a href="/update">update</a>
        </li>
        <li>
          <input type="button" value="delete" />
        </li>
      </ul>
    );
  }
}

export default Control;
```

```javascript
// App.js

import React, { Component } from "react";
import Control from "./components/Control";

class App extends Component {
  render() {
    return (
      <div className="App">
        <Control></Control>
      </div>
    );
  }
}

export default App;
```

### Create 구현

#### mode 변경 기능

create를 클릭 시 `mode`를 `create`로 변경할 수 있도록 한다.

```javascript
// components/Control.js

import React, { Component } from "react";

class Control extends Component {
  render() {
    return (
      <ul>
        <li>
          <a
            href="/create"
            onClick={function (e) {
              e.preventDefault();
              this.props.onChangeMode("create");
            }.bind(this)}
          >
            create
          </a>
        </li>
      </ul>
    );
  }
}

export default Control;
```

```javascript
// App.js

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      mode: "read",
    };
  }
  render() {
    return (
      <div className="App">
        <Control
          onChangeMode={function (mode) {
            this.setState({
              mode,
            });
          }.bind(this)}
        ></Control>
      </div>
    );
  }
}
```

#### mode 전환 기능

`mode`에 해당되는 `Content` 컴포넌트를 보여줄 수 있도록 한다. 예를 들어 `mode`가 `create`일 때 `CreateContent`를, `read`일 때 `ReadContent` 컴포넌트로 교체하도록 한다.

따라서 `{_article}`로 하여 `mode`에 해당되는 컴포넌트를 사용하는 로직을 추가한다.

```javascript
// App.js

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      mode: "read",
      selectedContentId: 2,
      welcome: {
        title: "Welcome",
        desc: "Hello, React!!!",
      },
      subject: {
        title: "WEB",
        sub: "world wide web!",
      },
      contents: [
        { id: 1, title: "HTML", desc: "HTML is for information" },
        { id: 2, title: "CSS", desc: "CSS is for design" },
        { id: 3, title: "JavaScript", desc: "JavaScript is for interactive" },
      ],
    };
  }
  render() {
    let _title, _desc, _article;
    if (this.state.mode === "welcome") {
      _title = this.state.welcome.title;
      _desc = this.state.welcome.desc;
      _article = <ReadContent title={_title} desc={_desc}></ReadContent>;
    } else if (this.state.mode === "read") {
      const idx = this.state.contents.findIndex(
        (content) => content.id === this.state.selectedContentId
      );

      _title = this.state.contents[idx].title;
      _desc = this.state.contents[idx].desc;
      _article = <ReadContent title={_title} desc={_desc}></ReadContent>;
    } else if (this.state.mode === "create") {
      _article = <CreateContent></CreateContent>;
    }
    return (
      <div className="App">
        <Subject
          title={this.state.subject.title}
          sub={this.state.subject.sub}
          onChangePage={function () {
            this.setState({
              mode: "welcome",
            });
          }.bind(this)}
        ></Subject>
        <TOC
          onChangePage={function (id) {
            this.setState({
              mode: "read",
              selectedContentId: Number(id),
            });
          }.bind(this)}
          data={this.state.contents}
        ></TOC>
        <Control
          onChangeMode={function (mode) {
            this.setState({
              mode,
            });
          }.bind(this)}
        ></Control>
        {_article}
      </div>
    );
  }
}
```

#### form onSubmit Event

`onSubmit` 이벤트 함수를 통해 `form` 내에 `input value`를 가져올 수 있다. 이는 `e.target.<input name>.value`로 접근이 가능하다.

```javascript
// components/CreateContent.js

class CreateContent extends Component {
  render() {
    return (
      <article>
        <h2>Create</h2>
        <form
          onSubmit={function (e) {
            e.preventDefault();
            // debugger;
            this.props.onSubmit(e.target.title.value, e.target.desc.value);
          }.bind(this)}
        >
          <p>
            <input type="text" name="title" placeholder="title" />
          </p>
          <p>
            <textarea name="desc" placeholder="description"></textarea>
          </p>
          <p>
            <input type="submit" value="Submit" />
          </p>
        </form>
      </article>
    );
  }
}
```

```javascript
// App.js

_article = (
  <CreateContent
    onSubmit={function (title, desc) {
      // add content to this.state.contents
      console.log(title, desc);
    }}
  ></CreateContent>
);
```

#### Contents 변경

`contents`를 추가할 때 마지막 `id` 를 참조하기 위해 `recentContentId`를 추가한다. 이는 렌더링 시 `UI`에 영향을 주는 것이 아니기 때문에 `state`로 관리하지 않는다.

그리고 원본을 수정하는 `push()` 보다는 복제하는 `concat()`을 활용하여 변경하도록 한다.

```javascript
// App.js

class App extends Component {
  constructor(props) {
    super(props);
    this.recentContentId = 3,
    this.state = {
      mode: "read",
      selectedContentId: 2,
      welcome: {
        title: "Welcome",
        desc: "Hello, React!!!",
      },
      subject: {
        title: "WEB",
        sub: "world wide web!",
      },
      contents: [
        { id: 1, title: "HTML", desc: "HTML is for information" },
        { id: 2, title: "CSS", desc: "CSS is for design" },
        { id: 3, title: "JavaScript", desc: "JavaScript is for interactive" },
      ],
    };
  }
  render() {
    let _title, _desc, _article;
    if (this.state.mode === "welcome") {
      _title = this.state.welcome.title;
      _desc = this.state.welcome.desc;
      _article = <ReadContent title={_title} desc={_desc}></ReadContent>;
    } else if (this.state.mode === "read") {
      const idx = this.state.contents.findIndex(
        (content) => content.id === this.state.selectedContentId
      );

      _title = this.state.contents[idx].title;
      _desc = this.state.contents[idx].desc;
      _article = <ReadContent title={_title} desc={_desc}></ReadContent>;
    } else if (this.state.mode === "create") {
      _article = (
        <CreateContent
          onSubmit={function (title, desc) {
            this.recentContentId += 1;
            const contents = this.state.contents.concat({
              id: this.recentContentId,
              title: title,
              desc: desc,
            });
            this.setState({
              contents,
            });
          }.bind(this)}
        ></CreateContent>
      );
    }
    return (

    );
  }
}
```

#### shouldComponentUpdate

왜 원본을 수정하는 `push()` 보다는 복제하는 `concat()`을 사용해야 하는가? 이는 `shouldComponentUpdate()`를 통해 알아본다.

현재 `TOC` 컴포넌트는 `this.state.contents`를 `props`로 전달받아 사용하기 때문에 만약 변경이 이루어진다면 `render()`를 호출하여 다시 렌더링 하도록 되어있다.

하지만 상위 컴포넌트에서 `this.state.contents`가 아닌 다른 값의 변경이 이루어져도 모든 하위 컴포넌트에서 `render()`를 호출하여 다시 렌더링 한다.

이는 `shouldComponentUpdate()`로 해결이 가능하다.

1. `render()` 이전에 `shouldComponentUpdate()`가 실행된다.

2. `shouldComponentUpdate()`의 `return` 값이 `true`이면 `render()`가 호출되고, `false`이면 호출되지 않는다.

3. 변경 전과 변경 후의 값을 알아낼 수 있다.

```javascript
class TOC extends Component {
  shouldComponentUpdate(newProps, newState) {
    if (this.props.data === newProps.data) {
      // 변경 사항이 없을 때, render() 호출 X
      return false;
    }
    return true;
  }
  render() {}
}
```

하지만 이전에 원본을 수정하는 `push()` 방식을 사용했다면, `this.props.data === newProps.data`는 항상 `true`를 반환하는 이슈가 발생하게 된다. 이는 변경 전과 변경 후의 값 추적이 어려워진다.

따라서 `this.setState()`를 진행할 때는 항상 원본 수정보다는 복제하여 사용하고 주의하도록 한다.

#### Immutable

원본을 변경하지 않는다를 **불변성(immutable)** 이라고 한다. `concat()`을 사용하여도 되지만 이것이 불변인 지 또는 가변인 지 확인이 어려울 때가 있다.

따라서 `Array.from()`을 사용하여 기존 배열을 복제하여 사용해도 된다. 복제된 배열은 내용물만 같을 뿐 서로 다른 주소값을 가진다.

```javascript
// Array
let a = [1, 2];
let b = Array.from(a);

console.log(a, b, a === b); // [1, 2], [1, 2], false

// Object
let a = { name: "Jiheon Lee" };
let b = Object.assign({}, a);

console.log(a, b, a === b); // {name: 'Jiheon Lee'}, {name: 'Jiheon Lee'}, false
```

이를 통해 `push()`를 사용할 때는 다음과 같이 사용할 수 있다.

```javascript
let newContents = Array.from(this.state.contents);

newContents.push({
  id: this.recentContentId,
  title: title,
  desc: desc,
});

this.setState({
  contents: newContents,
});
```

### Update 구현

기존 목록과 내용을 수정하기 위해 선택된 목록에 대한 내용들을 `form`에 넣어야 한다.

`components/` 내에 `UpdateContent.js` 컴포넌트를 추가한다.

```javascript
// components/UpdateContent.js

class UpdateContent extends Component {
  render() {
    return (
      <article>
        <h2>Update</h2>
        <form
          onSubmit={function (e) {
            e.preventDefault();
            this.props.onSubmit(e.target.title.value, e.target.desc.value);
          }.bind(this)}
        >
          <p>
            <input type="text" name="title" placeholder="title" />
          </p>
          <p>
            <textarea name="desc" placeholder="description"></textarea>
          </p>
          <p>
            <input type="submit" value="Submit" />
          </p>
        </form>
      </article>
    );
  }
}
```

`App.js`에서 불러온 후 `this.state.mode`가 `update`인 경우에 보여질 컴포넌트 로직을 추가한다.

```javascript
// App.js

import UpdateContent from "./components/UpdateContent";

class App extends Component {
  render() {
    let _title, _desc, _article;
    if (this.state.mode === "welcome") {
      _title = this.state.welcome.title;
      _desc = this.state.welcome.desc;
      _article = <ReadContent title={_title} desc={_desc}></ReadContent>;
    } else if (this.state.mode === "read") {
      const idx = this.state.contents.findIndex(
        (content) => content.id === this.state.selectedContentId
      );

      _title = this.state.contents[idx].title
      _desc = this.state.contents[idx].desc

      _article = (
        <ReadContent title={_title} desc={_desc}></ReadContent>
      );
    } else if (this.state.mode === "create") {
      _article = (
        <CreateContent
          onSubmit={function (title, desc) {
            this.recentContentId += 1;
            const contents = this.state.contents.concat({
              id: this.recentContentId,
              title: title,
              desc: desc,
            });
            this.setState({
              contents,
            });
          }.bind(this)}
        ></CreateContent>
      );
    } else if (this.state.mode === "update") {
      _article = (
        <UpdateContent
          onSubmit={function (title, desc) {
            this.recentContentId += 1;
            const contents = this.state.contents.concat({
              id: this.recentContentId,
              title: title,
              desc: desc,
            });
            this.setState({
              contents,
            });
          }.bind(this)}
        ></UpdateContent>
      );
    }
    return ()
  }
}
```

`this.state.mode`에 따라 보여질 컴포넌트 로직을 `getContents()` 함수로 빼내어 리팩터링을 진행한다.

```javascript
// App.js

class App extends Component {
  getContents() {
    let _title, _desc, _article;
    if (this.state.mode === "welcome") {
      _title = this.state.welcome.title;
      _desc = this.state.welcome.desc;
      _article = <ReadContent title={_title} desc={_desc}></ReadContent>;
    } else if (this.state.mode === "read") {
      const idx = this.state.contents.findIndex(
        (content) => content.id === this.state.selectedContentId
      );

      _title = this.state.contents[idx].title;
      _desc = this.state.contents[idx].desc;

      _article = <ReadContent title={_title} desc={_desc}></ReadContent>;
    } else if (this.state.mode === "create") {
      _article = (
        <CreateContent
          onSubmit={function (title, desc) {
            this.recentContentId += 1;
            const contents = this.state.contents.concat({
              id: this.recentContentId,
              title: title,
              desc: desc,
            });
            this.setState({
              contents,
            });
          }.bind(this)}
        ></CreateContent>
      );
    } else if (this.state.mode === "update") {
      _article = (
        <UpdateContent
          onSubmit={function (title, desc) {
            this.recentContentId += 1;
            const contents = this.state.contents.concat({
              id: this.recentContentId,
              title: title,
              desc: desc,
            });
            this.setState({
              contents,
            });
          }.bind(this)}
        ></UpdateContent>
      );
    }
    return _article;
  }
  render() {
    return <div className="App">{this.getContents()}</div>;
  }
}
```

선택된 목록에 대한 내용들을 가져오기 위해 `this.recentContentId` 해당되는 컨텐츠를 찾아야 한다. 이는 `this.state.mode`가 `read`인 경우에서 이미 다뤘으므로, 중복해서 사용되기 때문에 이를 `getReadContent()`로 함수화 한다.

`read`, `update`인 경우에서 호출하여 사용하고, `update`인 경우에서는 해당 컨텐츠 내용을 하위 컴포넌트에 `props`로 전달한다.

```javascript
// App.js

class App extends Component {
  getReadContent() {
    const idx = this.state.contents.findIndex(
      (content) => content.id === this.state.selectedContentId
    );

    return this.state.contents[idx];
  }
  getContents() {
    let _title, _desc, _article;
    if (this.state.mode === "welcome") {
      _title = this.state.welcome.title;
      _desc = this.state.welcome.desc;
      _article = <ReadContent title={_title} desc={_desc}></ReadContent>;
    } else if (this.state.mode === "read") {
      const content = this.getReadContent();

      _article = (
        <ReadContent title={content.title} desc={content.desc}></ReadContent>
      );
    } else if (this.state.mode === "create") {
      _article = (
        <CreateContent
          onSubmit={function (title, desc) {
            this.recentContentId += 1;
            const contents = this.state.contents.concat({
              id: this.recentContentId,
              title: title,
              desc: desc,
            });
            this.setState({
              contents,
            });
          }.bind(this)}
        ></CreateContent>
      );
    } else if (this.state.mode === "update") {
      const content = this.getReadContent();

      _article = (
        <UpdateContent
          data={content}
          onSubmit={function (title, desc) {
            this.recentContentId += 1;
            const contents = this.state.contents.concat({
              id: this.recentContentId,
              title: title,
              desc: desc,
            });
            this.setState({
              contents,
            });
          }.bind(this)}
        ></UpdateContent>
      );
    }
    return _article;
  }
  render() {
    return <div className="App">{this.getContents()}</div>;
  }
}
```

#### form

상위 컴포넌트에서 `props`로 전달받은 데이터를 `form`내에 `<input value={this.props}>`를 통해 값을 넣어 주어야 한다.

```javascript
// components/UpdateContent.js

class UpdateContent extends Component {
  render() {
    return (
      <article>
        <h2>Update</h2>
        <form
          onSubmit={function (e) {
            e.preventDefault();
            this.props.onSubmit(e.target.title.value, e.target.desc.value);
          }.bind(this)}
        >
          <input
            type="text"
            name="title"
            placeholder="title"
            value={this.props.data.title}
          />
        </form>
      </article>
    );
  }
}
```

하지만 다음과 같은 에러가 발생하며, 수정 또한 되지 않고 `read-only` 상태가 된다.

```
Warning: You provided a `value` prop to a form field without an `onChange` handler.
This will render a read-only field.
If the field should be mutable use `defaultValue`.
Otherwise, set either `onChange` or `readOnly`.
```

이를 해결하기 위해, 먼저 `props`로 전달받는 데이터를 가변적인 데이터 즉, 해당 컴포넌트에서 `state`화 한다. 그 다음 `onChange` 이벤트를 추가한 후 변경사항을 추적하도록 `this.setState()`를 진행한다.

```javascript
// components/UpdateContent.js

class UpdateContent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      title: this.props.data.title,
      desc: this.props.data.desc,
    };
  }
  render() {
    return (
      <article>
        <h2>Update</h2>
        <form
          onSubmit={function (e) {
            e.preventDefault();
            this.props.onSubmit(e.target.title.value, e.target.desc.value);
          }.bind(this)}
        >
          <p>
            <input
              type="text"
              name="title"
              placeholder="title"
              value={this.state.title}
              onChange={function (e) {
                this.setState({
                  title: e.target.value,
                });
              }.bind(this)}
            />
          </p>
          <p>
            <textarea
              name="desc"
              placeholder="description"
              value={this.state.desc}
              onChange={function (e) {
                this.setState({
                  desc: e.target.value,
                });
              }.bind(this)}
            ></textarea>
          </p>
          <p>
            <input type="submit" value="Submit" />
          </p>
        </form>
      </article>
    );
  }
}
```

`<input>`과 `<textarea>`에서의 `onChange` 이벤트 함수는 중복되므로, 해당 부분을 함수화 한다.

`{ [e.target.name]: e.target.value }`는 객체 안에서 `key`를 `[ ]`로 감싸면 그 안에 넣은 레퍼런스가 가리키는 실제 값이 `key` 값으로 사용된다.

```javascript
// components/UpdateContent.js

class UpdateContent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      title: this.props.data.title,
      desc: this.props.data.desc,
    };
  }
  inputFormHandler(e) {
    this.setState({ [e.target.name]: e.target.value });
  }
  render() {
    return (
      <article>
        <h2>Update</h2>
        <form
          onSubmit={function (e) {
            e.preventDefault();
            this.props.onSubmit(e.target.title.value, e.target.desc.value);
          }.bind(this)}
        >
          <p>
            <input
              type="text"
              name="title"
              placeholder="title"
              value={this.state.title}
              onChange={this.inputFormHandler.bind(this)}
            />
          </p>
          <p>
            <textarea
              name="desc"
              placeholder="description"
              value={this.state.desc}
              onChange={this.inputFormHandler.bind(this)}
            ></textarea>
          </p>
          <p>
            <input type="submit" value="Submit" />
          </p>
        </form>
      </article>
    );
  }
}
```

`onChange={this.inputFormHandler.bind(this)}` 에서의 `.bind(this)`처럼 중복되는 부분 또한 다음과 같이 변경할 수 있다.

```javascript
// components/UpdateContent.js

class UpdateContent extends Component {
  constructor(props) {
    super(props);
    this.state = {
      title: this.props.data.title,
      desc: this.props.data.desc,
    };
    this.inputFormHandler = this.inputFormHandler.bind(this);
  }
  inputFormHandler(e) {
    this.setState({ [e.target.name]: e.target.value });
  }
  render() {
    return (
      <article>
        <h2>Update</h2>
        <form
          onSubmit={function (e) {
            e.preventDefault();
            this.props.onSubmit(e.target.title.value, e.target.desc.value);
          }.bind(this)}
        >
          <p>
            <input
              type="text"
              name="title"
              placeholder="title"
              value={this.state.title}
              onChange={this.inputFormHandler}
            />
          </p>
          <p>
            <textarea
              name="desc"
              placeholder="description"
              value={this.state.desc}
              onChange={this.inputFormHandler}
            ></textarea>
          </p>
          <p>
            <input type="submit" value="Submit" />
          </p>
        </form>
      </article>
    );
  }
}
```
