from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column('user_id', db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    
    def __init__(self, username, email):
        self.username = username
        self.email = email

db.create_all()

@app.route('/')
def main():
    return 'hello'

@app.route('/create_user', methods=['GET'])
def create_user():
    return render_template('index.html')

@app.route('/internal_create_user', methods=['POST'])
def internal_create_user():
    user = User(request.form.get('username'), request.form.get('email'))
    return 'hello'

if __name__ == '__main__':
    app.run(debug=True)