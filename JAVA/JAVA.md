# Courses
## JAVA
- [Do it! 자바 프로그래밍 입문](https://www.inflearn.com/course/%EC%9E%90%EB%B0%94-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%EC%9E%85%EB%AC%B8/), 이지스퍼블리싱

# 변수와 자료형

## 2, 8, 10, 16 진수

- 숫자 10을 출력

```java
package chapter2;
public class BinaryTest {
		public static void main(String[] args) {
				int num = 10;
				int bNum = 0B1010;   // 2진수 0B
				int oNum = 012;      // 8진수 0
				int hNum = 0XA;      // 16진수 0X
				
				// 10
				System.out.println(num);
				System.out.println(bNum);
				System.out.println(oNum);
				System.out.println(hNum);
		}
}
```

## 정수 자료형

- `byte` : 1byte | 동영상, 음악 파일 등 실행 파일의 자료를 처리할 때 사용
- `short` : 2byte | 주로 C/C++ 언어와의 호환 시 사용
- `int` : 4byte | 자바에서 정수에 대한 기본 자료 형, 프로그램에서 사용하는 모든 숫자(리터럴)는 기본적으로 int 로 저장
- `long` : 8byte | 가장 큰 정수 자료형, 숫자뒤에 식별자  `L` 또는 `l` 을 붙여 long 자료형을 표시해야 함

```java
// 컴파일 에러
int num = 12345678900;
long num = 12345678900;

// long 자료형 표시
long num = 12345678900L;
```

## 문자 자료형

- `char` : 2byte
    - 인코딩 - 각 문자에 따른 특정한 숫자 값(코드 값)을 부여 | 자바는 **유니코드 UTF-16** 인코딩 사용
    - 디코딩 - 숫자 값을 원래의 문자로 변환

```java
char ch = 'A';
System.out.println(ch);      // A
System.out.println((int)ch)  // 65

int ch2 = 66;
System.out.println(ch2);     // 66
System.out.println((char)ch2)  // B
```

## 실수 자료형

- `float` : 4byte | 숫자뒤에 식별자 `F` 또는 `f` 을 붙여 float 자료형을 표시해야 함
- `double` : 8byte | 실수는 기본적으로 long 으로 처리

```java
double dNum = 3.14;
float fNum = 3.14;  // 컴파일 에러

float fNum = 3.14F;
```

## 논리 자료형

- `boolean` : 1byte

```java
boolean isMarried = false;
```

## 자료형 없이 변수 사용

- 자료형이 필요한 이유 - 변수를 선언할 때는 변수가 사용할 메모리 크기와 타입을 구분하기 위해
- 지역 변수 자료형 추론 - 변수에 대입되는 값을 보고 컴파일러가 추론

```java
package chapter2;
public class BinaryTest {
		public static void main(String[] args) {
				// 지역 변수로 자료형 추론이 가능
				var num = 10;  // int
				var dNum = 10.0;  // double
				var str = "hello";  // String

				num = 3.14;  // 컴파일 에러 - int 형으로 추론된 변수는 double 값을 다시 할당할 수 없음
		}
}
```

## 상수

- 변하지 않는 값 (cf 변수 : 변하는 값)
- 상수를 선언 : `final` 사용

```java
final double PI = 3.14;
final int MAX_NUM = 100;

PI = 3.15;  // 컴파일 에러 - final로 선언된 변수에 새로운 값을 할당할 수 없음
```

## 리터럴(literal)

- 프로그램에서 사용하는 모든 숫자, 값, 논리 값

    ex) 10, 3.14, 'A', true

- 리터럴에 해당되는 값은 특정 메모리 공간인 상수 풀(constant pool)에 있음
- 필요한 경우 상수 풀에서 가져와서 사용
- 상수 풀에 저장할 때 정수는 `int` , 실수는 `double` 로 저장
- `long` , `float` 값으로 저장해야 하는 경우 식별자 `L` or `l` , `F` or `f` 명시

## 형 변환(type conversion)

- 서로 다른 자료형의 값이 대입되는 경우 형 변환이 일어 남
- 묵시적 형변환 : 작은 byte → 큰 byte, 덜 정밀한 수 → 더 정밀한 수 대입
- 명시적 형변환 : 반대의 경우, 변환 되는 자료형을 명시해야 함, 자료의 손실이 발생할 수 있음

