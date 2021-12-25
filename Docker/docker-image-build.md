- [Docker 이미지 만들기](#docker-이미지-만들기)
  - [Commit](#commit)
  - [Dockerfile & Build](#dockerfile--build)
    - [Dockerfile 작성 및 명령어](#dockerfile-작성-및-명령어)
      - [FROM](#from)
      - [RUN](#run)
      - [CMD](#cmd)
      - [LABEL](#label)
      - [MAINTAINER (Deprecated)](#maintainer-deprecated)
    - [예시](#예시)
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

|    명령어    |                                         설명                                          |
| :----------: | :-----------------------------------------------------------------------------------: |
|    `FROM`    |                                  베이스 이미지 지정                                   |
|    `RUN`     |           새로운 레이어에서 명령을 실행하고 결과를 이미지에 반영 (`commit`)           |
|    `CMD`     |                             컨테이너 실행 시 명령을 실행                              |
|   `LABEL`    |                       이미지에 Key-Value 형태의 메타데이터 추가                       |
| `MAINTAINER` |                             (Deprecated) 작성자 정보 추가                             |
|   `EXPOSE`   |                              공개할 컨테이너의 포트 지정                              |
|    `ENV`     |                             환경 변수를 Key-Value로 설정                              |
|    `ADD`     |     새 파일, 디렉토리 또는 원격 파일(URL)을 복사하여 이미지의 파일 시스템에 추가      |
|    `COPY`    |            새 파일 또는 디렉토리를 복사하여 컨테이너의 파일 시스템에 추가             |
| `ENTRYPOINT` |                             컨테이너 실행 시 명령을 실행                              |
|   `VOLUME`   |                                      볼륨 마운트                                      |
|    `USER`    |                                   사용자 권한 지정                                    |
|  `WORKDIR`   |                                  작업 디렉토리 지정                                   |
|    `ARG`     | `build` 시에만 사용되는 변수 정의, `--build-arg <name>=<value>` 옵션을 통해 전달 가능 |

#### FROM

베이스 이미지를 지정한다. `Dockerfile`은 `FROM`으로 시작해야 유효하다. 단, `ARG`는 `FROM` 앞에 올 수 있다.

`FROM`은 하나의 `Dockerfile` 내에서 여러 번 나타나 여러 이미지를 만들거나 한 빌드 단게를 다른 빌드 단계에 대한 종속성으로 사용할 수 있다.

```dockerfile
FROM <image>[:<tag>] [AS <name>]
```

첫 번째 `FROM` 이전에 발생하는 `ARG`에 의해 선언된 변수를 지원한다. 하지만 `FROM` 이전에 선언된 `ARG`는 빌드 단계 밖에 있으므로 `FROM` 이후에는 사용할 수 없다.

```dockerfile
ARG VERSION=latest

FROM <image>:${VERSION}

ARG VERSION # 빌드 단계에서 사용하려면 다시 ARG를 선언해야 한다.
```

#### RUN

현재 이미지 위에 있는 새 레이어에서 명령을 실행하여 결과를 `commit`한다. 이는 `Dockerfile`의 `RUN` 다음 단계에 사용된다.

`RUN`은 2가지 형식이 있다.

1. shell

`\`을 통해 하나의 `RUN`을 다음 줄로 계속할 수 있다.

```dockerfile
RUN <command>
```

2. exec

shell 문자열 병합을 방지할 수 있다. JSON 배열로 구문 분석되므로 `'`가 아닌 `"`를 사용해야 한다.

```dockerfile
RUN ["executable", "param1", "param2"]
```

exec 형식은 shell을 호출하지 않는다. 따라서 `RUN ["echo", "$HOME"]`에서 `$HOME`은 변수 대체를 수행하지 않기 때문에 shell 형식을 사용하거나 `RUN ["sh", "-c", "echo $HOME"]`처럼 shell을 직접 실행해야 한다.

#### CMD

컨테이너 실행 시 해당 명령을 실행한다. `Dockerfile`에는 하나의 `CMD` 명령어만 있을 수 있다. 여러 개의 `CMD`가 존재한다면 마지막 `CMD`만 적용된다.

`docker run`을 통해 실행될 때 직접 실행할 명령어를 인자로 전달한 경우 `Dockfile` 내에 `CMD`는 무시되고 전달한 명령어만 실행된다. 만약 `docker run <image> ls` 하게 되면 `ls` 명령만을 실행한다.

주로 배포하는 시점 및 환경에 따라 `<command>`를 다양하게 지정해야 하는 경우 활용할 수 있다.

`CMD`는 3가지 형식이 있다.

1. exec (선호)

JSON 배열로 구문 분석되므로 `'`가 아닌 `"`를 사용해야 한다.

```dockerfile
CMD ["executable","param1","param2"]
```

2. `ENTRYPOINT`에 대한 기본 매개변수

```dockerfile
CMD ["param1","param2"]
```

3. shell

```dockerfile
CMD command param1 param2
```

exec 형식은 shell을 호출하지 않는다. 따라서 `RUN ["echo", "$HOME"]`에서 `$HOME`은 변수 대체를 수행하지 않기 때문에 shell 형식을 사용하거나 `RUN ["sh", "-c", "echo $HOME"]`처럼 shell을 직접 실행해야 한다.

#### LABEL

이미지에 Key-Value 형태의 메타데이터를 추가한다.

```dockerfile
LABEL <key>=<value> <key>=<value> <key>=<value> ...
```

`LABEL`의 value 내에 공백을 포함하려면 `"`와 `\`를 사용한다.

```dockerfile
LABEL "com.example.vendor"="ACME Incorporated"
LABEL com.example.label-with-value="foo"
LABEL version="1.0"
LABEL description="This text illustrates \
that label-values can span multiple lines."
```

이미지는 여러 개의 `LABEL`이 있을 수 있으며 한 줄에 여러 `LABEL`을 지정할 수 있다. 기본 또는 상위 이미지에 포함된 `LABEL`은 이미지에 상속된다. 중복된 `LABEL`은 가장 최근에 설정된 값이 우선 적용된다.

```dockerfile
LABEL multi.label1="value1" multi.label2="value2" other="value3"

LABEL multi.label1="value4" \
      multi.label2="value5" \
      other="value6"

# "multi.label1": "value4",
# "multi.label2": "value5",
# "other": "value6",
```

이미지의 `LABEL`은 `docker image inspect`를 통해 확인이 가능하다. `LABEL`만 표시할 때는 `--format='{{ .Config.Labels }}'`를 사용한다.

```bash
$ docker image inspect --format='' <image>
```

```json
[
  {
    "Config": {
      "Labels": {
        "com.example.label-with-value": "foo",
        "com.example.vendor": "ACME Incorporated",
        "description": "This text illustrates that label-values can span multiple lines.",
        "multi.label1": "value4",
        "multi.label2": "value5",
        "other": "value6",
        "version": "1.0"
      }
      // ...
    }
    // ...
  }
]
```

#### MAINTAINER (Deprecated)

이미지의 작성자 정보를 추가한다.

```dockerfile
MAINTAINER <name>
```

`MAINTAINER`은 더 이상 사용되지 않으므로 `LABEL`을 사용해야 한다.

```dockerfile
LABEL maintainer="Jiheon Lee <jiheon.lee.dev@gmail.com>"
```

### 예시

```bash
$ echo "<h1>Hello, Docker</h1>" > index.html
```

```dockerfile
# ./Dockerfile

# 사용할 이미지 지정
FROM ubuntu:20.04

# 해당 명령을 실행하여 결과를 이미지에 반영
# DEBIAN_FRONTEND=noninteractive
#   - apt를 통해 설치하는 동안 상호작용하지 않도록 설정
RUN apt update && \
    DEBIAN_FRONTEND=noninteractive apt install -y apache2

# 작업 디렉토리 지정
WORKDIR /var/www/html

# 호스트의 파일을 컨테이너 경로 내에 복사
# WORKDIR를 통해 현재 경로는 /var/www/html
COPY ["index.html", "."]

# 공개할 컨테이너의 포트 지정
EXPOSE 80

# 컨테이너가 생성된 이후에 해당 명령을 실행
CMD ["apachectl", "-D", "FOREGROUND"]
```

```bash
$ docker build -t apache-server .
```

```bash
$ docker run -p 80:80 --name web-server apache-server
```

# References

- [Docker Docs](https://docs.docker.com/engine/reference/builder/)
- [[docker] RUN vs CMD vs ENTRYPOINT](https://blog.naver.com/PostView.nhn?isHttpsRedirect=true&blogId=freepsw&logNo=220982529575)
- [[Stack Overflow] Docker: Having issues installing apt-utils](https://stackoverflow.com/questions/51023312/docker-having-issues-installing-apt-utils/56569081#56569081)
