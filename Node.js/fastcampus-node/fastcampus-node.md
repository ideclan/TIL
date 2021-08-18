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

### TypeScript 설정 파일

- TypeScript의 Type Checking만 도움을 받을 때
- `strict` : 엄격하게 검사하도록 추가

```json
// jsconfig.json
{
  "compilerOptions": {
    "strict": true
  },
  "include": ["src/**/*"]
}
```

## JavaScript & Event Loop

- Node를 이해하기 위해서는 자바스크립트의 동시성 모델애 이해가 필요
- 자바스크립트 실행 모델은 **event loop, call statck, callback queue** 개념으로 이루어짐

### Event Loop, Main Thread

- 이벤트 루프 모델은 여러 스레드를 사용
- 작성한 자바스크립트 코드가 실행되는 스레드는 **메인 스레드**
- **하나의 Node.js 프로세스에서 메인 스레드는 하나, 한 순간에 한줄씩만 실행**
- 하지만 그 외의 일(file I/O, network 등)을 하는 **워커 스레드**는 여럿이 있을 수 있음

### Call Stack

- 지금 시점까지 불린 함수들의 스택

### Run-to-completion

- → 빈 상태 → callback 처리 → 빈 상태 → callback 처리
- 이벤트 루프가 다음 콜백을 처리하려면 지금 처리하고 있는 콜백의 실행이 완전히 끝나야함

  = call stack이 완전히 빌 때까지 처리

### Callback Queue

- 콜백 큐(메세지 큐)는 앞으로 실행할 콜백(함수와 그 인자)들을 쌓아두는 큐
- 콜백은 브라우저나 Node가 어떤 일이 발생하면(event) 메인 스레드에 이를 알려주기 위해(callback) 사용

  = 이벤트는 파일 처리의 완료, 네트워크 작업의 완료, 타이머 호출 등

```jsx
console.log('1')

setTimeout(() => {
  console.log('2')
}, 0)

console.log('3')

// 1, 2, 3 순서로 출력? X
// 1, 3, 2 순서로 출력 O
// 1 -> setTimeout 호출 -> 3 -> callback 실행 -> 2
```

```jsx
setInterval(() => {
  console.log('Hey !')
  while (true) {}
}, 1000)

// Hey ! 4번 출력? X
// Hey ! 1번 출력 O
// while loop이 도는 동안 call stack이 절대 비지 않음
// 이 동안 callback queue에서 콜백을 꺼낼 수가 없기 때문에
// setInterval이 아무리 콜백을 쌓아도 메인 스레드에서 실행될 수 없음
// 이를 event loop울 block 한다고 함
```

### Non-blocking I/O & Offloading

- 브라우저나 Node.js에서나, Web API 혹은 Node API의 동작이 끝나면 callback queue에 등록
- 브라우저나 Node가 요청 받은 일을 하고 있는 동안 메인 스레드와 이벤트 루프는 영향을 받지 않고 계속 실행

  = 이를 **offloading** 이라 함, **Node 서버의 메인 스레드가 하나임에도 불구하고 빠르게 동작할 수 있는 이유**

## Scope, Hoisting

### Hoisting - var

- **hoisting**이란 변수의 선언(만)을 해당 스코프의 맨 위로 끌어올리는 것

```jsx
var x = 1
console.log(x) // 1

// ---

console.log(x) // undefined
var x = 1
// x 변수가 선언되면서 최상단으로 이동(hoisting)하여 참조는 할 수 있으나
// 값이 할당되지 않음

// ---

// 해당 코드와 같음
var x
console.log(x)
x = 1

// ---
console.log(x)
x = 1 // ReferenceError
// var가 없으므로 변수의 선언 자체가 이루어지지 않았음
```

### Hoisting - function

- function도 hoisting의 대상
- 함수의 선언 ≠ 값의 초기화

### Function, Lexical scope

- 코드의 어떤 식별자가 실제로 어떤 값이 가리키는지를 결정하는 것을 **binding** 이라 함
- 자바스크립트에서의 binding은 **Lexical scope**를 통해 이루어짐

  = 안쪽에서 바깥쪽 변수에 접근할 수 있다는 뜻

