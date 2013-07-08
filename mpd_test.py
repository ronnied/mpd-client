import mpd
import json

client = mpd.MPDClient()
client.timeout = 10
client.idletimeout = None
client.connect("localhost", 6600)
print(client.mpd_version)

# Read JSON status
status_json =  client.status()
#print status_json
status = json.loads(json.dumps(status_json))
print status

print client.currentsong()
print client.setvol(100)

#print(client.find("any", "h"))
client.close()
client.disconnect()
