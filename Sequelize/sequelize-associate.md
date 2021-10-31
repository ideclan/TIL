# Sequelize Associate

`Sequelize CLI` 를 통해 `Model`을 정의하고, `Migration`으로 스키마를 관리  
이때, `RDBMS`의 가장 중요한 `Table` 간의 관계를 `Sequelize`에서 `Model` 간의 관계로 정의하는 것

## 모델 및 마이그레이션 생성

유저가 리뷰를 작성하는 예시로 `users`와 `reviews`  
총 2개의 테이블에 대한 모델 정의 그리고 마이그레이션을 진행

```bash
# users
$ sequelize model:generate --name User --attributes email:string,password:string,name:string

# reviews
$ sequelize model:generate --name Review --attributes users_id:integer,content:string
```

> 모델명은 복수가 아닌 단수를 사용하고, 첫 글자는 대문자를 권장

모델을 생성하면 다음과 같은 구조로 파일이 생성됨

```
|-- migrations
|    `-- <timestamp>-user.js
|    `-- <timestamp>-review.js
|-- models
|    `-- index.js
|    `-- user.js
|    `-- review.js
```

## 모델 관계 정의

예시인 `users`와 `reviews` 테이블 간의 관계는  
하나의 유저는 여러 개의 리뷰를 가질 수 있으며, 하나의 리뷰는 하나의 유저에 속함  
따라서 `1 : N` 관계

`Sequelize` 에서는 이러한 관계를 정의하기 위해 `hasMany()`와 `belongsTo()` 메소드를 지원

- `hasMany()` : `users` 는 여러 개의 리뷰를 가짐
- `belongsTo()` : `reviews` 는 하나의 유저에 속함

`models/` 내에 두 모델 파일에서 해당 메소드를 사용하여 관계를 정의

> `1 : N` 관계 이외에도 `1 : 1` 또는 `N : M` 관계를 정의할 수 있음
>
> ```javascript
> // 1 : 1
> hasOne();
> belongsTo();
>
> // 1 : N
> hasMany();
> belongsTo();
>
> // N : M
> belongsToMany();
> ```

`static associate(models) {}` 부분을 수정

해당 모델의 `hasMany()`, `belongsTo()` 메소드를 호출하여  
인자 값으로 관계에 속하는 모델과 옵션(생략 가능)을 넘겨줌

**Options**

- `as` : target 모델의 별명, 이후 include 시 쿼리 결과 값의 이름으로도 사용
- `foreignKey` : 외래 키 정의, 생략 시 `모델명 + Id` 로 컬럼을 생성
- `onUpdate`, `onDelete` : `RESTRICT`, `CASCADE`, `NO ACTION`, `SET DEFAULT`, `SET NULL` 선택

```javascript
// models/user.js

"use strict";
const { Model } = require("sequelize");
module.exports = (sequelize, DataTypes) => {
  class User extends Model {
    static associate(models) {
      this.hasMany(models.Review, {
        as: "reviews",
        foreignKey: "userId",
        // onUpdate: defaults to CASCADE
        onDelete: "cascade",
      });
    }
  }
  User.init(
    {
      email: {
        type: DataTypes.STRING,
        unique: true,
        allowNull: false,
      },
      password: {
        type: DataTypes.STRING,
        allowNull: false,
      },
      name: {
        type: DataTypes.STRING,
        allowNull: false,
      },
    },
    {
      sequelize,
      modelName: "User",
    }
  );
  return User;
};
```

`Review` 모델은 외래 키를 사용하므로, 외래 키 컬럼을 추가

`field`를 지정한 후, 사용할 컬럼명을 정의할 수 있음 (`AS`)

```javascript
// models/review.js

"use strict";
const { Model } = require("sequelize");
module.exports = (sequelize, DataTypes) => {
  class Review extends Model {
    static associate(models) {
      this.belongsTo(models.User, {
        as: "users",
        foreignKey: "userId",
        onDelete: "cascade",
      });
    }
  }
  Review.init(
    {
      userId: {
        field: "users_id",
        type: DataTypes.INTEGER,
        allowNull: false,
      },
      content: {
        type: DataTypes.STRING,
        allowNull: false,
      },
    },
    {
      sequelize,
      modelName: "Review",
    }
  );
  return Review;
};
```

> 주의할 점
>
> 1. `foreignKey` 설정을 하지 않으면, 자동으로 `테이블명 + Id` 컬럼을 생성
> 2. `foreignKey` 설정 시 두 모델에서 동일한 설정이 필요, 하나의 모델에서만 정의하는 경우 자동으로 컬럼을 생성하여 중복 이슈가 일어남
> 3. `include` 사용 시 쿼리 결과 값이 모델명으로 지정되는데, 이는 `foreignKey`에서 `AS` 사용으로 include 에서도 같은 `AS` 명을 사용해야 함

## 마이그레이션 관계 정의

`migrations/` 내에 해당 테이블을 관리하는 마이그레이션 정의

```javascript
// migrations/<timestamp>-create-user.js

module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.createTable("users", {
      id: {
        allowNull: false,
        autoIncrement: true,
        primaryKey: true,
        type: Sequelize.INTEGER,
      },
      email: {
        allowNull: false,
        unique: true,
        type: Sequelize.STRING,
      },
      password: {
        allowNull: false,
        type: Sequelize.STRING,
      },
      name: {
        allowNull: false,
        type: Sequelize.STRING,
      },
    });
  },
  down: async (queryInterface) => {
    await queryInterface.dropTable("users");
  },
};
```

외래 키 컬럼을 추가하여, `references: {}` 로 관계를 정의

**references**

- `model` : 참조하는 테이블 정의
- `key` : 참조하는 키 정의

```javascript
// migrations/<timestamp>-create-review.js

module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.createTable("reviews", {
      id: {
        allowNull: false,
        autoIncrement: true,
        primaryKey: true,
        type: Sequelize.INTEGER,
      },
      users_id: {
        allowNull: false,
        type: Sequelize.INTEGER,
        references: {
          model: "users",
          key: "id",
        },
        onDelete: "cascade",
      },
      content: {
        allowNull: false,
        type: Sequelize.STRING,
      },
    });
  },
  down: async (queryInterface) => {
    await queryInterface.dropTable("reviews");
  },
};
```
