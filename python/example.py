import hopper_api
import base64
import traceback

api = hopper_api.HopperApi(hopper_api.HopperDev)

if not api.check_connectivity():
    print("Could not connect!")
    exit()

print("Connected to Hopper!")

# on first run
try:
    app = api.create_app("Hopper", "http://localhost", "https://hoppercloud.net/logo.png", "https://hoppercloud.net/manageSubscription", "info@hoppercloud.net")
except:
    traceback.print_exc()
app.update(name = "HopperApp")
app.generate_new_keys()
strToStore = app.serialize()
print(strToStore)

# on each run

print(app.create_subscribe_request("https://listener.hoppercloud.net?id=123123", accountName="Test User"))

### after key received

not_id = api.post_notification('key', hopper_api.Notification.default('TestTest', 'this is the body').isDone(False).actions([
    hopper_api.Action.submit("Hallo", "https://abcd.xyz").markAsDone(True),
    hopper_api.Action.text("Reply", "https://abcde.xyz")
]))
api.update_notification(not_id, heading="Updated!!", imageUrl="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/SNice.svg/220px-SNice.svg.png")
api.delete_notification(not_id)

