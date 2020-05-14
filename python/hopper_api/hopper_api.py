from hopper_api.app import App
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
        return App(self, obj["id"], obj["key"])
    
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
        return App(self, "123", "abcd1234")

    def post_notification(self, subscriptionId, notification):
        return "000000000000000"
    
    def update_notification(self, notificationId, notification):
        return True
    
    def delete_notification(self, notificationId):
        return True
