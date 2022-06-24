# DOM-based open redirection

Sau khi vào trang sản phẩm view source thì thấy đoạn code sau

![image](https://user-images.githubusercontent.com/68894302/175653801-47840073-ea14-4eb7-b921-92c25cd65364.png)

Nó sẽ kiểm tra nếu không có tham số url trong URL của trang thì sẽ chuyển tới url cục bộ. Tuy nhiên nếu tham số url tồn tại và bắt đầu bằng http hoặc https thì nó sẽ được sử dụng là url đích của liên kết

Test thử burp collab xem thế có requests đến không thì thấy đã có request

![image](https://user-images.githubusercontent.com/68894302/175655883-fedfbf14-9a1e-4bcb-b779-2e674479be65.png)

Payload:
```
https://0a6300dd041408d9c0e92727005b0047.web-security-academy.net/post?postId=5&url=https://exploit-0aba0053047208b2c0f327ea01ff0080.web-security-academy.net/exploit
```

![image](https://user-images.githubusercontent.com/68894302/175656169-d302cd6e-8a87-4f01-9b0b-bffaf7b3ae88.png)