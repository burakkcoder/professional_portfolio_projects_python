from datetime import timezone
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import datetime

app = Flask(__name__)
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CREATE TABLE
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    ddate = db.Column(db.String(250), unique=True, nullable=False)
    complete = db.Column(db.Boolean)
#db.create_all()

@app.route("/")
def index():
    todos = Todo.query.all()
    return render_template("index.html", todos = todos)

@app.route("/add",methods = ["POST"])
def addTodo():
    title = request.form.get("title")
    ddate = request.form.get("ddate")
    newTodo = Todo(title = title, ddate = ddate, complete = False)
    db.session.add(newTodo)
    db.session.commit()

    return redirect(url_for("index"))

@app.route("/complete/<string:id>")
def completeTodo(id):
    todo = Todo.query.filter_by(id = id).first() # id ye göre filter yapıcak ve o id nin ilkini alıcak kiii, zaten o id den bir tane var.
    """if todo.complete == True:
        todo.complete = False
    else:
        todo.complete = True"""
    todo.complete = not todo.complete # yukarıdaki if işleminin daha kısa halini yapmış olduk burada.

    db.session.commit()
    
    return redirect(url_for("index"))

@app.route("/delete/<string:id>")
def deleteTodo(id):
    todo = Todo.query.filter_by(id = id).first()
    db.session.delete(todo)
    db.session.commit()

    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)