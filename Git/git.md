# Git

- 리누스 토발즈에 의해 개발된 Git은 컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율하기 위한 **분산 버전 관리 시스템**이다.
- 소프트웨어를 개발하는 기업의 핵심 자산인 소스코드를 효율적으로 관리할 수 있게 해주는 **형상 관리 도구**라고도 한다.
- 무료이며 오픈소스이다.

## Git을 사용해야하는 이유

1. 소스코드를 주고 받을 필요 없이, 같은 파일을 **여러 명이 동시에 작업하는 병렬 개발이 가능**하다.
2. 분산 버전관리이기 때문에 인터넷이 연결되지 않은 곳에서도 개발을 진행할 수 있으며, 중앙 저장소가 날라가버려도 다시 **원상복구**할 수 있습니다.
3. 다른 사람과 함께 일하는 경우, **여러명과 함께 코드 공유를 공유**하고 변경사항에 대해 충돌하는 일이 발생하지 않는다.
4. 팀 프로젝트가 아닌, 개인 프로젝트일지라도 Git을 통해 버전 관리를 하면 **체계적인 개발이 가능**하다.
5. 개발 환경에서 **실수를 할 수 있기 때문**이다.

## Git 명령어 정리

### 환경 설정

- 전역 사용자명/이메일 설정

```bash
$ git config - -global user.name “Your name”
$ git config - -global user.email “Your email address”
```

### 기본 명령어

- 현재 git의 버전을 확인

```bash
$ git --version
```

- 현재 디렉토리에 git 저장소를 생성

```bash
$ git init
```

- 파일은 수정했지만 아직 stage area에 올라가지 않은 파일들을 staging area에 올림

```bash
$ git add {파일이름}
```

- staging area에 올라가 있는 파일들을 commit

```bash
$ git commit {옵션} {파일이름}
       -a : 기존에 add를 하지 않아도 바로 staging area에 올려서 commit 함
       -m : editor없이 commit의 메시지를 입력 # $ git commit -m test.txt "Version1"
```

- 파일들의 변경사항을 조회

```bash
$ git status
```

- 이전에 어떠한 작업을 했는지 조회

```bash
$ git diff
```

- 두 개의 버전에서 소스코드의 차이점을 보여줌

```bash
$ git diff {commit 고유번호}..{다른 commit 고유번호}
```

### Branch

- 현재 존재하는 브랜치를 조회

```bash
$ git branch
       -r : 원격저장소의 브랜치를 확인
```

- 브랜치 생성

```bash
$ git branch {branch명}
       - master가 기본 branch
```

- 다른 브랜치로 변경

```bash
$ git checkout {branch명}
```

### Merge

- 현재 브랜치에서 입력한 브랜치와 merge(합치다)

```bash
$ git merge {branch명}
```

### 로그 관리

- 변경된 사항의 기록들을 확인

```bash
$ git log
       -p : 더 자세하게 보여줌
```

- 기존의 commit에서 변경한 내용을 취소해서 새로운 commit을 만듬

```bash
$ git revert
       -n : 바로 commit 하지 않기 때문에 여러번한 다음에 commit이 가능
```

- 예전 버전으로 돌아감

```bash
$ git reset {commit 고유번호} --hard
```

### 원격저장소 (remote repository)

- 원격저장소 만들 때는 수정이 불가한 저장소의 역할만 하는 디렉토리를 만들어야 한다.

```bash
$ git init --bare {디렉토리명}
```

- 현재 저장소에 원격저장소를 add(연결)한다. 경로 앞에 origin이라 하면 경로는 origin을 가르킴, 원격저장소의 기본 이름은 origin

```bash
$ git remote add origin {경로}
```

- 추가한 원격저장소의 목록을 확인

```bash
$ git remote
       -v : 자세하게 보여줌
```

- 원격저장소를 제거

```bash
$ git remote remove origin
```

- 현재 브랜치를 연결시킨 지역저장소에서 원격저장소에 푸쉬, 즉 업로드

```bash
$ git push origin
```

- 원격저장소의 파일들을 지역저장소로 가져옴

```bash
$ git pull
```

- 원격저장소의 파일들을 디렉토리를 생성하여 안에 다운로드

```bash
$ git clone {원격저장소 주소} {디렉토리명}
```
