import hopper_api
import base64
import traceback

api = hopper_api.HopperApi(hopper_api.HopperDev)

if not api.check_connectivity():
    print("Could not connect!")
    exit()

print("Connected to Hopper!")

# on first run
#try:
#    app = api.create_app("Hopper", "http://localhost", "https://hoppercloud.net/logo.png", "https://hoppercloud.net/manageSubscription", "info@hoppercloud.net")
#except:
#    traceback.print_exc()
#    pass
#app.update(name = "HopperApp")
#app.generate_new_keys()
#strToStore = app.serialize()
#print(strToStore)

# on each run
app2 = api.deserialize_app("""
{"id": "5ebed346de8776bea3bfc96b", "key": "LS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0tCk1JSUV2Z0lCQURBTkJna3Foa2lHOXcwQkFRRUZBQVNDQktnd2dnU2tBZ0VBQW9JQkFRREE4NFZBNEpuYlNDODUKaHp2RGJNcmRqMnFXSExBZWNZbThsSDFrZjZZYjJSMlIxencySkRLL1VZZDdTMGsyUllHcHRZL0thK1pPL0REdQpUc1dWV01oY0cyUFZBMGZNZGRKNEllNXYzVHJZa1ZFcVZ4ZXlFR3FBNXRKcjhKQ3o2QVZSYWNWc2JwL2JZREN3CmJBRWNiZEsyaEtXT25vS3RvZmlzL0R3MmZlemV6VVNKRWdJcFh4dU5uS08wV1ZNU2ZOQ3UrakZ0TStrRmRqUU0KWG9sRVFwT0FtTWtJTGw4alJSaHV5ckxBMnZzNmVYbHFnTTJVVVRuT0hrUTRZa1lLWUlVNnRqSUFxRGtxb2Z6QwpnRzFRNXZ2c0VRSWgxa2tqZktlRWZhV3ZXemNQWmMzb0J6TXBIT1ROZGVlUUdIa2t1NVE4MStPdDBpcEpCblZkCmtlc1Iyci94QWdNQkFBRUNnZ0VCQUpXQ25QaCtrUG1IWDRCMk4ycmdlL2xlVGJydms5Q2pMWlZBZ2tGRFlCVW8KRVcrV2xnTmwzU1MrS2ZyeGhWTldYSGlDUlY4V2FLay9aVExqT3RyVXByd29SUjBqbzVqY215K1hLMGptNWRnMgpFZXg2KzlOd1FQYU01UFBhdm1XSkhjWE43YnB0cGRTNUhrRTJEMDVXRXZaMnBrcHlyTk9hTkRUbVprbmJIWll0Cm84RmJxZWtCbkpoNDdtVXBpL2VVKy9ESy9DS3V5YitUZTFEQlIwczIvQXVSaHdJLzB2cnJkM3VIYlE5V3ZXMnoKbkJoRUxvaGIvRnZLdnJRS2VOMWxhdGh4RXU5bTU4NkYzZnZDV2dqVXVpcDkzNVpyTmRLdkhUcXV5OUp0MFZhMwpxQ2lTS25pbEs4TGlZV05VWHMzMG5Ucmlqais0dnhFcVRSSHNzMlNLY0FFQ2dZRUE0RUhKK1dtK3lXai9YcnY4ClRJUTBpWVY2WDZPbmxTdjU4REVPZHhPN0ppZFF5VTAyT2NrOHhWNmpMTXpDK0dEd0NQa1l4NktZMVNyNDMvRE0KVnFoWVdqWE50NEJqQjMrM2pvakR0S2Jpa01odGwvSUtISkwzTXFJU3BJSldNZEVseU03cWJWdXdUeFNjUUliNApXWXp3di9yU0xnYU0yRTlvRWNHWHlERW5PSEVDZ1lFQTNFTlZBUE9YeUgwaEhJZVFFUkRpUWVrTWFhT0F3RGoxCmJnZWhzbnhiVDRoV2Flc2JzS0FBWXoxOWJvSWRRQVJVd0FYM3cwSFB3cUxFZDh1RzZHcXVYUmxHV1JYN3ZQOTgKNGpsMEJOSG92TTlVY0l3VHNtQ2xVUzhhbXc1WFNJSjQyWGlGQ2VlRTNHdEJpZ3pxNnhwUGpvcU9OK2ZJVU5OOQpseFFPLy84cnY0RUNnWUJaMHNBZGdIZUVvT080aEQ5WVBwUDBpVndzdHBaSEw2Z2F4dXR1VXA3aGQxbnFaMXpTCjVJSE01RTBqZ3BpTmQvWnRBYWtsUFVGT0VMcENxR2FRUnptc1dHU2ZuWE1NNitFUDNFUFhOZ2tGeU9Ic3ZHdkUKYWpGTlBKR1BCdzJUUXB5SnhDY3R5azNpUHZVZSszQzZIYlBJa2FSaC93bW5FcGN5bFlKQUUwQU1ZUUtCZ0hyTgp3NGZiU0VYTWxmaHRFSUtqVWpLRE41dHlRR2RybWxLMVNJN1Z6S2NFRVlIT1JrcnNlaXJhYnFOOVFjZWVZbzRKCkJjRkVZUXhZYVllTTN2T1gvdzBDK1hqVHk5M3M1L2pOSllWR2J5ZE54UHRXN2VobS8rVEtpVi9uMS93aVdqU04KZ0Vjc1lLUHYzTU9XUGlmRUxKVUJaUmVBVCt2WWJrNGNMZHpHck9LQkFvR0JBTlQ1Z3NYWlRUdnQwaEZqYWxaVApiMmx4RitCdFF1NURNbDlmWE1IbU1BWmp6M09odFVUL2ltVU5pNTdzY3ExcFVrc3JILzdFbnFuQzlWWDNlWmxQCjlETjF0Z3VDNlhlb2FCRFhLYk1tMkpTUHd3elVGL2VzbmJJQTZBSXBOaHV0Wlh3blQ1azRrU281dEt1VDBpWDMKUFo1bE92d3RyOUErakpHZEIwM3NNRk1pCi0tLS0tRU5EIFBSSVZBVEUgS0VZLS0tLS0K"}
""")
app2.update(name="Hopper Python Test", imageUrl="https://raw.githubusercontent.com/hopperteam/hopper-server/master/res/logo_small.svg")
#app2.generate_new_keys()
#print(app2.serialize())
#print(app2.create_subscribe_request("https://listener.hoppercloud.net?id=123123", accountName="Test User"))

### after key received

print(api.post_notification('5ebfc0ea6c5d6c8955afae68', hopper_api.Notification.default('TestTest', 'this is the body').isDone(False).actions([
    hopper_api.Action.submit("Hallo", "https://abcd.xyz").markAsDone(True),
    hopper_api.Action.text("Reply", "https://abcde.xyz")
])))
api.delete_notification('5ebfcb2a6c5d6cce9bafae96')
