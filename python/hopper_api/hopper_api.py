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

        json = res.json()
        if res.status_code != 200:
            if "reason" in json:
                raise ConnectionError(json['reason'])
            raise ConnectionError(json)
        
        return App(self, json['id'], priv)

    def post_notification(self, subscriptionId, notification):
        data = notification.data
        data['subscription'] = subscriptionId
        print(json.dumps({
            'subscriptionId': subscriptionId,
            'notification': notification.data
        }))
        res = requests.post(self.baseUrl + '/notification', json={
            'subscriptionId': subscriptionId,
            'notification': notification.data
        })

        json_res = res.json()
        if res.status_code != 200:
            if "reason" in json_res:
                raise ConnectionError(json_res['reason'])
            raise ConnectionError(json_res)
 
        return json_res['id']
    
    def update_notification(self, notificationId, notification):
        return True
    
    def delete_notification(self, notificationId):
        res = requests.delete(self.baseUrl + '/notification?id=' + notificationId)

        json_res = res.json()
        if res.status_code != 200:
            if "reason" in json_res:
                raise ConnectionError(json_res['reason'])
            raise ConnectionError(json_res)
 
