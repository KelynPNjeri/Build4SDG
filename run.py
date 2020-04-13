import logging
import time
from dicttoxml import dicttoxml
from flask import Flask, json, request, Response, g
from src.estimator import estimator

app = Flask(__name__)
logging.basicConfig(filename='logs.txt', level=logging.INFO)


@app.before_request
def get_time():
    """
        Get time before request
    """
    g.start = time.time()


@app.route('/api/v1/on-covid-19', methods=["GET", "POST"])
@app.route('/api/v1/on-covid-19/json', methods=["GET", "POST"])
def render_json():
    """
        This is the JSON endpoint.
        It takes in data and returns the output from the estimator function in JSON format.
    """
    if request.method == 'GET':
        return Response("Working GET Json Endpoint", mimetype="application/json", status=200)
    elif request.method == 'POST':
        req = request.get_json()
        return Response(json.dumps(estimator(req)), mimetype="application/json", status=201)


@app.route('/api/v1/on-covid-19/xml', methods=["GET", "POST"])
def render_xml():
    """
        This is the XML endpoint.
        It takes in data and returns the output from the estimator function in XML format.
    """
    if request.method == 'GET':
        
        return Response("Working XML Endpoint...", content_type="text/xml", status=200)
    elif request.method == 'POST':
        req = request.get_json()
        return Response (dicttoxml(estimator(req), attr_type=False), content_type='text/xml', mimetype='application/xml', status=201)


@app.route("/api/v1/on-covid-19/logs", methods=["GET", "POST"])
def logs_index():
    """
        Handles Logging
    """
    if request.method != "GET":
        return Response("Method not allowed", mimetype="text/plain", status=405)

    LOGS = []  # logging list
    with open("logs.txt", "rt") as f:   # read logs file and take cycles
        data = f.readlines()
    for line in data:
        if "root" in line and "404" not in line:
            LOGS.append(line[10:])

    return Response("".join(LOGS), mimetype="text/plain")


@app.after_request
def log_request_info(response):
    """
        Gets response as input and returns the logging
        details
    """
    time_taken = int((time.time() - g.start) * 1000)
    status_code = response.status.split()[0]
    logging.info(
        f"{request.method}\t\t{request.path}\t\t{status_code}\t\t{str(time_taken).zfill(2)}ms\n"
    )

    return response


if __name__ == "__main__":
    app.run(debug=True) 