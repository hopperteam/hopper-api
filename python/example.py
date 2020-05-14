import hopper_api

api = hopper_api.HopperApi(hopper_api.HopperDev)

if not api.check_connectivity():
    print("Could not connect!")
    exit()

print("Connected to Hopper!")

# on first run
try:
    app = api.create_app("Hopper", "hoppercloud.net", "https://hoppercloud.net/logo.png", "https://hoppercloud.net/manageSubscription", "info@hoppercloud.net")
except:
    pass
app.update(name = "HopperApp")
app.generate_new_keys()
strToStore = app.serialize()
print(strToStore)

# on each run
app2 = api.deserialize_app(strToStore)
print(app.create_subscribe_request("https://listener.hoppercloud.net?id=123123"))
