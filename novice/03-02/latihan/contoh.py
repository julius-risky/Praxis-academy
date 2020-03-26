from flask import Flask

app = Flask('aplikasi keren')

@app.route('/')
def indeks():
    return 'hello'

@app.route('/login')
def login():
    return 'login'

@app.route('/hello/<name>')
def hello(name):
    return f'hello,{name}!'    
    
app.run(debug=True)