import json
import sys
import requests

if len(sys.argv)!=2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search",
    params={
                 "entity":"song",
                 "term" : "1",
                  "term" : sys.argv[1]
                      
    }
)
    
print(json.dumps(response.json(), indent=2))
