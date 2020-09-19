### Android 개발 환경 종류

|개발 환경|사용 언어|개발 ToolKit|
|------|---|---|
|응용 프로그램 개발|XML, Java|SDK(Software Development Kit)|
|시스템 응용 프로그램 개발|C, C++|NDK(Native Development Kit)|
|하드웨어 제어 및 커널 관련|C, C++|PDK(Platform Development Kit)|

### Android 특징

- 구글에서 무료로 배포한 오픈 소스
- 안드로이드의 핵심 커널은 리눅스로 구성
- 안드로이드 앱 개발 언어는 XML, JAVA를 사용
- 안드로이드 SDK에서 많은 라이브러리를 포함하고 있어 개발이 용이

### Android App 개발 절차

1. 개발 환경 설정
2. 프로젝트 생성
3. 소스 코드 작성
4. 컴파일 및 실행
5. 디버깅 및 테스트
6. 앱 마켓 등록

**안드로이드 스튜디오 (1, 2) → XML, JAVA (3, 4) → 생성된 APK 파일 (4, 5) → 구글 플레이 스토어 (6)**

### Android Studio 프로젝트 생성

![Configure Your Project](https://user-images.githubusercontent.com/48443734/93674183-7b85a680-fae6-11ea-8b30-9dbc175b8ba8.png)

- Name : 구글 플레이 스토어에 올렸을 때 사용자에게 보이는 이름
- Package name : 구글 플레이 스토어에 공개할 때 앱을 구별할 수 있는 고유 ID
- Save location : 프로젝트 저장 폴더 지정
- Language : 언어 선택 (자바, 코틀린)
- Minimum API level : 안드로이드 OS 최소 버전 선택

### 소스 코드 작성

- XML : 화면 구성을 디자인
- JAVA : 화면의 처리, 기능 (동작) 등을 담당하는 소스코드 작성

컴파일 및 실행

- 에뮬레이터(AVD) : 실제 안드로이드 기기와 비슷하게 소프트웨어로 만든 가상의 기기
- 실제 안드로이드 기기 이용 (스마트폰, 태블릿)

### Java for Android

- JAVA는 객체지향언어, 모든 것이 객체로 표현
- 객체와 클래스에 대한 이해 필요
- JAVA에서는 모든 것이 클래스 안에 들어감, 반드시 1개 이상의 클래스가 필요

```java
class 클래스 이름 {
	// ...
}
```

### main 메소드 (함수)

- main 메소드 (함수) 는 자바 프로그램의 시작점, 반드시 main 메소드가 필요

  (자바 프로그램 실행 : 자바 가상 머신에 해당 클래스를 불러오고, main 메소드 안의 모든 코드를 실행시켜라)

- main 메소드는 반드시 `public static void main(String[ ] args)` 로 표기
- 자바 프로그램의 기본 구조 (자바에서는 모든 것이 클래스 안에 들어가야 함)

```java
class 클래스 이름 {
		public static void main(String[] args) {
				// ...
		}
}
```

### Hello World

- `System.out.println( )`

```java
class 클래스 이름 {
		public static void main(String[] args) {
				System.out.println("Hello World");
		}
}
```

- `System.out.print( )` 는 줄바꿈을 하지 않음
- String (문자열) 은 `" "` Char (문자) 는 `' '`
- 자바는 False 과 True 를 0 과 1 로 사용하지 못함 (반드시 Boolean 타입을 사용)

### final 키워드와 상수

- 상수 : 변하지 않고 일정한 값을 갖는 수 (`final` 선언)

```java
class Scratch {
		public static void main(String[] args) {
				final double PI = 3.141592; // 변하면 안되는 값
		}
}
```

### 자동 형변환

- 컴파일러에 의해 원래의 자료형보다 큰 자료형으로 자동 변환
- 치환문(=) 이나 수식 내에서 타입이 일치하지 않을 때 ex) 정수와 실수 연산 결과 값은 실수형

```java
class Scratch {
		public static void main(String[] args) {
				int a = 10;
				double b;

				b = a; // 10이라는 정수가 10.0 이라는 실수로 자동 형변환
				System.out.println(b); // 10.0
		}
}
```

```java
double a = 5 / 2; // 정수형 연산 결과 값 2가 실수로 형변환 2.0
double b = 5 / 2.0; // 정수와 실수 연산 2.5
```

### 강제 형변환

- 개발자의 의도적 자료형 변환
- `( )` 안에 개발자가 명시적으로 자료형 지정

