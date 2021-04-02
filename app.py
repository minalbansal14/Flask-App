from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/', methods=['GET','POST'])
def hello_world():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo_obj = todo(title=title, desc=desc)
        db.session.add(todo_obj)
        db.session.commit()
    new_todo = todo.query.all()
    return render_template("index.html", new_todo= new_todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    new_todo = todo.query.filter_by(sno=sno).first()
    db.session.delete(new_todo)
    db.session.commit()
    return redirect("/")

@app.route('/show')
def show1():
    new_todo = todo.query.all()
    print(new_todo)
    return 'Minal Bansal'

class todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

if __name__ =="__main__":
    app.run(debug=True)