# CSRF token is not tied to the user session

## Mô tả:

Chức năng thay đổi email của lab dễ bị tấn công bởi CSRF, nó sử dụng các mã thông báo để cố  gắng ngăn chặn các cuộc tấn công CSRF, nhưng chúng không được tích hợp  vào hệ thống xử lý phiên của trang web.   

Có 2 tài khoản để phục vụ cho việc tấn công:

- `wiener:peter`            
- `carlos:montoya`        

---

Trong một thế giới lí tưởng thì mỗi lần sử dụng mã thông báo CSRF đều tạo ra môt mã thông báo mới và duy nhất. Và hầu như trong quá trình đăng xuất mọi mã thông báo cũ đều bị vô hiệu hóa.

Ở chall này mục tiêu là thay đổi email của người dùng bằng mã thông báo còn hiệu lực của attacker, vì ứng dụng này có vẻ như duy trì một nhóm mã thông báo mà nó đã phát hành và chấp nhận bất kì mã thông báo nào trong nhóm này kể cả có khác session có thay đổi

---

## Các bước

+ Đăng nhập bằng tài khoản người dùng wiener, thay đổi mật khẩu và chúng ta thấy mã thông báo CSRF cũng thay đổi

+ Mở một tab ẩn danh hoặc trên trình duyệt khác, đăng nhập vào tài khoản carlos và cũng chọn chức năng thay đổi email người dùng

+ Bật burp lên để bắt requests, sau khi copy mã CSRF vào clipboard rồi thì Drop requests đi để mã thông báo còn hiệu lực

+ Thay thế mã thông báo CSRF vừa copy vào mã thông báo bên /my-account/change-email của wiener (coi wiener là nạn nhân) rồi gen ra CSRF POC 

  ![image](https://user-images.githubusercontent.com/68894302/173544090-84ba2f6b-67d2-417b-aeec-fd9899c3ad16.png)

+ Dùng exploit server như máy chủ của attacker, lừa người dùng truy cập. Sau khi người dùng truy cập vào chỉ thấy mỗi nút submit,  nếu ấn nó thì người dùng sẽ bị đổi email. Còn trong lab chúng ta chỉ cần delivery là coi như người dùng đã ấn submit

![image](https://user-images.githubusercontent.com/68894302/173545025-1a6e7bdb-df52-45d5-b274-1134379d7eca.png)             