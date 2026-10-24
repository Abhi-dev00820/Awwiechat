#imports

from flask import Flask , render_template,session,flash,request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# secret key

app.secret_key = "XYZsecretkey"

#model configs

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

#Models

class User(db.Model):

    id = db.Column(db.Integer,nullable = False, primary_key= True)
    username = db.Column(db.String,nullable = False,unique = True)
    password = db.Column(db.String,nullable = False)


with app.app_context():
    db.create_all()


#Routes

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["LoginAwwieU"]
        password = request.form["LoginAwwieP"]

        user = User.query.filter_by(username=username).first()

        if user and password == user.password:
            session["user_id"] = user.id
            return render_template("home.html")

        else:
            flash("Invalid Credentials")
    return render_template("login.html")


@app.route("/signup", methods = ["GET","POST"])
def signup():
    if request.method == "POST":
        username = request.form["SignupAwwieU"]
        password = request.form["SignupAwwieP"]

        existing_user = User.query.filter_by(username = username).first()

        if existing_user:

            flash("User already exits please login")
            return render_template("signup.html")
        
            
        new_user = User(
            username = username,
            password = password
        )
        db.session.add(new_user)
        db.session.commit()

        flash("Account created succesfully please Login.")

        return render_template("signup.html")
    
    return render_template("signup.html")

if __name__ == '__main__':
    app.run(debug = True)