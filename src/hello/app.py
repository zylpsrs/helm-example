import os
import requests
from flask import Flask, request

_greeter   = "http://localhost:9081" if (os.environ.get("GREETER") is None) else os.environ.get("GREETER")
_port      = 9080 if (os.environ.get("PORT") is None) else os.environ.get("PORT")

app = Flask(__name__)

@app.route('/')
def hello():
    hello_to = request.args.get('helloTo')
    messages=greeter(_greeter, 'helloTo', hello_to)
    return "{}".format(messages)

def greeter(url, param, value):
    r = requests.get(url, params={param: value})
    assert r.status_code == 200
    return r.text

if __name__ == "__main__":
    app.run(host='::', port=_port, debug=True, threaded=True)
