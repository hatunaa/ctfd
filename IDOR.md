**IDOR**

**Lab 18**: Insecure Direct Object References - Edit Another User's Profile

![1](https://user-images.githubusercontent.com/68894302/139593980-4cbf4229-6942-4af6-b473-d45bfb6ca54f.png)



Tên người dùng là ứng với UID bằng 5 là bryce. Tại sao?

Hãy nhìn kĩ URL sau, ta có thể dễ dàng thay đổi uid người dùng:

![hehe](https://user-images.githubusercontent.com/68894302/139594449-5fd1cc8c-9de5-4884-a4f5-4cdcf9d92c53.png)

chuyển thành 5 sẽ ra kết quả:

![2](https://user-images.githubusercontent.com/68894302/139594454-64d19df2-a97c-4fc4-8a35-f3724cc225b9.png)

Đây là lab khá ease!



-----

**Lab 19**: Insecure Direct Object References - Extracting User Accounts

![4](https://user-images.githubusercontent.com/68894302/139593991-eeacb250-f9c6-4784-8147-40fb3be1040d.png)

Đây là lab liên quan đến LFI. Tức là về cơ bản  chúng ta có thể khai thác lỗi tệp cục bộ của máy chủ web. Tệp /etc/passwd sẽ chứa tài khoản tên `root`. Vì:

![3](https://user-images.githubusercontent.com/68894302/139594461-100d40a8-067f-4a98-9752-df5e39470d2d.png)

(Để ý kĩ phần url nhé). lỗi tại page=... khiến ta có thể truy xuất đến 1 tệp bất kì của server.





----



**Lab 20**: Insecure Direct Object References - Extracting User Accounts with Local File Inclusion


(Nhìn lại bức ảnh lab 19). Ta dùng công cụ find để tìm xem tên người dùng nào xuất hiện: -> `ntp` 

![4](https://user-images.githubusercontent.com/68894302/139594462-f6d990e8-ca03-4165-aa35-b72aeb8a756d.png)





-----



**Lab 21**: Insecure Direct Object Reference - Web Shell with Local File Inclusion

![acc](https://user-images.githubusercontent.com/68894302/139594464-a9fa34bf-5398-4214-8c9e-a6dac92c17b1.png)

Cơ bản thì câu hỏi này liên nó bảo dùng pwd (mà pwd tức là in ra vị trí tại đâu). Thực ra đáp án là  /var/www/mutillidae luôn. Vì sao? Tự làm tay mới to nên tự tìm cách kết nối shell nhé haha :))



--------

Oke chuyển sang lab RFI (vẫn trong phần IDOR)

**Lab 22**: Insecure Direct Object Reference - Web Shell with Remote File Inclusion (RFI)

![6](https://user-images.githubusercontent.com/68894302/139594465-ba1a1dd9-71e0-4188-b3b1-c2d3f16402b3.png)

Đề bài dài vờ lờ. À câu này lí thuyết => Đ/Á cuối



-----

Chuyển hướng mở.

**Lab 23**: Open Redirects - Part 1

![7](https://user-images.githubusercontent.com/68894302/139594004-f8ee336c-a265-4ed3-9940-6fd83173ad0a.png)
