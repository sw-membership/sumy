# sumy

## 설치하는 방법

KoNLPy를 설치해야해서 과정이 좀 복잡합니다. 설치하기 전에 파이썬 가상환경을 켜주세요.

먼저 JDK를 설치하고, JAVA_HOME 환경변수를 설정해주어야 합니다. 윈도우 사용자라면 [여기](https://devpad.tistory.com/5#:~:text=%EB%90%98%EC%97%88%EB%8A%94%EC%A7%80%20%ED%99%95%EC%9D%B8%ED%95%98%EC%9E%90.-,'%EC%9C%88%EB%8F%84%EC%9A%B0%ED%82%A4%2BR'%EC%9D%84%20%EB%88%8C%EB%9F%AC%EC%84%9C%20%EB%82%98%ED%83%80%EB%82%9C%20%EC%8B%A4%ED%96%89%EC%B0%BD%EC%97%90,%EC%A3%BC%EC%86%8C%EA%B0%80%20%EC%9E%88%EB%8A%94%EC%A7%80%20%ED%99%95%EC%9D%B8%ED%95%B4%EB%B3%B4%EC%9E%90.)를 참고해서 설치해주세요.

다음으로 Jpype 를 설치해주세요. 터미널에서 아래 명령어를 입력하면 됩니다.

```
pip install --upgrade pip
pip install JPype1-0.5.7-cp27-none-win_amd64.whl
```

그리고 다음 명령어를 사용해서 필요한 파이썬 패키지를 모두 다운로드합니다.

```
pip install -r requirements.txt
```

그러면 이제 sumy 를 사용할 수 있습니다. 아래는 테스트 코드입니다.

```shell
python3 test.py
# 이것은 요약하고 싶은 문자열입니다.
# 라고 나오면 성공
```

## 참고

[KoNLPy 설치](https://konlpy.org/ko/v0.5.2/install/)
