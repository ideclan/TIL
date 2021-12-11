# Express.js

- Node.js 기반 웹 프레임워크
- 설치

```bash
$ npm i express --save
```

```javascript
// index.js

const express = require("express");
const app = express();

// 서버를 대기 상태로
app.listen(3000, function () {
  console.log("Sever is running");
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

## 어플리케이션

- Express 인스턴스를 어플리케이션이라 함
- 서버에 필요한 기능인 미들웨어를 어플리케이션에 추가
- 라우팅 설정이 가능
- 서버를 요청 대기 상태로 만들 수 있음

## 미들웨어

- 미들웨어는 함수들의 연속
- 사용법
  - 미들웨어는 할 일을 끝내고 마지막에 `next ( )` 함수를 호출해야 다음 로직을 수행함
  - 실행순서 : `app.use(logger)` ⇒ `function logger( )` ⇒ `app.use(logger2)` ⇒ `function logger2( )`

```javascript
// index.js

function logger(req, res, next) {
  console.log("I am logger");
  // next();
}

function logger2(req, res, next) {
  console.log("I am logger2");
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

  ```javascript
  // index.js

  const morgan = require("morgan");

  app.use(morgan("dev")); // 개발중이므로 dev 설정
  ```

- 에러 미들웨어

```javascript
function commonmw(req, res, next) {
  console.log("commonmw");
  next(new Error("error ouccered"));
}

function errormw(err, req, res, next) {
  console.log(err.message);
  // 에러 처리
  next();
}

app.use(commonmw);
app.use(errormw);
```

## 라우팅

- 요청 url에 대해 적절한 핸들러 함수로 연결해 주는 기능을 라우팅이라고 함
- 어플리케이션의 `get( )` , `post( )` 메소드로 구현
- 라우팅을 위한 전용 Router 클래스를 사용할 수도 있음

## 요청 객체

- 클라이언트의 요청 정보를 담은 객체를 요청(Request) 객체라고 함
- http 모듈의 request 객체를 래핑한 것
- `req.params( )` , `req.query( )` , `req.body( )` 메소드를 주로 사용

## 응답 객체

- 클라이언트의 응답 정보를 담은 객체를 응답(Response) 객체라고 함
- http 모듈의 response 객체를 래핑한 것
- `res.send( )` , `res.status( )` , `res.json( )` 메소드를 주로 사용

## npm

- package.json

```json
{
  "scripts": {
    "start": "node index.js"
  }
}
```

```bash
// server run

$ npm start
```

## Cookie 생성

- 개발자 도구 → Network → [localhost](http://localhost) > Headers 또는 Cookies 에서 확인
- Application → Cookies 에서 제거

```javascript
var http = require("http");
http
  .createServer(function (request, response) {
    response.writeHead(200, {
      "Set-Cookie": ["yummy_cookie=choco", "tasty_cookie=strawberry"],
    });
    response.end("Cookie!!");
  })
  .listen(3000);
```

## Cookie 읽기

```javascript
var http = require("http");
var cookie = require("cookie"); // npm cookie module
http
  .createServer(function (request, response) {
    console.log(request.headers.cookie); // yummy_cookie=choco; tasty_cookie=strawberry
    var cookies = cookie.parse(request.headers.cookie); // {'yummy_cookie': 'choco', 'tasty_cookie': 'strawberry'}
    console.log(cookies.yummy_cookie); // choco
    response.writeHead(200, {
      "Set-Cookie": ["yummy_cookie=choco", "tasty_cookie=strawberry"],
    });
    response.end("Cookie!!");
  })
  .listen(3000);
```

## Session Cookie VS Permanent Cookie

- Session Cookie : 웹 브라우저가 켜져 있는 동안 유효 끄면 사라짐
- Permanent Cookie : 웹 브라우저를 껐다 켜도 유효
  - `Expires` : 쿠키를 언제 삭제할 것 인지
  - `Max-Age` : 쿠키를 얼마나 사용할 것 인지 (단위 : 초)

```javascript
response.writeHead(200, {
  "Set-Cookie": [
    "yummy_cookie=choco",
    "tasty_cookie=strawberry",
    `Permanent=cookies; Max-Age=${60 * 60 * 24 * 30}`, // 30일 동안 유효
  ],
});
```

## Secure & HttpOnly Cookies

- `Secure` : Https 를 통해서 통신하는 경우에만 쿠키를 전송
- `HttpOnly` : 웹 브라우저와 웹 서버가 통신할 때만 쿠키를 전송

```javascript
'Set-Cookie': [
  '{쿠키명}={쿠키값}; Secure',
  '{쿠키명}={쿠키값}; HttpOnly'
]
```

## Path & Domain

- `Path` : 해당 path 에서만 유효하도록
- `Domain` : 어떠한 서브 도메인에서도 유효할 수 있음 (지정 값 앞에 점 생략)

```javascript
'Set-Cookie': [
  '{쿠키명}={쿠키값}; Path=/cookie',
  '{쿠키명}={쿠키값}; Domain=o2.org'  //.o2.org
]
```

## 인증 구현 - 로그인

- 쿠키 생성 (해당 코드는 쿠키에 아이디, 비밀번호를 저장하는 학습용 코드. 본 프로젝트에 적용하면 안됨)
- 따라서 세션 방법을 사용해야 함 (추후 학습 예정)

```javascript
request.on("end", function () {
  var post = qs.parse(body);
  if (post.email === "test@gmail.com" && post.password === "1234") {
    response.writeHead(302, {
      "Set-Cookie": [
        `email=${post.email}`,
        `password=${post.password}`,
        `nickname=test`,
      ],
      Location: `/`,
    });
    response.end();
  } else {
    response.end("Who?");
  }
});
```

## 인증 구현 - 로그아웃

- 쿠키 삭제

```javascript
request.on("end", function () {
  var post = qs.parse(body);
  response.writeHead(302, {
    "Set-Cookie": [
      `email=; Max-age=0`,
      `password=; Max-age=0`,
      `nickname=; Max-age=0`,
    ],
    Location: `/`,
  });
  response.end();
});
```

## 인증 구현 - 접근제어

```javascript
function authIsOwner(request, response) {
  var isOwner = false;
  var cookies = {};
  if (request.headers.cookie) {
    cookies = cookie.parse(request.headers.cookie);
  }
  if (cookies.email === "test@gmail.com" && cookies.password === "1234") {
    isOwner = true;
  }
  return isOwner;
}

if (authIsOwner(request, response) === false) {
  response.end("Login required!!");
  return false;
}
```

## express-session 설치

```bash
$ npm install express-session --save
```

## express-session 사용법

```javascript
var express = require("express");
var session = require("express-session");

var app = express();

app.use(
  session({
    secret: "@%$#@5dasjkhfaskdjg",
    resave: false,
    saveUninitialized: true,
  })
);

app.get("/", function (req, res, next) {
  console.log(req.session);
  res.send("Hello session");
});

app.listen(3000, function () {
  console.log("3000!");
});
```

## express-session 옵션

- `secret` : 꼭 포함해야 함. 노출되면 안됨. 별도 파일로 관리.
- `resave` : false 권장
- `saveUninitialized` : true 권장
- `secure` : true 권장. true일 때 https에서만 세션 정보를 주고 받음. 사용자가 전달한 자바스크립트 코드 거부.
- `HttpOnly` : true일 때 자바스크립트를 통해 세션 쿠키를 이용할 수 없도록 함.

## session 객체

- 메모리에 저장. 휘발성을 가짐. 서버를 껐다 키면 초기화.
- 따라서 session-store 사용 필요

```javascript
app.get("/", function (req, res, next) {
  console.log(req.session);
  if (req.session.num === undefined) {
    req.session.num = 1; // 기존 num이 없으므로 num 변수 값 1로 초기화
  } else {
    req.session.num += 1; // 요청할 때마다 1 증가
  }
  res.send(`Views : ${req.session.num}`);
});
```

## session store

- session-store 관련 여러 모듈 중 session-file-store 사용
- session-file-store 대체로 mysql을 session-store로 사용이 가능하다고 함 (mongoDB?)

```bash
$ npm install session-file-store --save
```

- session 디렉토리 안에 파일이 생성

```javascript
var FileStore = require("session-file-store")(session);

app.use(
  session({
    secret: "@%$#@5dasjkhfaskdjg",
    resave: false,
    saveUninitialized: true,
    store: new FileStore(),
  })
);
```

## 인증 구현 - 로그인 세션

```javascript
router.post("/login_process", function (request, response) {
  var post = request.body;
  var email = post.email;
  var password = post.pwd;
  if (email === authData.email && password === authData.password) {
    request.session.is_logined = true;
    request.session.nickname = authData.nickname;
    response.redirect(`/`);
  } else {
    response.send("Who?");
  }
});
```

## 인증 구현 - 로그아웃 세션

- `session.destroy(callback)`

```javascript
router.get("/logout", function (request, response) {
  request.session.destroy(function (err) {
    response.redirect("/");
  });
});
```

## 인증 구현 - 접근 제어

```javascript
router.post('/create_process', function (request, response) {
  if (!auth.isOwner(request, response)) {
    response.redirect('/');
    return false;
  }
}
```

## 인증 구현 - 세션 저장

- `session.save(callback)` : session-store 에 적용

```javascript
router.post("/login_process", function (request, response) {
  var post = request.body;
  var email = post.email;
  var password = post.pwd;
  if (email === authData.email && password === authData.password) {
    request.session.is_logined = true;
    request.session.nickname = authData.nickname;
    request.session.save(function () {
      response.redirect(`/`);
    });
  } else {
    response.send("Who?");
  }
});
```
