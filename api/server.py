from frasco import Frasco
import os, json

app = Frasco(__name__)

@app.get('/', 'json')
def index():
    with open(os.path.dirname(__file__) + '/data/users.json', 'rb') as f:
        return json.load(f)

# APIサーバー実行(localhost:1000)
if __name__ == "__main__":
    app.run(debug=True, port=1000)
