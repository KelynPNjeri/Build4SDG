from flask import Flask, json, request, Response
from estimator import estimator

app = Flask(__name__)

@app.route('/api/v1/on-covid-19', methods=["GET", "POST"])
@app.route('/api/v1/on-covid-19/json', methods=["GET", "POST"])
def render_json():
    """
        This is the JSON endpoint.
        It takes in data and returns the output from the estimator function in XML format.
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
        return Response (estimator(req), content_type='text/xml', mimetype='application/xml', status=201)

@app.route('/api/v1/on-covid-19/logs', methods=["GET"])
def render_load_time():

    pass

if __name__ == "__main__":
    app.run()