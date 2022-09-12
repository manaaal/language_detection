"""import requests
text = "hello good morning stupid people"
endpoint = "https://languagetest.herokuapp.com/"
req = requests.post(endpoint,json={'text':text})

req.json()"""

print("hello world !")

from flask import Flask, app
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/test")
def test():
    return "Hello from test!"

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=82)
