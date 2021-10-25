# -*- coding: utf-8 -*-
from flask import Flask, render_template
import os

app = Flask(__name__)


#@app.route('/')
#def hello():
    #return render_template('hello.html')

@app.route('/')
def hello():
    return render_template('sample.html')

def main():
    app.debug = True
    app.run(host='0.0.0.0', port=os.environ['PORT'])

if __name__ == '__main__':
    main()
