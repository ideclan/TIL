## Courses

### Express Bootcamp

- [Node.js - Express](https://www.inflearn.com/course/node-js-express)
  , 인프런

### Express

- Node.js 로 만들어진 웹 프레임워크
- 설치

```bash
$ npm i express --save
```

```jsx
// index.js

const express = require('express');
const app = express();

// 서버를 대기 상태로
app.listen(3000, function () {
  console.log('Sever is running');
});
```

```bash
$ node index.js
```

- 어플리케이션
- 미들웨어
- 라우팅
- 요청객체
- 응답객체

### 어플리케이션

- Express 인스턴스를 어플리케이션이라 함
- 서버에 필요한 기능인 미들웨어를 어플리케이션에 추가
- 라우팅 설정이 가능
- 서버를 요청 대기 상태로 만들 수 있음

### 미들웨어

- 미들웨어는 함수들의 연속
- 사용법
  - 미들웨어는 할 일을 끝내고 마지막에 `next ( )` 함수를 호출해야 다음 로직을 수행함
  - 실행순서 : `app.use(logger)` ⇒ `function logger( )` ⇒ `app.use(logger2)` ⇒ `function logger2( )`

```jsx
// index.js

function logger(req, res, next) {
  console.log('I am logger');
  // next();
}

function logger2(req, res, next) {
  console.log('I am logger2');
  next();
}

app.use(logger); // 인자 값으로 미들웨어 명
app.use(logger2);

// 실행결과
// I am logger
```

- 로깅 미들웨어 - morgan

  - 서버쪽에 로그를 남겨주는 미들웨어
  - 설치

  ```bash
  $ npm i morgan --save
  ```

  ```jsx
  // index.js

  const morgan = require('morgan');

  app.use(morgan('dev')); // 개발중이므로 dev 설정
  ```

- 에러 미들웨어

```jsx
function commonmw(req, res, next) {
  console.log('commonmw');
  next(new Error('error ouccered'));
}

function errormw(err, req, res, next) {
  console.log(err.message);
  // 에러 처리
  next();
}

app.use(commonmw);
app.use(errormw);
```

### 라우팅

- 요청 url에 대해 적절한 핸들러 함수로 연결해 주는 기능을 라우팅이라고 함
- 어플리케이션의 `get( )` , `post( )` 메소드로 구현
- 라우팅을 위한 전용 Router 클래스를 사용할 수도 있음

### 요청 객체

- 클라이언트의 요청 정보를 담은 객체를 요청(Request) 객체라고 함
- http 모듈의 request 객체를 래핑한 것
- `req.params( )` , `req.query( )` , `req.body( )` 메소드를 주로 사용

### 응답 객체

- 클라이언트의 응답 정보를 담은 객체를 응답(Response) 객체라고 함
- http 모듈의 response 객체를 래핑한 것
- `res.send( )` , `res.status( )` , `res.json( )` 메소드를 주로 사용

### npm

- package.json

```json
{
	...,
	"scripts": {
		"test": "...",
		"start": "node index.js"
	},
	...
}
```

```bash
// server run

$ npm start
```
