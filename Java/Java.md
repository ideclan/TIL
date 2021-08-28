# JAVA

## 변수와 자료형

### 2, 8, 10, 16 진수

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

### 정수 자료형

- `byte` : 1byte | 동영상, 음악 파일 등 실행 파일의 자료를 처리할 때 사용
- `short` : 2byte | 주로 C/C++ 언어와의 호환 시 사용
- `int` : 4byte | 자바에서 정수에 대한 기본 자료 형, 프로그램에서 사용하는 모든 숫자(리터럴)는 기본적으로 int 로 저장
- `long` : 8byte | 가장 큰 정수 자료형, 숫자뒤에 식별자 `L` 또는 `l` 을 붙여 long 자료형을 표시해야 함

```java
// 컴파일 에러
int num = 12345678900;
long num = 12345678900;

// long 자료형 표시
long num = 12345678900L;
```

### 문자 자료형

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

### 실수 자료형

- `float` : 4byte | 숫자뒤에 식별자 `F` 또는 `f` 을 붙여 float 자료형을 표시해야 함
- `double` : 8byte | 실수는 기본적으로 long 으로 처리

```java
double dNum = 3.14;
float fNum = 3.14;  // 컴파일 에러

float fNum = 3.14F;
```

### 논리 자료형

- `boolean` : 1byte

```java
boolean isMarried = false;
```

### 자료형 없이 변수 사용

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

### 상수

- 변하지 않는 값 (cf 변수 : 변하는 값)
- 상수를 선언 : `final` 사용

```java
final double PI = 3.14;
final int MAX_NUM = 100;

PI = 3.15;  // 컴파일 에러 - final로 선언된 변수에 새로운 값을 할당할 수 없음
```

### 리터럴(literal)

- 프로그램에서 사용하는 모든 숫자, 값, 논리 값

  ex) 10, 3.14, 'A', true

- 리터럴에 해당되는 값은 특정 메모리 공간인 상수 풀(constant pool)에 있음
- 필요한 경우 상수 풀에서 가져와서 사용
- 상수 풀에 저장할 때 정수는 `int` , 실수는 `double` 로 저장
- `long` , `float` 값으로 저장해야 하는 경우 식별자 `L` or `l` , `F` or `f` 명시

### 형 변환(type conversion)

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

## 자바의 연산자

### 항과 연산자

- 항(operand) : 연산에 사용되는 값
- 연산자(operator) : 항을 이용하여 연산하는 기호
  - 단항 연산자 : 항이 1개 ex) `++num;`
  - 이항 연산자 항이 2개 ex) `num1 + num2;`
  - 삼항 연산자 : 항이 3개 ex) `(5 > 3) ? 1: 0;`

### 대입 연산자

- 변수에 값을 대입 ex) `int age = 23;`

### 부호 연산자

- 값의 부호를 변경 ex) `int num = -age;`

### 산술 연산자

- `+` , `-` , `*` , `/` , `%`

### 증가 감소 연산자

- 단항 연산자, `++` , `--`

```java
int num = 10;
System.out.println(++num);  // 11, 출력 전 증가
System.out.println(num++);  // 10, 출력 후 증가, 다음 문장에서 11
```

### 관계 연산자

- 이항 연산자, `true` or `false` 결과 값 반환
  - `>` , `<` , `>=` , `<=` , `==` , `!=`

### 논리 연산자

- 관계 연산자와 혼합하여 많이 사용, `true` or `false` 결과 값 반환
  - 논리 곱 : `&&`
  - 논리 합 : `||`
  - 부정 : `!`
    - 단락 회로 평가(short circuit evaluation)
      - 논리 곱은 두 항이 모두 `true` 일 때 `true`
      - 논리 합은 두 항이 모두 `false` 일 때 `false`

### 복합 대입 연산자

- 대입 연산자와 다른 연산자를 함께 사용
  - `+=` , `-=` , `*=` , `/=` , `%=`

### 조건 연산자

- 삼항 연산자, 조건 식의 결과 `true` or `false` 에 따라 다른 식이나 결과 값을 반환
  - `조건식 ? 참 결과 : 거짓 결과;` `int num = (5 > 3) ? 10 : 20;`

### 비트 연산자

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

## 클래스와 객체

### 객체 지향 프로그래밍(Object Oriented Programming, OOP)

- 객체를 기반으로 하는 프로그래밍 ex) C++, Python, JAVA

### 절차 프로그래밍(Procedural Programming)

- 시간의 흐름에 따른 프로그래밍 ex) C언어

### 클래스(class)

- 객체에 대한 속성과 기능을 코드로 구현 한 것
- 객체에 대한 청사진(blueprint)
  - 객체의 속성
    - 객체의 특성(property), 속성(attribute), 멤버 변수(member variable)
  - 객체의 기능
    - 객체가 하는 기능들을 메서드로 구현
    - method, member function

### 클래스 정의

