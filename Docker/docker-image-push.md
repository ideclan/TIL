- [Docker 이미지 배포하기](#docker-이미지-배포하기)
  - [Docker Hub](#docker-hub)
  - [GitHub](#github)
- [References](#references)

# Docker 이미지 배포하기

Image를 Registry로 `push`하여 업로드하는 과정을 통해 Image를 배포할 수 있다.

**Registry**

- Docker Hub Registry
- GitHub Packages Container Registry
- Amazon Elastic Container Registry
- Google Container Registry
- Harbor Registry

> Registry는 Docker Image를 공유하기 위한 서버 애플리케이션이다.

## Docker Hub

[Docker Hub](https://hub.docker.com/)에서 회원가입 후 로그인을 진행한다.

Repositories로 이동한 후 Create Repository를 클릭한다.

<img width="1392" alt="" src="https://user-images.githubusercontent.com/48443734/147847257-6625c05c-22be-4fdb-bd73-b8bd4c437892.png" />

생성할 Repository의 이름을 입력한 후 공개 여부를 선택하고 Create를 클릭한다. Private은 계정당 무료로 하나만을 제공하기 때문에 더 필요한 경우 비용을 지불해야 한다.

<img width="1392" alt="" src="https://user-images.githubusercontent.com/48443734/147847270-d2334b15-bd07-42c3-9c99-7ab0b341f5e4.png" />

생성된 Repository를 확인한 후 사전 준비를 마친다.

<img width="1392" alt="" src="https://user-images.githubusercontent.com/48443734/147847402-27c83624-ca9c-49be-b3c3-fc4446909732.png" />

CLI 환경에서 Docker Hub로 이미지를 업로드하기 위해 먼저 로그인을 진행한다.

```bash
$ docker login
```

`docker push`를 통해 원하는 이미지를 업로드한다.

```bash
$ docker push <username>/<image>:<tag>

# ex) docker push jiheon/apache-server:1.0
```

Docker Hub에 이미지가 업로드된 것을 확인할 수 있다.

<img width="1392" alt="" src="https://user-images.githubusercontent.com/48443734/147847693-4e1d334f-2dce-4a6d-9f4f-f9b0b4087d7b.png" />

`docker pull`을 통해 Docker Hub에 업로드된 이미지를 다운로드할 수 있다.

```bash
$ docker pull <username>/<image>:<tag>

# ex) docker pull jiheon/apache-server:1.0
```

## GitHub

사용 방법에 대하여 자세한 설명은 [Working with the Container registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry)에서 참고할 수 있습니다.

먼저 Container Registry에 인증하기 위한 Personal access token을 생성해야 한다.

우측 상단 Profile > Settings > 좌측 Developer settings > 좌측 Personal access tokens로 이동하여 Generate new token을 클릭한다.

Personal access token의 이름과 유효기간을 설정하고, 범위를 write/delete:packages로 선택한 후 Generate token 버튼을 클릭하면 생성된다.

<img width="1649" alt="" src="https://user-images.githubusercontent.com/48443734/147902102-7380db0d-5409-481b-b68d-7f19080cd48a.png" />

CLI 환경에서 생성한 Personal access token을 환경 변수로 저장한다.

```bash
$ export CR_PAT=YOUR_TOKEN
```

Container Registry에 로그인한다.

```bash
$ echo $CR_PAT | docker login ghcr.io -u USERNAME --password-stdin
```

`docker push`를 통해 원하는 이미지를 업로드한다.

```bash
$ docker push ghcr.io/<username>/<image>:<tag>

# ex) docker push ghcr.io/jiheon/apache-server:1.0
```

GitHub Packages에 이미지가 업로드된 것을 확인할 수 있다.

<img width="1649" alt="" src="https://user-images.githubusercontent.com/48443734/147903217-54bb0bbb-65a1-49ee-9c75-b32a5a774104.png" />

기본적으로 Private으로 되므로 Packages settings에서 Public으로 변경이 가능하다. 그리고 Connect Repository을 통해 원하는 Repository를 선택하여 연결이 가능하다.

<img width="1649" alt="" src="https://user-images.githubusercontent.com/48443734/147903388-63a695d2-4863-4f57-a9c1-8c4ba1fadce2.png" />

<img width="1649" alt="" src="https://user-images.githubusercontent.com/48443734/147903595-deeae4af-a637-437c-97ee-20a44b77da4b.png" />

# References

- [Docker Docs](https://docs.docker.com/engine/reference/run/)
- [GitHub Docs](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry)
