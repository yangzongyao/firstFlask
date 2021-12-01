from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World</h1>'

@app.route('/name/<name>')
def user(name):
    s = '<h1>Hi, '+ name +'</h1>'
    return s

app.run()