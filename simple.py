from flask import Flask, request, flash, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user,UserMixin

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["SECRET_KEY"] = "thisissecret"
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, index=True)
    password = db.Column(db.String(100), index=True)
    address = db.Column(db.String(256))
    city = db.Column(db.String(64), index=True)

    def __repr__(self):
        return '<user % r>' % self.email,self.password,self.address,self.city


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
def index_fun():
    return render_template('index.html')
    # return "<p>Hello, World!</p>"


@app.route("/main")
def main_fun():
    return render_template('main.html')


@app.route("/login", methods=['POST', 'GET'])
def login_fun():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        print(user.email,user.password)
        if user and user.password == password:
            login_user(user)
            return redirect("/")
        else:
            flash('Invalid User', 'warning')
            return redirect("/login")

    return render_template('login.html')


@app.route("/register", methods=['POST', 'GET'])
def register_fun():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        address = request.form.get('address')
        city = request.form.get('city')
        print(email, password, address, city)

        result = User(email=email, password=password, address=address, city=city)
        db.session.add(result)
        db.session.commit()
        flash('User Has been Successfully registered...', 'success')
        return redirect("/login")

    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
