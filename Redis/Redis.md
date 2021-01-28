## SQL vs NoSQL

### SQL

- 스키마 정의에 일치하지 않은 데이터는 저장할 수 없음
- Table 에 Record 로 저장
- Table 마다 구조(Structure) 를 가짐
- 데이터를 여러 Table 에 나누어 중복없이 저장
- Table 간의 관계를 나타냄
- 다른 Table 에 데이터를 저장하기 위해 구조(Structure) 정의가 필요

### NoSQL

- 스키마 , 관계 개념 없음
- Table (SQL) => Collections (NoSQL) Record (SQL) => Documents (NoSQL)
- 구조에 따르지 않고 데이터를 저장할 수 있음
- Documents 는 JSON 과 비슷한 형태
- Join 개념 없음
- 데이터를 여러 Collctions 에 나누어 저장하지 않고 필요한 모든 데이터를 포함시켜 저장
- 중복된 데이터를 수정할 때 동일하게 업데이트 필요

### Redis ?

- Open source, NoSQL Database
- Key-Value 구조로 데이터 저장 및 관리
- 디스크가 아닌 메모리 기반
- 빠른 처리 속도

### Redis의 특징

- 다양한 Value data type을 지원
    - string, list, set, sorted set, hash(list data 입력과 삭제가 MySQL 보다 10배 빠름)
- 서버를 종료해도 Data는 사라지지 않음
    - Disk에서 읽어서 Memory에 올림Snapshot 기능 제공 (파일로 저장, 복구 가능)
    - 명시적으로 삭제 명령을 하지 않으면데이터는 영구적 보존

### Data type: String

- 최대 512 MB
- 문자열 뿐만 아니라 integer와 같은 숫자나JPEG 같은 Binary File 까지 저장 가능

### Data type: Set

- 데이터 정렬, 중복되지 않은 집합
- 여러개의 값을 하나의 Value에 저장
- 교집합, 합집합, 차이를 매우 빠른 시간내에 추출

### Data type: Sorted set

- Set 에 score 가 추가된 데이터 형
- score 기준으로 오름차순 정렬
- score는 실수 값을 가지며 중복될 수 있음

### Data type: Hash

- value내에 “field name”: string value 쌍으로이루어진 데이터 형
- 객체를 나타내는데 사용 가능

### Data type: List

- 일종의 양방향 Linked List
- PUSH/POP 연산 또는 index 값을 이용하여데이터 삽입 또는 삭제 가능

### Reference

- **Dave Nielsen: Top 5 uses of Redis as a Database | PyData Seattle 2015**

    ([https://www.youtube.com/watch?v=jTTlBc2-T9Q](https://www.youtube.com/watch?v=jTTlBc2-T9Q))

- **레디스(Redis)란 무엇인가?**(https://medium.com/@jyejye9201/%EB%A0%88%EB%94%94%EC%8A%A4-redis-%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80-2b7af75fa818)
- **[In memory dictionary Redis 소개](https://bcho.tistory.com/654)**

    (https://bcho.tistory.com/654)