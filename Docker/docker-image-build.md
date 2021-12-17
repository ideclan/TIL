- [Docker 이미지 만들기](#docker-이미지-만들기)
  - [Commit](#commit)
  - [Dockerfile & Build](#dockerfile--build)

# Docker 이미지 만들기

## Commit

```bash
$ docker pull ubuntu
```

```bash
$ docker run -it --name ubuntu-basic ubuntu bash
```

```bash
$ apt update && apt install git
```

```bash
$ docker commit ubuntu-basic jiheon:ubuntu-git
```

```bash
$ docker images
```

```bash
$ docker run -it --name nodejs jiheon:ubuntu-git bash
```

```bash
$ apt update && apt install nodejs
```

## Dockerfile & Build
