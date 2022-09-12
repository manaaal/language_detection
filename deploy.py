import requests
text = input()
endpoint = "https://languagetest.herokuapp.com/"
req = requests.post(endpoint,json={'text':text})

req.json()
