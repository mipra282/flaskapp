# -*- coding: utf-8 -*- 
from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template('home.html')

@app.route('/user/<name>')
def home(name):
    mylist = ['California','New York','Boston','New Hampshire','London']
    return render_template('user.html',name=name,mylist=mylist)

if __name__ == '__main__':
   app.run(debug=True)