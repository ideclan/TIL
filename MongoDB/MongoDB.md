# MongoDB

## NoSQL

- **Not Only** SQL
- 스키마 없이 데이터를 표현하는 것이 주된 특징인 일련의 데이터베이스들

## NoSQL 데이터베이스의 특징

- 정해진 스키마가 없음
- 데이터베이스의 종류에 따라 그 특성이 매우 다름 (RDBMS가 비슷비슷한 것과 다름)

## 장점

- **높은 수평 확장성**
- 초기 개발의 용이성
- 스키마 설계의 유연성

### 수직 확장 (vertical scaling)

ex) CPU 1개, 메모리 2GB인 인스턴스의 DB가 유저 1만명의 요청을 처리한다. 2만명의 유저로 늘어 문제가 생긴다면 가용 자원을 2배로 늘리면 되지만 지속적으로는 비용에 한정적이다.

- 한 인스턴스의 가용자원(CPU, memory, storage)을 키워 더 큰 로드를 감당
- 어디까지나 한 인스턴스를 키우는 것이기 때문에 확장이 제한

### 수평 확장 (horizontal scaling)

- 더 많은 인스턴스를 만들어 더 큰 로드를 감당
- 수평 확장이 가능한 구조이고, 운영 비용만 감당할 수 있다면 **이론적으로 얼마나 많은 로드라도 받아낼 수 있음**

## 단점

- 표준의 부재
- SQL에 비해 약한 query capability
- data consistency를 어플리케이션 레벨에서 보장해야 함

## NoSQL 데이터베이스의 종류

- key-value
- Document
- Graph

### key-value

- Redis, AWS DynamoDB
- 모든 레코드는 key-value의 페어
- value는 어떤 값이든 될 수 있음
- NoSQL 데이터베이스의 가장 단순한 형태

### Document-based

- **DynamoDB**, CouchDB
- 각 레코드가 하나의 문서가 됨
- 문서는 데이터베이스에 따라 XML, YAML, JSON, BSON 등을 사용
- 문서의 내부적 구조를 통한 쿼리 최적화, 활용성 높은 API 등이 제공

### Graph-based

- Neo4j, AWS Neptune
- 그래프 이론을 바탕으로, 데이터베이스를 그래프로 표현
- 그래프는 node(객체)와 egde(관계), 그리고 property(객체의 속성)로 이루어 짐
- 관계가 first-class citizen이기 떄문에 관계 기반 문제(실시간 추천 등)에 유리

## MongoDB Atlas

- AWS, GCP 등 클라우드 호스팅 MongoDB 서비스

## MongoDB 접속

```bash
$ npm install --save mongodb

# npm install --save-dev @types/mongodb
```

```javascript
const { MongoClient } = require("mongodb");
const uri =
  "mongodb+srv://<username>:<password>@cluster0.zr1pn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";
const client = new MongoClient(uri, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});
client.connect((err) => {
  const collection = client.db("test").collection("devices");
  // perform actions on the collection object
  client.close();
});
```

## MongoDB Access

One or Many

- `users = client.db('데이터베이스명').collection('컬렉션명')` : 기존에 없다면 생성
- `users.deleteMany({})` : 삭제
- `users.insertMany({})` : 생성
- `users.updateOne({})` : 수정
- `users.findMany({})` : 조회

```javascript
async function main() {
  await client.connect();

  const users = client.db("test").collection("users");

  // Reset
  await users.deleteMany({});
  await users.insertMany([
    {
      name: "Foo",
      birthYear: 2000,
    },
    {
      name: "Bar",
      birthYear: 1995,
    },
    {
      name: "Baz",
      birthYear: 1990,
    },
    {
      name: "Poo",
      birthYear: 1993,
    },
  ]);

  await users.deleteOne({
    name: "Baz",
  });

  const cursor = users.find(
    {
      birthYear: {
        $gte: 1990,
      },
    },
    {
      sort: {
        birthYear: -1,
      },
    }
  );
  await cursor.forEach(console.log);

  await client.close();
}

main();
```

