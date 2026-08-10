from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Momin Engineering Website is Live!</h1>"

if __name__ == "__main__":
    app.run()
