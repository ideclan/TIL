# Sequelize

Node.js에서 사용할 수 있고, 가장 인기있는 ORM

> Sequelize is a promise-based Node.js ORM for Postgres, MySQL, MariaDB, SQLite and Microsoft SQL Server. It features solid transaction support, relations, eager and lazy loading, read replication and more.
>
> Sequelize는 Postgres, MySQL, MariaDB, SQLite, Microsoft SQL Server를 지원하는 Promise 패턴 기반의 Node.js ORM입니다. Solid 트랜잭션, 관계 설정, 즉시 로딩, 지연 로딩, 읽기 전용 복제본 등을 포함해 많은 기능을 제공합니다.

## ORM

- Object Relational Mapping(객체-관계 매핑)
- 객체를 관계형 데이터베이스(RDB)에 매핑(연결)하여 데이터베이스의 기능들을 추상적으로 사용할 수 있게 함

### ORM의 장점

- ORM 을 통해 데이터베이스 쿼리를 추상화하여 기능을 구현하는 로직에만 집중할 수 있음
- 특정 데이터베이스에 대한 종속성이 줄어 데이터베이스가 바뀌는 상황에도 유연하게 대처할 수 있음
- 데이터베이스 마이그레이션을 쉽게 할 수 있음

### ORM의 단점

- ORM 으로만 서비스를 구현하기 어려운 경우가 존재
- Raw Query를 사용하는 것 보다 성능이 떨어짐

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
- seeders : 생성된 테이블에 데이터를 추가

연결할 데이터베이스에 대한 정보를 `config/config.json` 에서 수정

