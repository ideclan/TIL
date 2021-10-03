# Sequelize

Node.js에서 가장 많이 사용되는 ORM

> Sequelize is a promise-based Node.js ORM for Postgres, MySQL, MariaDB, SQLite and Microsoft SQL Server. It features solid transaction support, relations, eager and lazy loading, read replication and more.
>
> Sequelize는 Postgres, MySQL, MariaDB, SQLite, Microsoft SQL Server를 지원하는 Promise 패턴 기반의 Node.js ORM입니다. Solid 트랜잭션, 관계 설정, 즉시 로딩, 지연 로딩, 읽기 전용 복제본 등을 포함해 많은 기능을 제공합니다.

## ORM

- Object Relational Mapping(객체-관계 매핑)
- 객체와 관계형 데이터베이스(RDB)의 데이터를 자동으로 매핑(연결)해주는 것

### ORM의 장점

- 객체 지향적인 코드로 직관적인 이해가 쉬움
- 객체를 재활용할 수 있다는 측면에서 재사용 및 유지보수의 편리성 증가
- DBMS에 대한 종속성이 줄어듬

### ORM의 단점

- ORM 으로만 서비스를 구현하기 어려움
- 프로젝트의 복잡성이 커질 경우 난이도 증가

## Sequelize 설치

MySQL에 Sequelize 적용

```bash
$ npm install sequelize mysql2
```

## Sequelize CLI

```bash
$ npm install -g sequelize-cli
```

프로젝트 루트 경로에서 Sequelize 초기화 진행

```bash
$ sequelize init
```

```
|-- config
|    `-- config.json
|-- migrations
|-- models
|    `-- index.js
|-- seeders
```

- config : 데이터베이스 연결 정보
- migrations : 스키마의 버전 관리
- models : 각 테이블의 정보 및 필드 타입을 정의
- seeders : 테이블에 기본 데이터를 넣고 싶은 경우 사용

연결할 데이터베이스에 대한 정보를 `config/config.json` 에서 수정

```json
{
  "development": {
    "username": "root",
    "password": null,
    "database": "database_development",
    "host": "127.0.0.1",
    "dialect": "mysql"
  },
  "test": {
    "username": "root",
    "password": null,
    "database": "database_test",
    "host": "127.0.0.1",
    "dialect": "mysql"
  },
  "production": {
    "username": "root",
    "password": null,
    "database": "database_production",
    "host": "127.0.0.1",
    "dialect": "mysql"
  }
}
```

## Sequelize 모델 정의

`$ sequelize init` 를 통해 생성된 `models/index.js` 는 `models/` 내에 있는 모든 파일들을 읽어 모델로 정의한다.
