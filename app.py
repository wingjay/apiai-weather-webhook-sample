#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

import weather

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return 'Hi, Here is wingjay AI bot'

@app.route('/ping', methods=['GET', 'POST'])
def ping():
    return 'pong'

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    if req.get("result").get("action") != "yahooWeatherForecast":
        res = {}
    else: 
        res = weather.processRequest(req)

    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=False, port=port, host='0.0.0.0')
