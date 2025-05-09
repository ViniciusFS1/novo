from flask import Flask

app = Flask(__name__)

@app.route('/')
def oi():
    return "<p>teste</p>"

if __name__ == "__main__":
    app.run(debug = True)