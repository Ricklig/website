from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/')
def main():
    message = "hello"
    return render_template("lander.html", message=message)
