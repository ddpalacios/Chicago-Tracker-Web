from flask import Flask, render_template, request, redirect, Response, url_for,jsonify
import random, json
from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup
from time import sleep
from prettytable import PrettyTable
from flask_socketio import SocketIO, send
chicago_cta_api = '94202b724e284d4eb8db9c5c5d074dcd'
chicago_train_lines = "red,blue,G,pink,Brn,Org,P,Y"
cta_url = "http://lapi.transitchicago.com/api/1.0/ttpositions.aspx?key={0}&rt={1}".format(chicago_cta_api, chicago_train_lines)
app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    cta = request.form['cta_line']
    print("LINE: "+ str(cta))
    return render_template('Frontend.html')








if __name__ == '__main__':
    app.run(debug=True)


##    print("Tracking --> {0} Line".format(cta))
##    while(1):
##        request_to_open_url= urllib.request.urlopen(cta_url)
##        train_content = BeautifulSoup(request_to_open_url, 'xml')
##        train = train_content.select_one('route[name={0}] train'.format(cta))
##        lati = train.select_one('lat').get_text()
##        lon = train.select_one('lon').get_text()
##        return lati, lon
