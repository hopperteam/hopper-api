import json
import base64
from hopper_api.crypto import *

class App:
    def __init__(self, api, id, privateKey):
        self.api = api
        self.id = id
        self.privateKey = privateKey
    
    def update(self, name = None, imageUrl = None, manageUrl = None, contactEmail = None):
        pass

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
        return True

    def serialize(self):
        return json.dumps({
            "id": self.id,
            "key": encodeKeyBase64(self.privateKey)
        })
