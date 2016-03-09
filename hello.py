#!/usr/bin/python
def application(environ, start_response):
    status = "200 OK"
    headers = [ ('Content-Type', 'text/plant') ]
    body=environ['QUERY_STRPING'].replace('&', '\n')
    start_response(status, headers )
    return [ body ]