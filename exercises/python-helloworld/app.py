from flask import Flask

import logging

log_format = logging.Formatter('"%(asctime)s, %(message)s"')

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(log_format)
logger.addHandler(file_handler)

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/status")
def status():
    logger.debug("/status endpoint was reached")
    return {
        "result": "OK - healthy"
    }


@app.route("/metrics")
def metrics():
    logger.debug("/metrics endpoint was reached")
    return {
        "data":
            {
                "UserCount": 140,
                "UserCountActive": 23
            }
    }


if __name__ == "__main__":
    app.run(host='0.0.0.0')
