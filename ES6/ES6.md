### ES6?

- =ECMAScript 2015
- ES5(2009)에서 ES6으로 2015년도에 업데이트
- 최신 프론트엔드 웹 프레임워크(React, Vue)에서 권고하는 언어 형식
- ES5에 비해 문법이 간결하여 훨씬 편하게 코딩이 가능

### Babel

- 구 버전 브라우저 중에서는 ES6의 기능을 지원하지 않는 브라우저가 있으므로 transpiling 이 필요
- ES6의 문법을 각 브라우저의 호환 가능한 ES5로 변환하는 컴파일러

### const & let - 변수 선언 방식

- 블록 단위 `{ }`로 변수의 범위가 제한되었음
- `const` : 한번 선언한 값에 대해서 변경할 수 없음 (상수 개념)
- `let` : 한번 선언한 값에 대해서 다시 선언할 수 없음

### ES5 - 변수의 Scope

- Scope : 블록의 유효범위
- 기존 JavaScript(ES5)는 `{ }` 에 상관없이 스코프가 설정됨 (=전역변수)

### ES5 - Hoisting

- Hoisting : 선언한 함수와 변수를 가장 상단에 있는 것처럼 인식
- 코드의 라인 순서와 관계 없이 함수 선언식과 변수를 위한 메모리 공간을 먼저 확보
- 따라서, `function a( )` 와 `var` 는 코드의 최상단으로 끌어 올려진 것(hoisted) 처럼 보임
- 함수 표현식은 포함되지 않음

```jsx
// 함수 선언식
function myNumber() {
  return 10;
}
myNumber(); // 5
function myNumber() {
  return 5;
}

// 함수 표현식
var num1 = function myNumber() {
  return 10;
};
console.log(num1); // 10
var num1 = function myNumber() {
  return 5;
};
```

```jsx
var sum = 5;
sum = sum + i;

function sumAllNumbers() {
  // ...
}

var i = 10;

// 실행결과 : NaN

// 해당 코드는 실제 동작되는 순서는 다음과 같다.
// #1 - 함수 선언식과 변수 선언을 hoisting
var sum;
function sumAllNumbers() {
  // ...
}
var i;

// #2 - 변수 대입 및 할당
sum = 5;
sum = sum + i;
i = 10;
```

### ES6 - `{ }` 단위로 변수의 범위가 제한

```jsx
let sum = 0;
for (let i = 1; i <= 5; i++) {
  sum = sum + i;
}
console.log(sum); // 10
console.log(i); // i is not defined
```

### ES6 - `const` 로 지정한 값 변경 불가능

- 하지만 객체나 배열의 내부는 변경할 수 있음

```jsx
const a = 10;
a = 20; // Error
```

```jsx
const a = {};
a.num = 10;
console.log(a); // {num: 10}

const a = [];
a.push(20);
console.log(a); // [20]
```

```jsx
function f() {
  {
    let x;
    {
      // 새로운 블록안에 새로운 x의 스코프가 생김
      const x = 'hi';
      x = 'hello'; // 위에 이미 const로 x를 선언했으므로 다시 값을 대입하면 에러
    }
    // 이전 블록 범위로 돌아왔기 때문에 let x 에 해당하는 메모리에 값을 대입
    x = 'bye';
    let x = 'see you later'; // Error
  }
}
```

### Arrow Function - 화살표 함수

- 함수를 정의할 때 `function` 대신 `=>` 로 사용
- 콜백 함수의 문법을 간결화

```jsx
// ES5
var sum = function (a, b) {
  return a + b;
};

var arr = ['a', 'b', 'c'];
arr.forEach(function (value) {
  console.log(value);
});

// ES6
var sum = (a, b) => {
  return a + b;
};

var arr = ['a', 'b', 'c'];
arr.forEach((value) => console.log(value));
```

### Enhanced Object Literals - 향상된 객체 리터럴

- 객체의 속성을 메서드로 사용할 때 `function` 예약어를 생략하고 생성 가능

```jsx
var dictionary = {
  words: 100,
  // ES5
  lookup: function () {
    console.log('find words');
  },
  // ES6
  lookup() {
    console.log('find words');
  },
};
```

- 객체의 속성과 값이 동일할 때 축약 가능

```jsx
var words = 10;
var dictionary = {
  // words: words,
  words,
};
```

### Modules - 자바스크립트 모듈화 방법

- 자바스크립트 모듈 로더 라이브러리(AMD, Commons JS) 기능을 JS 언어 자체에서 지원
- 호출되기 전까지는 코드 실행과 동작을 하지 않는 특징이 있음

```jsx
// libs/math.js
export function sum(x, y) {
  return x + y;
}
export var pi = 3.14;

// main.js
import { sum } from 'libs/math.js';
sum(1, 2);
```

- Vue.js 에서 `export default` 는 하나의 파일에서 한 번만을 export 하도록 허용

### ES6 Object Spread Operator

```jsx
let josh = {
	field: 'web',
	language: 'js'
};

let developer = {
	nation: 'korea',
	...josh
};

console.log(developer)
// [object Object] { field: "web", language: "js", nation: "korea" }
```
