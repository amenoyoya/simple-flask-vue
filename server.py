from api.frasco import Frasco
import json

# Frascoアプリケーション
app = Frasco(__name__)

# ルートパス: index
@app.get('/', 'html')
def index():
    return 'html/index' # html/index.html描画

# APIルート
@app.get('/api/<string:target>', 'json')
def api(target):
    with open('./api/' + target + '.json', 'rb') as f:
        return json.load(f)

# Frascoサーバー実行(localhost:8000)
if __name__ == "__main__":
    app.run(debug=True, port=8000)
