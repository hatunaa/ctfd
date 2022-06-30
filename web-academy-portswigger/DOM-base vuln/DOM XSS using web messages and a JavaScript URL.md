# DOM XSS using web messages and a JavaScript URL

Sau khi lướt qua một vòng trang web thấy cũng không có chức năng gì nhiều ngoài tính năng comment. Ctrl+U thì chúng ta thấy có đoạn code khá thú vị![image](https://user-images.githubusercontent.com/68894302/175619088-84b3e992-5463-47f0-a448-9ab9c3214a38.png)

Đoạn code này kiểm tra khi window nhận được message có chứa `http` hoặc `https` hay không. Nếu phát hiện thì nó sẽ chuyển hướng đến trang web hiện tại.

Mục tiêu của thử thách này là call đến hàm `print()` tức là thực thi javascript khi gửi lên message. Chúng ta sẽ sử dụng `javascript:print()` để thay thế cho url và sau đó thêm phần bình luận phía sau có chứa http như sau `/*http*/` để lừa ứng dụng hiểu rằng trong cái url này có chứa đoạn `http` vì nó không yêu cầu vị trí phải ở đầu chuỗi.

Payload:
``` 
<iframe src = "$URL" onload = "contentWindow.postMessage ('javascript:print)();/*https:*/', '*');"> 
```

Mozilla chỉ ra cú pháp chính xác để gửi message đến đối tượng window của iframe

``` 
postMessage(message, targetOrigin) 
postMessage(message, targetOrigin, transfer)
```

> Dấu `*` là một từ đồng nghĩa với the full word, chúng ta có thể thay thế bằng chính URL đầy đủ

![image](https://user-images.githubusercontent.com/68894302/175644305-937c00cc-b637-49d3-9274-b70b3cc6aba5.png)

![image](https://user-images.githubusercontent.com/68894302/175644343-412b4be7-1c06-4383-a0e5-af11f83fd41f.png)