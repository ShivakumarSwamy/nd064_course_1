from flask import Flask

import logging

log_format = "%(asctime)s, %(message)s"

logging.basicConfig(filename="app.log", level=logging.DEBUG, format=log_format)

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/status")
def status():
    logging.debug("/status endpoint was reached")
    return {
        "result": "OK - healthy"
    }


@app.route("/metrics")
def metrics():
    logging.debug("/metrics endpoint was reached")
    return {
        "data":
            {
                "UserCount": 140,
                "UserCountActive": 23
            }
    }


if __name__ == "__main__":
    app.run(host='0.0.0.0')