- class는 대부분 대문자로 시작
- 하나의 java 파일에 하나의 클래스를 두는 것이 원칙이나
- 여러 개의 클래스가 같이 있는 경우 public 클래스는 단 하나이며
- public 클래스와 자바 파일의 이름은 동일해야 함
- 자바의 모든 코드는 class 내부에 위치

```java
(접근 제어자) class 클래스 이름 {
  멤버 변수;
  메서드;
}
```

```java
// Student.java

package classpart;  // 패키지는 소문자

public class Student {  // 클래스 이름 대문자로 시작
  int studentID;
  String studentName;
  int grade;
  String address;

  public void showStudentInfo() {  // 메소드 이름 소문자로 시작
    System.out.println(studentName + "," + address);
  }

  // 해당 파일에서 실행시켜야 하는 경우
  /* public static void main(String[] args) {
    Student studentLee = new Student();
    studentLee.studentName = "이순신";
    studentLee.address = "서울시 서초구 서초동";

    studentLee.showStudentInfo();
  } */
}
```

```java
// StudentTest.java

package classpart;

public class StudentTest {

  public static void main(String[] args) {
    Student studentLee = new Student();
    studentLee.studentName = "이순신";
    studentLee.address = "서울시 서초구 서초동";

    studentLee.showStudentInfo();
  }
}
```

## 메서드

- 함수의 일종, 객체의 기능을 제공하기 위해 클래스 내부에 구현되는 함수

### 함수 구현하고 호출하기

```java
package classpart;

public class FunctionTest {

  public static void main(String[] args) {
    int num1 = 10;
    int num2 = 20;

    int sum = addNum(num1, num2);
    System.out.println(sum);  // 30
  }

  public static int addNum(int n1, int n2) {
    int result = n1 + n2;
    return result;
  }

}
```

### 메서드 정의

```java
package classpart;

public class Student {
  int studentID;
  String studentName;
  int grade;
  String address;

  public void showStudentInfo() {
    System.out.println(studentName + "," + address);
  }

  public String getStudentName() {
    return studentName;
  }

  public void setStudentName(String name) {
    studentName = name;
  }
}
```

## 클래스와 인스턴스

- 클래스(static 코드) → 생성(인스턴스 화) → 인스턴스(dynamic memory)

### 클래스 생성

- 클래스를 사용하기 위해서는 클래스를 생성해야 함
- `new` 예약어를 이용하여 클래스 생성

```java
클래스형 변수이름 = new 생성자;

// 참조형데이터타입 참조변수 = new 디폴트생성자
Student studentA = new Student();
```

### 인스턴스와 힙(heap) 메모리

- 하나의 클래스 코드로 부터 여러 개의 인스턴스를 생성
- 인스턴스는 힙(heap) 메모리에 생성됨
- 각각의 인스턴스는 다른 메모리에 다른 값을 가짐

### 참조 변수와 참조 값

- 참조 변수 : 인스턴스 생성 시 선언하는 변수
- 참조 값 : 인스턴스가 생성되는 힙 메모리 주소

```java
Student student1 = new Student();
System.out.println(student1);  // 패지키명.클래스명@16f65612
```

### 생성자(constructor)

- 인스턴스 생성 시 `new` 키워드와 함께 사용했던 생성자

```java
// Student.java

package classpart;

public class Student {
  int studentID;
  String studentName;
  int grade;
  String address;

  public Student() {}  // 디폴트 생성자, 작성하지 않아도 컴파일 시 자동으로 추가됨, 직접 작성한 생성자가 있다면 추가 X

  public Student(int id, String name) {  // 생성자 직접 작성, 디폴트 생성자와 같은 이름 사용할 수 있으나 매개변수가 달라야 함
    studentID = id;
    studentName = name;
  }

  // ...
}
```

```java
// StudentTest.java

package classpart;

public class StudentTest {

  public static void main(String[] args) {
    Student studentLee = new Student(100, "이순신");
  }
}
```

- 생성자는 인스턴스를 초기화 할 때의 명령어 집합
- 생성자의 이름은 그 클래스의 이름과 같음
- 생성자는 메소드가 아님, 상속되지 않으며, 리턴 값은 없음

### 디폴트 생성자(default constructor)

- 하나의 클래스에는 반드시 적어도 하나 이상의 Constructor가 존재
- Constructor를 기술하지 않으면 Default Constructor가 자동으로 생김
  - Default Constructor는 매개 변수, 구현부가 없음
- 만약 클래스에 매개변수가 있는 생성자를 추가하면 디폴트 생성자는 제공되지 않음

### 생성자 오버로드(constructor overload)

- 필요에 의해 생성자를 추가하는 경우 여러 개의 생성자가 하나의 클래스에 있음 (overload)

```java
package classpart;

public class Student {
  int studentID;
  String studentName;
  int grade;
  String address;

  public Student() {}  // 디폴트 생성자

  public Student(int id, String name) {  // 아이디와 이름을 매개변수로 입력받는 생성자
    studentID = id;
    studentName = name;
  }
}
```
