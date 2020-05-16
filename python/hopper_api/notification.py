from datetime import datetime
from datetime import timezone

class Notification:
    @staticmethod
    def default(heading, content):
        return Notification("default", heading, content, int(datetime.now().timestamp()*1000), False, False, [])

 
    def __init__(self, notificationType, heading, content, timestamp, isDone, isSilent, actions):
        self.data = {
            'type': notificationType,
            'heading': heading,
            'content': content,
            'timestamp': timestamp,
            'isDone': isDone,
            'isSilent': isSilent,
            'actions': []
        }
        print(timestamp)


    def isDone(self, val):
        self.data['isDone'] = val
        return self
        

    def isSilent(self, val):
        self.data['isSilent'] = val
        return self
    

    def timestamp(self, val):
        self.data['timestamp'] = val
        return self

   
    def action(self, action_obj):
        self.data['actions'].append(action_obj.data)
        return self


    def actions(self, action_ary):
        self.data['actions'] = [x.data for x in action_ary]
        return self



class Action:
    @staticmethod
    def submit(text, url):
        return Action('submit', text, url, False)

    
    @staticmethod
    def text(text, url):
        return Action('text', text, url, False)


    @staticmethod
    def redirect(text, url):
        return Action('text', text, url, False)


    def __init__(self, actionType, text, url, markAsDone):
        self.data = {
            'type': actionType,
            'text': text,
            'url': url,
            'markAsDone': markAsDone
        }

    
    def markAsDone(self,val):
        self.data['markAsDone'] = val
        return self


