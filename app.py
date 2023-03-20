import sys
sys.path.append('C:/Users/anikd/virtusa-bot/controller')

from suggestion import *

from flask import Flask,request

app = Flask(__name__)

getSuggestionByLocation('kolkata')

if __name__ == '__main__':
    app.run();