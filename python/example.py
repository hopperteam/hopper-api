import hopperApi

api = hopperApi.HopperApi(hopperApi.HopperDev)

if not api.checkConnectivity():
    print("Could not connect!")
    exit()

print("Connected to Hopper!")

# on first run
app = api.createApp("Hopper", "hoppercloud.net", "https://hoppercloud.net/logo.png", "https://hoppercloud.net/manageSubscription", "info@hoppercloud.net")
app.update(name = "HopperApp")
app.generateNewKeys()
strToStore = app.serialize()
print(strToStore)

# on each run
app2 = api.deserializeApp(strToStore)
print(app.createSubscribeRequest("https://listener.hoppercloud.net?id=123123"))
