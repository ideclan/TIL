여러 개발자들은 서로 다른 코드 스타일을 가지고 있습니다.  
혼자 프로젝트를 진행한다면 문제는 없지만, 함께 진행하는 개발자 수가 늘어남과 동시에  
각자 원하는 코드 스타일로 충돌이 일어나게 되고, 코드 스타일 통합을 하면서 큰 어려움을 겪게 됩니다.  
이때 ESLint 와 Prettier 를 도입한다면, 해당 문제 해결에 큰 도움이 될 수 있습니다.

# ESLint

코드 내에 문법 에러, 버그를 찾아 보고해주는 소스코드 분석기

```bash
$ npm install eslint --save-dev
```

# Prettier

정해진 규칙에 따른 코드 강제 formatter

```bash
$ npm install prettier --save-dev --save-exact
```

> `--save-exact` : 버전 업데이트로 생길 스타일 변화를 막기 위해서 사용 (Prettier 에서 사용 권장)

# ESLint & Prettier 설정하기

## 필요한 추가 Modules

```bash
# 필수사항
$ npm install --save-dev eslint-config-prettier eslint-plugin-prettier

# 선택사항
$ npm install --save-dev eslint-config-airbnb-base eslint-plugin-import
```

- `eslint-config-prettier` : ESLint 와 Prettier 의 충돌하는 설정들을 비활성화
- `eslint-plugin-prettier` : Prettier 의 format 오류를 ESLint 오류로 출력
- `eslint-config-airbnb` : Airbnb 의 code style 규칙, 리액트 관련 code style 이 포함되어 있으므로, 제외가 필요하다면 `eslint-config-airbnb-base` 사용
- `eslint-plugin-import` : 파일 경로와 함께 `import/export` 문에 관한 linting 에 도움

> code style 은 Airbnb, Standard, Google 중 원하는 것을 선택하여 사용하셔도 좋습니다.

## 프로젝트 설정

프로젝트 root 경로에 설정 파일들을 생성하여 구성합니다.

**.eslintrc.json**

```json
{
  "plugins": ["import", "prettier"],
  "extends": [
    "airbnb-base",
    "plugin:import/errors",
    "plugin:import/warnings",
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
    "prettier/prettier": "error"
  }
}
```

**.prettierrc.json**

```json
{
  "printWidth": 80,
  "tabWidth": 2,
  "useTabs": false,
  "semi": false,
  "singleQuote": true,
  "trailingComma": "all",
  "bracketSpacing": true,
  "arrowParens": "avoid"
}
```

> 자세한 옵션들은 아래 공식 문서를 참고해 주세요.
> [ESLint 공식 문서](https://eslint.org/docs/user-guide/configuring/), [Prettier 공식 문서](https://prettier.io/docs/en/options.html)

# VS Code 설정하기

VS Code > Marketplace > ESLint, Prettier 검색 후 설치

![vscode-extension](https://images.velog.io/images/jiheon/post/bfafdf98-aeb8-4ed3-93cd-71f67095dbab/_2021-07-09__11.58.36.png)

**settings.json**

```json
{
  "[javascript]": {
    "editor.formatOnSave": true,
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true
  }
}
```

# Husky & Lint-staged

여러명과 프로젝트 협업 시 누군가 잘못된 코드를 포함시키는 행위를 방지하도록 사용합니다.

## Husky

정해진 규칙에 맞는 코드가 아니라면 `git commit` 을 못하도록 합니다.

```bash
$ npm install husky@4 --save-dev
```

**package.json**

```json
{
  "husky": {
    "hooks": {
      "pre-commit": "eslint --fix && prettier --write"
    }
  }
}
```

## Lint-staged

모든 코드를 검사하는 Husky 의 단점을 보완하기 위해 사용합니다.
staged 된 코드들만 검사하도록 합니다.

```bash
$ npm install lint-staged --save-dev
```

**package.json**

```json
{
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged"
    }
  },
  "lint-staged": {
    "src/**/*.js": ["eslint --fix", "prettier --write"]
  }
}
```

# References

- [ESLint 설정 살펴보기](https://velog.io/@kyusung/eslint-config-2)
- [VScode Code Formater 인 Prettier 완벽 적용하기](https://uxgjs.tistory.com/150)
- [husky , lint-staged로 git hook하기 - 컨벤션 세팅](https://shiningjean.tistory.com/m/86)
