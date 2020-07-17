import mysql.connector as sq

import random
from flask import Flask, flash, request, redirect, render_template

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)