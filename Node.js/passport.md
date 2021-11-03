# Passport

Node.js 를 위한 인증 미들웨어이며, Express 기반 웹에서 유용하게 사용할 수 있음  
Facebook, Twitter 등 소셜 로그인 인증을 지원

> Passport is authentication middleware for Node.js. Extremely flexible and modular, Passport can be unobtrusively dropped in to any Express-based web application. A comprehensive set of strategies support authentication using a username and password, Facebook, Twitter, and more.

## Passport 설치

- `passport-local` : 직접 구현할 때 사용
- `express-session` : passport를 통해 로그인 후 유저 정보를 세션에 저장하기 위해 사용

```bash
$ npm install passport passport-local express-session
```

> 소셜 로그인 인증을 위한 패키지
>
> ```bash
> passport-google-oauth
> passport-facebook
> passport-twitter
> passport-kakao
> passport-naver
> ```

## Session 및 Passport 설정

`auth/` 내에 `passport.js`와 `session.js`를 생성합니다.

그리고 프로젝트 루트 경로 내에 `.env`를 생성한 후 다음과 같이 작성합니다.

`SESSION_SECRET`은 임의로 작성한 것이므로, 원하는 값으로 변경해도 좋습니다.  
해당 정보는 인증에 관련되어 있어 배포 과정에서 노출되면  
보안적인 이슈가 발생할 수 있기 때문에  
이와 같이 환경 변수 파일을 만들어 관리합니다.

```
// .env

SESSION_SECRET=d4SDLFKD24SDfd3s
```

```
|-- src
     |-- auth
     |   `-- passport.js
     |   `-- session.js
     |-- app.js
|-- .env
```

### Session

`ES6` 문법 기준으로 `auth/session.js` 파일을 작성합니다.

`dotenv`는 앞에서 작성한 환경 변수 파일인 `.env`에 접근하기 위해 사용되는 패키지 입니다.
만약, 존재하지 않다면 다음 명령어로 설치할 수 있습니다.

```bash
$ npm install dotenv
```

> 패키지를 `import` 한 후 `dotenv.config()` 함수를 호출하면  
> `process.env.변수명`으로 접근이 가능합니다.

**express-session option**

- `secret` : 필수 옵션이며, 세션을 암호화할 때 사용
- `cookie`
  - `path` : 쿠키 경로 설정
  - `httpOnly` : 클라이언트 측 자바스크립트를 통하여 쿠키에 접근을 제한
  - `secure` : HTTPS 필요
  - `maxAge` : 쿠키 유효기간 설정
- `resave` : 세션에 변경사항이 없어도 요청마다 세션을 다시 저장, 기본 옵션인 true는 deprecated 상태로 false 권장
- `saveUninitialized` : 세션에 저장할 내용이 없더라도 uninitialized 상태의 세션을 저장, 기본 옵션인 true는 deprecated 상태로 false 권장

> `cookie`의 기본 값은  
> `{ path: '/', httpOnly: true, secure: false, maxAge: null }`

```javascript
// auth/session.js

import session from "express-session";
import dotenv from "dotenv";

dotenv.config();

export default (app) => {
  app.use(
    session({
      secret: process.env.SESSION_SECRET,
      cookie: { maxAge: 60 * 60 * 1000 },
      resave: false,
      saveUninitialized: false,
    })
  );
};
```

# References

- [dotenv](https://github.com/motdotla/dotenv)
- [express-session](https://github.com/expressjs/session)
