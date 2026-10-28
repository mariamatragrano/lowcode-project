from flask import Flask, render_template, request
import re

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Welcome to my Flask application!</h1>"


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        # Validate required fields
        if not name or not email or not message:
            return render_template(
                "contact.html",
                error="All fields are required.",
                name=name,
                email=email,
                message=message
            ), 400

        # Validate email format
        email_pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

        if not re.fullmatch(email_pattern, email):
            return render_template(
                "contact.html",
                error="Please enter a valid email address.",
                name=name,
                email=email,
                message=message
            ), 400

        # Successful submission
        return render_template(
            "confirmation.html",
            name=name
        ), 200

    # Display empty contact form
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)