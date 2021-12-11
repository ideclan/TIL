# Express.js

- `npm install express` : express 설치
- `npm install --save-dev @types/express` : express를 사용하면서 타입 체크 도움

```javascript
// @ts-check

const express = require("express");

const app = express();

const PORT = 3000;

app.use("/", (req, res) => {
  res.send("Hello, express!");
});

app.listen(PORT, () => {
  console.log(`The Express server is listening at port: ${PORT}`);
});
```

## 미들웨어

- Express가 실행되면서 어떤 하나의 요청(request)이 응답(response)될 때까지 여러 함수들을 거침, 이때 모든 함수 그리고 각 하나의 함수들을 미들웨어라고 함
- `next` : 비동기 작업이 끝난 후, 다음 미들웨어에게 실행을 넘기기 위해 사용

```javascript
app.use("/", (req, res, next) => {
  console.log("Middleware 1");
  const requestedAt = new Date();
  // @ts-ignore
  req.requestedAt = requestedAt;
  next();
});

app.use((req, res) => {
  console.log("Middleware 2");
  // @ts-ignore
  res.send(`Hello, express! Requested at ${req.requestedAt}`);
});
```

## Path & Path Pattern

- `'/abcd'` , `'/abc?d'` , `'/ab*cd'` , `'/a(bd)?d'` , `/^\/abcd$/` , `['/abc', '/xyz']`

## REST API 라우팅

- `app.get('/', (req,res) => {})`
- `app.post('/', (req,res) => {})`

```javascript
const express = require("express");
const userRouter = express.Router();
const app = express();
app.use(express.json()); // body-parser

userRouter.param("id", (req, res, next, value) => {
  next();
});
userRouter.get("/", (req, res) => {});
userRouter.post("/", (req, res) => {});

app.use("/users", userRouter);
```

- `req.accepts([types])` : 클라이언트가 해당하는 타입을 받을 수 있는 지 확인

```javascript
userRouter.get("/:id", (req, res) => {
  const resMimeType = req.accepts(["json", "html"]);

  if (resMimeType === "json") {
    // @ts-ignore
    res.send(req.user);
  } else if (resMimeType === "html") {
    res.render("user-profile");
  }
});
```

## View Engine

- Pug, Ejs etc
- `npm install pug`
  - `app.set('view', 'src/views')`
  - `app.set('view engine', 'pug')`

## Static 파일 서빙

- `app.use(express.static('src/public'))`
- 요청 경로와 동일한 경로로 public 내에 파일이 있을 경우 다운로드하는 이슈
  1. 미들웨어는 순차적으로 진행하므로 위치를 하단으로 이동
  2. `app.use('/public', express.static('src/public'))`

## Error 핸들링

- Error 핸들링 미들웨어 추가
  - Express에서는 4개의 인자를 받는 경우, Error 핸들링 미들웨어로 취급
  - async 함수로 작성할 때는 `try` , `catch` 필요

```javascript
// app.js
app.use((err, req, res, next) => {
  res.statusCode = err.statusCode || 500;
  res.send(err.message);
});

// routes/users.js
router.param("id", (req, res, next, value) => {
  try {
    // @ts-ignore
    const user = USERS[value];

    if (!user) {
      const err = new Error("User not found.");
      err.statusCode = 404;
      throw err;
    }

    // @ts-ignore
    req.user = USERS[value];
    next();
  } catch (err) {
    next(err); // 인자를 넣어주면 에러
  }
});
```

## Jest를 활용한 API testing

Test 프레임 워크

- Jest
- Supertest

```bash
npm install --save-dev jest @types/jest supertest  @types/supertest
```

- app.js 파일을 testing 한다면 `app.spec.js` 파일명 규칙 권장
- Jest 실행 시 `app.listen()`으로 종료되지 않는 이슈 발생할 수 있음 → `app.listen()`을 분리

```jsx
// package.json
"scripts": {
  "test": "jest",
},

// app.spec.js
const supertest = require('supertest')
const app = require('./app')

const request = supertest(app)

test('retrieve user json', async () => {
  const result = await request.get('/users/15').accept('application/json')

  expect(result.body).toMatchObject({
    nickname: expect.any(String),
  })
})

test('retrieve user page', async () => {
  const result = await request.get('/users/15').accept('text/html')

  expect(result.text).toMatch(/^<html>.*<\/html>$/)
})

test('update nickname', async () => {
  const newNickname = 'newNickname'

  const res = await request
    .post('/users/15/nickname')
    .send({ nickname: newNickname })
  expect(res.status).toBe(200)

  const userResult = await request.get('/users/15').accept('application/json')
  expect(userResult.status).toBe(200)
  expect(userResult.body).toMatchObject({
    nickname: newNickname,
  })
})
```

## 이미지 업로드 핸들링

- Contetn-Type : `multipart/form-data`;
- 주로 바이너리, 이미지 파일을 서버로 업로드 할 때 사용하는 포멧

```html
<!-- 이미지 업로드 html form 예시 -->
<form action="/users/15/profile" method="POST" enctype="multipart/form-data">
  <input type="file" name="profile" />
  <button type="submit">Upload Profile Picture</button>
</form>
```

### multer

- `multipart/form-data` 형태로 요청된 데이터를 핸들링할 수 있게 하는 라이브러리

```bash
$ npm install --save multer
```

- 저장 경로 옵션(`dest`)과 함께 `upload` 미들웨어 생성
- router 에 미들웨어 추가
  - `upload.single('input file의 name')` : 이미지 1개
  - `upload.array('input file의 name')` : 이미지 여러 개

```javascript
// users.js

const multer = require("multer");

const upload = multer({ dest: "uploads/" });

router.post("/:id/profile", upload.single("profile"), (req, res) => {
  console.log(req.file);

  // {
  //   fieldname: 'profile',
  //   originalname: 'test.png',
  //   encoding: '7bit',
  //   mimetype: 'image/png',
  //   destination: 'uploads/',
  //   filename: '5aedb548f84b02773bb52c8143e5bb6d',
  //   path: 'uploads/5aedb548f84b02773bb52c8143e5bb6d',
  //   size: 1045676
  // }
});
```

- static 설정

```javascript
// app.js

app.use("/uploads", express.static("uploads"));
```