```jsx
function foo() {
  // outer scope
  let x = 1
  function bar() {
    // inner scope
    console.log(x) // 가장 가까운 스코프에서 일치하는 변수에 binding 됨
  }
}

// ---
function foo() {
  var x = 'Hello'
  console.log(x) // 'Hello'
}

console.log(x) // ReferenceError
// Lexical scope에서는 밖에서 안을 참조할 수는 없음

// ---
var x = 'Hello'

function foo() {
  console.log(x) // 'Hello'
}

console.log(x) // 'Hello'

// ---
var x = 1
if (true) {
  var x = 2
}
console.log(x) // 2
// var는 block scoping의 대상이 아님
// 그러나 let과 const는 block scoping이 됨
```

## Closure

- closure = function + environment
- closure는 function이 하나 생길 때(선언)마다 하나씩 생김
- environment는 함수 자신을 둘러싼, 접근할 수 있는 모든 스코프를 뜻함
- closure는 higher-order function(ex. and 함수)을 만드는 데 유용

```jsx
function and(x) {
  return function print(y) {
    return x + ' and ' + y
  }
}

const saltAnd = and('salt')
console.log(saltAnd('pepper')) // salt and pepper
console.log(saltAnd('sugar')) // salt and sugar

// and 함수로 만들어진 saltAnd의 closure는
// 함수 : print, 환경 : x -> "salt"

const waterAnd = and('water')
console.log(waterAnd('juice')) // water and juice
```

```jsx
function foo() {
  function bar() {}
  function baz() {}
}
foo()

// closure는 총 몇개 생성?
// 3개 (foo, bar, baz)

// ---

function foo() {
  function bar() {}
  function baz() {}
}
foo()
foo()

// closure는 총 몇개 생성?
// 5개 (foo, bar, baz, bar, baz)
// bar, baz는 이미 선언된 것으로 착각할 수 있으나 X
```

### VScode-Debug 활용

```json
// .vscode/launch.json
// 구성 추가 -> Node.js : Launch via npm
{
  "configurations": [
    {
      "name": "Launch via NPM",
      "request": "launch",
      "runtimeArgs": ["run-script", "debug"],
      "runtimeExecutable": "npm",
      "skipFiles": ["<node_internals>/**"],
      "type": "pwa-node"
    }
  ]
}

// package.json
// 왼쪽 탭 디버그
{
	"scripts": {
    "debug": "node src/main.js"
  },
}
```

## Prototype

- prototype chain 개념

  = `me.toString()`은 어디에서? me 객체에서는 존재 X → `__proto__` 존재 X → `__proto__` 존재 O

```jsx
// class를 정의하는데 function 사용?
// class 키워드가 존재하지만 존재하기 전에는 function을 이용해 정의했음
// prototype을 기반으로 한 function
// new로 선언하면 function은 생성자 역할
function Student(name) {
  this.name = name
}

Student.prototype.greet = function greet() {
  return `Hi, ${this.name}!`
}

const me = new Student('Jiheon')
console.log(me) // Student { name: 'Jiheon' }
console.log(me.greet()) // Hi, Jiheon!

// $ me.name 'Jiheon'
// $ me.toString() '[object Object]'
```

```jsx
// 고전
function Person(name) {
  this.name = name
}

Person.prototype.greet = function greet() {
  return `Hi, ${this.name}!`
}

function Student(name) {
  this.__proto__.constructor(name)
}

Student.prototype.study = function study() {
  return `${this.name} is studyung.`
}

Object.setPrototypeOf(Student.prototype, Person.prototype)

const me = new Student('Jiheon')
console.log(me.greet())
console.log(me.study())

console.log(me instanceof Student)
console.log(me instanceof Person)

const anotherPerson = new Person('Foo')
console.log(anotherPerson instanceof Student)
console.log(anotherPerson instanceof Person)

console.log([] instanceof Array, [] instanceof Object)
```

- Class도 결국 prototype chain을 사용

```jsx
// 변경
class Person {
  constructor(name) {
    this.name = name
  }

  greet() {
    return `Hi, ${this.name}.`
  }
}

class Student extends Person {
  constructor(name) {
    super(name)
  }

  study() {
    return `${this.name} is studying.`
  }
}

const me = new Student('Jiheon')
console.log(me.study())
console.log(me.greet())
```

