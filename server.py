from api.frasco import Frasco
from urllib.request import Request, urlopen
import json

# Frascoアプリケーション
app = Frasco(__name__)

# ルートパス: index
@app.get('/', 'html')
def index():
    return 'html/index' # html/index.html描画

# APIサーバーを叩くためのルート
@app.get('/api/', 'json')
def api():
    with urlopen(Request('http://localhost:1000')) as res:
        return json.load(res)

# Frascoサーバー実行(localhost:8000)
if __name__ == "__main__":
    app.run(debug=True, port=8000)
