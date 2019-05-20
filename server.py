from frasco import Frasco, Response
import json

# 認証処理用ユーザークラス
class User:
    def __init__(self, username):
        self.name = username

    @staticmethod
    def auth(data):
        with open('./data/users.json', 'rb') as f:
            users = json.load(f)
        # users.jsonに定義されているユーザーならログイン
        name = data.get('username')
        if name in users and data.get('password') == 'pass':
            return User(name)

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
#@app.secret(Response.redirect('/login'))
def index():
    return Response.html('html/index')

@app.get('/login')
def login():
    return Response.html('html/login')

# API
@app.get('/api/users')
@app.secret(Response.text('ログインしてください', 401))
def get_users():
    with open('./data/users.json', 'rb') as f:
        return Response.json({
            'user': app.current_user.name,
            'users': json.load(f)
        })

@app.auth('/api/login', '/api/logout', Response.text('ログアウトしました'))
def auth(user):
    if user:
        return Response.json({'user': user.name})
    return '', 400

# Frascoサーバー実行(localhost:8000)
if __name__ == "__main__":
    app.run(debug=True, port=8000)
