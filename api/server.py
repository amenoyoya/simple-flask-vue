#!/usr/bin python
from pylib.web.frasco import Frasco, Response
from typing import Tuple

app: Frasco = Frasco(__name__)

@app.get('/api/')
def index() -> Tuple[str, int]:
    return Response.json({
        'message': 'Hello, World'
    })

if __name__ == "__main__":
    app.run(port='8000', debug=True)
