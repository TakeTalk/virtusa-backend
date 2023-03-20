import sys
sys.path.append('C:/Users/anikd/virtusa-bot/service') 
from location import *

from flask import Flask,request

app = Flask(__name__)
 
@app.route('/suggestion-hospital-by-location/<address>')

def getSuggestionByLocation(address):
    # address = request.args.get('address')
    return fetch(address)
 


if __name__ == '__main__':
    app.run()