- 조회 시 필터
- contacts안에 type이 phone인 데이터

```javascript
{
  name: 'Foo',
  birthYear: 2000,
  contacts: [
    {
      type: 'phone',
      number: '+821000001111',
    },
    {
      type: 'home',
      number: '+821022223333',
    },
  ],
  city: '서울',
},

const cursor = users.find({
  "contacts.type": "phone",
});
```

## One to Many

- `contacts` 임베딩하여 `One to Many` 관계
- contacts는 새로 collection을 만들어야 하는 것이 아닌가?
  - Join은 무거운 작업이기 때문에 임베딩하여 `One to Many` 관계를 사용
  - 하지만 한 document의 크기가 `16MB` 또는 `100개의 중첩`을 넘어간다면 새로운 collection으로 관리

```javascript
{
  name: 'Foo',
  birthYear: 2000,
  contacts: [
    {
      type: 'phone',
      number: '+821000001111',
    },
    {
      type: 'home',
      number: '+821022223333',
    },
  ],
},
```

## Many to Many

- 서울의 인구수가 990 변경됐다면 users를 모두 돌면서 수정해야 함
- 각 `city`가 각자 만의 property를 가져야하는 경우 `Many to Many`
  - 이런 경우 city에 대한 새로운 collection을 만드는 것이 좋은 방안

```javascript
{
  name: 'Foo',
  birthYear: 2000,
  contacts: [
    {
      type: 'phone',
      number: '+821000001111',
    },
    {
      type: 'home',
      number: '+821022223333',
    },
  ],
  city: {
    name: '서울',
    population: 1000,
  },
  {
    name: 'Bar',
    birthYear: 1995,
    contacts: [
      {
        type: 'phone',
      },
    ],
    city: {
      name: '서울',
      population: 1000,
    },
  },
},
```

- `users.aggregate([{}])` 컬렉션을 합쳐서 조회

```javascript
const users = client.db("test").collection("users");
const cities = client.db("test").collection("cities");

// Reset
await users.deleteMany({});
await cities.deleteMany({});

// Init
await cities.insertMany([
  {
    name: "서울",
    population: 1000,
  },
  {
    name: "부산",
    population: 350,
  },
]);

await users.insertMany([
  {
    name: "Foo",
    birthYear: 2000,
    contacts: [
      {
        type: "phone",
        number: "+821000001111",
      },
      {
        type: "home",
        number: "+821022223333",
      },
    ],
    city: "서울",
  },
  {
    name: "Bar",
    birthYear: 1995,
    contacts: [
      {
        type: "phone",
      },
    ],
    city: "부산",
  },
  {
    name: "Baz",
    birthYear: 1990,
    city: "부산",
  },
  {
    name: "Poo",
    birthYear: 1993,
    city: "부산",
  },
]);

const cursor = users.aggregate([
  {
    $lookup: {
      from: "cities",
      localField: "city",
      foreignField: "name",
      as: "city_info",
    },
  },
]);
```

- 조건 조회

```javascript
const cursor = users.aggregate([
  {
    $lookup: {
      from: "cities",
      localField: "city",
      foreignField: "name",
      as: "city_info",
    },
  },
  {
    $match: {
      "city_info.population": {
        $gte: 500,
      },
    },
  },
]);
```

- 여러 조건 조회
  - `and` 또는 `or` 사용

```javascript
const cursor = users.aggregate([
  {
    $lookup: {
      from: "cities",
      localField: "city",
      foreignField: "name",
      as: "city_info",
    },
  },
  {
    $match: {
      $and: [
        {
          "city_info.population": {
            $gte: 500,
          },
        },
        {
          birthYear: {
            $gte: 1995,
          },
        },
      ],
    },
  },
  // 해당 레코드 개수
  // {
  //   $count: 'num_users',
  // },
]);
```
