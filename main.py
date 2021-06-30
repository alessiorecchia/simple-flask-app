from flask import Flask,render_template



app = Flask(__name__)

APP_NAME="Ubeyt's Portfolio"

MENU_ITEMS= ["about","projects","backoffice"]

@app.route("/")
def index():
    return render_template('/views/home.html',APP_NAME=APP_NAME,MENU_ITEMS=MENU_ITEMS)


@app.route("/about")
def about():
    return render_template('/about/index.html',APP_NAME=APP_NAME,MENU_ITEMS=MENU_ITEMS)

@app.route("/projects")
def projects():
    return  "<h1>Projects</h1>"


@app.route("/backoffice")
def backoffice():
    return  "<h1>Backoffice</h1>"



if __name__ == '__main__':
    app.run(debug=True)
