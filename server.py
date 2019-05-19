from api.frasco import Frasco, Response
from flask import request
import json

# 認証処理用ユーザークラス
class User:
    def __init__(self, username):
        self.name = username

    @staticmethod
    def auth(data):
        if data.get('username') == 'admin' and data.get('password') == 'pass':
            return User('admin')

    @staticmethod
    def save(user):
        return user.name
    
    @staticmethod
    def load(session_id):
        return User(session_id)


# Frascoアプリケーション
app = Frasco(__name__, User=User)

# HTML
@app.get('/')
@app.require_login(Response.redirect('/login'))
def index():
    return Response.html('html/index') # html/index.html描画

@app.get('/login')
def login():
    return Response.html('html/login')

# API
@app.get('/api/users')
def get_users():
    with open('./api/users.json', 'rb') as f:
        return Response.json(json.load(f))

@app.auth('/api/login', '/api/logout', Response.redirect('/'))
def auth(user):
    if user:
        return Response.json({'user': user.name})
    return '', 400

# Frascoサーバー実行(localhost:8000)
if __name__ == "__main__":
    app.run(debug=True, port=8000)
