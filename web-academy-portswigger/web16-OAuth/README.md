## Authentication bypass via OAuth implicit flow

Vào trang đăng nhập, người dùng được chuyển hướng sang một trang web khác

![image](https://user-images.githubusercontent.com/68894302/186353180-bd04f32f-0db9-490c-879a-037da576f002.png)

Dùng tài khoản được cung cấp để thực hiện xác thực

![image](https://user-images.githubusercontent.com/68894302/186353457-7b98eddc-8019-4035-862c-7c712281e6f3.png)

![image](https://user-images.githubusercontent.com/68894302/186354157-8e68eb14-1b03-4ce0-8502-54adc1ef2b39.png)

![image](https://user-images.githubusercontent.com/68894302/186354205-b03522b4-ce21-4c5a-bf3d-4e8bce43147c.png)

Tiếp theo khi người dùng vào my-account thì nó sẽ gửi một GET đến trang web oauth.xxx để yêu cầu xác thực, và dữ liệu sẽ được gửi về cho người dùng dưới dạng json

![image](https://user-images.githubusercontent.com/68894302/186354873-4b14a088-1b2c-46df-9fcb-61fdc3a67361.png)

Nó dẫn tới một lỗ hổng nghiêm trọng khi ứng dụng không kiểm tra token này có khớp với dữ liệu khác trong yêu cầu hay không hay nói cách khác là có sự ràng buộc hay không. Trong thường hợp này chúng ta có thể thay đổi email và username thành tài khoản carlos 

Sau khi gửi request thì chúng ta đã chiếm được tài khoản của carlos

![image](https://user-images.githubusercontent.com/68894302/186356982-687e0fdf-9c25-4b10-ba22-223fc65dbcc4.png)

Vấn đề được giải quyết.
