**IDOR**

**Lab 18**: Insecure Direct Object References - Edit Another User's Profile

![1](https://user-images.githubusercontent.com/68894302/139593980-4cbf4229-6942-4af6-b473-d45bfb6ca54f.png)



Tên người dùng là ứng với UID bằng 5 là bryce. Tại sao?

Hãy nhìn kĩ URL sau, ta có thể dễ dàng thay đổi uid người dùng:

![2](https://user-images.githubusercontent.com/68894302/139593988-d8d8f988-dd9c-4fc1-958f-a745c4bde4ad.png)

chuyển thành 5 sẽ ra kết quả:

![3](https://user-images.githubusercontent.com/68894302/139593989-e287f60b-db56-4ec5-b416-5dedf9c6dc1f.png)

Đây là lab khá ease!



-----

**Lab 19**: Insecure Direct Object References - Extracting User Accounts

![4](https://user-images.githubusercontent.com/68894302/139593991-eeacb250-f9c6-4784-8147-40fb3be1040d.png)

Đây là lab liên quan đến LFI. Tức là về cơ bản  chúng ta có thể khai thác lỗi tệp cục bộ của máy chủ web. Tệp /etc/passwd sẽ chứa tài khoản tên `root`. Vì:

![5](https://user-images.githubusercontent.com/68894302/139593995-9a567d2b-6c7d-48f5-92e2-4c8c2dd86e51.png)

(Để ý kĩ phần url nhé). lỗi tại page=... khiến ta có thể truy xuất đến 1 tệp bất kì của server.





----



**Lab 20**: Insecure Direct Object References - Extracting User Accounts with Local File Inclusion

![image-20211031225457260](C:/Users/tuandv/AppData/Roaming/Typora/typora-user-images/image-20211031225457260.png)

(Nhìn lại bức ảnh lab 19). Ta dùng công cụ find để tìm xem tên người dùng nào xuất hiện: -> `ntp` 

![image-20211031225644260](C:/Users/tuandv/AppData/Roaming/Typora/typora-user-images/image-20211031225644260.png)





-----



**Lab 21**: Insecure Direct Object Reference - Web Shell with Local File Inclusion

![6](https://user-images.githubusercontent.com/68894302/139594001-c52f813c-8ef0-48a9-9558-578302ed6b2d.png)

Cơ bản thì câu hỏi này liên nó bảo dùng pwd (mà pwd tức là in ra vị trí tại đâu). Thực ra đáp án là  /var/www/mutillidae luôn. Vì sao? Tự làm tay mới to nên tự tìm cách kết nối shell nhé haha :))



--------

Oke chuyển sang lab RFI (vẫn trong phần IDOR)

**Lab 22**: Insecure Direct Object Reference - Web Shell with Remote File Inclusion (RFI)

![image-20211031230429583](C:/Users/tuandv/AppData/Roaming/Typora/typora-user-images/image-20211031230429583.png)

Đề bài dài vờ lờ. À câu này lí thuyết => Đ/Á cuối



-----

Chuyển hướng mở.

**Lab 23**: Open Redirects - Part 1

![7](https://user-images.githubusercontent.com/68894302/139594004-f8ee336c-a265-4ed3-9940-6fd83173ad0a.png)
