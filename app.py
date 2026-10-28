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
    <h1>My Task Organizer</h1>

    <p>If I could build an application in one evening instead of spending three months developing it, I would create a Task Organizer. I often have different responsibilities, deadlines, and personal activities to manage, so I would like a simple tool that keeps everything in one place.</p>

    <p>My application would allow users to add tasks, set deadlines, choose priorities, and mark activities as completed. It would display pending tasks clearly, helping people plan their day and avoid forgetting important commitments.</p>

    <p>I would use Python, Flask, and AI assistance to create a basic working version in one evening. Later, I could add reminders, a calendar, and intelligent suggestions about which tasks to complete first.</p>

    <p>This project would be useful in everyday life and would also help me improve my programming skills. Most importantly, it would show me how low-code tools and AI can turn a practical idea into something usable much faster.</p>
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