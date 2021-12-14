- [Docker 등장 배경](#docker-등장-배경)
  - [가상 머신 (VMware, virtualbox)](#가상-머신-vmware-virtualbox)
  - [Docker 개념](#docker-개념)
- [이미지 Pull](#이미지-pull)
- [컨테이너 Run](#컨테이너-run)

## Docker 등장 배경

하나의 어플리케이션을 만들기 위해서는 운영체제에 여러 소프트웨어를 설치해야 한다. 여러 개를 설치하는 과정에서 생각지도 못한 에러가 발생하거나 시간도 많이 소모하게 된다.

따라서 내가 원하는 운영체제와 소프트웨어가 설치되어 있는 컴퓨터를 누군가 제공해 준다면 얼마나 좋을까? 하지만 각각 필요한 운영체제와 소프트웨어가 설치된 여러 개의 컴퓨터를 빌린다는 것은 비용이 많이 든다.

### 가상 머신 (VMware, virtualbox)

하나의 컴퓨터 위에 여러 가상 컴퓨터를 만든 후, 그 위에 각각 필요한 운영체제와 소프트웨어를 설치한다. 이를 통해 여러 개의 컴퓨터를 별도로 구매하는 것이 필요하지 않게 된다.

하지만 큰 용량을 차지하는 운영체제를 여러 개 설치해야 하고 그리고 운영체제 위에 또 다른 운영체제가 있기 때문에 실행 속도 또한 느려지게 된다.

### Docker 개념

하나의 컴퓨터 안에서 가상 머신처럼 독립된 여러 실행환경을 만든다. 이는 실제 운영체제를 설치하지 않기 때문에 설치 용량이 적고 실행 속도 또한 빠르다.

이때 운영체제가 설치된 하나의 컴퓨터를 `host`, 각각의 독립된 실행환경을 `container`라고 한다.

## 이미지 Pull

- `Pull` : `Docker Hub`에서 `Image`를 다운로드 받는 행위
- `Run` : `Image`를 실행시켜 `Container`가 되도록 하는 행위

|         다운로드 서비스         | 소프트웨어 |   실행    |
| :-----------------------------: | :--------: | :-------: |
|            App Store            |  Program   |  Process  |
| Docker Hub 또는 Docker Registry |   Image    | Container |

[Docker Hub](https://hub.docker.com/)에서 Explore ❯ Containers로 이동하여 여러 이미지를 확인할 수 있다. 그중에 Official Image는 도커에서 공식적으로 관리하는 이미지이다.

> `Docker Registry`는 도커 이미지를 공유하기 위한 서버 어플리케이션이다.

CLI 환경에서 `pull` 명령어를 통해 진행한다. 예를 들어 Nginx 이미지라면 `NAME` 부분에 작성하면 된다.

```bash
$ docker pull NAME
```

`Pull`한 이미지들은 `images` 명령어를 통해 확인이 가능하다.

```bash
$ docker images
```

```bash
❯ docker pull nginx
Using default tag: latest
latest: Pulling from library/nginx
e5ae68f74026: Pull complete
21e0df283cd6: Pull complete
ed835de16acd: Pull complete
881ff011f1c9: Pull complete
77700c52c969: Pull complete
44be98c0fab6: Pull complete
Digest: sha256:9522864dd661dcadfd9958f9e0de192a1fdda2c162a35668ab6ac42b465f0603
Status: Downloaded newer image for nginx:latest
docker.io/library/nginx:latest

❯ docker images
REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
nginx        latest    f652ca386ed1   11 days ago   141MB
```

이미지를 삭제할 때는 `rmi` 명령어를 통해 진행한다. 해당 이미지를 `IMAGE` 부분에 작성한다.

```bash
$ docker rmi IMAGE
```

## 컨테이너 Run

이미지를 실행시켜 `Container`를 생성한다. `run` 명령어를 통해 진행하며 해당 이미지를 `IMAGE` 부분에 작성한다. 컨테이너에 이름을 부여할 때는 `--name` 옵션을 사용하여 `NAME` 부분에 원하는 이름을 작성한다.

```bash
$ docker run IMAGE

$ docker --name NAME IMAGE
```

생성된 여러 컨테이너들의 정보를 확인할 때는 `ps` 명령어를 통해 가능하다. 실행중인 컨테이너만 보이기 때문에 `-a` 옵션을 통해 종료된 컨테이너 또한 확인할 수 있다.

```bash
$ docker ps

$ docker ps -a
```

실행중인 컨테이너를 종료할 때는 `stop` 명령어를 통해 가능하다. 해당 컨테이너의 이름을 `CONTAINER` 부분에 작성한다.

```bash
$ docker stop CONTAINER
```

종료된 컨테이너를 다시 실행할 때는 `start` 명령어를 통해 진행한다. 해당 컨테이너의 이름을 `CONTAINER` 부분에 작성한다.

```bash
$ docker start CONTAINER
```

컨테이너의 로그들을 확인할 때는 `logs` 명령어를 통해 가능하다. 실시간 로그들을 확인하려면 `-f` 옵션을 사용한다.

```bash
$ docker logs CONTAINER

$ docker logs -f CONTAINER
```

컨테이너를 삭제할 때는 `rm` 명령어를 통해 진행한다. 해당 컨테이너의 이름을 `CONTAINER` 부분에 작성한다. 하지만 실행중인 컨테이너는 삭제할 수 없으므로, `stop`을 진행한 후 시도해야 한다. `stop`을 하지 않고 강제 삭제를 원한다면 `--force` 옵션을 사용한다.

```bash
$ docker rm CONTAINER

$ docker rm --force CONTAINER
```
