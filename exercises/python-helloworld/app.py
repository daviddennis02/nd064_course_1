from flask import Flask
from flask import json
import logging

app = Flask(__name__)

# healthcheck endpoint
@app.route("/status")
def healthcheck():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )
    app.logger.info('Status request successful')
    return response

# metrics endpoint
@app.route("/metrics")
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )
    # implement logging
    app.logger.info('Metrics request successful')
    return response

@app.route("/")
def hello():
    app.logger.info("Main request successful")
    return "Hello World!"

if __name__ == "__main__":
    # Stream logs to a file
    logging.basicConfig(filename='app.log', encoding='utf-8', level=logging.DEBUG)
    app.run(host='0.0.0.0')