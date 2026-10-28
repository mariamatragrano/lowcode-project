from flask import Flask

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)