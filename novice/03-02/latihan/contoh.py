from flask import Flask

app = Flask('aplikasi keren')

@app.route('/')
def indeks():
    return 'hello'
app.run(debug=True)