class Snail:
    def __call__(self, environ, start_response):
        data = b'Hello world. Yhis is cool banana!git'
        start_response('200 OK', [
            ('Content-Type', 'text/plain'),
            ('Content-Length', str(len(data)))
        ])
        return iter([data])