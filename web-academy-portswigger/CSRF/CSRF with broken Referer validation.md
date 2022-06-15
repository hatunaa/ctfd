# CSRF with broken Referer validation

### Kiểm tra Referrer header

Khi nhận được yêu cầu, chúng ta có thể có hai thông tin có sẵn để chỉ ra yêu cầu đến từ đâu. Đó là Origin header và Referer  header.  Kiểm tra một hoặc cả hai giá trị này để xem yêu cầu  có xuất xứ từ nguồn gốc khác  hay không. Origin header và Referer header được gửi bởi trình duyệt để tránh giả  mạo nhưng không phải lúc nào cũng có.

Đăng nhập và thay đổi email chúng ta thấy có header Referer như hình dưới. Sau khi xóa trường Referrer chúng ta thấy có thông báo lỗi như sau

![image](https://user-images.githubusercontent.com/68894302/173722742-a14f9028-2e51-4309-a14e-fdef20bdbd7f.png)

![image](https://user-images.githubusercontent.com/68894302/173723010-6b6deebe-6502-4270-b841-c7731982edc4.png)

Nếu thay đổi giá trị Referer thành máy chủ của chúng ta thì kết quả sẽ như sau

![image](https://user-images.githubusercontent.com/68894302/173751283-76a2e486-ac17-4d44-8aa8-a44be12ef73a.png)

Thông báo lỗi `"Invalid referer header"`. Nhưng sau khi thêm URL vào cuối đường dẫn Referer, về cơ bản như một đường dẫn

``` 
Referer: https://0qcmj4pnexsju4p0.b.requestbin.net/ac171feb1fe283a3c09e2689009d00a4.web-security-academy.net
```

![image](https://user-images.githubusercontent.com/68894302/173752867-c3563bb3-464b-4aa9-a8b6-cc535753a97b.png)

Thì chúng ta thực hiện được reuquest và thay đổi email thành công. 

Đi đến máy chủ exploit, thay đổi đường dẫn thành URL và tạo một CSRF poc như sau:

![image](https://user-images.githubusercontent.com/68894302/173753451-9e17f700-8ed7-4975-a423-33fab5066dd2.png)

Nhưng khi view exploit chúng ta chỉ nhận được phần domain của URL

![image](https://user-images.githubusercontent.com/68894302/173753738-00756e61-3396-42e6-b26c-eca8cb0513f3.png)

Trong một tài liệu về [Referrer-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy) nếu dùng chỉ thi unsafe-url thì chúng ta có thể chuyển hướng đến bất cứ URL nào mà không bị chặn

![image](https://user-images.githubusercontent.com/68894302/173753970-cdfe8a80-54d2-4db0-bfbe-ed0f6057e817.png)

Vận dụng điều này chúng ta thêm `Referrer-Policy: unsafe-url` phần Head, 

 Chỉnh sửa JavaScript để đối số thứ ba của `history.pushState()`hàm bao gồm một chuỗi truy vấn với URL phiên bản phòng thí nghiệm của bạn như sau:                         

`history.pushState("", "", "/?ac171feb1fe283a3c09e2689009d00a4.web-security-academy.net")` 

Điều này sẽ làm cho tiêu đề Referer trong yêu cầu được tạo chứa URL của trang web đích trong  chuỗi truy vấn.                   

Payload:

![image](https://user-images.githubusercontent.com/68894302/173755132-6b16aab8-e13d-4958-9883-314b372ebeb5.png)

![image](https://user-images.githubusercontent.com/68894302/173755191-6bdf2b15-10e7-418b-85cd-19bc2f5897ff.png)