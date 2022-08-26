## OAuth account hijacking via redirect_uri



``` bash 
# This lab uses an [OAuth](https://portswigger.net/web-security/oauth) service to allow users to log in with their social media account. A misconfiguration by the OAuth provider makes it possible for an attacker to steal authorization codes associated with other users' accounts.

# To solve the lab, steal an authorization code associated with the admin user, then use it to access their account and delete Carlos.

# The admin user will open anything you send from the exploit server and they always have an active session with the OAuth service.

# You can log in with your own social media account using the following credentials: `wiener:peter`.

```

Đi tới My account, ứng dụng chuyển hướng người dùng tới trang đăng nhập và ủy quyền. Request giống như sau:
``` bash 
GET /auth?client_id=zfuh2lnyt8l2feyazid1w&redirect_uri=https://0ac100c504a04276c076d739003f003b.web-security-academy.net/oauth-callback&response_type=code&scope=openid%20profile%20email
```

Gửi request này đến repeater. Khi người dùng đồng ý đăng nhập thì ứng dụng cấp cho một mã ủy quyền `code`

![image](https://user-images.githubusercontent.com/68894302/186813706-9e75aaef-3c30-4646-9263-79e5e4858dfe.png)

Trong repeater, sửa redirect_uri thành url exploit server

![image](https://user-images.githubusercontent.com/68894302/186813969-3a0ddae1-1e04-4379-a72c-2d94ecdb9848.png)

Người dùng được chuyển hướng tới exploit server. Nếu chúng ta làm cho admin click vào exploit server url thì sau đó mọi thông tin ủy quyền và chuyển hướng sẽ được log lại.

Trong trường hợp dòng mã ủy quyền, kẻ tấn công có thể ăn cắp mã của nạn  nhân trước khi nó được sử dụng.  Sau đó, họ có thể gửi mã này đến endpoint /callback của ứng dụng client(redirect_uri ban đầu) để có  quyền truy cập vào tài khoản của người dùng.  Trong trường hợp này, kẻ  tấn công thậm chí không cần biết bí mật của client app hoặc mã thông báo  truy cập kết quả.  Miễn là nạn nhân có một phiên hợp lệ với dịch vụ  OAuth, ứng dụng khách sẽ chỉ cần hoàn thành việc trao đổi code/token thay mặt cho kẻ tấn công trước khi đăng nhập vào tài khoản của nạn nhân.

![Screenshot 2022-08-26 105734](https://user-images.githubusercontent.com/68894302/186815435-52154816-5f31-4cce-9ad0-59dc1251900a.png)

![image](https://user-images.githubusercontent.com/68894302/186816561-30c4a478-7dc7-4432-899a-c9469594160e.png)

Tại địa chỉ 10.0.4.66 là địa chỉ ip của quản trị viên, bây giờ chúng ta sẽ steal giá trị  `code`  để đăng nhập vào trang quản trị

![image](https://user-images.githubusercontent.com/68894302/186818347-9f621ed2-b549-4d61-b37a-ac307c988054.png)

Forwarded 

![image](https://user-images.githubusercontent.com/68894302/186820503-0bf99ff5-069b-41d4-8a07-13b50a4f978a.png)

Vào admin panel và xóa carlos

![image](https://user-images.githubusercontent.com/68894302/186820608-1ee6db64-2585-451b-b69d-74712f117bcc.png)







