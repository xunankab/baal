import os
import signal
import subprocess

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

service = None
stream = {'enable': 'False'}
server = {'address': '127.0.0.1', 'port': '5600'}

class Stream(Resource):
    def get(self):
        return stream

    def post(self):
        global service
        command = "gst-launch-1.0 v4l2src ! video/x-raw,width=640,height=480 ! x264enc ! rtph264pay ! udpsink host=%s port=%s" % (server['address'], server['port'])
        data = request.get_json()
        if eval(data['enable']):
            try:
                service = subprocess.Popen(command, stdout=subprocess.PIPE,
                       shell=True, preexec_fn=os.setsid)
                stream['enable'] = data['enable']
            except subprocess.CalledProcessError as e:
                return stream, 201
        else:
            try:
                os.killpg(os.getpgid(service.pid), signal.SIGTERM)
                stream['enable'] = data['enable']
            except OSError:
                pass
        return stream, 201

class Server(Resource):
    def get(self):
        return server

    def post(self):
        data = request.get_json()
        server['address'] = data['address']
        server['port'] = data['port']
        return server, 201

api.add_resource(Stream, '/api/stream')
api.add_resource(Server, '/api/server')

if __name__ == '__main__':
    app.run(debug=True)