## 모던 JavaScript

### let, const

- `let` 과 `const` 는 ES2015(ES6)에 추가된 **변수 선언** 키워드
- hoisting 규칙이 없고, block scoping을 지원

### Spread syntax

- ES2015에서 새로 추가됨
- 병합, 구조 분배 할당(destructuring) 등에 다양하게 활용

### Spread operator - object merge

```jsx
const personalData = {
  nickname: 'JH',
  email: 'wlgjsdl0@gmail.com',
}

const publicData = {
  age: 23,
}

const user = {
  ...personalData,
  ...publicData,
}

// ---

const overrides = {
  DATABASE_HOST: 'myhost.com',
  DATABASE_PASSWORD: 'mypassword',
}

const config = {
  DATABASE_HOST: 'default.host.com',
  DATABASE_PASSWORD: '****',
  DATABASE_USERNAME: 'myuser',
  ...overrides, // 순서 중요! 앞으로 되면 덮어쓰기 안됨
}
/*
{
	DATABASE_HOST: 'myhost.com',
	DATABASE_PASSWORD: 'mypassword',
	DATABASE_USERNAME: 'myuser',
}
*/

// ---

const shouldOverride = false

const user = {
  ...{
    nickname: 'JH',
    email: 'foo',
  },
  ...{
    age: 23,
  },
  ...(shouldOverride // true이면 덮어씌우기
    ? {
        email: 'wlgjsdl0@gmail.com',
      }
    : null),
}
```

### Spread operator - object rest

```jsx
const user = {
  nickname: 'JH',
  age: 23,
  email: 'wlgjsdl0@gmail.com',
}

const { nickname, ...personalData } = user
console.log(personalData) // { age: 23, email: 'wlgjsdl0@gmail.com' }
```

### Spread operator - array merge

```jsx
const pets = ['dog', 'cat']
const predators = ['wolf', 'cougar']
const animals = [...pets, ...predators]
console.log(animals) // ['dog', 'cat', 'wolf', 'cougar']
```

### Spread operator - array rest

```jsx
const [head, ...rest] - [1, 2, 3]
console.log(head)  // 1
console.log(rest)  // [2, 3]

// ---

function foo(head, ...rest) {
	console.log(head)
	console.log(rest)
}

foo(1, 2, 3, 4)
// 1
// [2, 3, 4]
```

### Functional approach

```jsx
/**
 * A. 30대 미만이 한 명이라도 사는 모든 도시
 * B. 각 도시별로 개와 고양이를 키우는 사람의 수
 */

// 고전 방식
function solveA() {
  /** @type {string[]} */
  const cities = []

  for (const person of people) {
    if (person.age < 30) {
      if (!cities.find((city) => person.city === city)) {
        cities.push(person.city)
      }
    }
  }

  return cities
}

// 모던 방식
function solveAModern() {
  const allCities = people
    // .filter((person) => person.age < 30)
    .filter(({ age }) => age < 30)
    // .map((person) => person.city)
    .map(({ city }) => city)
  const set = new Set(allCities)
  return Array.from(set)
}

console.log('solveA', solveA())
console.log('solveAModern', solveAModern())
```

```jsx
/** @typedef {Object.<string, Object.<string, number>>} PetsOfCities */

function solveB() {
  /** @type {PetsOfCities} */
  const result = {}

  for (const person of people) {
    const { city, pet: petOrPets } = person

    if (petOrPets) {
      const petsOfCity = result[city] || {}

      if (typeof petOrPets === 'string') {
        const pet = petOrPets
        const origNumPetsOfCity = petsOfCity[pet] || 0
        petsOfCity[pet] = origNumPetsOfCity + 1
      } else {
        for (const pet of petOrPets) {
          const origNumPetsOfCity = petsOfCity[pet] || 0
          petsOfCity[pet] = origNumPetsOfCity + 1
        }
      }

      result[city] = petsOfCity
    }
  }

  return result
}

function solveBModern() {
  return people
    .map(({ pet: petOrPets, city }) => {
      const pets =
        (typeof petOrPets === 'string' ? [petOrPets] : petOrPets) || []

      return {
        city,
        pets,
      }
    })
    .flatMap(({ city, pets }) => pets.map((pet) => [city, pet]))
    .reduce((/** @type {PetsOfCities} */ result, [city, pet]) => {
      if (!city || !pet) {
        return result
      }

      return {
        ...result,
        [city]: {
          ...result[city],
          [pet]: (result[city]?.[pet] || 0) + 1,
        },
      }
    }, {})
}

console.log('solveB', solveB())
console.log('solveBModern', solveBModern())
```

