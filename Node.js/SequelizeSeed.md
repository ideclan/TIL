# Sequelize Seed

`Sequelize CLI` 를 통해 아래 명령어로 초기화를 진행하면  
다음과 같은 구조로 여러 파일들이 생성됨

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

이 중에서 `seeders` 는 생성된 각 테이블에  
기본으로 필요한 데이터나 예시 데이터를 추가할 때 사용  
**즉, 정적인 데이터 삽입 기능**

> 기존에 `seeders` 를 삭제했거나, 존재하지 않는다면 아래 명령어로 초기화 진행  
> `$ sequelize init:seeders`

## Seeder 생성

아래 명령어를 통해 `Seeder` 를 생성  
예시로 `products` 테이블의 데이터를 삽입하기 위한 것이므로 파일명을 `products` 로 진행

```bash
$ sequelize seed:generate --name <파일명>

# ex) sequelize seed:generate --name products
```

`seeders` 내에 `<timestamp>-<파일명>.js` 파일이 생성됨

- `up` : 해당 `seeder` 내용을 반영할 때 수행할 로직
- `down` : 반영된 내용을 취소하여 되돌릴 때 수행할 로직

```javascript
// 20211026102120-products.js

"use strict";

module.exports = {
  up: async (queryInterface, Sequelize) => {
    /**
     * Add seed commands here.
     *
     * Example:
     * await queryInterface.bulkInsert('People', [{
     *   name: 'John Doe',
     *   isBetaMember: false
     * }], {});
     */
  },

  down: async (queryInterface, Sequelize) => {
    /**
     * Add commands to revert seed here.
     *
     * Example:
     * await queryInterface.bulkDelete('People', null, {});
     */
  },
};
```

## Seeder 작성

예시로 적용할 `products` 테이블은 다음과 같은 정보를 가짐

```
+-------------------+--------------+------+-----+---------+----------------+
| Field             | Type         | Null | Key | Default | Extra          |
+-------------------+--------------+------+-----+---------+----------------+
| id                | int          | NO   | PRI | NULL    | auto_increment |
| brands_id         | int          | NO   | MUL | NULL    |                |
| categories_id     | int          | NO   | MUL | NULL    |                |
| code              | varchar(255) | NO   | UNI | NULL    |                |
| name              | varchar(255) | NO   |     | NULL    |                |
| price             | decimal(7,0) | NO   |     | NULL    |                |
| description       | varchar(255) | NO   |     | NULL    |                |
| image             | varchar(255) | NO   |     | NULL    |                |
| type              | varchar(255) | NO   |     | NULL    |                |
| registration_date | datetime     | NO   |     | NULL    |                |
+-------------------+--------------+------+-----+---------+----------------+
```

`Seeder` 를 작성할 때, 컬럼이나 데이터 타입이 일치하지 않으면  
정상적으로 수행되지 않으므로 적용할 테이블의 정보를 확인 후 주의하여  
주석으로 제공된 메뉴얼을 참고하여 작성

> `FK` 가 존재하는 경우, 테이블 관계에 맞게 순서대로 `Seed` 진행이 필요  
> 현재 예시는 `brands`, `categories` 테이블 데이터가 존재하는 경우

```javascript
// 20211026102120-products.js

module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.bulkInsert(
      "products", // 테이블 명
      [
        {
          id: 1,
          brands_id: 1,
          categories_id: 1,
          code: "921826-101",
          name: "나이키 에어맥스 97 OG",
          price: 159200,
          description:
            "특유의 물결 라인과 반사체 파이핑, 그리고 발 전체에 적용된 맥스 에어 쿠셔닝과 같은 디테일을 그대로 간직한 디자인",
          image: "/product/img/921826-101.jpg",
          type: "남녀공용",
          registration_date: new Date(2018, 1, 18),
        },
        {
          id: 2,
          brands_id: 2,
          categories_id: 3,
          code: "AQ0021",
          name: "아디다스 하든 LS 2 버클",
          price: 58780,
          description:
            "코트를 압도하는 폭발적인 스피드. 혁신적인 핏과 강력한 락다운으로 더욱 자유로운 움직임을 이끄는 아디다스 농구화",
          image: "/product/img/AQ0021.jpg",
          type: "남성용",
          registration_date: new Date(2018, 7, 21),
        },
        {
          id: 3,
          brands_id: 1,
          categories_id: 2,
          code: "AR4494-003",
          name: "나이키 울트라 컴포트 3",
          price: 49000,
          description: "NIKE ULTRA COMFORT 3 SLIDE",
          image: "/product/img/AR4494-003.jpg",
          type: "남성용",
          registration_date: new Date(2020, 5, 25),
        },
      ],
      {}
    );
  },

  down: async (queryInterface, Sequelize) => {
    await queryInterface.bulkDelete("products", null, {});
  },
};
```

## Seeder 실행

`Seeder` 를 작성후 반영하기 위해 아래와 같이 명령어 실행

```bash
$ sequelize db:seed --seed <파일명>

# ex) sequelize db:seed --seed 20211026102120-products.js
```

반영된 내용을 취소하여 되돌릴 때

```bash
$ sequelize db:seed:undo
```

> `seeders` 내의 모든 파일들을 실행할 때
>
> ```bash
> $ sequelize db:seed:all
> ```
>
> 반영된 모든 내용을 취소하여 되돌릴 때
>
> ```bash
> $ sequelize db:seed:undo:all
> ```
