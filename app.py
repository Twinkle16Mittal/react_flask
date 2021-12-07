from flask import Flask,request,app
import hashlib
from flask.templating import render_template
from models import *

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/registersuccess', methods=["GET","POST"])
def registerSuccess():
    if request.method=="POST":
        id = request.form.get('id')
        email = request.form.get('email')
        password = request.form.get('password')
        username = request.form.get('username')
        name = request.form.get('name')
        #hashing the password
        hashpass = hashlib.md5(bytes(str(password),encoding='utf-8')).hexdigest()
        entry = userlogin(id=id,email=email,password=hashpass,username=name,name=name)
        db.session.add(entry)
        db.session.commit()
    return render_template('login.html') 

if __name__=='__main__':
    app.run(debug=True ,port=8000)