### Promise

```jsx
function sleep(duration) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(undefined)
    }, duration)
  })
}

sleep()
  .then((value) => {
    console.log(value)
    return sleep()
  })
  .then((value) => {
    console.log(value)
    return sleep()
  })
  .then((value) => {
    console.log(value)
    return sleep()
  })
  .then((value) => {
    console.log(value)
    return sleep()
  })

sleep()

// ---

// @ts-check

const fs = require('fs')

/**
 * @param {string} fileName
 */
function readFileInPromise(fileName) {
  return new Promise((resolve, reject) => {
    fs.readFile(fileName, 'utf-8', (error, value) => {
      if (error) {
        reject(error)
      }
      resolve(value)
    })
  })
}

// promises 형태의 API를 지원
fs.promises.readFile('.gitignore', 'utf-8').then((value) => console.log(value))

readFileInPromise('.gitignore').then((value) => console.log(value))
```

### async & await

- 위의 예제 코드를 변환
- async & await 에서는 에러 처리는 ? `try, catch` 사용

```jsx
/**
 * @param {number} duration
 */
async function sleep(duration) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(undefined)
    }, duration)
  })
}

async function main() {
  console.log('first')
  await sleep(1000)
  console.log('second')
  await sleep(1000)
  console.log('third')
  await sleep(1000)
  console.log('finish!')
}

main()

// ----

// @ts-check

const fs = require('fs')

async function main() {
  try {
    const result = await fs.promises.readFile('.gitignora', 'utf-8')
    console.log(result)
  } catch (error) {
    console.log('error', error)
  }
}

main()
```

### Polyfill

- JS standard library에 표준으로 등록되어 있으나, 아직 브라우저나 Node.js에서 구현되지 않은 기능을 미리 써 볼 수 있도록 만들어진 구현체

  ex) core.js

  ref) [node.green](http://node.green) : Node.js Support

```bash
$ npm install core-js
```

```jsx
// @ts-check

require('core-js')

const complicatedArray = [1, [2, 3]]
const flattendArray = complicatedArray.flat()

console.log(flattendArray) // [1, 2, 3]
```

### Transpile

- 코드를 A 언어 → B 언어로 변환하는 작업
- 자바스크립트의 경우 보통 구형 런타임(브라우저, 혹은 구버전 Node 등)에서 신규 문법적 요소(optional, chaining 등)를 활용하기 위해 사용
- **신규 언어 스펙(ES6+)에서 구형 언어 스펙(ES5 등) 으로 트랜스파일을 할 때** 주로 사용
- 자바스크립트 대상으로 하는 트랜스파일러는 Babel, tsc(TypeScript Compiler), ESBuild 등

## 프레임워크 없이 RESTful API 서버

- HTTTPie를 이용한 테스팅

  - `brew install httpie` or `apt-get install httpie`
  - ex) `http POST [localhost:3000/posts](http://localhost:3000/posts) title=foo content=bar --print=hHbB`

    → `—print` : req, res를 출력, `hb` : 응답 / `HB` : 요청 에 대한 헤더와 바디

- JSDoc : 타입스크립트가 파싱을 자동으로 하여 타입 정의를 표기할 수 있음(= 타입 세이프티)

