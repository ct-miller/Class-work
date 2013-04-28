#!/usr/bin/env python

from bottle import template, route, run

@route('/hello')
@route('/hello/<name>')
def hello(name = 'World'):
    return template('hello_template', name=name)

run(host='localhost', port=8080, debug=True)
