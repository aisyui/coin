#!/usr/bin/python
import os
import sys
import json
import requests
import time
import hmac
import hashlib
 
class ApiCall:
    def __init__(self,api_key,api_secret,api_endpoint):
        self.api_key = api_key
        self.api_secret = api_secret
        self.api_endpoint = api_endpoint
        
    def get_api_call(self,path):
        method = 'GET'
        timestamp = str(time.time())
        text = timestamp + method + path
        sign = hmac.new(bytes(self.api_secret.encode('ascii')), bytes(text.encode('ascii')), hashlib.sha256).hexdigest()
        request_data=requests.get(
            self.api_endpoint+path
            ,headers = {
                'ACCESS-KEY': self.api_key,
                'ACCESS-TIMESTAMP': timestamp,
                'ACCESS-SIGN': sign,
                'Content-Type': 'application/json'
            })
        return request_data
    
    
    def post_api_call(self,path,body):
        body = json.dumps(body)
        method = 'POST'
        timestamp = str(time.time())
        text = timestamp + method + path + body
        sign = hmac.new(bytes(self.api_secret.encode('ascii')), bytes(text.encode('ascii')), hashlib.sha256).hexdigest()
        request_data=requests.post(
            self.api_endpoint+path
            ,data= body
            ,headers = {
                'ACCESS-KEY': self.api_key,
                'ACCESS-TIMESTAMP': timestamp,
                'ACCESS-SIGN': sign,
                'Content-Type': 'application/json'
            })
        return request_data


api_key = sys.argv[1]
api_secret = sys.argv[2]
api_endpoint = 'https://api.bitflyer.jp'
path = '/v1/me/getbalance'
 
if __name__ == '__main__':
    api = ApiCall(api_key,api_secret,api_endpoint)
    result = api.get_api_call(path).json()
    print(result)
