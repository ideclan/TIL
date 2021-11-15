Node.js 개발 환경에서 프로젝트를 진행하던 도중에 ES6의 중요성을 깨닫고 도입하게 되었습니다. ES6 모듈 부분에서 기존 `require` & `module.exports` 를 `import` & `export` 로 변경 후 실행해보니 에러가 저를 맞이했습니다.

![](https://images.velog.io/images/jiheon/post/dfced76d-bd12-4620-8eb7-fa776c1ec6ef/RLRlP6kQU.png)

# Node.js에서 ES6 코드 실행 오류

Node.js의 `require` 구문을 ES6의 `import` 구문으로 변경하여 실행하면 아래와 같은 에러가 발생합니다.

```bash
SyntaxError: Cannot use import statement outside a module
    at wrapSafe (internal/modules/cjs/loader.js:1047:16)
    at Module._compile (internal/modules/cjs/loader.js:1097:27)
    at Object.Module._extensions..js (internal/modules/cjs/loader.js:1153:10)
    at Module.load (internal/modules/cjs/loader.js:977:32)
    at Function.Module._load (internal/modules/cjs/loader.js:877:14)
    at Function.executeUserEntryPoint [as runMain] (internal/modules/run_main.js:74:12)
    at internal/main/run_main_module.js:18:47
```

**Why?**
Node.js는 CommonJS 기반 모듈 시스템을 사용하기 때문에 지원하지 않는다고 합니다.

**해결방안?**

1. 파일의 확장자를 `.mjs` 로 변경 후 `--experimental-modules` 옵션과 함께 실행 (실험적인 기능으로 권장 X)
   **2. Babel 사용**

# Babel: JavaScript Transpiler

- C언어 코드를 실행하려면 `compile` 하는 것과 비슷하면서도 조금 다름
- `ES6`로 작성된 코드를 `ES5`로 변환하는데 사용
- Babel은 JavaScript Transpiler 중에서 가장 널리 사용

> Babel is a toolchain that is mainly used to convert ECMAScript 2015+ code into a backwards compatible version of JavaScript in current and older browsers or environments.
> 바벨은 주로 ECMAScript 2015+ 코드를 현재 및 과거의 브라우저와 같은 환경에서 호환되는 버전으로 변환하는데 주로 사용되는 도구입니다.

```bash
$ npm install @babel/core --save-dev
```

## Babel CLI

Babel 커맨드 라인 도구 설치

```bash
$ npm install @babel/cli --save-dev
```

## Babel Preset 설정

- 어떻게 변환할지 Babel 설정이 필요
- 가장 범용적인 Preset인 `env` 사용
- `env` Preset은 ES2015 이상의 최신 JavaScript 문법을 해석

```bash
$ npm install @babel/preset-env --save-dev
```

프로젝트 루트 경로 내에 `.babelrc` 생성

```json
{
  "presets": ["@babel/env"]
}
```

또는 `.babelrc` 대신 `package.json` 내에 설정 가능

```json
"babel": {
  "presets": ["@babel/env"]
}
```

## Babel Node

`transpile` 과 함께 실행을 한번에 할 수 있도록 함

```bash
$ npm install @babel/node --save-dev
```

**package.json**

```json
"scripts": {
  "start": "babel-node app.js"
}
```

# References

[Node.js로 ES6 코드 실행하기 (Babel)](https://www.daleseo.com/js-babel-node/)
