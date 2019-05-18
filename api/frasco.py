'''
Flask Webserver Wrapper
'''
import flask
from flask import Flask, render_template, jsonify
from functools import wraps

class Frasco(Flask):
    ''' Flask wrapper class '''
    class Response:
        ''' Response class '''
        @classmethod
        def text(self, string, status=200):
            ''' render string '''
            return string, status

        @classmethod
        def html(self, filename, status=200):
            ''' render html file '''
            with open(filename + '.html', 'rb') as f:
                return f.read(), status
        
        @classmethod
        def template(self, filename, kwargs, status=200):
            ''' render template html file '''
            # template file should be in 'templates/'
            return render_template(filename + '.html', **kwargs), status

        @classmethod
        def json(self, data, status=200):
            ''' response of json '''
            res = jsonify(data)
            res.status_code = status
            return res
        
        @classmethod
        def redirect(self, url, status=302):
            ''' redirect to url '''
            return flask.redirect(url, status)
    
    def routes(self, route, action, methods):
        ''' routing decorator base
        params:
            route: '/<int:arg>/<string:arg>/<float:arg>/<path:arg>/<uuid:arg>'
            action: 'text' | 'html' | 'template' | 'json' | 'redirect'
            methods: ['GET', 'POST', 'PUT', 'DELETE']
        example:
            @frasco.routes('/', 'template', ['GET'])
            def index():
                return 'template/index', {'content': 'Hello, world'}, 200
        '''
        def _deco(func):
            @wraps(func) # デコレータした関数名が`wrapper`になるのを防ぐ: ルーティングを複数定義したときルートが上書きされるのを防ぐ
            def wrapper(*args, **kwargs):
                act = getattr(self.Response, action, None)
                if act:
                    act_args = func(*args, **kwargs)
                    if isinstance(act_args, tuple):
                        return act(*act_args)
                    return act(act_args)
                return '<p>Unexpected action: "' + action + '"</p>\n' \
                    + '<p>Available actions: "text", "html", "template", "json", "redirect"</p>', 500
            return self.route(route, methods=methods)(wrapper)
        return _deco

    def get(self, route, action):
        ''' get method routing decorator '''
        return self.routes(route, action, ['GET'])

    def post(self, route, action):
        ''' post method routing decorator '''
        return self.routes(route, action, ['POST'])
    
    def put(self, route, action):
        ''' put method routing decorator '''
        return self.routes(route, action, ['PUT'])
    
    def delete(self, route, action):
        ''' delete method routing decorator '''
        return self.routes(route, action, ['DELETE'])
