from hopper_api.app import App
from hopper_api.crypto import *
import requests
import json

HopperProd = ["https://api.hoppercloud.net/v1", "https://app.hoppercloud.net/subscribe"]
HopperDev = ["https://api-dev.hoppercloud.net/v1", "https://dev.hoppercloud.net/subscribe"]

class HopperApi:
    def __init__(self, hopperEnv):
        self.baseUrl = hopperEnv[0]
        self.subscribeUrl = hopperEnv[1]

    def deserialize_app(self, serialized):
        obj = json.loads(serialized)
        return App(self, obj["id"], decode_private_key_base64(obj["key"]))
    
    def check_connectivity(self):
        try:
            res = requests.get(self.baseUrl)
            if (res.json()["type"]):
                print("You are using a DEV instance of Hopper! This is not intended for production!")
        except ConnectionError as e:
            print(json.dumps(e))
            return False
        return True

    def create_app(self, name, baseUrl, imageUrl, manageUrl, contactEmail, key = None, cert = None):
        (pub, priv) = generate_keys()
        res = requests.post(self.baseUrl + '/app', json={
            "name": name,
            "baseUrl": baseUrl,
            "imageUrl": imageUrl,
            "manageUrl": manageUrl,
            "contactEmail": contactEmail,
            "cert": encode_key_base64(pub)            
        })

        if res.status_code != 200:
            json = res.json()
            if "reason" in json:
                raise ConnectionError(res.json()['reason'])
            raise ConnectionError(json)
        
        return App(self, res.json()['id'], priv)

    def post_notification(self, subscriptionId, notification):
        return "000000000000000"
    
    def update_notification(self, notificationId, notification):
        return True
    
    def delete_notification(self, notificationId):
        return True
