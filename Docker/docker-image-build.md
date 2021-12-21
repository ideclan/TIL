- [Docker 이미지 만들기](#docker-이미지-만들기)
  - [Commit](#commit)
  - [Dockerfile & Build](#dockerfile--build)
    - [Dockerfile 작성 및 명령어](#dockerfile-작성-및-명령어)
- [References](#references)

# Docker 이미지 만들기

## Commit

만약 컨테이너에서 여러 작업을 통해 수정한 후 컨테이너를 삭제한다면?  
모든 변경 사항들은 없어지게 된다.

따라서 `commit` 명령어를 통해 현재 컨테이너를 이미지로 저장하여 생성이 필요하다. 이때 변경 사항을 반영한 새 이미지를 생성한다.

```bash
$ docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]

# [:TAG] default : latest
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

해당 이미지를 `run` 하여 `ubuntu-base` 이름의 컨테이너를 생성하고 접속한다.

```bash
$ docker run -it --name ubuntu-base ubuntu bash
```

해당 컨테이너에서 git을 설치하고 `exit` 한다.

```bash
$ apt update && apt install git

$ exit
```

현재 `ubuntu-base` 이름의 컨테이너를 `REPOSITORY/IMAGE:TAG`로 `commit` 한다.

```bash
$ docker commit ubuntu-base jiheon/ubuntu-git:latest
```

`images`를 통해 생성된 새 이미지를 확인할 수 있다. 그리고 해당 이미지를 기반으로 여러 컨테이너를 생성하여 각각의 실행 환경을 구성할 수 있다.

```bash
$ docker images

❯ docker images
REPOSITORY          TAG       IMAGE ID       CREATED         SIZE
jiheon/ubuntu-git   latest    12648a4880cb   6 seconds ago   207MB
ubuntu              latest    ba6acccedd29   2 months ago    72.8MB
```

하지만 `commit`을 통해 만들어진 새 이미지는 어떻게 만들어졌는지 구체적으로 알 수 없으며 변경 사항의 추적이 어려워 불명확하다. 이는 일종의 백업의 느낌이 강하다.

## Dockerfile & Build

앞서 말했듯이 `commit`은 새 이미지를 만들 때 사용되는 명령어이다. `build` 또한 이와 같은 행동을 취하지만 `Dockerfile`을 통해 만들고자 하는 새 이미지를 구체적으로 실행 순서에 따라 기록할 수 있다.

- `Dockerfile` : `Container`에 필요한 패키지, 명령어, 환경 변수 설정 등을 기록한 텍스트 파일
- `build` : `Dockerfile`을 기반으로 새로운 `Image`를 생성하는 행위

```bash
$ docker build [OPTIONS] PATH | URL

# [OPTIONS]:
#   --tag , -t NAME:TAG
```

### Dockerfile 작성 및 명령어

|    명령어    |                                     설명                                     |
| :----------: | :--------------------------------------------------------------------------: |
|    `FROM`    |                              베이스 이미지 지정                              |
|    `RUN`     |      새로운 레이어에서 명령을 실행하고 결과를 이미지에 반영 (`commit`)       |
|    `CMD`     |                         컨테이너 실행 시 명령을 실행                         |
|   `LABEL`    |                  이미지에 Key-Value 형태의 메타데이터 추가                   |
| `MAINTAINER` |                        (Deprecated) 작성자 정보 기입                         |
|   `EXPOSE`   |                         공개할 컨테이너의 포트 지정                          |
|    `ENV`     |                         환경 변수를 Key-Value로 설정                         |
|    `ADD`     | 새 파일, 디렉토리 또는 원격 파일(URL)을 복사하여 이미지의 파일 시스템에 추가 |
|    `COPY`    |        새 파일 또는 디렉토리를 복사하여 컨테이너의 파일 시스템에 추가        |
| `ENTRYPOINT` |                         컨테이너 실행 시 명령을 실행                         |
|   `VOLUME`   |                                 볼륨 마운트                                  |
|    `USER`    |                               사용자 권한 지정                               |
|  `WORKDIR`   |                              작업 디렉토리 지정                              |
|    `ARG`     |           `build` 할 때 `--build-arg` 옵션을 통해 전달할 변수 정의           |

# References

- [Docker Docs](https://docs.docker.com/engine/reference/run/)
- [[docker] RUN vs CMD vs ENTRYPOINT](https://blog.naver.com/PostView.nhn?isHttpsRedirect=true&blogId=freepsw&logNo=220982529575)
