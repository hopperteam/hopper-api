from datetime import datetime
from datetime import timezone

class Notification:
    @staticmethod
    def default(heading: str, content: str) -> 'Notification':
        """Creates a default notification with the given paramenters
        
           Returns: The created Notification
        """

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


    def isDone(self, val: bool) -> 'Notification':
        """Sets isDone

           Returns: The updated notification
        """

        self.data['isDone'] = val
        return self
        

    def isSilent(self, val: bool) -> 'Notification':
        """Sets isSilent

           Returns: The updated notification
        """

        self.data['isSilent'] = val
        return self
    

    def timestamp(self, val: int) -> 'Notification':
        """Sets the notification's timestamp

           Returns: The updated notification
        """

        self.data['timestamp'] = val
        return self

   
    def action(self, action_obj: 'Action') -> 'Notification':
        """Adds the action to the notification

           Returns: The updated notification
        """

        self.data['actions'].append(action_obj.data)
        return self


    def actions(self, action_ary: ['Action']) -> 'Notification':
        """Override all previous added actions with the given array

           Returns: The updated notification
        """

        self.data['actions'] = [x.data for x in action_ary]
        return self



class Action:
    @staticmethod
    def submit(text: str, url: str) -> 'Action':
        """Creates a an action of type submit
        
           Returns: The created Action
        """

        return Action('submit', text, url, False)

    
    @staticmethod
    def text(text: str, url: str) -> 'Action':
        """Creates a an action of type text
        
           Returns: The created Action
        """

        return Action('text', text, url, False)


    @staticmethod
    def redirect(text: str, url: str) -> 'Action':
        """Creates a an action of type redirect
        
           Returns: The created Action
        """

        return Action('text', text, url, False)


    def __init__(self, actionType, text, url, markAsDone):
        self.data = {
            'type': actionType,
            'text': text,
            'url': url,
            'markAsDone': markAsDone
        }

    
    def markAsDone(self, val: bool) -> 'Action':
        """Sets whether triggering the action marks the notification as done

           Returns: The updated notification
        """

        self.data['markAsDone'] = val
        return self


