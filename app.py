from flask import Flask, render_template, request

app = Flask(__name__)

def get_recommendations(interest, level):
    recommendations = {
        "Web Development": {
            "Beginner": ["HTML", "CSS", "JavaScript"],
            "Intermediate": ["React", "Node.js", "Bootstrap"],
            "Advanced": ["Full Stack Projects", "Deployment"]
        },
        "AI/ML": {
            "Beginner": ["Python Basics", "Machine Learning Intro"],
            "Intermediate": ["Pandas", "Scikit Learn"],
            "Advanced": ["Deep Learning", "TensorFlow"]
        }
    }

    return recommendations.get(interest, {}).get(level, [])

@app.route("/", methods=["GET", "POST"])
def home():
    result = []
    if request.method == "POST":
        interest = request.form["interest"]
        level = request.form["level"]
        result = get_recommendations(interest, level)

    return render_template("index.html", recommendations=result)

if __name__ == "__main__":
    app.run(debug=True)