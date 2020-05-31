
from flask import Flask, render_template, request, redirect

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import sys
sys.path.append("model")
from AccuracyScore import getAccuracyScore

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, nullable=False)
    status = db.Column(db.Boolean, default=False)

@app.route('/')
def index():
    return render_template('index.html', message=getAccuracyScore())
 
@app.route('/todo/')
def page_todo():
    entries = Entry.query.all()
    return render_template('todo.html',entries=entries)

@app.route('/todo/add/', methods=['POST'])
def page_todo_add():
    if request.method == 'POST':
            form = request.form
            title = form.get('title')
            if title:
                entry = Entry(title = title)
                db.session.add(entry)
                db.session.commit()
                return redirect('/todo/')
    return redirect('/'), 403 


@app.route('/todo/delete/<int:id>')
def action_todo_delete(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            db.session.delete(entry)
            db.session.commit()
        return redirect('/todo/')
    return redirect('/'), 403

@app.route('/todo/update/<int:id>')
def action_todo_trun(id):
    if id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            entry.status = not entry.status
            db.session.commit()
        return redirect('/todo/')
    return redirect('/'), 403

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="404 - Flask project"), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')