```jsx
// main.js
// @ts-check

const http = require('http')
const { routes } = require('./api')

const server = http.createServer((req, res) => {
  async function main() {
    const route = routes.find(
      (_route) =>
        req.url &&
        req.method &&
        _route.url.test(req.url) &&
        _route.method === req.method
    )

    if (!req.url || !route) {
      res.statusCode = 404
      res.end('Not found.')
      return
    }

    const regexResult = route.url.exec(req.url)

    if (!regexResult) {
      res.statusCode = 404
      res.end('Not found.')
      return
    }

    /** @type {Object.<string, *> | undefined} */
    const reqBody =
      (req.headers['content-type'] === 'application/json' &&
        (await new Promise((resolve, reject) => {
          req.setEncoding('utf-8')
          req.on('data', (data) => {
            try {
              resolve(JSON.parse(data))
            } catch {
              reject(new Error('Ill-formed json'))
            }
          })
        }))) ||
      undefined

    const result = await route.callback(regexResult, reqBody)
    res.statusCode = result.statusCode

    if (typeof result.body === 'string') {
      res.end(result.body)
    } else {
      res.setHeader('Content-Type', 'application/json; charset=utf-8')
      res.end(JSON.stringify(result.body))
    }
  }

  main()
})

const PORT = 3000

server.listen(PORT, () => {
  console.log(`The server is listening at port: ${PORT}`)
})
```

```jsx
// api.js
// @ts-check

/**
 * @typedef Post
 * @property {string} id
 * @property {string} title
 * @property {string} content
 */

/**
 * @typedef APIResponse
 * @property {number} statusCode
 * @property {string | Object} body
 */

/**
 * @typedef Route
 * @property {RegExp} url
 * @property {'GET' | 'POST'} method
 * @property {(matches: string[], body: Object.<string, *> | undefined) => Promise<APIResponse>} callback
 */

const fs = require('fs')

const DB_JSON_FILENAME = 'database.json'

/** @returns {Promise<Post[]>} */
async function getPosts() {
  const json = await fs.promises.readFile(DB_JSON_FILENAME, 'utf-8')
  return JSON.parse(json).posts
}

/**
 * @param {Post[]} posts
 */
async function savePosts(posts) {
  const content = {
    posts,
  }

  return fs.promises.writeFile(
    DB_JSON_FILENAME,
    JSON.stringify(content),
    'utf-8'
  )
}

/** @type {Route[]} */
const routes = [
  {
    url: /^\/posts$/,
    method: 'GET',
    callback: async () => ({
      statusCode: 200,
      body: await getPosts(),
    }),
  },

  {
    url: /^\/posts\/([a-zA-Z0-9-_]+)$/,
    method: 'GET',
    callback: async (matches) => {
      const postId = matches[1]
      if (!postId) {
        return {
          statusCode: 404,
          body: 'Not found',
        }
      }

      const posts = await getPosts()
      const post = posts.find((_post) => _post.id === postId)

      if (!post) {
        return {
          statusCode: 404,
          body: 'Not found',
        }
      }

      return {
        statusCode: 200,
        body: post,
      }
    },
  },

  {
    url: /^\/posts$/,
    method: 'POST',
    callback: async (_, body) => {
      if (!body) {
        return {
          statusCode: 400,
          body: 'Ill-formed request.',
        }
      }

      /** @type {string} */
      /* eslint-disable-next-line prefer-destructuring */
      const title = body.title
      const newPost = {
        id: title.replace(/\s/g, '_'),
        title,
        content: body.content,
      }

      const posts = await getPosts()
      posts.push(newPost)
      savePosts(posts)

      return {
        statusCode: 200,
        body: newPost,
      }
    },
  },
]

module.exports = {
  routes,
}
```

### Require & Module, Module Resolution

- CommonJS modules : `require`
  - node standard library에 있는 모듈은 절대경로를 지정해 가져옴
  - 프로젝트 내의 다른 파일은 상대경로를 지정해 가져옴
  - 절대경로를 지정하면 `module.paths` 의 경로들을 순서대로 검사하여 해당 모듈을 가져옴
- ECMAScript modules: `export` , `import` (\*.mjs)
- `require('decamelize')` , `require('decamelize/index')` 와 동일, 즉 index.js를 참고

### Package manager & package.json

- npm, yarn : 패키지 매니저

  - `npm install -g yarn` : yarn 설치
  - `yarn add decamelize` : yarn을 통한 라이브러리 설치, yarn.lock 파일 생성 (=package-lock.json)
  - `remove` , `-D` , `yarn eslint` , `yarn run lint` etc
  - Ultra Fast, 스크립트 실행 편리 장점

- package.json : 대략적인 버전 정보
  - `^` , `~` : Semantic Versioning
- package-lock.json : 실제로 설치된 버전 정보

