from flask import Flask, request, render_template, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'aVerySecretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class UserData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128))
    dob = db.Column(db.String(20))
    
@app.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('feed'))
    return render_template('index.html')

@app.route('/feed')
def feed():
    if 'user' in session:
        return render_template('feed.html', **session['user'])
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET': return redirect(url_for('index'))
    user = UserData.query.filter_by(username=str(request.form['username']), password=str(request.form['password'])).first()
    if user:
        session['user'] = {'username':user.username, 'password':user.password, 'first_name':user.first_name, 'last_name':user.last_name, 'dob':user.dob}
        return redirect(url_for('feed'))
    else:
        return redirect(url_for('index'))

@app.post('/signup')
def signup():
    user = UserData.query.filter_by(username=str(request.form['username'])).first()
    if user:
        return redirect(url_for('index'))
    data = {'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'username': request.form['username'],
            'password': request.form['password'],
            'dob': f"{request.form['mob']} {request.form['dayob']}, {request.form['yob']}"}
    user = UserData(**data)
    db.session.add(user)
    db.session.commit()
    session['user'] = data
    return redirect(url_for('feed'))
    
@app.get('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
