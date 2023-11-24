from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hi. I'm pretending to be a UI."

@app.route("/test_1")
def test_service_1():
    return requests.get('http://flask_service_1:1123').text
    ##return requests.get('http://localhost:1123').text

@app.route("/test_2")
def test_service_2():
    return requests.get('http://flask_service_2:2234').text
    ##return requests.get('http://localhost:2234').text

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555)