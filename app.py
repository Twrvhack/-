from flask import Flask, request, jsonify, render_template
import sqlite3
import urllib.parse
from verify import check_url_safety
from search import get_search_results

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    query = request.args.get("q")
    results = get_search_results(query)
    return jsonify(results)

@app.route("/api/verify")
def verify():
    url = request.args.get("url")
    safe = check_url_safety(url)
    return jsonify({"isSafe": safe})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
