# Black

- Black 은 Code formatter 입니다.
- 설정의 여지가 없이 정해놓은 규칙을 무조건 따라야 하기 때문에
- 모든 개발자가 일관성 있는 코드를 작성할 수 있게 됩니다.
- black 패키지 설치 방법

```bash
$ pip install black
```

## Code Style

- 대부분 프로젝트는 여러 사람들과 협업하여 개발을 진행합니다.
- 개발자마다 선호하는 Code Style 이 다를 수 있으며
- 서로 다른 Code Style 로 갈등이 생기게 됩니다.

```python
# A 개발자
temp = {
   ‘a’: 1,
   ‘b’: 2,
   ‘c’: 3
}

# B 개발자
temp = { "a": 1, "b": 2, "c": 3 }
```

## Code format 검사

- 해당 파일이 Code format 이 필요한 지 확인이 가능합니다.
- `--check` 옵션 사용합니다.

![_2021-01-08__4 29 19](https://user-images.githubusercontent.com/48443734/106098736-e1f99000-617c-11eb-8c17-52da676a8b18.png)

## Code format 적용

- Black 명령어로 Code format 적용

```bash
$ black test.py
reformatted test.py
All done! ✨ 🍰 ✨
1 file reformatted.
```

![_2021-01-08__4 30 01](https://user-images.githubusercontent.com/48443734/106098745-e4f48080-617c-11eb-86ce-ff1dcbbad8a5.png)

## VSCode Black 적용

- VSCode 에서 코드를 수정하거나 저장 시 자동 black 실행시킵니다.
- 윈도우 Ctrl + Shift + P | 맥 Command + Shift + P

![_2021-01-08__4 31 45](https://user-images.githubusercontent.com/48443734/106098750-e6be4400-617c-11eb-901b-5180c4b56718.png)

## Git hook 설정

- 만약 black 적용을 안한 개발자가 commit 을 시도한다면
- 코드의 일관성이 깨지게 됩니다. 따라서 유지하기 위해서 방지가 필요합니다.
- Git hook 스크립트를 실행해주는 ‘pre-commit’ 패키지 설치

```bash
$ pip install pre-commit
```

- .pre-commit-config.yaml 파일 생성 후 내용을 추가합니다.

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: stable
    hooks:
      - id: black
```

- Git hook 스크립트 설치

```bash
$ pre-commit installed at .git/hooks/pre-commit
```

```bash
$ git commit
black…………………………………………………………………Failed
- hook id: black
- files were modified by this hook

reformatted test.py
All done! ✨ 🍰 ✨
1 file reformatted.
```
