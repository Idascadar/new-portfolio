from flask import Flask, render_template, jsonify
import mysql.connector

app = Flask(__name__)

# DB Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Use your MySQL password if set
    database="my portfolio"  # ✅ NOTE: Not recommended to use spaces in database names
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/about")
def get_about():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM about LIMIT 1")
    result = cursor.fetchone()
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
