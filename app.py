from flask import Flask, render_template, request, jsonify
from sentiment import analyze_sentiments

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    text = data.get("text", "")
    sentences = text.split("\n")
    result = analyze_sentiments(sentences)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
