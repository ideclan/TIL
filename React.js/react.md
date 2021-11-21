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
