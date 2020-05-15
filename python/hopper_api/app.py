import json
import base64
from hopper_api.crypto import *
import requests

class App:
    def __init__(self, api, id, privateKey):
        self.api = api
        self.id = id
        self.privateKey = privateKey

    def __send_update(self, data):
        requests.put(self.api.baseUrl + '/app', json={
            "id": self.id, 
            "content": sign(data, self.privateKey)
        })
    
    def update(self, name = None, imageUrl = None, manageUrl = None, contactEmail = None):
        data = {}
        if name is not None:
            data['name'] = name

        if imageUrl is not None:
            data['imageUrl'] = imageUrl

        if manageUrl is not None:
            data['manageUrl'] = manageUrl

        if contactEmail is not None:
            data['contactEmail'] = contactEmail

        self.__send_update(data)
    
    def create_subscribe_request(self, callback, accountName=None):
        subReq = {
            "id": self.id,
            "callback": callback,
            "requestedInfos": []
        }
        if accountName is not None:
            subReq['accountName'] = accountName

        encSubReq = sign(subReq, self.privateKey)

        return self.api.subscribeUrl + "?id=" + self.id + "&content=" + encSubReq

    def generate_new_keys(self):
        (pub, priv) = generate_keys()
        self.__send_update({
            "cert": encode_key_base64(pub)
        });
        self.privateKey = priv
        return True

    def serialize(self):
        return json.dumps({
            "id": self.id,
            "key": encode_key_base64(self.privateKey)
        })
