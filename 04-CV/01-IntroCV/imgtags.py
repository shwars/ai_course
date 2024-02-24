import requests
import base64
import sys

min_confidence = 5
max_number = 10
basic_auth = "== Insert your code here =="

b = base64.b64encode(open(sys.argv[1],'rb').read())

url = "http://api.imagga.com/v2/tags"

h = { "Authorization" : f"Basic {basic_auth}"}
d = { "image_base64" : b  }

res = requests.post(url, data = d, headers=h)

res = res.json()

print(' '.join([ x['tag']['en'] for x in res['result']['tags'] 
                 if x['confidence']>min_confidence][:max_number]))
