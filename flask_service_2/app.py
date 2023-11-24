from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello"

@app.route("/test")
def test_path():
    return "test success 2"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2234)