# 테스트 주도 개발 (TDD)

- 테스트 코드를 먼저 작성하고 테스트를 통과하도록 코드를 작성
- TDD를 위한 라이브러리 **mocha, should, superTest**

## Mocha

- Mocha는 테스트 코드를 돌려주는 테스트 러너
- 테스트 수트 : 테스트 환경으로 Mocha에서는 `describe( )` 으로 구현
- 테스트 케이스 : 실제 테스트를 말하며 Mocha에서는 `it( )` 으로 구현
- 설치

```bash
$ npm i mocha --save-dev
```

**utils.spec.js** (테스트하고자하는 파일명 뒤에 .spec.js)

```javascript
// utils.spec.js

const utils = require("./utils");
const assert = require("assert");

// 테스트 수트
describe("utils.js 모듈의 capitialize() 함수는", () => {
  // 테스트 케이스
  it("문자열의 첫번째 문자를 대문자로 변환한다", () => {
    const result = utils.capitialize("hello");
    assert.equal(result, "Hello");
  });
});
```

```javascript
// utils.js

function capitialize(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

module.exports = {
  capitialize: capitialize,
};
```

- 실행

```bash
$ node_modules/.bin/mocha utils.spec.js
```

## Should

- assert는 테스트코드에서 사용하지 말라고 권장함
- 대신 서드파티 라이브러리를 사용하자
- should는 검증(assertion) 라이브러리
- 가독성 높은 테스트 코드를 만듬
- 설치

```bash
$ npm i should --save-dev
```

- 검증 코드 수정

```javascript
// utils.spec.js

describe("utils.js 모듈의 capitialize() 함수는", () => {
  it("문자열의 첫번째 문자를 대문자로 변환한다", () => {
    const result = utils.capitialize("hello");
    // assert.equal(result, 'Hello');
    result.should.be.equal("Hello");
  });
});
```

## SuperTest

- 단위 테스트 : 함수의 기능 테스트 (위에서 정의한 테스트 코드를 의미)
- 통합 테스트 : API의 기능 테스트
- SuperTest는 Express 통합 테스트용 라이브러리
- 내부적으로 Express 서버를 구동시켜 실제 요청을 보낸 뒤 결과를 검증
- 설치

```bash
$ npm i supertest --save-dev
```

- 테스트 코드 작성

```javascript
// index.spec.js

const app = require('./index');
const request = require('supertest');

describe('GET /user는', (done) => {
  it('...', () => {
    request(app)
      .get('/users')
      .end((err, res) => {
        console.log(res.body);
        done();
      })
  })
}
```

- 실행

```bash
$ node_modules/.bin/mocha index.spec.js
```

### npm 테스트 스크립트

- package.json

```json
{
  "scripts": {
    "test": "mocha index.spec.js" // mocha 앞에 node_modules/.bin/ 생략 가능
  }
}
```

```bash

$ npm test

# 또는

$ npm t
```

### 테스트 환경 개선

```json
{
  "scripts": {
    "test": "NODE_ENV=test mocha routes/users.spec.js"
  }
}
```

```javascript
// app.js

// 테스트 환경에서는 morgan 미들웨어 사용하지 않음
if (process.env.NODE_ENV !== "test") {
  app.use(morgan("dev"));
}
```
