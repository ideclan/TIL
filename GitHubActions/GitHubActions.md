## 언어 및 프레임 워크

- 프로그래밍 언어로 작성된 프로젝트를 빌드하고 테스트하는 CI(Continuous Integration) workflow 작성
- workflow : 저장소에서 GitHub의 프로젝트를 빌드, 테스트, 패키지, 릴리스 또는 배포하기 위한 사용자 지정 자동화 프로세스
- 다양한 프로그래밍 언어 GitHub Actions 지원

## Python을 위한 GitHub Actions

- GitHub Runner는 Python, PyPy를 포함하여 사전에 설치된 tool cache가 존재
- Python Workflow 템플릿 제공
- 여러 Python 버전과 특정 Python 버전을 사용 가능
- 패키지 종속성 관리 가능
- 고유 키를 사용하여 pip 종속성 cache 하여 Workflow 실행할 때 종속성 복원
- 코드 빌드와 테스트

## CI : 지속적인 통합

- CI(Continuous Integration)는 매번 코드를 commit 할 때마다 오류의 원인을 찾을 때 디버그해야하는 코드의 양이 줄어듬
- 따라서 코드를 지속적으로 빌드 또는 테스트 필요
- 변경 사항을 보다 쉽게 병합 할 수 있음
- 디버깅 또는 병합 충돌 해결에 더 적은 시간을 소비하여 개발자는 코드 작성에 더 많은 시간 투자가 가능
- GitHub workflow를 사용한 CI

## 예제

- Django Test

                                                                                                       [ .github/workflows/Makefile.yml ]

```yaml
name: Makefile    // workflow 이름

on: [push]    // push 이벤트가 일어날 때 workflow 실행

jobs:
  build:

    runs-on: ubuntu-latest    // 최신 Ubuntu OS 에서 실행

    steps:
    - uses: actions/checkout@v2    // 현재 repository 파일 Checkout

    - name: Set up Python 3.7
      uses: actions/setup-python@v2    // 파이썬 버전 지정 action 사용
      with:
        python-version: 3.7

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install mypy pytest pylint pylint-django
        pip install -r app/requirements.txt

    - name: Run Makefile    // 아래 설명
      run:
        make checklist
```

- Django 는 Model 클래스 내부에 Objects 를 동적으로 생성하기 때문에 기존 pylint 를 사용하면 다음과 같은 에러 메시지를 확인 —> Class '{name}' has no 'objects' member
- 따라서 pylint-django 를 사용하여 해결 (플러그인 적용 = --load-plugins pylint_django)

                                                                                                                                                    [ Makefile ]

```makefile
typehint:
	mypy app/teacher/views.py

test:
	pytest app/teacher/views.py

lint:
	pylint --load-plugins pylint_django app/teacher/views.py

checklist: lint typehint test

.PHONY: typehint test lint checklist
```

- Makefile 은 리눅스 개발환경에서 빌드 또는 검사, 테스트를 자동화하는 방법
  mypy, pytest, pylint 를 target 으로 생성, 모든 target 을 실행하는 또 다른 target 을 생성 (=checklist)
- Shell 에서 make checklist 로 실행 (checklist 에서 작성한 lint, typehint, test 순서대로 target 실행)

- workflow 실행 결과

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b4ce166d-3928-4b68-96c6-48bc2a46db5e/_2020-08-03__12.35.43.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b4ce166d-3928-4b68-96c6-48bc2a46db5e/_2020-08-03__12.35.43.png)

## 참고

- GitHub Actions : [https://docs.github.com/en/actions](https://docs.github.com/en/actions)
- 폴더 캐싱하기 : [https://velog.io/@loakick/Github-Action-React-빌드하기](https://velog.io/@loakick/Github-Action-React-%EB%B9%8C%EB%93%9C%ED%95%98%EA%B8%B0)
- Code Coverage, Python 버전별 실행 : [https://blog.pingpong.us/python-in-pingpong/](https://blog.pingpong.us/python-in-pingpong/)
