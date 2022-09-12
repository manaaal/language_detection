import requests
text = "hello good morning stupid people"
endpoint = "https://languagetest.herokuapp.com/"
req = requests.post(endpoint,json={'text':text})

req.json()
