import urllib
import json

endpoint = 'https://api.pinterest.com/v1/boards'
api_token = "ARyOSrqPEcG3Ut2O9DLgah-lT2d5FRWuMOh-XWREuKym6mApVAAAAAA&fields=id%2Clink%2Cnote%2Curl"

username = raw_input('Enter your username: ').replace(' ','+')

Board = raw_input('Destination Board Name: ').replace(' ','+')

request = endpoint+"/"+username+"/"+Board+"/pins/?&access_token="+api_token


response = urllib.urlopen(request).read()
directions = json.loads(response)
print json.dumps(directions,indent=4,sort_keys=True)