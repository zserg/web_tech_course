def app(env, start_response):
     q = env['QUERY_STRING'].split('&')
     body = ''
     for i in q:
        body += '{0}\r\n'.format(i)
     
     start_response('200 OK', [('Content-Type', 'text/plain')])
     return [body]

