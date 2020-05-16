from hopper_api.app import App
from hopper_api.crypto import *
from hopper_api.notification import Notification, Action
import requests
import json

HopperProd = ["https://api.hoppercloud.net/v1", "https://app.hoppercloud.net/subscribe"]
HopperDev = ["https://api-dev.hoppercloud.net/v1", "https://dev.hoppercloud.net/subscribe"]

class HopperApi:
    """API Connection to all Hopper related tasks"""
    
    def __init__(self, hopperEnv):
        self.baseUrl = hopperEnv[0]
        self.subscribeUrl = hopperEnv[1]


    def deserialize_app(self, serialized: str) -> App:
        """Convert a JSON-Serialized app into an actual App

           Returns: The deserialized App's object
        """

        obj = json.loads(serialized)
        return App(self, obj["id"], decode_private_key_base64(obj["key"]))

    
    def check_connectivity(self) -> bool:
        """Checks whether Hopper can be reached with the current parameters

           Returns: Whether the check was successful
        """

        try:
            res = requests.get(self.baseUrl)
            if (res.json()["type"]):
                print("You are using a DEV instance of Hopper! This is not intended for production!")
        except ConnectionError as e:
            print(json.dumps(e))
            return False
        return True


    def create_app(self, name: str, baseUrl: str, imageUrl: str, manageUrl: str, contactEmail: str) -> App:
        """Creates an App and registers it with hopper

           Returns: The registed App's object
        """

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


    def post_notification(self, subscriptionId: str, notification: Notification) -> str:
        """Posts a notification on the given subscription

           Returns: The Id of the posted notification
        """

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

    
    def update_notification(self, notificationId: str, heading: str=None, timestamp: str=None, imageUrl: str=None, isDone: str=None, isSilent: str=None, content: str=None, actions: [Action]=None):
        """Updates an already posted notification"""
        
        data = {}
        if heading is not None:
            data['heading'] = heading

        if timestamp is not None:
            data['timestamp'] = timestamp

        if imageUrl is not None:
            data['imageUrl'] = imageUrl

        if isDone is not None:
            data['isDone'] = isDone

        if isSilent is not None:
            data['isSilent'] = isSilent

        if content is not None:
            data['content'] =  content
 
        if actions is not None:
            data['actions'] = actions


        res = requests.put(self.baseUrl + '/notification', json={
            "id": notificationId,
            "notification": data
        })

        json_res = res.json()
        if res.status_code != 200:
            if "reason" in json_res:
                raise ConnectionError(json_res['reason'])
            raise ConnectionError(json_res)

            
    def delete_notification(self, notificationId: str):
        """Deletes an already posted notification"""
        res = requests.delete(self.baseUrl + '/notification?id=' + notificationId)

        json_res = res.json()
        if res.status_code != 200:
            if "reason" in json_res:
                raise ConnectionError(json_res['reason'])
            raise ConnectionError(json_res)
 
