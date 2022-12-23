# 함수형 프로그래밍과 JavaScript ES6+

## 평가와 일급, 고차 함수

### 평가

코드가 계산되어 값을 만드는 것이다.

```javascript
console.log(1 + 2)  // 1 + 2는 3으로 평가된다
console.log((1 + 2) + 4)  // 1 + 2는 3으로 평가되고, 3 + 4는 7로 평가된다
console.log([1, 2 + 3])  // 2 + 3은 5로 평가되고, 배열 요소로 1과 5를 가진 배열로 평가된다
```

### 일급

값으로 다룰 수 있으며, 변수에 담을 수 있다. 그리고 함수의 인자 또는 결과로 사용될 수 있다.

```javascript
const a = 10;  // 10을 값으로 다루고, 변수 a에 담는다
const add10 = (a) => a + 10;  // a + 10은 함수의 결과로 사용된다
const r = add2(a)  // a는 add10 함수의 인자로 사용되고, 함수의 결과인 20을 변수 r에 담는다
```

### 일급 함수

함수를 값으로 다룰 수 있다. 즉, 변수에 함수를 담을 수 있으며, 함수의 인자 또는 결과로 함수가 사용될 수 있다.

JavaScript에서 함수가 일급이라는 성질을 이용해서 많은 조합성을 만들어 낼 수 있으며, 추상화의 좋은 도구로 사용될 수 있다.

```javascript
const add5 = (a) => a + 5;  // 함수를 변수 add5에 담는다
console.log(add5)  // (a) => a + 5, 함수의 인자로 함수가 사용된다
console.log(add5(5))  // 10

const f1 = () => () => 1;  // 함수의 결과로 함수가 사용된다
console.log(f1)  // () => () => 1

const f2 = f1();
console.log(f2)  // () => 1
console.log(f2())  // 1
```

### 고차 함수

함수를 값으로 다루는 함수이다. 고차 함수는 크게 2가지가 있다.

#### 함수를 인자로 받아서 실행하는 함수

```javascript
const apply1 = (f) => f(1);
const add2 = (a) => a + 2;
console.log(apply1(add2));  // 3, ((a) => a + 2)(1)
console.log(apply1((a) => a - 1));  // 0, ((a) => a - 1)(1)

const times = (f, n) => {
  let i = -1;
  while (++i < n) f(i);
}
times(console.log, 3);  // 0 1 2
times((a) => console.log(a + 10), 3)  // 10 11 12
```

#### 함수를 만들어 반환하는 함수

`addMaker()` 함수는 `(b) => a + b` 함수를 반환한다. 그리고 `addMaker()` 함수가 호출될 때, `(b) => a + b` 함수는 `a`를 기억하고 있다. 즉, `(b) => a + b` 함수는 클로저이며, `addMaker()` 함수는 클로저를 만들어 반환하는 함수이다.

> 클로저란?
> 
> 자신이 선언될 당시의 환경을 기억하는 함수이다.

```javascript
const addMaker = (a) => (b) => a + b;
const add10 = addMaker(10);
console.log(add10);  // (b) => a + b
console.log(add10(5))  // 15
```