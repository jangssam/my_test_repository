# Flask on Render 실습용

## 1) 로컬 실행
가상환경 생성 후 설치한다.

- Windows (PowerShell)
  - python -m venv .venv
  - .\.venv\Scripts\activate
  - pip install -r requirements.txt
  - python app.py

브라우저에서 아래 주소로 확인한다.
- http://127.0.0.1:5000/
- http://127.0.0.1:5000/health

## 2) Render 배포(Web Service)
Render에서 New -> Web Service -> GitHub 저장소 선택 후 아래처럼 설정한다.

- Build Command
  - pip install -r requirements.txt

- Start Command
  - gunicorn app:app

배포 후 Render가 제공하는 URL로 접속해서 확인한다.
