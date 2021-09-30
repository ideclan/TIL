# PostgreSQL

- 객체 관계형(object-relational) 데이터베이스 시스템
- 기본적으로는 관계형 데이터베이스지만 객체 데이터베이스와 연관되는 기능(테이블 상속 및 함수 오버로딩)도 포함

> `ORDBMS` : 객체 지향 데이터베이스 시스템과 관계형 데이터베이스 시스템을 기반으로하며 복잡한 객체가 중심 역할을 하는 DBMS

## PostgreSQL의 특징

- 동시에 여러 작업을 효율적으로 처리할 수 있도록 하는 `동시성`(Concurrency)
- 트랜잭션의 `ACID`를 보장하는 `MVCC`(Multiversion Concurrency Control)
  - `Atomicity` (원자성) : 트랜잭션과 관련된 작업들이 부분적으로 실행되다가 중단되지 않는 것을 보장
  - `Consistency` (일관성) : 트랜잭션이 실행을 성공적으로 완료하면 언제나 일관성 있는 데이터베이스 상태로 유지
  - `Isolation` (독립성) : 트랜잭션을 수행 시 다른 트랜잭션의 연산 작업이 끼어들지 못하도록 보장
  - `Durability` (지속성) : 성공적으로 수행된 트랜잭션은 영원히 반영되어야 함

> `MVCC` (다중 버전 동시성 제어) : 동시 접근을 허용하는 데이터베이스에서 동시성을 제어하기 위해 사용하는 방법, 잠금을 필요로 하지 않기 때문에 일반적인 RDBMS보다 매우 빠르게 작동

## PostgreSQL의 장점

- 표준 `SQL`을 준수
- `ACID`를 완벽히 준수하고 데이터 일관성이 유지되도록 `MVCC`를 구현하여 데이터 무결성이 중요한 경우 적합
- 더 빠른 속도로 쿼리에 응답하기 위해 여러 CPU를 활용할 수 있는 쿼리 계획을 지원하므로 복잡한 작업 연산을 수행하는 경우 적합

## PostgreSQL의 단점

- 읽기가 많은 간단한 작업의 경우 MySQL과 같은 다른 `RDBMS` 보다 성능이 떨어짐
- `Update`를 할 때, 과거 행을 삭제하고 변경된 데이터를 가진 새로운 행을 추가하는 형태로 빈번한 Update가 필요한 경우 적합하지 않음

## PostgreSQL 설치

Mac OS brew

```bash
$ brew install postgresql
```

postgresql 서비스 실행

```bash
$ pg_ctl -D /usr/local/var/postgres start

$ brew services start postgresql
```

서비스가 정상적으로 실행되었는 지 확인

```bash
$ postgres -V
```

## PostgreSQL 접속

- 설치하고 나면, 기본적으로 postgres 유저가 자동적으로 생성
- PostgreSQL 에서는 PostgreSQL 연결을 위해서 `psql` 이라는 쉘을 제공

```bash
$ psql postgres
```

## PostgreSQL Database Setup

데이터베이스 생성

```postgresql
$ postgres=# CREATE test;

$ postgres=# \list;
```

데이터베이스 유저 생성

```postgresql
$ postgres=# CREATE USER myuser WITH ENCRYPTED PASSWORD 'mypass';
```

> 생성한 유저로 데이터베이스 접속 시
>
> `$ psql postgres -U <username> -d <dbname> -h localhost --password`

유저의 데이터베이스 접근 권한 (모든)

```postgresql
$ postgres=# GRANT ALL PRIVILEGES ON DATABASE test TO myuser;
```

## node-postgres

`pg` : PostgreSQL 데이터베이스 접근하기 위한 Node.js Module

```bash
$ npm install pg
```

```javascript
const { Client } = require("pg");

const client = new Client({
  user: "myuser",
  password: "mypass",
  database: "test",
});

await client.connect();

const res = await client.query("SELECT $1::text as message", ["Hello world!"]);
console.log(res.rows[0].message); // Hello world!

await client.end();
```
