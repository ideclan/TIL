### PHP 개요

- 웹 응용 프로그램을 개발하는 웹 프로그래밍 언어
    - PHP, ASP, JSP 등
- PHP 사용 목적
    - 웹 사이트의 회원가입, 로그인, 예약 시스템, 장바구니, 배송 조회, 결제 등

### PHP 특징

- 다양한 운영체제에서 구현 가능
- 쉽고 편리한 데이터베이스 연동
- 리눅스 서버 운영체제 사용에 따른 구축 비용이 적게 듬
- 쉬운 코드 작성, 단순한 문법

### APM 연동 과정

![APM](https://user-images.githubusercontent.com/48443734/95990738-db156e80-0e66-11eb-95ae-78e86dea4b16.png)

- Apache
    - 웹 서버 프로그램
    - PHP가 제공한 HTML 파일을 HTTP 규약에 따라 클라이언트에 전송
    - 성능이 우수하며 대부분의 운영체제에서 사용 가능
- PHP
    - 동적인 웹 사이트 제작하는 웹 프로그래밍 언어
    - 작성된 프로그램을 내장된 PHP 해석기를 통해 HTML 형태로 변환해 웹 서버인 Apache에 제공
- MySQL
    - Apache, PHP와 함께 패키지 형태로 쓰이는 DBMS로 데이터를 저장

### AMP 환경 셋팅

- AMP의 약자는 Apache, PHP, MySQL
- 여러 방법이 있지만 손쉽게 세팅할 수 있는 비트나미(Bitnami)로 설정

### Bitnami 설치

- [참고](https://velog.io/@sik2/PHP-MVC-%EA%B2%8C%EC%8B%9C%ED%8C%90-%EB%A7%8C%EB%93%A4%EA%B8%B0)

### PHP 기본 문법

- HTML 코드 안에 PHP 코드가 함께 존재할 수 있음
- `<?` 와 `?>` 으로 PHP의 시작과 끝을 나타냄
- 하나의 문장(코드)의 끝은 `;`

```php
// 문자열 출력 예제

<?
	echo "Hello, World!<br>";
	echo "Good, Bye~";
?>
```