from flask import Flask, request, make_response
import os

app = Flask(__name__)

# Общее количество всех посещений (в памяти)
total_visits = 0

@app.route('/')
def hello():
    global total_visits
    total_visits += 1

    # Читаем, сколько раз текущий пользователь заходил
    visits = request.cookies.get('visits')
    if visits:
        visits = int(visits) + 1
    else:
        visits = 1

    # Формируем ответ
    response_text = f"""
    <html>
    <head><title>Моя PaaS-лабораторная</title></head>
    <body style="font-family: Arial; text-align: center; padding: 50px; background: #f0f8ff;">
        <h1>✨ Привет из Render! ✨</h1>
        <p>Ты заходишь уже <strong>{visits}</strong> раз(а)!</p>
        <p>Всего посещений приложения: <strong>{total_visits}</strong></p>
        <p>Это демонстрация PaaS + простой логики на Python</p>
        <hr>
        <small>Обнови страницу, чтобы увидеть счётчики в действии!</small>
    </body>
    </html>
    """

    resp = make_response(response_text)
    resp.set_cookie('visits', str(visits))
    return resp

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)