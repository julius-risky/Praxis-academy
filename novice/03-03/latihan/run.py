from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def templatetest():
    return render_template("F:\\Praxis-academy\\novice\\03-03\latihan\\template.html",my_string='wheeee!',my_list = [0,1,2,3,4,5])

if __name__ == "__main__":
    app.run(debug=True) 

