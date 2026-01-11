import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from jinja2 import ChoiceLoader, FileSystemLoader

# -----------------------------
# Initialize Flask app
# -----------------------------
app = Flask(__name__, template_folder="templates")  # main templates folder

# Add multiple template folders (ChoiceLoader)
questions_folder = os.path.join(os.path.dirname(__file__), "user_personality", "templates")
app.jinja_loader = ChoiceLoader([
    app.jinja_loader,  # default templates/
    FileSystemLoader(questions_folder)  # questions.html folder
])

# -----------------------------
# SQLite setup
# -----------------------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# -----------------------------
# User model
# -----------------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()

# -----------------------------
# Questions + Traits
# -----------------------------
questions = [
    ("I enjoy exploring new ideas, cultures, or perspectives.", "O"),
    ("I often reflect on abstract or philosophical topics.", "O"),
    ("I like experimenting with new approaches or experiences.", "O"),
    ("I am curious about why people think and behave the way they do.", "O"),
    ("I make detailed plans and follow through with them.", "C"),
    ("I stay focused on tasks even when distracted or stressed.", "C"),
    ("I can control my impulses in emotionally charged situations.", "C"),
    ("I take responsibility for my actions and learn from mistakes.", "C"),
    ("I feel energized and comfortable around people.", "E"),
    ("I can express my thoughts and feelings clearly in social settings.", "E"),
    ("I enjoy leading or participating actively in group activities.", "E"),
    ("I am aware of how my moods affect others in social interactions.", "E"),
    ("I am considerate of other people’s feelings.", "A"),
    ("I seek to understand and support others without expecting rewards.", "A"),
    ("I trust others but also notice when someone may take advantage.", "A"),
    ("I reflect on how my actions impact those around me emotionally.", "A"),
    ("I recover from setbacks fairly quickly and learn from them.", "R"),
    ("I notice and reflect on my emotional reactions to difficult situations.", "R"),
    ("I act in ways that align with my core values, even when it’s difficult.", "R"),
    ("I strive to live a life that feels meaningful and true to myself.", "R"),
]

# -----------------------------
# Routes
# -----------------------------
@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            return redirect(url_for("ui"))
        return "Invalid credentials, try again!"
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        fullname = request.form["fullname"]
        email = request.form["email"]
        password = request.form["password"]

        if User.query.filter_by(email=email).first():
            return "Email already registered. Please login."

        new_user = User(fullname=fullname, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        # Redirect new user to questions page
        return redirect(url_for("questions_route"))

    return render_template("signup.html")

@app.route("/questions", methods=["GET", "POST"])
def questions_route():
    if request.method == "POST":
        # Here you can process submitted answers if needed
        return redirect(url_for("ui"))

    # Render questions.html from user_personality/templates/
    return render_template("questions.html", questions=questions)

@app.route("/ui")
def ui():
    return render_template("ui.html")

# -----------------------------
# Run app
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
