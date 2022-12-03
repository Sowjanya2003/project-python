from flask import Flask, render_template, request
from pymongo import MongoClient

app=Flask(__name__)

@app.route("/")

@app.route("/mainhome")
def mainhome():
    return render_template('mainhome.html')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/menu")
def menu():
    return render_template('menu.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/table")
def table():
    return render_template('table.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/cart")
def cart():
    return render_template('cart.html')


"""@app.route("/login_validation", methods =["GET", "POST"])
def login_validation():
       user_name = request.form.get("user_name")
       mobile_no = request.form.get("mobile_no")
       pswd = request.form.get("pswd")
       return render_template('login.html',user_name=user_name,mobile_no=mobile_no,pswd=pswd)"""

client=MongoClient("mongodb://127.0.0.1:27017")
db=client['Restaurant']
data=db.details

@app.route("/insert")
def insert():
    user_name = request.args.get("user_name")
    mobile_no = request.args.get("mobile_no")
    pswd = request.args.get("pswd")
    info={"Username":user_name, "Mobile No.":mobile_no, "Password":pswd}
    x=data.insert_one(info)
    return render_template("login.html",res=x)

if __name__=='__main__':
    app.run(debug=True)

