from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <h1>Привет из Render! 👋</h1>
    <p>Это моя лабораторная работа по модели PaaS.</p>
    <p>Версия: 1.0</p>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)