```java
int a;

a = (int) 2.5; // 2
```

### 클래스와 객체

- 클래스 생성

```java
class Greeting {
		void g1() {
				System.out.println("Hello World")
		}
}
```

- 객체 생성

```java
// b는 참조변수라 함
Greeting b = new Greeting();
```

- 객체 안의 함수 호출

```java
class Scratch {
    public static void main(String[] args) {
        Greeting b = new Greeting();
        b.g1();
    }
}

class Greeting {
    void g1() {
        System.out.println("Hello World");
    }
}

// Hello World
```

### 메소드 오버로딩(overloading)

- 같은 이름의 메소드를 2개 이상 정의할 수 있는 기능
- 한 클래스 내에 있는 메소드의 매개 변수의 개수 또는 자료형이 다르면 중복 정의 가능
  (반환형만 다른 것은 적용 불가)

```java
class Calc {
		int sum(int num1, int num2) {
				return num1 + num2;
		}
		int sum(int num1, int num2, int num3) {
				return num1 + num2 + num3;
		}
}
```

```java
// 다음 함수들을 하나의 클래스 안에 모두 정의해도 문제 없음
// 모두 매개변수의 1. 자료형이 다르거나 2. 개수가 다르므로
void func1(int a) {...}
void func1(int a, int b) {...}
void func1(int a, int b, int c) {...}
void func1(double a) {...}
void func1(int a, double b) {...}
void func1(int a, double b, char c) {...}
```

```java
// 반환형이 다른 것은 함수를 구분하는 기준이 될 수 없음
// 오버로딩 불가능하므로 오류 발생
void func1(int a) {...}
int func1(int a) {...}
```

### 생성자

- 객체가 생성될 때 대부분 초기화 목적으로 실행되는 메소드
- 객체가 생성되는 순간에 자동 호출

```java
class Scratch {
    public static void main(String[] args) {
        Student s1 = new Student();
        Student s2 = new Student();
				// 맴버 변수에 값을 일일이 직접 입력하려면 복잡하고 번거로움
        s1.name = "홍길동";
        s1.kor = 80;
        s1.eng = 90;
        s1.math = 70;
        s2.name = "장발장";
        s2.kor = 40;
        s2.eng = 80;
        s2.math = 60;
    }
}

class Student {
    String name;
    int kor;
    int eng;
    int math;
}
```

- 생성자 이름은 클래스 이름과 동일
- 생성자는 반환형을 지정할 수 없고
- 객체 생성 시 한번 자동으로 호출 → 임의로 호출 불가능
- 단, 객체 생성 시 생성자에서 정의한 파라미터 개수가 동일 해야함

```java
Student s1 = new Student("홍길동", 80, 90, 70);
Student s2 = new Student("장발장", 40, 80, 60);

class Student {
    String name;
    int kor;
    int eng;
    int math;
		// 생성자 Student
		Student(String n, int k, int e, int m) {
				name = n;
				kor = k;
				eng = e;
				math = m;
		}
}
```

### 생성자 오버로딩

- 여러 생성자를 생성할 수 있음
- 클래스는 반드시 1개 이상의 생성자가 있어야 함 → 생성자를 정의하지 않으면 컴파일 시 default 생성자가 자동으로 입력됨
- 하지만 생성자를 하나라도 넣어주면 default 생성자는 입력되지 않으므로 직접 작성해야 사용이 가능

```java
Student s1 = new Student("홍길동", 80, 90, 70);  // Student 생성자 호출
Student s2 = new Student(); // default 생성자 호출

class Student {
    String name;
    int kor;
    int eng;
    int math;
		// default 생성자
		Student() {

		}
		Student(String n, int k, int e, int m) {
				name = n;
				kor = k;
				eng = e;
				math = m;
		}
}
```

### this

- 객체 자기 자신을 가리키는 키워드, 레퍼런스
- 위에서는 지역변수와 전역변수가 다르므로 가능했지만 서로 같다면 this 로 클래스 내에 맴버변수를 가르키도록 해야함

```java
class Student {
    String name;
    int kor;
    int eng;
    int math;
		Student(String name, int kor, int eng, int math) {
				this.name = name;
				this.kor = kor;
				this.eng = eng;
				this.math = math;
		}
}
```

### 참고

- 객체 안에는 맴버 함수 즉, 메소드가 있는 것이 아님
- 메소드는 한번만 만들어져서 공유
- 메모리의 프로그램 영역에 저장이 되고, 모든 객체가 공유해서 사용
