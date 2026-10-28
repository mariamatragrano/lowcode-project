import re
from flask import Flask, render_template, request

app = Flask(__name__)
EMAIL_RE = re.compile(
    r"^[A-Za-z0-9._%+-]+@"
    r"(?:[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\.)+[A-Za-z]{2,}$"
)

MAX_NAME = 100
MAX_EMAIL = 254
MAX_MESSAGE = 5000

def validate_contact(form):
    """Return cleaned values and validation errors."""
    values = {
        "name": form.get("name", "").strip(),
        "email": form.get("email", "").strip(),
        "message": form.get("message", "").strip(),
    }

    errors = {}

    if not values["name"]:
        errors["name"] = "Please enter your name."
    elif len(values["name"]) > MAX_NAME:
        errors["name"] = f"Name must be at most {MAX_NAME} characters."

    if not values["email"]:
        errors["email"] = "Please enter your email address."
    elif len(values["email"]) > MAX_EMAIL or not EMAIL_RE.fullmatch(values["email"]):
        errors["email"] = "Please enter a valid email address."

    if not values["message"]:
        errors["message"] = "Please enter a message."
    elif len(values["message"]) > MAX_MESSAGE:
        errors["message"] = f"Message must be at most {MAX_MESSAGE} characters."

    return values, errors

# Pragmatic email check: local part, "@", then a dotted domain with a 2+ letter TLD.
# Whitespace and newlines can't match, which also blocks header-injection attempts.
EMAIL_RE = re.compile(
    r"^[A-Za-z0-9._%+-]+@"
    r"(?:[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?\.)+[A-Za-z]{2,}$"
)

MAX_NAME = 100
MAX_EMAIL = 254
MAX_MESSAGE = 5000


def validate_contact(form):
    """Return (cleaned_values, errors). `errors` is empty when everything is valid."""
    values = {
        "name": form.get("name", "").strip(),
        "email": form.get("email", "").strip(),
        "message": form.get("message", "").strip(),
    }
    errors = {}

    if not values["name"]:
        errors["name"] = "Please enter your name."
    elif len(values["name"]) > MAX_NAME:
        errors["name"] = f"Name must be at most {MAX_NAME} characters."

    if not values["email"]:
        errors["email"] = "Please enter your email address."
    elif len(values["email"]) > MAX_EMAIL or not EMAIL_RE.match(values["email"]):
        errors["email"] = "Please enter a valid email address."

    if not values["message"]:
        errors["message"] = "Please enter a message."
    elif len(values["message"]) > MAX_MESSAGE:
        errors["message"] = f"Message must be at most {MAX_MESSAGE} characters."

    return values, errors


@app.route("/")
def home():
    return '<h1 style="color: red;">Hello Maria Antonieta Mattos Matragrano!!! ❤️</h1>'

@app.route("/about")
def about():
    return """
    <h1>My Contact Form Application</h1>

    <p>If I could build an application in one evening instead of spending three months developing it, I would create a Contact Form Application. The purpose of this application would be to provide a simple and practical way for users to send messages through a website.</p>

    <p>My application would allow users to enter their name, email address, and message. It would validate the information to ensure that all required fields are completed and that the email address has a valid format. If any information is missing or incorrect, the application would display an error message.</p>

    <p>I would use Python, Flask, HTML, and AI assistance to develop a basic working version in one evening. After a successful submission, the application would display a confirmation page. In the future, I could improve the design, store messages in a database, and add automatic email notifications.</p>

    <p>This project would help me understand how web applications process user input, validate information, and provide feedback. It would also allow me to improve my programming skills and explore how low-code tools and AI-assisted development can make application development faster and more accessible.</p>
    """

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template(
            "contact.html", values={}, errors={}, sent=False
        )

    values, errors = validate_contact(request.form)

    if errors:
        return render_template(
            "contact.html",
            values=values,
            errors=errors,
            sent=False
        ), 400

    app.logger.info(
        "Contact form from %s <%s>",
        values["name"],
        values["email"]
    )

    return render_template(
        "contact.html",
        values=values,
        errors={},
        sent=True
    )

if __name__ == "__main__":
    app.run(debug=True)
