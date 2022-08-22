#  JWT attack

![image](https://user-images.githubusercontent.com/68894302/184280385-44a27d84-5ab6-4cea-89e5-c1f55995eefd.png)

## JWTs là gì?

JSON web token là một định dạng tiêu chuẩn hóa để gửi dữ liệu JSON được ký mã hóa giữa các hệ thống .Về mặt lí thuyết chúng có thể chứa bất kì loại dữ liệu nào, nhưng được sử dụng phổ biến nhất để gửi thông tin ("xác nhận quyền sở hữu") về người dùng như mộ phần cơ chế để authentication, xử lí session, và access control. 

Không giống như session token cổ điển, tất cả dữ liệu mà máy chủ cần được lưu trữ phía client trong chính JWT. Điều này làm cho  JWT trở thành lựa chọn phổ biến cho các trang web có tính phân tán cao, nơi người dùng cần tương tác liền mạch với nhiều máy chủ back-end. 

### JWT format

JWT bao gồm 3 phần: 

+ Header
+ Payload
+ Signature

Chúng được phân tách bằng dấu chấm như thể hiện trong ví dụ sau:

``` 
eyJraWQiOiI5MTM2ZGRiMy1jYjBhLTRhMTktYTA3ZS1lYWRmNWE0NGM4YjUiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJsYWIiLCJleHAiOjE2NDgwMzcxNjQsIm5hbWUiOiJ0dWFuZHYiLCJzdWIiOiJjYXJsb3MiLCJyb2xlIjoiYmxvZ19hdXRob3IiLCJlbWFpbCI6InRlc3RAbnVsbCIsImlhdCI6MTUxNjIzOTAyMn0.cNQt_UoIK6L2VPizjL4peXWjsoboEosrGe1vJDMfdq8giUodXMSHXw1sYCVuf0mwDtS-DTS4DCxMYKWv4oJslA
```

Phần __Header__ và __Payload__ của JWT chỉ là các đối tượng JSON được mã hóa base64url. Header chứa siêu dữ liệu về chính mã thông báo, trong khi Payload chứa các "xác nhận quyền sở hữu" thực tế về người dùng. Ví dụ: bạn có thể giải mã tải trọng từ mã thông báo ở trên để tiết lộ các xác nhận quyền sở hữu sau:

``` 
{
  "iss": "lab",
  "exp": 1648037164,
  "name": "tuandv",
  "sub": "carlos",
  "role": "blog_author",
  "email": "test@null",
  "iat": 1516239022
}
```

Trong hầu hết các trường hợp bất kì ai có quyền truy cập vào mã thông báo đều có thể dễ dàng đọc hoặc sửa đổi dữ liệu này. Do đó tính bảo mật của bất kì cơ chế dứa trên JWT đều phụ thuộc rất nhiều vào phần __Signature__.

### JWT signature

Máy chủ phát hành mã thông báo thường tạo chữ kí bằng cách hash phần header và payload. Trong một số trường hợp chúng cũng mã hóa hàm băm kết quả. Dù bằng cách nào, quá trình này liên quan đến sign một secret key. 

+ Vì signature được lấy trực tiếp từ phần còn lại của token, nên việc thay đổi một byte duy nhất của header hoặc payload dẫ đến chữ kí không khớp. 
+ Nếu không biết secret key của máy chủ, sẽ không thể tạo chữ kí chính xác cho headẻ hoặc payload nhất định

> Note: 
>
> Nếu bạn muốn hiểu rõ hơn về cách JWT được xây dựng, bạn có thể sử dụng trình debugger trên jwt.io để thử nghiệm với các mã thông báo tùy ý.

### JWT vs JWS vs JWE

Đặc điểm kỹ thuật JWT thực sự rất hạn chế. Nó chỉ xác định một định dạng đại diện cho thông tin ("yêu cầu") như một đối tượng JSON có thể được chuyển giữa hai bên. Trong thực tế, JWT không thực sự được sử dụng như một thực thể độc lập. Thông số JWT được mở rộng bởi cả thông số kỹ thuật  JSON Web Signature (JWS) và JSON Web Encryption (JWE), xác định các cách cụ thể để thực hiện JWT

![image](https://user-images.githubusercontent.com/68894302/184283055-582cb1cb-65f3-462e-b4c1-6193083b12e4.png)

Nói cách khác, JWT thường là JWS hoặc JWE token. Khi mọi người sử dụng thuật ngữ "JWT", chúng hầu như luôn có nghĩa là JWS token. JWE rất giống nhau, ngoại trừ việc nội dung thực tế của mã thông báo được mã hóa thay vì chỉ được mã hóa.

> Note:
>
> Để đơn giản, trong bài viết này, "JWT" chủ yếu đề cập đến mã thông báo JWS, mặc dù một số lỗ hổng được mô tả cũng có thể áp dụng cho mã thông báo JWE

## Tấn công JWT là gì?

Các cuộc tấn công JWT liên quan đến việc người dùng gửi các JWT đã được sửa đổi đến máy chủ để đạt được mục đích xấu. Thông thường, mục tiêu này là bypass authentication và access control bằng cách mạo danh một người dùng khác đã được xác thực

##  Các lỗ hổng đối với cuộc tấn công JWT phát sinh như thế nào?

Các lỗ hổng JWT thường phát sinh do việc xử lý JWT thiếu sót trong chính ứng dụng. Các thông số kỹ thuật khác nhau liên quan đến JWT tương đối linh hoạt theo thiết kế, cho phép các nhà phát triển trang web quyết định nhiều chi tiết triển khai cho chính họ. Điều này có thể dẫn đến việc chúng vô tình tạo ra các lỗ hổng bảo mật ngay cả khi sử dụng các thư viện đã được khắc phục. Những sai sót khi thực hiện này thường có nghĩa là chữ ký của JWT không được xác minh đúng cách. Điều này cho phép kẻ tấn công giả mạo các giá trị được chuyển đến ứng dụng thông qua trọng tải của mã thông báo. 

Ngay cả khi chữ ký được xác minh chặt chẽ, liệu nó có thể thực sự đáng tin cậy hay không phụ thuộc rất nhiều vào khóa bí mật của máy chủ vẫn còn là bí mật. Nếu khóa này bị rò rỉ theo một cách nào đó, hoặc có thể bị đoán hoặc bị cưỡng bức, kẻ tấn công có thể tạo chữ ký hợp lệ cho bất kỳ mã thông báo tùy ý nào, làm ảnh hưởng đến toàn bộ cơ chế