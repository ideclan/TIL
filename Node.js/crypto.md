# Crypto

Node.js 내장 모듈이며, 여러 해시 함수를 통한 암호화 기능을 제공

> The crypto module provides cryptographic functionality that includes a set of wrappers for OpenSSL's hash, HMAC, cipher, decipher, sign, and verify functions.

## Hash

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

사용자의 비밀번호는 본인만이 알 수 있어야하고, 만약 비밀번호를 잃어버린 경우 복호화하는 과정에서 노출되기 때문에 대부분 재설정을 할 수 있도록 한다. 따라서 단방향 암호화 방식을 사용한다.

## Crypto vs Bcrypt

[Bcrypt](https://github.com/kelektiv/node.bcrypt.js)는 암호를 해시하는 데 도움이 되는 라이브러리입니다. 해싱에 느리고 비용이 많이 드는 Blowfish 알고리즘으로 구현되었습니다. 따라서 강력한 보안이 필요로 할 때 사용하면 좋을 것 같습니다.

# References

- [crypto](https://nodejs.org/api/crypto.html)
- [(Crypto) 해시(hash)란?](https://medium.com/@su_bak/crypto-%ED%95%B4%EC%8B%9C-hash-%EB%9E%80-6962be197523)
- [NodeJS: bcrypt vs native crypto](https://stackoverflow.com/questions/6951867/nodejs-bcrypt-vs-native-crypto)
- [왜 Password hashing시 Bcrypt 가 추천되어질까?](https://velog.io/@kylexid/%EC%99%9C-bcrypt-%EC%95%94%ED%98%B8%ED%99%94-%EB%B0%A9%EC%8B%9D%EC%9D%B4-%EC%B6%94%EC%B2%9C%EB%90%98%EC%96%B4%EC%A7%88%EA%B9%8C#%EC%9A%94%EC%95%BD)
