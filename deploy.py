
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
