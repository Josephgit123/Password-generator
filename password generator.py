import random
import string
from flask import Flask, render_template, request

app = Flask(__name__)

def generate_password(length=12):
    """Generate a strong random password"""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

@app.route("/", methods=["GET", "POST"])
def home():
    password = None
    if request.method == "POST":
        length = int(request.form.get("length", 12))  # Default length 12
        password = generate_password(length)
    
    return render_template("index.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)
