# Crypto

Node.js 내장 모듈이며, 여러 해시 함수를 통한 암호화 기능을 제공

> The crypto module provides cryptographic functionality that includes a set of wrappers for OpenSSL's hash, HMAC, cipher, decipher, sign, and verify functions.

## Crypto vs Bcrypt

[Bcrypt](https://github.com/kelektiv/node.bcrypt.js)는 암호를 해시하는 데 도움이 되는 라이브러리입니다. 해싱에 느리고 비용이 많이 드는 Blowfish 알고리즘으로 구현되었습니다. 따라서 강력한 보안이 필요로 할 때는 `Bcrypt`를 사용하면 좋을 것 같습니다.

## 해시(hash)

- **해시(hash)** : 해시 함수에 의해 얻어지는 값
- **해시 함수(hash function)** : 해시 알고리즘(hash algorism)이라고도 하며, 임의의 길이의 데이터를 고정된 길이의 데이터로 매핑하는 함수
  - **키(key)** : 매핑 전 원래 데이터의 값
  - **해시 값(hash value)** : 매핑 후 데이터의 값
  - **해싱(hashing)** : 매핑하는 과정

## 단방향 암호화와 양방향 암호화

암호화 방식은 크게 단방향과 양방향으로 나뉘어진다. **단방향**은 암호화를 할 수 있지만 복호화는 불가능하다. 반면 **양방향**은 암호화, 복호화 모두 가능하다.

그리고 단방향 암호화는 Hash 방식, 양방향 암호화는 대칭키(비공개키), 비대칭키(공개키) 방식을 사용한다.

|        | 암호화 | 복호화 |            암호화 방식             |
| :----: | :----: | :----: | :--------------------------------: |
| 단방향 |   O    |   X    |                Hash                |
| 양방향 |   O    |   O    | 대칭키(비공개키), 비대칭키(공개키) |

사용자의 비밀번호는 본인만이 알 수 있어야하고, 만약 비밀번호를 잃어버린 경우 복호화하는 과정에서 노출되기 때문에 대부분 재설정을 할 수 있도록 한다. 따라서 **단방향 암호화 방식을 사용한다**.

## 해시 알고리즘(hash algorism)

다양한 종류의 해시 알고리즘이 있으며, 알고리즘마다 서로 다른 hash 길이를 가지기도 합니다.

그리고 해시 알고리즘은 공개되어 있기 때문에 해커에게도 공개됩니다. 따라서 이미 보안이 뚫린 해시 함수가 존재하며, 이는 `MD5`, `SHA-1`, `HAS-180`로 사용해선 안된다고 합니다.

보다 안전한 `SHA-256`, `SHA-512` 등을 사용하기를 권고하고 있습니다.

## 비밀번호 암호화하기

`crypto`의 `createHash()` 메소드를 사용합니다.

각 메소드에 대한 인자는 다음과 같습니다.

- `createHash()` : 사용할 알고리즘
- `update()` : 암호화할 비밀번호
- `digest()` : 인코딩 방식

```javascript
import crypto from "crypto";

const createHashedPassword = (password) => {
  return crypto.createHash("sha512").update(password).digest("base64");
};

console.log(createHashedPassword("1234"));
console.log(createHashedPassword("1234"));
console.log(createHashedPassword("1234"));

/*
  1ARVn2Auq2/WAqx2gNrL+q3RNjAzXpUfCXrzkA6d4Xa22yhRLy4AC50E+6UTPoscbo31nbOoq51gvkuXzJ6B2w==
  1ARVn2Auq2/WAqx2gNrL+q3RNjAzXpUfCXrzkA6d4Xa22yhRLy4AC50E+6UTPoscbo31nbOoq51gvkuXzJ6B2w==
  1ARVn2Auq2/WAqx2gNrL+q3RNjAzXpUfCXrzkA6d4Xa22yhRLy4AC50E+6UTPoscbo31nbOoq51gvkuXzJ6B2w==
*/
```

### 문제점

위와 같이 비밀번호를 암호화하였지만 동일한 해시 알고리즘과 인코딩 방식을 사용할 때 사용자의 비밀번호가 동일한 경우 같은 해시 값을 반환합니다. 이를 **레인보우 테이블**이라고 합니다.

이를 통해 해커는 임의의 값을 입력하면서 유추하며 입력된 값을 알아낼 수도 있습니다.

이 점을 보완하기 위한 방법은

1. 소금을 뿌리듯이 입력 값에 `salt`라는 특정 값을 붙여 변형시킨다.
2. 해시 함수를 여러번 돌린다.

2가지 방법을 합하여 입력 값에 salt 값을 붙여서 여러번 반복 해싱할 수도 있습니다.

> 입력은 길이 제한이 없지만, 출력인 해시 값은 항상 고정된 길이를 가지므로 한계가 있기 때문에 다른 입력이지만 같은 해시 값이 나오는 경우도 있다고 합니다.

## 비밀번호 암호화 보완하기

`salt` 생성에서는 `crypto` 모듈의 `randomBytes()`, 비밀번호 암호화 또는 검증에서는 `pbkdf2()` 메소드를 사용할 것 입니다.

앞으로 구현할 함수들을 정의할 때 `new Promise()`로 감싸주려고 하였으나, Node.js의 내장 모듈인 `util`의 `promisify()` 를 사용하면 좀 더 가독성 좋은 코드를 작성할 수 있습니다.

```javascript
import util from "util";
import crypto from "crypto";

const randomBytesPromise = util.promisify(crypto.randomBytes);
const pbkdf2Promise = util.promisify(crypto.pbkdf2);
```

### Salt 생성

`salt` 값은 `crypto` 모듈의 `randomBytes()` 메소드를 통해 64바이트 길이로 생성합니다. `buffer` 형식을 가지고 있으므로 `base64` 문자열로 변경하면 랜덤 문자열이 됩니다.

> `salt`는 이후 검증을 위해 회원가입 시 `password`와 함께 DB에 저장이 필요합니다.

```javascript
const createSalt = async () => {
  const buf = await randomBytesPromise(64);

  return buf.toString("base64");
};
```

### 비밀번호 암호화

단방향 암호화에서 많이 사용되는 `crypto` 모듈의 `pbkdf2()` 메소드를 사용합니다.

인자로는 총 5개로 `해싱할 값`, `salt`, `해시 함수 반복 횟수`, `해시 값 길이`, `해시 알고리즘` 입니다.

> `해시 함수 반복 횟수`는 딱 떨어지는 `100000` 보다는 `104906` 와 같은 수를 넣는게 좋다고 합니다.

`salt` 생성을 위해 앞에서 정의한 `createSalt()` 함수를 사용합니다.  
`key` 또한 `buffer` 형식을 가지고 있으므로 `base64` 문자열로 변경해줍니다.

```javascript
export const createHashedPassword = async (password) => {
  const salt = await createSalt();
  const key = await pbkdf2Promise(password, salt, 104906, 64, "sha512");
  const hashedPassword = key.toString("base64");

  return { hashedPassword, salt };
};
```

### 비밀번호 검증

- `password` : 로그인 인증할 때의 사용자가 입력한 비밀번호
- `userSalt` : DB에 저장되어있는 사용자의 `salt`
- `userPassword` : DB에 저장되어있는 사용자의 암호화된 비밀번호(해시 값)

단방향 암호화이므로 복호화는 진행할 수 없습니다. 따라서 비밀번호 암호화할 때의 동일한 방법으로 암호화를 진행하여 비교합니다. 이때 `salt`는 기존에 생성된 값을 사용해야 합니다.

만약 일치한다면 `true`, 일치하지 않는다면 `false`를 반환하도록 합니다.

```javascript
export const verifyPassword = async (password, userSalt, userPassword) => {
  const key = await pbkdf2Promise(password, userSalt, 99999, 64, "sha512");
  const hashedPassword = key.toString("base64");

  if (hashedPassword === userPassword) return true;
  return false;
};
```

`verifyPassword()` 함수의 사용 예시는 다음과 같습니다.  
이는 `passport`의 로그인 인증을 위한 콜백함수에서의 사용 예시입니다.

```javascript
passport.use(
  new LocalStrategy(
    {
      session: true, // 세션 저장 여부
      usernameField: "id", // form > input name
      passwordField: "password",
    },
    async (id, password, done) => {
      try {
        // 회원정보 조회
        const user = await User.findOne({
          where: {
            email: id,
          },
          raw: true,
        });

        // 회원정보가 없는 경우
        if (!user) {
          done(null, false, {
            message: "존재하지 않는 아이디입니다.",
          });
        }

        const verified = await verifyPassword(
          password,
          user.salt,
          user.password
        );
        // 비밀번호가 일치하지 않는 경우
        if (!verified) {
          done(null, false, {
            message: "비밀번호가 일치하지 않습니다.",
          });
        }
        done(null, user); // serializeUser로 user 전달
      } catch {
        done(null, false, {
          message: "서버의 문제가 발생했습니다. 잠시 후 다시 시도해 주세요.",
        });
      }
    }
  )
);
```

# References

- [crypto](https://nodejs.org/api/crypto.html)
- [(Crypto) 해시(hash)란?](https://medium.com/@su_bak/crypto-%ED%95%B4%EC%8B%9C-hash-%EB%9E%80-6962be197523)
- [NodeJS: bcrypt vs native crypto](https://stackoverflow.com/questions/6951867/nodejs-bcrypt-vs-native-crypto)
- [왜 Password hashing시 Bcrypt 가 추천되어질까?](https://velog.io/@kylexid/%EC%99%9C-bcrypt-%EC%95%94%ED%98%B8%ED%99%94-%EB%B0%A9%EC%8B%9D%EC%9D%B4-%EC%B6%94%EC%B2%9C%EB%90%98%EC%96%B4%EC%A7%88%EA%B9%8C#%EC%9A%94%EC%95%BD)
