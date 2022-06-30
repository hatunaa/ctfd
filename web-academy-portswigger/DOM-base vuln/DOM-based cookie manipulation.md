# DOM-based cookie manipulation

Gọi đến hàm `print()` để giải quyết thử thách. 

Tại tham số `lastViewedProduct` trên cookie, chúng ta có thể thoát ra khỏi liên kết và chèn mã javascript tùy ý

![image](https://user-images.githubusercontent.com/68894302/176343366-ccab9d5b-aeaf-466b-899b-2c317d1a24b2.png)

Cookie là cái mà ta có thể control, xác định được sink `document.cookie` có thể dẫn đến lỗ hổng thao túng cookie dựa trên DOM.

Chúng ta có thể lấy một URL chứa sản phẩm hợp lệ và đính kèm payload của mình trong đó theo cách mà URL vẫn hợp lệ và tạo ra một trang sản phẩm. 

Ví dụ:

`https://0adf0098030d8438c1819d42005e00f7.web-security-academy.net/product?productId=3&evil='><script>alert()</script>`

Kiểm tra và thấy popup alert() hiện lên.

Nếu tải URL đó một cách thủ công trong iframe của trang web mà chúng ta kiểm soát, nó có thể đưa javascript tùy ý vào cookie. Nhưng yêu cầu phải tải lại trang thì cookie mới được gửi đến máy chủ và đưa javascript vào trang

![image](https://user-images.githubusercontent.com/68894302/176344321-340c9dbb-049c-42f9-9745-2718903f009d.png)

Vì chúng ta không xác định được người dùng sau khi kích hoạt vào trang web của attacker có load lại trang không nên có thể dùng [setTimeout](https://developer.mozilla.org/en-US/docs/Web/API/setTimeout) để thực hiện những gì sau đó, mặc dù theo cách không đồng bộ

![image](https://user-images.githubusercontent.com/68894302/176343818-415887f4-1c9d-423c-bed7-b0f38b4d207c.png)
