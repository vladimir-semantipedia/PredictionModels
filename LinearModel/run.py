import sys, getopt
import os
import urlparse
import json
import calendar
import datetime
import copy
#import numpy as np
from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression
from sklearn.isotonic import IsotonicRegression
from sklearn.utils import check_random_state
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.svm import SVR

class HTTPHelper(object):
    def __init__(self):
        self._headers = {}
        self._query = {}
        self._env = {}
        
        for x in os.environ:
            if x[:12] == "REQ_HEADERS_":
                self._headers[x[12:].lower()] = os.environ[x]
            elif x[:10] == "REQ_QUERY_":
                self._query[x[10:].lower()] = os.environ[x]
            else:
                self._env[x.lower()] = str(os.environ[x])
    @property
    def headers(self):
        return self._headers
    @property
    def get(self):
        return self._query
    @property
    def env(self):
        return self._env
    @property
    def post(self):
        postData = open(os.environ['req'], "r").read()
        postDataParsed = urlparse.parse_qs(postData)
        return postDataParsed
        
def LinearModel(arr1):
    return arr1

# This is a little class used to abstract away some basic HTTP functionality
http = HTTPHelper()

# All these print statements get sent to the Azure Functions live log
#print "--- GET ---"
#print http.get
#print

#print "--- POST ---"
postData = open(os.environ['req'], "r").read()
postDataParsed = urlparse.parse_qs(postData)
x = postDataParsed['x'][0].split(',')
y = postDataParsed['y'][0].split(',')
print "x=", x
print "y=", y
print x[1],y[0]

str = str(x)
print str

s = {'x': x, 'y':y}
ss = json.dumps(s)
print ss

# All data to be returned to the client gets put into this dict
returnData = {
    #HTTP Status Code:
    "status": 200,
    
    #Response Body:
 #   "body": "<h1>Azure python function Works :)</h1>",
     "body": ss,
   
    # Send any number of HTTP headers
    "headers": {
        "Content-Type": "text/html",
        "X-Awesome-Header": "YesItIs"
    }
}

# Output the response to the client
output = open(os.environ['res'], 'w')
output.write(json.dumps(returnData))

     