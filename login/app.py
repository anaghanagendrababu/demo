from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

# -------------------- HOME --------------------
@app.route("/")
def home():
    return render_template("login.html")

# -------------------- LOGIN --------------------
@app.route("/login", methods=["POST"])
def login():
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    password = request.form.get("password")

    # Backend validation
    if not (name and email and phone and password):
        return "All fields are required!"

    if not re.match(r"^[0-9]{10}$", phone):
        return "Phone must be 10 digits!"

    if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$", password):
        return "Weak password!"

    return redirect(url_for("dashboard", name=name))

# -------------------- DASHBOARD --------------------
@app.route("/dashboard")
def dashboard():
    name = request.args.get("name")
    return render_template("dashboard.html", name=name)

# -------------------- LOGOUT --------------------
@app.route("/logout", methods=["POST"])
def logout():
    return redirect(url_for("home"))

# -------------------- RUN --------------------
if __name__ == "__main__":
    app.run(debug=True)