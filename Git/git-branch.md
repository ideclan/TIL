![git-branch](https://images.velog.io/images/jiheon/post/9add9631-ca19-427c-ae1f-ba3551f8011d/04%20Hotfix%20branches.svg)

> branch 의 전체 흐름

최근에 `issue01/login` 처럼 branch naming 을 하면서 개발을 진행하던 도중에, 좀 더 체계적인 방법 찾아 적용하면서 해당 글을 작성하게 되었습니다.

따라서 git branch 를 어떻게 활용하는 게 좋을 지 알아보겠습니다.

# Git branch 종류

## 1. main (= master)

제품 출시를 위한 branch
배포 (= release) 이력을 관리하기 위해 사용한다.

## 2. develop

제품 출시를 앞두어, 각 출시 버전들을 개발하기 위한 branch
기능 개발이 이루어진 branch (= feaure branch) 와 병합하기 위해 사용한다.

## 3. feature

기능을 개발하기 위한 branch
develop branch 로 부터 분기하여, 새로운 기능 개발 또는 버그 수정하기 위해 사용한다.

개발을 완료한 feature branch 는 공유할 필요가 없기에,
develop branch 와 merge 후 자신의 로컬 저장소에서 관리하거나 삭제하는 것을 권장한다.

> 코드 변경사항은 develop branch 에서 공유합니다.

```bash
# develop branch 로 부터 분기
$ git checkout -b feature/login develop

# 개발을 완료 후 develop branch 이동
$ git checkout develop

# [--no-ff] : feature branch 의 commit 이력들을 모두 합쳐서 하나의 새로운 commit 객체 생성
$ git merge --no-ff feature/login

---

# 선택사항 : feature branch 제거
$ git branch -d feature/login
```

![--no-ff](https://images.velog.io/images/jiheon/post/ab70a581-ef49-4335-9ef1-8c68c22dd5c4/feature-branch-merge.png)

## 4. release

출시 버전을 위한 branch
배포를 위해 사용하며, develop branch 에 여러 기능들이 모여
배포 가능한 상태가 될 때 release branch 로 분기한다.

> 여러 팀이 각 버전 별로 진행하여 배포가 가능하다.
> A 팀은 1.2 버전을 준비하는 동안 B 팀은 다음 배포 1.3 버전을 준비한다.

## 5. hotfix

출시 버전에서 버그를 수정하기 위한 branch
배포 후 문제가 발생하여 긴급하게 버그 수정이 필요할 때
master 로 부터 분기하여 진행 후 merge 하는데 사용한다.

> 새로운 버전 이름으로 태그를 해야한다.
> hotfix branch 의 변경 사항은 develop branch 에도 병합해야한다.

```bash
# develop branch 로 부터 분기
$ git checkout -b hotfix-1.2.1 master

# 수정 후 master branch 로 이동
$ git checkout master

# hotfix branch 와 master branch 병합
$ git merge --no-ff hotfix-1.2.1

# 병합한 commit 에 새로운 버전으로 태그 부여
$ git tag -a 1.2.1

---

# develop branch 도 master branch 와 동일하게 진행
$ git checkout develop
$ git merge --no-ff hotfix-1.2.1
```

![hotfix](https://images.velog.io/images/jiheon/post/2db1885e-fab1-43a1-b25e-d4cc9e748a8a/hotfix-branch.png)

# References

- [Git branch & naming](https://velog.io/@kim-jaemin420/Git-branch-naming)
- [[GitHub] Git 브랜치의 종류 및 사용법 (5가지)](https://gmlwjd9405.github.io/2018/05/11/types-of-git-branch.html)
