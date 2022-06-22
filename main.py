from flask import Flask, render_template, request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.secret_key = 'secret'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column('user_id', db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    
    def __init__(self, username, email):
        self.username = username
        self.email = email
    def __repr__(self):
        return str(self.username) + " emails is " + str(self.email)

db.create_all()

@app.route('/')
def main():
    return 'hello'

@app.route('/create_user', methods=['GET'])
def create_user():
    return render_template('index.html')

@app.route("/all_users")
def get_all_users():
    return Users.Query.all()

@app.route('/internal_create_user', methods=['POST'])
def internal_create_user():
    user = User(request.form.get('username'), request.form.get('email'))
    users_with_usernames = User.query.filter_by(username=user.username)
    users_with_emails = User.query.filter_by(email=user.email)
    if users_with_usernames:
        flash("Username already exist" ,'error')
        return redirect(url_for('create_user'))
    if users_with_emails:
        flash("Email already exist" ,'error')
        return redirect(url_for('create_user'))
    if True:
        db.session.add(user)
        db.session.commit()
        created_user = User.query.filter_by(username=user.username)
        return 'user created' + str(created_user)

if __name__ == '__main__':
    app.run(debug=True)