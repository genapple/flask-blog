#!/usr/bin/python
#-*- coding:UTF-8 -*-

from blog import app
@app.route('/')
def hello_world():
    return 'hello world'
if __name__ == '__main__':
    app.run(debug=True)