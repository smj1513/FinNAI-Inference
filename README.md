# FinNAI Inference Server

이 프로젝트는 FinNAI 모델을 제공하기 위한 FastAPI 기반의 추론 서버입니다.

## 🚀 시작하기

### 1. 사전 요구 사항

- Python 3.11 이상
- Git

### 2. 설치

프로젝트를 클론하고 필요한 패키지를 설치합니다.

```bash
# 1. 프로젝트 클론
git clone <repository-url>
cd FinNAI-Inference

# 2. 가상 환경 생성 및 활성화
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .\.venv\Scripts\activate  # Windows

# 3. 의존성 패키지 설치 ** 순서 꼭 지키기
pip install uv #Rust 기반 패키지 관리자 uv 설치 (매우 빠름)

#uv 모듈을 사용하여 현재 환경에 맞는 requirements.txt 파일을 자동으로 생성
uv pip compile requirements.in -o requirements.txt 
#생성된 requirements.txt 파일을 기반으로 의존성 설치
pip install -r requirements.txt
```

### 3. 서버 실행

아래 명령어를 사용하여 FastAPI 개발 서버를 실행합니다.

```bash
uvicorn web.main:app --host 0.0.0.0 --port 8000 --reload
```

서버가 정상적으로 실행되면 `http://127.0.0.1:8000` 주소로 접속할 수 있습니다.

## 📖 API 엔드포인트

서버가 정상적으로 실행되면 `http://127.0.0.1:8000/docs` 주소로 API 문서에 접속할 수 있습니다.

