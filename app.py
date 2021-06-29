import sys

from flask import Flask
from flask import json
import logging

app = Flask(__name__)


@app.route("/")
def hello():
    response = app.response_class(
        response=json.dumps({"Welcome": "Sample Project"}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('Service Root request successful')
    return response


@app.route("/status")
def status():
    response = app.response_class(
        response=json.dumps({"results": "Health - OK"}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('Status request successful')
    return response


@app.route("/metrics")
def metrics():
    response = app.response_class(
        response=json.dumps({"status": "success", "data": {"UserCount": 140, "UserCountActive": 23}}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('Metrics request successful')
    return response


if __name__ == "__main__":
    file_handler = logging.FileHandler(filename='tmp.log')
    stdout_handler = logging.StreamHandler(sys.stdout)
    handlers = [file_handler, stdout_handler]
    logging.basicConfig(handlers=handlers,
                        format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
                        level=logging.DEBUG)
    app.run(host='0.0.0.0')
