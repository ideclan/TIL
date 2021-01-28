## Dynamic language

- 파이썬은 동적 프로그래밍 언어로 변수의 타입은 고정되어 있지 않습니다. 따라서 타입을 명시적으로 표시할 필요가 없습니다.

```python
a = 1
type(a)    # <type ‘int’>

a = "Hi~"
type(a)    # <type ‘str’>
```

- 반면 정적 프로그래밍 언어인 C나 Java 에서 같은 예시의 코드를 실행시켰을 때에는 컴파일 에러를 맞이하게 됩니다.

```c
int a = 1;
 a = "Hi~";    // compile error
```

- 따라서 파이썬은 다른 언어에 비해 유연하다고 할 수 있습니다.
- 하지만 만약 타입 변경 코드가 1,000 줄 이상이 된다면

    → **예상하지 못한 타입이 변수에 할당 또는 치명적인 버그로 이어질 수 있습니다.**

## Type Annotation (타입 주석)

- PEP 484 ( Type hint 지원 )

    → [https://www.python.org/dev/peps/pep-0484/](https://www.python.org/dev/peps/pep-0484/)

- Python 3.5 버전에는 **함수의 인자와 반환값**에 대한 타입 힌트가 처음으로 도입했습니다.

```python
def greeting(name: str) -> str:
   return 'Hello ' + name
```

- 이후 3.6 버전에는 인자와 반환값 만이 아니라 **변수**에도 타입 힌트 표기 가능해졌습니다.

```python
def greeting(name: str) -> str:
   s: str = 'Hello ' + name
   return s
```

- 기존 Type hint 는 타입 표시 코드가 IDE나 Linter에서 오류라고 판단하는 문제가 생겨
- 문제점을 보완한 Type Annotation을 도입하여 IDE나 Linter가 해석할 수 있도록 해결했습니다.

## 도입 기대효과

- 코드 내에 타입을 표시하려는 주석 불필요하게 됩니다.
- 다른 개발자가 코드를 읽기 수월해지며
- 예상하지 못한 타입을 방지하여 코드 품질을 향상시킬 수 있습니다.

```python
# 사용 전
def repeat(message, times = 2):
   # type: (str, int) -> list
   return [message] * times

# 사용 후
def repeat(message: str, times: int = 2) -> list:
   return [message] * times
```

## 타입 주석 활용 개발환경

- VSCode + Python ( Extension )

    ![_2021-01-08__4 21 09](https://user-images.githubusercontent.com/48443734/106098473-71eb0a00-617c-11eb-9aeb-d6a0e917fd0a.png)


## 변수 Type Annotation

- 변수 이름 뒤에 콜론 ( : ) 을 붙이고 타입을 명시합니다.

```python
name: str = "Jiheon Lee"

age: int = 23

emails: list = ["test@abc.com", "test2@abc.com"]

subject: dict = {
   "frosh": "Python",
   "sophomore": "DataBase",
   "junior": "C"
}
```

## 함수 Type Annotation

- 함수 인자는 변수와 동일한 문법입니다.
- 반환값은 화살표 ( -> ) 를 사용하고
- 콜론 ( : ) 은 뒤에만 한 칸, 화살표 ( -> ) 는 앞뒤로 한 칸 띄어야 합니다.

```python
def add(a: int, b: int) -> str:
   result: int = a + b
   return str(result)
```

## typing module

- 좀 더 복잡한 Type Annotation 을 추가해야 할 때는 typing module 을 사용할 수 있습니다.

```python
from typing import List, Set, Dict, Tuple

nums: List[int] = [1, 2, 3]

unique_nums: Set[int] = {5, 6}

vision: Dict[str, float] = {"left": 0.3, "right": 0.4}

jiheon: Tuple[int, str, List[float]] = (23, "Jiheon Lee", [0.3, 0.4])
```

## Type Annotation 검사

- Type Annotaion 을 검사는 `__**annotations__**` 를 사용합니다.

```python
# test.py
def add(a: int, b: int) -> str:
   result: int = a + b
   return str(result)

print(add.__annotations__)

$ python test.py
{‘a’: <class ‘int’>, ‘b’: <class ‘int’>, ‘return’: <class ‘str’>}
```