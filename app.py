import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return """
    <h2>Hello Render + Flask</h2>
    <p>이 페이지가 보이면 배포가 정상이다.</p>
    <p><a href="/health">/health</a> 로 헬스체크 확인 가능하다.</p>
    """

@app.get("/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    # Render는 PORT 환경변수로 포트를 전달한다.
    port = int(os.environ.get("PORT", "5000"))
    # 외부 접속을 위해 0.0.0.0 바인딩이 필요하다.
    app.run(host="0.0.0.0", port=port)
