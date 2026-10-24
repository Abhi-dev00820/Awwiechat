#imports

from flask import Flask , render_template,session,flash


app = Flask(__name__)

# secret key

app.secret_key = "XYZsecretkey"

#model configs

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite3:///users.db"
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
    if request.method == POST:
        username = request.form["LoginAwwieU"]
        password = request.form["LoginAwwieP"]

        User = user.query.filter_by(username=username).first()

        if user and password == user.password:
            return render_template("index.html")
        else:
            flash("Invalid Credentials")
    return render_template("login.html")


@app.route("/")