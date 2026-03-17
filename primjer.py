from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, this is my cloud app!"

@app.route("/about")
def about():
    return "This app is deployed in the cloud."

if __name__ == "__main__":
    app.run(debug=True)