- `--save-dev` : 개발하는 환경에서만 필요한 패키지 정보
- 라이브러리 종속성으로 불 필요한 라이브러리까지 모두 설치하여 용량을 차지하게 됨

  - `du -h node_modules` : 용량 확인 커맨드
  - `npm install --production` : 프로덕션 서버에서 필요한 라이브러리만 설치

- `npm install decamelize@3.1.0` : `@` 로 버전을 명시하여 설치
- `npm update decamelize` | `^3.1.0` : 최신 Minor 버전으로 업데이트 3.1.0 ⇒ 3.2.0
- `npm update decamelize` | `~3.1.0` : 최신 Patch 버전으로 업데이트 3.1.0 ⇒ 3.1.1

- `./node_modules/.bin/eslint src/**/*` : 바이너리 파일 실행 예시
  - package.json 내 에서는 scripts에 추가하여 `eslint src/**/*` 로 사용 가능

## Stream

- stream은 스트림 가능한 소스로부터 데이터를 작은 청크로 쪼개 처리할 수 있게 함
- 큰 데이터를 처리해야 하거나, 비동기적으로만 얻을 수 있는 데이터르 처리해야 할 때 유용
- `data`, `error`, `end` 등의 이벤트 핸들러를 달아 처리
    - 특별히 지정하지 않으면 data는 Buffer가 됨

```jsx
const fs = require('fs)

// const rs = fs.createReadStream('file.txt')
const rs = fs.createReadStream('file.txt', {
	encoding: 'utf-8',
})

rs.on('data', data => {
	// ...
})
rs.on('error', error => { /* ... */ })
rs.on('end', () => { /* ... */ })
```

### Stream의 종류

- Readable
    - 스트림으로부터 읽을 수 있음
        - `fs.createReadStream`
        - `process.stdin`
        - 서버 입장의 HTTP 요청
        - 클라이언트 입장의 HTTP 응답

- Writable
    - 스트림에 출력할 수 있음
        - `fs.createWriteStream`
        - `process.stdout`
        - 클라이언트 입장의 HTTP 요청
        - 서버 입장의 HTTP 응답

- Duplex
    - 이 스트림에 입력을 받을 수 있고, 출력을 보낼 수도 있음
        - TCP sockets
        - zlib streams
        - crypto streams

- Transform
    - 입력받은 스트림을 변환해 새로운 스트림으로 만듬
        - zlib streams
        - crypto streams

### Stream을 사용할 때와 아닐 때의 퍼모먼스 차이

- `fs.readFileSync` 로 처리할 때 해당 파일을 통째로 RAM으로 올려 순차적으로 읽고 완료될 때 까지 버퍼를 내려놓지 못함, 따라서 상당한 메모리를 사용함
- `fs.createReadStream` 는 큰 파일을 작은 chunk 단위로 쪼개 해당 chunck 사이즈만큼 RAM으로 올려 chunk 단위로 처리함, 따라서 큰 파일을 처리할 때는 stream으로 처리해야 메모리 측면에서 유리
- 네트워크 입력 받거나 파일을 전송, 파일을 업로드할 때 등 stream 활용하는 것이 좋음

### Stream 처리 시 유의점

- json : 어디에서 chunk가 짤릴 지 예측할 수 없음

    ex) `{"data": 4}\n{"da`

### Pipeline과 Promise

- pipeline은 transform stream을 쉽게 활용하게 도와줌

```jsx
// @ts-check

/*
stream.pipeline(
  fs.createReadStream('local/big-file'),
  zlib.createGzip(),
  fs.createWriteStream('local/big-file.gz')
)
*/

const fs = require('fs')
const stream = require('stream')
const zlib = require('zlib')
const util = require('util')

async function gzip() {
  return util.promisify(stream.pipeline)(
    fs.createReadStream('local/big-file'),
    zlib.createGzip(),
    fs.createWriteStream('local/big-file.gz')
  )
}

async function gunzip() {
  return util.promisify(stream.pipeline)(
    fs.createReadStream('local/big-file.gz'),
    zlib.createGunzip(),
    fs.createWriteStream('local/big-file.unzipped')
  )
}

async function main() {
  await gzip()
  await gunzip()
}

main()
```
