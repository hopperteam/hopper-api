import json

class App:
    def __init__(self, api, id, privateKey):
        self.api = api
        self.id = id
        self.privateKey = privateKey
    
    def update(self, name = None, imageUrl = None, manageUrl = None, contactEmail = None):
        pass

    def create_subscribe_request(self, callback, accountName=None):
        return self.api.subscribeUrl + "?id=" + self.id + "&content=1234"

    def generate_new_keys(self):
        return True

    def serialize(self):
        return json.dumps({
            "id": self.id,
            "key": self.privateKey
        })
