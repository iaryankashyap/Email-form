import mysql.connector as sq

import random
from flask import Flask, flash, request, redirect, render_template

app = Flask(__name__)

def regemail(email):
    sqcon = sq.connect(host='iaryankashyap.mysql.pythonanywhere-services.com', database='iaryankashyap$users',
                       user='iaryankashyap', password='rootrootroot')
    cursor = sqcon.cursor()
    query = "INSERT INTO users(email) VALUES('"+email+"')"
    cursor.execute(query)
    sqcon.commit()
    sqcon.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('secret.html')

@app.route('/validate', methods=["GET", "POST"])
def validate():
    if request.method == "POST":
        key = request.form.get("key")
        if key=="superuser12345":
            return render_template('dashboard.html')
        else:
            return render_template('wrong.html')

app.route('/submit', methods=["GET", "POST"])
def subem():
    if request.method == "POST":
        email = request.form.get("email")
        regemail(email)
        return render_template('dashboard.html')
    else:
        return render_template('wrong.html')
'''
if __name__ == "__main__":
    app.run(debug=True)
    '''