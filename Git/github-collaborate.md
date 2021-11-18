![Github](https://images.velog.io/images/jiheon/post/e801d981-6a5c-45a7-bd8e-dd6dfe7b3238/5.png)

Git 이란 무엇인지, 왜 사용해야 하는지에 대해서는 이해했지만 실제로 어떠한 방식으로 협업을 해야 하는 지 어려워하시는 분들에게 도움이 되고자 제가 협업할 때의 방법들을 글로 작성하게 되었습니다.

> 이 글은 먼저 Git과 Github 에 대하여 학습하신 후에 보시면 좋을 것 같습니다.

# 협업하는 방법

1. 공용 Repository 에서 오른쪽 상단의 Fork 버튼을 클릭하여 Fork 합니다.

![Fork](https://images.velog.io/images/jiheon/post/e0d9ec7c-b3f5-4de9-821c-827546569b8a/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-09-09%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%209.44.40.png)

2. Fork 한 자신의 Repository를 원하는 위치에서 Clone 합니다.
   직접 작성해도 좋고, Code 버튼을 클릭하여 복사해서 Clone 해도 좋습니다.

```bash
$ git clone https://github.com/<사용자명>/<Repository명>
```

![clone](https://images.velog.io/images/jiheon/post/d4eeb5ea-fc0b-493e-be5b-d2ec99529d18/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-09-09%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%209.46.38.png)

3. Clone 한 Repository 로 이동하여 Remote 를 추가합니다.

```bash
$ cd <Repository명>
$ git remote <추가할 remote명> https://github.com/<공용 Repository 소유자명>/<공용 Repository명>

# 추가된 remote 확인
$ git remote -v
```

4. 작업하기 전에 항상 공용 Repository 를 Pull 하여 최신 상태를 유지한 후 진행합니다.

```bash
$ git pull <추가한 remote명> main
```

5. Issues 에서 오른쪽에 New issue 버튼을 클릭하여 진행할 작업에 대한 issue 를 작성합니다.
   issue 를 추가하면 #86 과 같이 issue 번호가 붙게 됩니다.

![issue list](https://images.velog.io/images/jiheon/post/2756582d-56ad-427a-9f66-c15b0644a421/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-09-09%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2011.23.30.png)

![issue detail](https://images.velog.io/images/jiheon/post/ae5403b6-fd9a-4942-95b9-62407330945b/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-09-09%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2011.25.15.png)

6. issue 에 해당되는 Branch 를 생성 후 작업을 진행합니다.
   위의 5번에서의 issue 번호를 Branch 명에 넣게 되면 추후 진행사항들을 파악하기 쉬워집니다.
   ex) "feature/86-mobilePayment"

```bash
# branch 생성
$ git branch <branch명>
# branch 이동
$ git checkout <branch명>

# branch 생성과 함께 이동
$ git checkout -b <branch명>
```

7. 작업한 내용을 Add, Commit 합니다.

```bash
$ git add <파일명>
$ git commit -m "<commit 메세지>"
```

8. 자신의 Repository (=origin) 으로 Push 한 후,
   Github 으로 이동하여 Pull requests 에서 New pull request 버튼을 클릭하여
   해당 branch 를 공용 Repository main 으로 Pull Request 합니다.

```bash
$ git push origin <branch명>
```

![pull request](https://images.velog.io/images/jiheon/post/01c9eb0c-2c9e-4415-9f62-adb55dca6840/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-09-10%20%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB%2012.11.34.png)

왼쪽이 공용 Repository, 오른쪽이 자신의 Repository 입니다.

![pull request detail](https://images.velog.io/images/jiheon/post/43f7e210-24c7-418f-a5b5-0989300f8a03/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-09-10%20%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB%2012.13.13.png)

9. 리뷰어가 코드 리뷰를 진행하여 공용 Repository main 으로 Merge 합니다.

# 코드 충돌과 병합 오류

만약 작업하고 있는 도중에 누군가의 새로운 작업 내용이 반영되어 코드 충돌 또는 병합 오류가 발생했을 때는 어떻게 해야 할까요?

## git stash

`git stash` 는 변경사항들을 임시로 저장할 수 있도록 합니다.
따라서 현재 변경사항들을 stashed 상태로 만든 후 Pull 하여 stash 를 적용하면 대응할 수 있습니다.

> 작업하던 내용을 잠시 멈추고 다른 작업을 해야할 때도 유용합니다.

```bash
# 새로운 stash 를 생성하여 stack 에 저장
$ git stash

# stash 목록 조회
$ git stash list

# stash 적용
$ git stash apply [stash명]

# stash 제거
$ git stash drop [stash명]

# stash 되돌리기
$ git stash show -p [stash명] | git apply -R
```

stash 를 사용하다 보면 다음과 같은 상황들을 볼 수 있습니다.

```
<<<<<<< HEAD
function a() {}
=======
function a(str) {}
>>>>>>> develop
```

`=======` 기준으로 위의 내용이 현재 파일의 내용,
아래의 내용이 `develop` branch 의 파일의 내용입니다.
두 파일의 내용 참고하여 병합한 후에 특수기호들을 제거해주시면 됩니다.

# References

- [[Git] git stash 명령어 사용하기](https://gmlwjd9405.github.io/2018/05/18/git-stash.html)
