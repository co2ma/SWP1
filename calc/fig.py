from cgi import parse_qs
from template import html


def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]
    asb = ""
    amb = ""
    try:
        if '' not in [a, b]:
            a, b = int(a), int(b)
            asb = str(a + b)
            amb = str(a * b)
        else:
            asb = "Please"
            amb = "Input Value"
    except:
        asb = "Please"
        amb = "Input @@@INT@@@ Value"
    response_body = html.format(asb, amb)
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]
