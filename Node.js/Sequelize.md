# Sequelize

Node.js에서 가장 많이 사용되는 ORM

> Sequelize is a promise-based Node.js ORM for Postgres, MySQL, MariaDB, SQLite and Microsoft SQL Server. It features solid transaction support, relations, eager and lazy loading, read replication and more.
>
> Sequelize는 Postgres, MySQL, MariaDB, SQLite, Microsoft SQL Server를 지원하는 Promise 패턴 기반의 Node.js ORM입니다. Solid 트랜잭션, 관계 설정, 즉시 로딩, 지연 로딩, 읽기 전용 복제본 등을 포함해 많은 기능을 제공합니다.

## Promise 패턴 기반

- JavaScript의 비동기 코드를 더 우아하게 만듬
- Chaining을 통해 Callback Hell에서 탈출
- 깔끔한 예외 처리를 할 수 있게 함
- 'async'와 'await'를 이용하여 간편한 비동기 제어

## ORM

- Object Relational Mapping(객체-관계 매핑)
- 객체지향 패러다임을 활용하여 관계형 데이터베이스(RDB)의 데이터를 조작하게 하는 기술
- 쿼리를 작성하지 않고도 객체의 메서드를 활용하는 것처럼 쿼리 로직을 작성할 수 있게 함

## Sequelize 설치

MySQL에 Sequelize 적용하는 예시

```bash
$ npm install sequelize mysql2
```

## Sequelize CLI

```bash
$ npm install -g sequelize-cli
```

프로젝트 루트 경로에서 Sequelize 초기화

```bash
$ sequelize init
```
