from flask import Flask, request
from pprint import pprint

# HTMLファイル読み込み(描画)
def render(filename):
    with open(f'html/{filename}.html', 'rb') as f:
        return f.read()

# Flaskアプリケーション
app = Flask(__name__)

# ルートパス: index
@app.route('/', methods=['GET'])
def index():
    pprint(request.environ)
    return render('index') # html/index.html描画

# Flaskサーバー実行(localhost:8000)
if __name__ == "__main__":
    app.run(debug=True, port=8000)
