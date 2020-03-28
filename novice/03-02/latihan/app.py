from flask import Flask
from models import HelloModel

app = Flask(__name__)

@app.route('/')
def index():
    #membuat objek dari kelas model
    model= HelloModel()
    return model.gettext()

if __name__ == "__main__":
    app.run(debug=True)