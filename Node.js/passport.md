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
