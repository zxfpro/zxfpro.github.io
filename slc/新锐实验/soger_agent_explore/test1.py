
from flask import Flask, Response, request
from flask import stream_with_context, abort
import json
import asyncio
import base64
import requests
import hashlib
import json

class API_worker():
    def __init__(self,**kwargs):
        self.app = Flask(__name__)


        
    def start(self, server_name='0.0.0.0', server_port=9010,run=True,**kwargs):
        
        @self.app.route('/live', methods=['GET','POST'])
        def live():
            """
            判断服务是否存活
            """
            if request.method == "GET":
                db_name = request.args.get('db_name', default=None, type=None)
                return "success"
                
            if request.method == "POST":
                data = request.get_data()
                data_dict = json.loads(data)
                return f"success"
        self.app.run(host=server_name, port=server_port,**kwargs)

API_worker().start()