```json
{
  "development": {
    "username": "root",
    "password": null,
    "database": "database_development",
    "host": "127.0.0.1",
    "dialect": "mysql"
    // "timezone": "+09:00",
    // "define": {
    //   "freezeTableName": true,
    //   "timestamps": false
    // }
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

> 이후 `createdAt`, `updatedAt` 등 DATETIME 형태의 데이터를 삽입하는 경우 UTC 시간으로 입력되는 이슈가 발생하므로 필요한 경우 한국 시간(UTC+09:00) 으로 설정  
> `"timezone": "+09:00"`

> Sequelize는 기본적으로 테이블명을 복수형으로 만드는데, 복수형이 아닌 Model 이름 그대로 사용하기를 원할 때의 설정  
> `define: { freezeTableName: true }`

> Sequelize는 `SELECT` 또는 `INSERT` 때의 자동으로 `createdAt`과 `updatedAt`을 함께 적용, 이를 Off 할 때의 설정  
> `define: { timestamps: true }`

## Sequelize 모델 정의 및 마이그레이션

Sequelize CLI를 통해 모델을 정의하고 마이그레이션을 통해 실제 데이터베이스에 반영이 가능

다음 예제는 `name`와 `age`를 가진 `User` 모델을 생성

```bash
$ sequelize model:generate --name User --attributes name:string,age:integer
```

이를 통해 아래와 같이 총 2개의 파일이 생성됨

- `models/user.js`

```javascript
"use strict";
const { Model } = require("sequelize");
module.exports = (sequelize, DataTypes) => {
  class User extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
    }
  }
  User.init(
    {
      name: DataTypes.STRING,
      age: DataTypes.INTEGER,
    },
    {
      sequelize,
      modelName: "User",
    }
  );
  return User;
};
```

- `migrations/<timestamp>-create-user.js`

```javascript
"use strict";
module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.createTable("Users", {
      id: {
        allowNull: false,
        autoIncrement: true,
        primaryKey: true,
        type: Sequelize.INTEGER,
      },
      name: {
        type: Sequelize.STRING,
      },
      age: {
        type: Sequelize.INTEGER,
      },
      createdAt: {
        allowNull: false,
        type: Sequelize.DATE,
      },
      updatedAt: {
        allowNull: false,
        type: Sequelize.DATE,
      },
    });
  },
  down: async (queryInterface, Sequelize) => {
    await queryInterface.dropTable("Users");
  },
};
```

`id`, `createdAt`, `updatedAt` 필드는 정의하지 않아도 자동으로 생성

그리고 `up`과 `down`으로 구분되어 실제 데이터베이스에 적용할 때에는 `up`을, 적용된 내용을 취소할 때에는 `down`을 실행

실제 데이터베이스에 반영하기 위해 마이그레이션 진행

```bash
$ sequelize db:migrate
```

마이그레이션을 진행한 후 실제 데이터베이스를 살펴보면, 앞에서 정의한 필드와 함께 `Users` 테이블이 생성됨

```bash
mysql> DESC Users;
+-----------+--------------+------+-----+---------+----------------+
| Field     | Type         | Null | Key | Default | Extra          |
+-----------+--------------+------+-----+---------+----------------+
| id        | int          | NO   | PRI | NULL    | auto_increment |
| name      | varchar(255) | YES  |     | NULL    |                |
| age       | int          | YES  |     | NULL    |                |
| createdAt | datetime     | NO   |     | NULL    |                |
| updatedAt | datetime     | NO   |     | NULL    |                |
+-----------+--------------+------+-----+---------+----------------+
```

마이그레이션을 취소할 때에는 명령어 뒤에 `undo` 삽입

```bash
$ sequelize db:migrate:undo
```

## CRUD

Sequelize는 데이터베이스에서 데이터를 쿼리하는 데 도움이 되는 다양한 방법을 제공  
이를 통해 CRUD를 간단하게 구현이 가능

먼저 앞에서 정의한 모델을 불러오는 것이 필요

```javascript
const { User } = require("./models");
```

### CREATE

`Model.create({key: value})`

```javascript
(async () => {
  const user = await User.create({
    name: "Jiheon Lee",
    age: 23,
  });

  console.log(user.name); // Jiheon Lee
  console.log(user.age); // 23
})();
```

```bash
mysql> SELECT * FROM Users;
+----+------------+------+---------------------+---------------------+
| id | name       | age  | createdAt           | updatedAt           |
+----+------------+------+---------------------+---------------------+
|  1 | Jiheon Lee |   23 | 2021-10-06 10:25:45 | 2021-10-06 10:25:45 |
+----+------------+------+---------------------+---------------------+
```

### READ

- `Model.findAll()`
- `Model.findOne({ where: { id: 1 } })`

```javascript
(async () => {
  const users = await User.findAll();
  console.log(users);
})();
```

```bash
[
  User {
    dataValues: {
      id: 1,
      name: 'Jiheon Lee',
      age: 23,
      createdAt: 2021-10-06T01:25:45.000Z,
      updatedAt: 2021-10-06T01:25:45.000Z
    },
    _previousDataValues: {
      id: 1,
      name: 'Jiheon Lee',
      age: 23,
      createdAt: 2021-10-06T01:25:45.000Z,
      updatedAt: 2021-10-06T01:25:45.000Z
    },
    _changed: Set(0) {},
    _options: {
      isNewRecord: false,
      _schema: null,
      _schemaDelimiter: '',
      raw: true,
      attributes: [Array]
    },
    isNewRecord: false
  }
]
```

> findAll한 데이터에서 dataValues 이외의 정보 제외
>
> 1. `Model.findAll({ raw: true })`  
>    dataValues만 리턴되지만, include할 연관 테이블이 없을 때 사용
> 2. `const users = await User.findAll().map(el => el.get({ plain: true }));`  
>    위와 동일하게 dataValues만 리턴, include할 연관 테이블이 있을 때 추천

### UPDATE

`Model.update()`

```javascript
(async () => {
  await User.update(
    { name: "John" },
    {
      where: {
        id: 1,
      },
    }
  );
})();
```

### DELETE

`Model.destroy({ where: { id: 1 } })`

```javascript
(async () => {
  await User.destroy({
    where: {
      id: 1,
    },
  });
})();
```

## 기존 DB에서 모델 추출

ORM을 사용하고자 하는데 기존 DB의 모든 테이블을 모델로 정의하기에는 번거로움  
Sequelize에서는 해당 기능을 제공하고 있지 않지만, [sequelize-auto](https://github.com/sequelize/sequelize-auto)에서 제공

### sequelize-auto 설치

```bash
$ npm install -g sequelize-auto
```

### sequelize-auto 사용법

```bash
$ sequelize-auto -h localhost -d <database> -u <user> -x [password] -p [port]  --dialect [dialect] -c [/path/to/config] -o [/path/to/models] -t [tableName]
```
