# Courses

## Node.js Bootcamp

- [한 번에 끝내는 Node.js 웹 프로그래밍 초격자 패키지 Online](https://fastcampus.co.kr/dev_online_node), 패스트컴퍼스

## 프로젝트 설정

- `tj/n` : 노드 버전 관리 툴
- `npm init -y` : package.json 파일 생성

### Formatting

- `npm install --save-dev prettier` : prettier 설치

```json
// .prettierrc
{
  "semi": false,
  "singleQuote": true
}
```

```json
// .vscode/settings.json
// 해당 프로젝트에만 적용
{
  "[javascript]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  }
}
```

### Linting

- `npm install --save-dev eslint` : eslint 설치

```jsx
// .eslintrc.js
module.exports = {}
```

- `npm install --save-dev eslint-config-airbnb-base eslint-plugin-import` : Airbnb 코드 스타일 설치 (종속성 eslint-plugin-import 설치 필요)
- `npm install --save-dev eslint-config-prettier` : prettier eslint 충돌 해결하기 위해 설치 (잘 작동하기 위해서는 extends에서 항상 맨 뒤에 넣어야 함)
- `npm install --save-dev eslint-plugin-node` : node lint 설치

```jsx
// .eslintrc.js
module.exports = {
  extends: ['airbnb-base', 'plugin:node/recommended', 'prettier'],
}
```

### Type Checking

- `npm install --save-dev typescript` : JS 동적 언어, type 에러 체크가 필요, typescript 설치

```jsx
// @ts-check

const someString = 'Hello'
const result = Math.log(someString)
console.log(result)
```

- `npm install --save-dev @types/node` : node에서 typescript 사용하기 위해 설치

```jsx
// @ts-check

const http = require('http')

const server = http.createServer((req, res) => {
  res.statusCode = 200 // statuscode 나 200이 아닌 문자열을 넣을 때 type check!
  res.end('Hello!')
})

const PORT = 3000
server.listen(PORT, () => {
  console.log(`The server is listening at port: ${PORT}`)
})
```
