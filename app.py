from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"

questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "Rome", "Berlin", "London"], "answer": "Paris"},
    {"question": "2 + 2 = ?", "options": ["3", "4", "5", "6"], "answer": "4"},
    {"question": "Python is a ...?", "options": ["Snake", "Programming Language", "Car", "Planet"], "answer": "Programming Language"}
]

@app.route("/", methods=["GET", "POST"])
def quiz():
    return "App is working"
    if "current_question" not in session:
        session["current_question"] = 0
        session["score"] = 0

    current_index = session["current_question"]

    if request.method == "POST":
        selected = request.form.get("answer")

        if selected == questions[current_index]["answer"]:
            session["score"] += 1

        session["current_question"] += 1
        current_index = session["current_question"]

        if current_index >= len(questions):
            score = session["score"]
            session.clear()
            return render_template("result.html", score=score, total=len(questions))

        return redirect(url_for("quiz"))

    q = questions[current_index]
    return render_template("quiz.html", question=q, q_num=current_index + 1, total=len(questions))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
