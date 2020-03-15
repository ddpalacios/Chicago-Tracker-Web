import gevent.monkey
gevent.monkey.patch_all()
from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room, emit, send
from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup
from time import sleep
chicago_cta_api = '94202b724e284d4eb8db9c5c5d074dcd'
chicago_train_lines = "red,blue,G,pink,Brn,Org,P,Y"
cta_url = "http://lapi.transitchicago.com/api/1.0/ttpositions.aspx?key={0}&rt={1}".format(chicago_cta_api, chicago_train_lines)
app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('Frontend.html')

@socketio.on('train_line')
def handle_event(cta,number_of_trains):
    print("Tracking --> {} Line".format(cta))
    print("RANGE --> {}".format(number_of_trains))
    while(1):
        sleep(2.5)
        request_to_open_url= urllib.request.urlopen(cta_url)
        train_content = BeautifulSoup(request_to_open_url, 'xml')
        for train_line in cta:
                train = train_content.select_one('route[name={}]'.format(train_line))
                lat = train.findAll('lat', limit=int(number_of_trains))
                lon = train.findAll('lon', limit=int(number_of_trains))
                for (latitude,longitude) in zip(lat,lon):
                        latitude = latitude.text
                        longitude = longitude.text
                        print(train_line)
                        print("coordinates: {} , {}--> #{}".format(latitude, longitude, len(lon)))
                        emit('cord', (latitude,longitude,train_line))
                print()
          
if __name__ == '__main__':
    socketio.run(app, debug=True,host='0.0.0.0')
