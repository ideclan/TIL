- [Docker 이미지 만들기](#docker-이미지-만들기)
  - [Commit](#commit)
  - [Dockerfile & Build](#dockerfile--build)

# Docker 이미지 만들기

## Commit

만약 컨테이너에서 여러 작업을 통해 수정한 후 컨테이너를 삭제한다면?  
모든 변경 사항들은 없어지게 된다.

따라서 `commit` 명령어를 통해 현재 컨테이너를 새로운 이미지로 저장하여 생성이 필요하다. 이때 변경 사항을 반영한 이미지를 생성한다.

```bash
$ docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]
```

![](https://user-images.githubusercontent.com/48443734/146636457-bc008dc0-ca6b-46e8-8cb8-439146b87341.JPG)

- `Pull` : `Docker Hub`에서 `Image`를 다운로드 받는 행위
- `Run` : `Image`를 실행시켜 `Container`가 되도록 하는 행위
- `Commit` : `Container`의 변경 사항을 반영한 새로운 `Image`를 생성하는 행위
- `Push` : `Image`를 `Docker Hub`에 업로드 하는 행위

예시로 ubuntu 이미지로 컨테이너를 생성한다. 해당 컨테이너 내부에서 git을 설치한 후 `commit`을 통해 새 이미지를 생성한다. 이때 git을 설치하는 행위는 컨테이너의 변경 사항을 의미한다.

먼저 ubuntu 이미지를 `pull` 한다.

```bash
$ docker pull ubuntu
```

해당 이미지를 `run` 하여 `ubuntu-basic` 이름의 컨테이너를 생성하고 접속한다.

```bash
$ docker run -it --name ubuntu-basic ubuntu bash
```

해당 컨테이너에서 git을 설치하고 `exit` 한다.

```bash
$ apt update && apt install git

$ exit
```

현재 `ubuntu-basic` 이름의 컨테이너를 `REPOSITORY/IMAGE:TAG`로 `commit` 한다.

```bash
$ docker commit ubuntu-basic jiheon/ubuntu-git:latest
```

`images`를 통해 생성된 새 이미지를 확인할 수 있다. 그리고 해당 이미지를 기반으로 여러 컨테이너를 생성하여 각각의 실행 환경을 구성할 수 있다.

```bash
$ docker images

❯ docker images
REPOSITORY          TAG       IMAGE ID       CREATED         SIZE
jiheon/ubuntu-git   latest    12648a4880cb   6 seconds ago   207MB
ubuntu              latest    ba6acccedd29   2 months ago    72.8MB
```

하지만 `commit`을 통해 만들어진 새 이미지들은 어떻게 만들어졌는지 알 수 없어 불명확하다.

## Dockerfile & Build
