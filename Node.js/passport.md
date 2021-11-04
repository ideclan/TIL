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
      cookie: { maxAge: 1000 * 60 * 60 }, // 1 hour
      resave: false,
      saveUninitialized: false,
    })
  );
};
```

## Passport

코드 내의 주석으로 표기한 순서대로 이해하시면 좋을 것 같습니다.

1. `new LocalStrategy()` 를 통해 로컬 전략을 세웁니다.  
   소셜 로그인 인증을 위한 다른 전략을 세울 수도 있습니다.

   `usernameField`와 `passwordField`는 HTML form 내에 아이디, 비밀번호 관련 `<input name="" value="" />` 태그의 name 값을 넣어줍니다.

   이후 콜백 함수에서 해당 태그들의 value를 인자 값으로 전달받아  
   DB에 접근하여 요청한 정보가 일치하는 지 검증하는 로직을 수행합니다.  
   예제에서는 `sequelize`를 사용했습니다.

   만약, 일치한다면 `done()`을 통해 `passport.serializeUser()`로  
   `user` 를 전달합니다.

   DB를 설계한 방식에 따라 속성은 다를 수 있습니다.  
   ex) `user = { id: '', password: '', email: '' }`

2. `passport.serializeUser()` 함수를 통해 사용자 정보를 세션에 저장합니다.
   앞의 `LocalStrategy` 객체의 콜백 함수에서 `done()`으로 전달받은 `user`의 `id`를 세션에 저장하기 위해 `user.id`를 반환합니다.

3. `passport.deserializeUser()` 함수는 로그인 인증이 되어있는 경우, 요청할 때마다 호출하여 실행합니다.  
   이는 세션에 저장하려는 사용자 정보가 큰 경우, 메모리가 많이 소모되므로,  
   `passport.serializeUser()`에서 사용자의 키 값인 `id`만을 세션에 저장해 두고,  
   세션에 저장된 `id`를 이용하여 DB에 접근하여 사용자 정보를 추가로 `select` 한 후  
   `HTTP request` 객체에 붙여서 `req.user`를 반환합니다.

이를 정리하면 `serializeUser()`는 세션에 사용자 키 값 `id`만 저장하고,  
`deserializeUser()`는 세션에 저장된 `id`를 이용해서, 매번 DB에 추가로 필요한 사용자 정보를 `select`하여 `req.user`를 반환한다.

```javascript
// auth/passport.js

import * as passport from "passport";
import { Strategy as LocalStrategy } from "passport-local";
// import { Strategy as NaverStrategy } from "passport-naver";
// import { Strategy as KakaoStrategy } from "passport-kakao";

import { User } from "../db/models";

export default (app) => {
  app.use(passport.initialize());
  app.use(passport.session());

  // (2) - 로그인 인증 성공 시 한 번만 실행
  passport.serializeUser((user, done) => {
    done(null, user.id); // 세션에 사용자 정보인 id를 저장
  });
  // (3) - 로그인 인증이 되어있는 경우, 요청할 때마다 실행
  passport.deserializeUser(async (id, done) => {
    // 세션에 저장되어 있는 id를 인자 값으로 전달받음
    try {
      const user = await User.findOne({
        where: {
          id,
        },
        raw: true,
      });
      done(null, user); // req.user 객체 생성
    } catch {
      done(null, false, {
        message: "서버에 문제가 발생했습니다. 잠시 후 다시 시도해 주세요.",
      });
    }
  });

  // (1)
  passport.use(
    new LocalStrategy(
      {
        session: true, // 세션 저장 여부
        usernameField: "id", // form > input name
        passwordField: "password",
      },
      async (id, password, done) => {
        try {
          // 회원정보 조회
          const user = await User.findOne({
            where: {
              email: id,
            },
            raw: true,
          });

          // 회원정보가 없거나 비밀번호가 일치하지 않는 경우
          if (!user || user.password !== password) {
            done(null, false, {
              message:
                "존재하지 않는 아이디이거나 비밀번호가 일치하지 않습니다.",
            });
          } else {
            done(null, user); // serializeUser로 user 전달
          }
        } catch {
          done(null, false, {
            message: "서버에 문제가 발생했습니다. 잠시 후 다시 시도해 주세요.",
          });
        }
      }
    )
  );
};
```

## 로그인 및 로그아웃 API

# References

- [dotenv](https://github.com/motdotla/dotenv)
- [express-session](https://github.com/expressjs/session)
- [(Node.js) Serialize 와 Deserialize 로그인 정보 저장](https://heewon26.tistory.com/51)
