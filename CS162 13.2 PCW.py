from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cs162_user:cs162_password@db/cs162'
db = SQLAlchemy(app)

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    status = db.Column(db.Boolean)
    
    
@app.route('/')
def index():
    incomplete = Entry.query.filter_by(status=True).all()
    return render_template('index.html', element=element)


@app.route('/add', methods=['POST'])
def add():
    element = Entry(text=request.form['item'], status=False)
    db.session.add(element)
    db.session.commit()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
