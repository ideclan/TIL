- [Docker 등장 배경](#docker-등장-배경)
  - [가상 머신 (Virtual Machine)](#가상-머신-virtual-machine)
  - [Docker 개념](#docker-개념)
- [이미지](#이미지)
  - [다운로드](#다운로드)
  - [조회](#조회)
  - [삭제](#삭제)
- [컨테이너](#컨테이너)
  - [실행](#실행)
  - [조회](#조회-1)
  - [중지](#중지)
  - [재실행](#재실행)
  - [로그](#로그)
  - [삭제](#삭제-1)
  - [접속](#접속)
- [호스트와 컨테이너](#호스트와-컨테이너)
  - [포트 연결](#포트-연결)
  - [파일 시스템 연결](#파일-시스템-연결)

## Docker 등장 배경

하나의 어플리케이션을 만들기 위해서는 운영체제에 여러 소프트웨어를 설치해야 한다. 여러 개를 설치하는 과정에서 생각지도 못한 에러가 발생하거나 시간도 많이 소모하게 된다.

따라서 내가 원하는 운영체제와 소프트웨어가 설치되어 있는 컴퓨터를 누군가 제공해 준다면 얼마나 좋을까? 하지만 각각 필요한 운영체제와 소프트웨어가 설치된 여러 개의 컴퓨터를 빌린다는 것은 비용이 많이 든다.

### 가상 머신 (Virtual Machine)

하나의 컴퓨터 위에 여러 가상 컴퓨터를 만든 후, 그 위에 각각 필요한 운영체제와 소프트웨어를 설치한다. 이를 통해 여러 개의 컴퓨터를 별도로 구매하는 것이 필요하지 않게 된다.

하지만 큰 용량을 차지하는 운영체제를 여러 개 설치해야 하고 그리고 운영체제(Host OS) 위에 또 다른 운영체제(Guest OS)가 있기 때문에 실행 속도 또한 느려지게 된다.

![](https://user-images.githubusercontent.com/48443734/146320687-f385836a-2f40-4f28-bad9-0da9e331d4d5.JPG)

> 가상화 소프트웨어 : VMware, Virtualbox

### Docker 개념

하나의 컴퓨터 안에서 가상 머신처럼 독립된 여러 실행환경을 만든다. 이는 실제 운영체제를 설치하지 않기 때문에 설치 용량이 적고 실행 속도 또한 빠르다.

이때 운영체제가 설치된 하나의 컴퓨터를 `Host`, 각각의 독립된 실행환경을 `Container`라고 한다.

![](https://user-images.githubusercontent.com/48443734/146320756-1b51389a-3717-4d6c-95a4-e085deed51dc.JPG)

## 이미지

|         다운로드 서비스         | 소프트웨어 |   실행    |
| :-----------------------------: | :--------: | :-------: |
|            App Store            |  Program   |  Process  |
| Docker Hub 또는 Docker Registry |   Image    | Container |

- `Pull` : `Docker Hub`에서 `Image`를 다운로드 받는 행위
- `Run` : `Image`를 실행시켜 `Container`가 되도록 하는 행위

![](https://user-images.githubusercontent.com/48443734/146320793-a2267da1-3c05-4c67-9be2-a3dafccd0e89.JPG)

[Docker Hub](https://hub.docker.com/)에서 Explore ❯ Containers로 이동하여 여러 이미지를 확인할 수 있다. 그중에 Official Image는 도커에서 공식적으로 관리하는 이미지이다.

> `Docker Registry`는 도커 이미지를 공유하기 위한 서버 어플리케이션이다.

### 다운로드

CLI 환경에서 `pull` 명령어를 통해 진행한다. 예를 들어 httpd 이미지라면 `NAME` 부분에 작성하면 된다.

```bash
$ docker pull NAME
```

### 조회

`Pull`한 이미지들은 `images` 명령어를 통해 확인이 가능하다.

```bash
$ docker images
```

### 삭제

이미지를 삭제할 때는 `rmi` 명령어를 통해 진행한다. 해당 이미지를 `IMAGE` 부분에 작성한다.

```bash
$ docker rmi IMAGE
```

## 컨테이너

### 실행

이미지를 실행시켜 `Container`를 생성한다. `run` 명령어를 통해 진행하며 해당 이미지를 `IMAGE` 부분에 작성한다. 컨테이너에 이름을 부여할 때는 `--name` 옵션을 사용하여 `NAME` 부분에 원하는 이름을 작성한다.

```bash
$ docker run [OPTIONS] IMAGE

# [OPTIONS]:
#   --name NAME
```

### 조회

생성된 여러 컨테이너들의 정보를 확인할 때는 `ps` 명령어를 통해 가능하다. 실행중인 컨테이너만 보이기 때문에 `--all`, `-a` 옵션을 통해 중지된 컨테이너 또한 확인할 수 있다.

```bash
$ docker ps [OPTIONS]

# [OPTIONS]:
#   --all, -a
```

### 중지

실행중인 컨테이너를 중지할 때는 `stop` 명령어를 통해 가능하다. 해당 컨테이너의 이름을 `CONTAINER` 부분에 작성한다.

```bash
$ docker stop CONTAINER
```

### 재실행

중지된 컨테이너를 다시 실행할 때는 `start` 명령어를 통해 진행한다. 해당 컨테이너의 이름을 `CONTAINER` 부분에 작성한다.

```bash
$ docker start CONTAINER
```

### 로그

컨테이너의 로그들을 확인할 때는 `logs` 명령어를 통해 가능하다. 실시간 로그들을 확인하려면 `--follow`, `-f` 옵션을 사용한다.

```bash
$ docker logs [OPTIONS] CONTAINER

# [OPTIONS]:
#   --follow, -f
```

### 삭제

컨테이너를 삭제할 때는 `rm` 명령어를 통해 진행한다. 해당 컨테이너의 이름을 `CONTAINER` 부분에 작성한다. 하지만 실행중인 컨테이너는 삭제할 수 없으므로, `stop`을 진행한 후 시도해야 한다. `stop`을 하지 않고 강제 삭제를 원한다면 `--force`, `-f` 옵션을 사용한다.

```bash
$ docker rm [OPTIONS] CONTAINER

# [OPTIONS]:
#   --force, -f
```

### 접속

`exec` 명령어를 통해 실행중인 컨테이너에서 새 명령을 실행한다. 해당 컨테이너의 이름을 `CONTAINER`, 실행시키고자 하는 명령을 `COMMAND` 부분에 작성한다.

```bash
$ docker exec [OPTIONS] CONTAINER COMMAND

# [OPTIONS]:
#   --interactive, -i
#   --tty, -t
```

컨테이너와 연결을 원한다면 `COMMAND` 부분에 `/bin/sh`를 작성한다. 이는 사용자가 입력한 명령어들을 `본 쉘(Bourne shell: sh)`이 받아 운영체제에게 전달한다. 본 쉘을 대체하기 위해 만들어진 `배쉬 쉘(Borune-agin shell: bash)`이 있다면 이를 사용하는 것을 추천한다.

하지만 `/bin/sh` 명령어를 실행하면 아무것도 실행하지 않은 것 처럼 아무런 변화가 없다. `Docker`는 `Virtual Machine`처럼 하나의 온전한 서버를 제공하는 것이 아닌 명령을 실행하는 환경만 제공하고 그 명령을 실행할 뿐이다. 즉, `Container`는 단지 명령만 실행하고 그 결과만 보여주는 기능을 수행한다.

따라서 지속적인 연결을 위해 `-it` 옵션을 사용해야 한다.

- `--interactive`, `-i` : 표준 입력과 표준 출력을 키보드와 화면을 통해 가능하도록 한다.
- `--tty`, `-t` : 콘솔 및 터미널 환경(TTY: Tele Type Writer)을 에뮬레이션(Emulation) 하도록 한다.

> 에뮬레이션(Emulation) : 한 컴퓨터가 다른 컴퓨터처럼 똑같이 작동하도록 하는 것

```bash
$ docker exec -it CONTAINER /bin/sh # 또는 /bin/bash
```

컨테이너 접속을 종료하려면 `exit` 명령어를 통해 가능하다.

> `exec`와 `attach`의 차이점?
>
> - `exec` : 이미 시작된 컨테이너에서 새로운 것을 실행하기 위한 것, 쉘의 새 인스턴스를 사용한다. 컨테이너에서 나가도 컨테이너가 종료되지 않는다.
> - `attach` : 추가 작업을 실행하기 위한 것이 아닌 실행중인 프로세스에 연결하기 위한 것, 쉘의 한 인스턴스를 사용한다. 컨테이너에서 나가면 컨테이너가 종료된다.
>
> [[Stack Overflow] difference between docker attach and docker exec](https://stackoverflow.com/questions/30960686/difference-between-docker-attach-and-docker-exec)

## 호스트와 컨테이너

### 포트 연결

웹 브라우저가 `port: 80`으로 요청(request)을 보냈을 때 `port: 80`의 요청을 대기하는 웹 서버가 `File System`에서 이에 해당하는 `HTML`을 찾아 응답(response)한다.

도커를 사용하여 `port: 80`의 요청을 대기하는 웹 서버를 `Container`로 실행한다면 위와 동일하게 동작하는가?

이는 동작하지 않는다. [Docker 개념](#docker-개념)으로 `Host`와 `Container`는 서로 독립된 실행환경이므로 독립된 `port`와 `File System`을 갖는다. 따라서 `Host`와 `Container`의 `port`를 연결해주어야 한다.

![](https://user-images.githubusercontent.com/48443734/146320955-ea189b3c-8d24-498b-abad-6a16a4e46a66.JPG)

```bash
$ docker run -p HOST_PORT:CONTAINER_PORT IMAGE
```

`run` 명령어에서 `--publish`, `-p` 옵션을 사용한다. `:` 기준으로 앞에는 `Host`, 뒤에는 `Container`의 `port`를 작성하면 된다.

이처럼 연결된 `port`를 통해 신호를 전달하는 것을 `포트포워딩(Port Forwarding)`이라 한다.

### 파일 시스템 연결

만약 컨테이너에 접속하여 파일을 수정한 후 컨테이너를 삭제한다면 복구할 수 있는가?

이는 불가능하다. 앞서 말했듯이 `Host`와 `Container`는 서로 독립된 `File System`을 갖는다. 따라서 각 `File System`을 연결하여 `Host`에서 파일을 수정했을 때 `Container` 또한 수정사항이 반영되도록 하는 것이 바람직하다.

![](https://user-images.githubusercontent.com/48443734/146321666-bb1d7391-926a-4a06-9403-0b955bdf241e.JPG)

```bash
$ docker run -v HOST_PATH:CONTAINER_PATH IMAGE
```

`run` 명령어에서 `--volume`, `-v` 옵션을 사용한다. `:` 기준으로 앞에는 `Host`, 뒤에는 `Container`의 `path`를 작성하면 된다.

# References

- [Docker Docs](https://docs.docker.com/engine/reference/run/)
- [개발자가 처음 Docker 접할때 오는 멘붕 몇가지](https://www.popit.kr/%EA%B0%9C%EB%B0%9C%EC%9E%90%EA%B0%80-%EC%B2%98%EC%9D%8C-docker-%EC%A0%91%ED%95%A0%EB%95%8C-%EC%98%A4%EB%8A%94-%EB%A9%98%EB%B6%95-%EB%AA%87%EA%B0%80%EC%A7%80/)