```java
// 묵시적 형변환
long num = 3;  // int 에서 long 으로 자동 형 변환, L을 명시하지 않아도 됨

// 명시적 형변환
double dNum = 3.14;
int num = (int)dNum;  // 자료형 명시
```

# 자바의 연산자

## 항과 연산자

- 항(operand) : 연산에 사용되는 값
- 연산자(operator) : 항을 이용하여 연산하는 기호
    - 단항 연산자 : 항이 1개    ex) `++num;`
    - 이항 연산자 항이 2개     ex) `num1 + num2;`
    - 삼항 연산자 : 항이 3개   ex) `(5 > 3) ? 1: 0;`

## 대입 연산자

- 변수에 값을 대입  ex) `int age = 23;`

## 부호 연산자

- 값의 부호를 변경  ex) `int num = -age;`

## 산술 연산자

- `+` , `-` , `*` , `/` , `%`

## 증가 감소 연산자

- 단항 연산자, `++` , `--`

```java
int num = 10;
System.out.println(++num);  // 11, 출력 전 증가
System.out.println(num++);  // 10, 출력 후 증가, 다음 문장에서 11
```

## 관계 연산자

- 이항 연산자,  `true` or `false` 결과 값 반환
    - `>` , `<` , `>=` , `<=` , `==` , `!=`

## 논리 연산자

- 관계 연산자와 혼합하여 많이 사용,  `true` or `false` 결과 값 반환
    - 논리 곱 :  `&&`
    - 논리 합 :  `||`
    - 부정 :  `!`
        - 단락 회로 평가(short circuit evaluation)
            - 논리 곱은 두 항이 모두 `true` 일 때 `true`
            - 논리 합은 두 항이 모두 `false` 일 때 `false`

## 복합 대입 연산자

- 대입 연산자와 다른 연산자를 함께 사용
    - `+=` , `-=` , `*=` , `/=` , `%=`

## 조건 연산자

- 삼항 연산자, 조건 식의 결과 `true` or `false` 에 따라 다른 식이나 결과 값을 반환
    - `조건식 ? 참 결과 : 거짓 결과;`  `int num = (5 > 3) ? 10 : 20;`

## 비트 연산자

- `~` : 비트의 반전 (1의 보수)
- `&` : 비트 단위 AND
- `|` : 비트 단위 OR
- `^` : 비트 단위 XOR, 두개의 비트가 서로 다른 경우 1
- `<<` : `a << 2` 변수 a를 2 비트 만큼 왼쪽으로 이동
- `>>` : `a >> 2` 변수 a를 2 비트 만큼 오른쪽으로 이동
- `>>>` , `<<<` : `>>` , `<<` 와 동일한 연산, 채워지는 비트가 부호와 상관없이 0

```java
int num = 15;  // 00001111
System.out.println(num << 3);  // 120, 15 * 2^3(이동한 자릿수 만큼), 01111000

System.out.println(num >> 2);  // 3, 15 / 2^3, 00000011
```

# 제어 흐름

## 조건문

### if-else 문

- 조건에 따라 다른 수행문이 실행

```java
if(조건1) {
		수행문1;
}
else if(조건2) {
		수행문2;
}
else {
		수행문3;
}
```

### switch-case 문

```java
switch(rank) {
		case a: case b: case c:  // 값은 다르지만 같은 수행문을 해야 할 경우
				수행문1;
				break;
		case d: 수행문2;
				break;
		default: 수행문3;
}
```

## 반복문

### while 문

- 조건식이 참인 동안 수행문을 반복

```java
while(조건식) {
		수행문1;
}
```

### do-while 문

- 먼저 수행문을 한 번 수행하고 조건식 체크

```java
do {
		수행문1;
} while(조건식);
		수행문2;
```

### for 문

```java
for(초기화식; 조건식; 증감식) {
		수행문;
		for(초기화식; 조건식; 증감식) {  // 중첩 반복문
				수행문;
		}
}
```

### continue

```java
int total = 0;
int num;

for (num = 1; num <= 100; num++) {
		if(num % 2 == 1)
				continue;  // 홀수인 경우 아래 수행문 무시
		total += num;
}
```

### break

- 중첩된 반목문의 경우 내부 반복문만 빠져나옴

```java
int sum = 0;
int num

while(true) {
		sum += num;
		
		if(sum > 100)
				break;  // sum 이 100보다 클 때 반복문 종료
		
		num++;
}
```