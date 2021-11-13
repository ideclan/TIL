# TypeScript

JavaScript(ES5, ES6 등)의 확장판입니다.  
TypeScript는 정적 타입을 지원하므로 컴파일 단계에서 오류를 포착할 수 있는 장점이 있습니다.
명시적인 정적 타입 지정은 개발자의 의도를 명확하게 코드로 기술할 수 있게 됩니다.

> 기존에는 Node.js + Express 프로젝트에서 `ES6`를 사용하기 위해서는
> 별도의 Transpiler인 Babel이 필요했습니다.
> TypeScript에서 ES5, ES6를 사용할 수 있으므로 Babel을 사용하지 않아도 됩니다.

```bash
$ npm install -g typescript
```

## TypeScript 설정 파일

프로젝트 루트 경로내에 `tsconfig.json` 파일을 생성합니다.

```json
{
  "compilerOptions": {
    "target": "es5",
    "module": "commonjs",
    "outDir": "dist",
    "strict": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules"]
}
```

> `$ tsc --init` 을 통해 `tsconfig.json` 파일을 초기화하여 생성하셔도 좋습니다.

` $ tsc` 명령어를 통해 타입스크립트 설정 파일을 참고하여 `src/`내에 `.ts` 파일들을 변환합니다. 변환된 파일들은 `dist/` 내에 생성됩니다.

# Express 프로젝트 설정

`express-generator`를 통해 프로젝트를 생성하여 기존 파일들을 `src/`로 이동시킵니다.
그리고 앞에서 TypeScript 설정 파일을 참고하여 루트 경로내에 `tsconfig.json` 파일을 생성합니다.

```bash
$ npm install -g express-generator

$ express myapp
```

현재 프로젝트 구조는 다음과 같습니다.

```
|-- src
     |-- bin
     |   `-- www
     |--public
     |--routes
     |   `-- index.js
     |   `-- users.js
     |--views
     |--app.js
|-- tsconfig.json
```

## TypeScript 관련 패키지 설치

- `@types/node` : Node.js 타입 추가
- `@types/express` : Express 타입 추가
- `ts-node` : 사전 컴파일 없이 Node.js에서 TypeScript를 직접 실행
- `typescript` : TypeScript 설치

```bash
$ npm install --save-dev @types/node @types/express ts-node typescript
```

## Package.json 설정

`package.json` 내에 `scripts`를 추가합니다.

- `dev` : 주로 개발 환경에서 사용하며, `ts-node` 실행 결과를 `nodemon`으로 넘겨주어 함께 사용이 가능합니다.
- `copy-files` : `tsc`로 빌드 시 `.ts`가 아닌 파일들은 제외되므로, 정적 파일들을 복사하여 추가하는 부분입니다.
- `build` : `tsc` 명령어를 통해 컴파일하고 `copy-files`와 함께 빌드를 진행합니다.
- `start` : 빌드된 `dist/bin/www.js` 파일을 실행합니다.

```json
{
  "scripts": {
    "dev": "nodemon --exec ts-node src/bin/www.ts",
    "copyfiles": "cp -r src/public/ dist/public/ && cp -r src/views/ dist/views/",
    "build": "tsc && npm run copyfiles",
    "start": "node dist/bin/www.js"
  }
}
```

# TypeScript + ESLint + Prettier

TypeScript 또한 ESLint와 Prettier를 함께 사용이 가능합니다.

## 패키지 설치

- ESLint 와 Prettier를 설치합니다.

```bash
$ npm install --save-dev eslint prettier
```

- ESLint와 Prettier 관련 플러그인을 설치합니다.

```bash
$ npm install --save-dev eslint-config-airbnb-base eslint-config-prettier eslint-plugin-import eslint-plugin-prettier
```

- TypeScript 관련 플러그인을 설치합니다.

```bash
$ npm install --save-dev @typescript-eslint/eslint-plugin @typescript-eslint/parser
```

## ESLint 설정 파일

프로젝트 루트 경로내에 `.eslintrc.json` 파일을 생성합니다.

```json
{
  "parser": "@typescript-eslint/parser",
  "plugins": ["import", "@typescript-eslint", "prettier"],
  "extends": [
    "airbnb-base",
    "plugin:import/errors",
    "plugin:import/warnings",
    "plugin:@typescript-eslint/recommended",
    "plugin:prettier/recommended"
  ],
  "parserOptions": {
    "ecmaVersion": 6,
    "sourceType": "module"
  },
  "env": {
    "browser": true,
    "node": true
  },
  "ignorePatterns": ["node_modules/"],
  "rules": {
    "prettier/prettier": "error",
    "import/extensions": [
      "error",
      "ignorePackages",
      {
        "js": "never",
        "jsx": "never",
        "ts": "never",
        "tsx": "never"
      }
    ]
  },
  "settings": {
    "import/resolver": {
      "node": {
        "extensions": [".js", ".jsx", ".ts", ".tsx"]
      }
    }
  }
}
```

> Prettier 설정 파일은 다루지 않았지만, 동일하게 프로젝트 루트 경로내에 `.prettierrc.json` 파일을 생성하여 설정이 가능합니다.
