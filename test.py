#coding=utf8
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return ["Hello\n"] #python2
    #return [b"Hello World"] # python3
