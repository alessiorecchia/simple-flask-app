from flask import Flask,render_template,request,redirect,url_for
from constants.items import *
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config["UPLOAD_FOLDER"]="files"

@app.route("/")
def index():
    return render_template('/views/home.html',APP_NAME=APP_NAME,MENU_ITEMS=MENU_ITEMS,SOCIAL_LINKS=SOCIAL_LINKS,MY_PROJECTS=MY_PROJECTS)
 
@app.route("/projects")
def projects():
    return  render_template("/views/projects/index.html",APP_NAME=APP_NAME,MENU_ITEMS=MENU_ITEMS,SOCIAL_LINKS=MY_PROJECTS)


@app.route("/dashboard")
def dashboard():
    return  render_template("/views/dashboard/index.html",APP_NAME=APP_NAME,DASHBOARD_MENU=DASHBOARD_MENU)


@app.route("/dashboard/files",methods=["GET","POST"])
def files():
    if request.method=="POST":
        file = request.files["file"]
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))
        return redirect(url_for("files"))
       # FİLE UPLOAD
    else:
        files = os.listdir(os.path.join(app.config["UPLOAD_FOLDER"]))
        
        return render_template("/views/files/index.html",APP_NAME=APP_NAME,DASHBOARD_MENU=DASHBOARD_MENU,files=files)




if __name__ == '__main__':
    app.run(debug=True)
