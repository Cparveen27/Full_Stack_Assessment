from flask import Flask, render_template, request, redirect, session, jsonify
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"


# ---------- DATABASE FUNCTION ----------
def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


# ---------- LOGIN PAGE ----------
@app.route("/")
def login_page():
    return render_template("login.html")


# ---------- SIGNUP PAGE ----------
@app.route("/signup_page")
def signup_page():
    return render_template("signup.html")


# ---------- SIGNUP ----------
@app.route("/signup", methods=["POST"])
def signup():
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]

    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM admin WHERE email=?", (email,))
    if cur.fetchone():
        return "Email already exists"

    cur.execute("INSERT INTO admin (name,email,password) VALUES (?,?,?)",
                (name, email, password))
    conn.commit()

    return redirect("/")


# ---------- LOGIN ----------
@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]

    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM admin WHERE email=? AND password=?", (email, password))
    user = cur.fetchone()

    if user:
        session["user_id"] = user["id"]
        return redirect("/dashboard")
    else:
        return "Invalid login"


# ---------- DASHBOARD ----------
@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/")
    return render_template("dashboard.html")


# ---------- ADD OPPORTUNITY ----------
@app.route("/add", methods=["POST"])
def add():
    if "user_id" not in session:
        return redirect("/")

    name = request.form["name"]
    duration = request.form["duration"]
    desc = request.form["desc"]

    conn = get_db()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO opportunity (name, duration, description, admin_id) VALUES (?, ?, ?, ?)",
        (name, duration, desc, session["user_id"])
    )
    conn.commit()

    return redirect("/dashboard")


# ---------- GET DATA ----------
@app.route("/get_data")
def get_data():
    if "user_id" not in session:
        return jsonify([])

    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM opportunity WHERE admin_id=?", (session["user_id"],))
    data = cur.fetchall()

    result = []
    for d in data:
        result.append({
            "name": d["name"],
            "duration": d["duration"],
            "desc": d["description"]
        })

    return jsonify(result)


# ---------- LOGOUT ----------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# ---------- RUN ----------
if __name__ == "__main__":
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    # CREATE ADMIN TABLE
    cur.execute("""
    CREATE TABLE IF NOT EXISTS admin (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        password TEXT
    )
    """)

    # CREATE OPPORTUNITY TABLE
    cur.execute("""
    CREATE TABLE IF NOT EXISTS opportunity (
        id INTEGER PRIMARY KEY,
        name TEXT,
        duration TEXT,
        description TEXT,
        admin_id INTEGER
    )
    """)

    conn.commit()

    app.run(debug=True)