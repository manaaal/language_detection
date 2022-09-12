import requests
from flask import Flask, app
app = Flask(__name__)

text = "hello good morning stupid people"
endpoint = "https://languagetest.herokuapp.com/"
req = requests.post(endpoint,json={'text':text})

#req.json()

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/test")
def test():
    return "Hello from test!"

if __name__ == "__main__":
    main()
