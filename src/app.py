# Flask application
from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Codespaces!'

def find_free_port():
    """Находит свободный порт"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]

if __name__ == '__main__':
    port = find_free_port()
    print(f"Запуск на порту: {port}")
    app.run(debug=True, port=port)