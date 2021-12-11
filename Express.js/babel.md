주로 사용하는 Node.js 웹 프레임워크인 `Express`에서 ES6을 위한 Babel을 설정하는 방법을 알아보겠습니다.

# Express 프로젝트 생성

`express-generator`를 통해 간편하게 프로젝트 기본 구조를 만듭니다.

```bash
$ npm install -g express-generator

$ express myapp
```

생성된 기본 구조는 다음과 같습니다.

```
|-- bin
|    `-- www
|-- public
|-- routes
|    `-- index.js
|    `-- users.js
|-- views
|-- app.js
```

## 프로젝트 구조화

1. 프로젝트 루트 경로 내에 `src/` 생성
2. `bin/`, `public/`, `routes/`, `views/`, `app.js` -> `src/` 안으로 이동
3. `src/bin/` 내에 `www` -> `www.js`로 변경

그리고 `express-generator`를 통해 생성된 기본 파일들은  
`ES5` 이므로 `ES6` 코드로 변경합니다.

```javascript
// www.js
#!/user/bin/env node

/**
 * Module dependencies.
 */

import http from 'http';
import app from '../app';

/**
 * Normalize a port into a number, string, or false.
 */

const normalizePort = (val) => {
  const port = parseInt(val, 10);

  if (Number.isNaN(port)) {
    // named pipe
    return val;
  }

  if (port >= 0) {
    // port number
    return port;
  }

  return false;
};

/**
 * Get port from environment and store in Express.
 */

const port = normalizePort(process.env.PORT || '3000');
app.set('port', port);

/**
 * Create HTTP server.
 */

const server = http.createServer(app);

/**
 * Event listener for HTTP server "error" event.
 */

const onError = (error) => {
  if (error.syscall !== 'listen') {
    throw error;
  }

  const bind = typeof port === 'string' ? `Pipe ${port}` : `Port ${port}`;

  // handle specific listen errors with friendly messages
  switch (error.code) {
    case 'EACCES':
      console.error(`${bind} requires elevated privileges`);
      process.exit(1);
      break;
    case 'EADDRINUSE':
      console.error(`${bind} is already in use`);
      process.exit(1);
      break;
    default:
      throw error;
  }
};

/**
 * Event listener for HTTP server "listening" event.
 */

const onListening = () => {
  const addr = server.address();
  const bind = typeof addr === 'string' ? `pipe ${addr}` : `port ${addr.port}`;
  console.log(`Listening on ${bind}`);
};

/**
 * Listen on provided port, on all network interfaces.
 */

server.listen(port);
server.on('error', onError);
server.on('listening', onListening);

```

```javascript
// app.js
import createError from "http-errors";
import express from "express";
import path from "path";
import cookieParser from "cookie-parser";
import logger from "morgan";

import indexRouter from "./routes/index";
import usersRouter from "./routes/users";

const app = express();

// view engine setup
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "ejs");

app.use(logger("dev"));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, "public")));

app.use("/", indexRouter);
app.use("/users", usersRouter);

// catch 404 and forward to error handler
app.use((req, res, next) => {
  next(createError(404));
});

// error handler
app.use((err, req, res) => {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get("env") === "development" ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render("error");
});

export default app;
```

```javascript
// index.js
import express from "express";
const router = express.Router();

/* GET home page. */
router.get("/", (req, res, next) => {
  res.render("index", { title: "Express" });
});

export default router;
```

```javascript
// users.js
import express from "express";
const router = express.Router();

/* GET users listing. */
router.get("/", (req, res, next) => {
  res.send("respond with a resource");
});

export default router;
```

# Babel 설치

Babel을 사용하기 위해 관련 모듈을 설치합니다.

```bash
$ npm install --save-dev @babel/core @babel/cli @babel/preset-env @babel/node

$ npm install --save-dev @babel/plugin-transform-runtime
$ npm install --save @babel/runtime  # runtime 종속성, -dev 옵션 X

$ npm install --save-dev babel-plugin-transform-remove-console # build 할 때 console.log 제거
```

## Babel 설정 파일

프로젝트 루트 경로 내에 `babel.config.js` 파일을 생성합니다.  
코드를 살펴보면 삼항 조건 연산자(`?`)가 존재하는데,  
이것은 `production` 환경에서 빌드 시`console.log`를 제거합니다.

```javascript
module.exports = {
  presets: ["@babel/env"],
  plugins:
    process.env.NODE_ENV === "production"
      ? ["transform-remove-console", "@babel/plugin-transform-runtime"]
      : ["@babel/plugin-transform-runtime"],
  ignore: ["./src/public/**/*.js"],
};
```

# Express 실행

`package.json` 내에 `scripts`를 추가합니다.

```json
{
  "scripts": {
    "dev": "nodemon --exec babel-node src/bin/www.js",
    "build": "NODE_ENV=production babel src --out-dir dist --copy-files",
    "start": "node dist/bin/www.js"
  }
}
```

`$ npm run build`를 통해 빌드 시 `src/` 내에 ES6 문법으로 구성된 모든 파일들을 ES5로 변환하여 `dist/` 내에 생성하게 됩니다. 이후 `$ npm run start`를 통해 프로젝트를 실행시킬 수 있습니다.

# References

- [What is Babel?
  ](https://babeljs.io/docs/en/)
- [운영 빌드 시 console.log 제거하기. 덤으로 no-console 에러도 해결](https://gitabout.com/3)
