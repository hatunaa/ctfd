**IDOR**

**Lab 18**: Insecure Direct Object References - Edit Another User's Profile

![image-20211031222941350](C:/Users/tuandv/AppData/Roaming/Typora/typora-user-images/image-20211031222941350.png)



Tên người dùng là ứng với UID bằng 5 là bryce. Tại sao?

Hãy nhìn kĩ URL sau, ta có thể dễ dàng thay đổi uid người dùng:

![image-20211031224622243](C:/Users/tuandv/AppData/Roaming/Typora/typora-user-images/image-20211031224622243.png)

chuyển thành 5 sẽ ra kết quả:

![image-20211031224700953](C:/Users/tuandv/AppData/Roaming/Typora/typora-user-images/image-20211031224700953.png)

Đây là lab khá ease!



-----

**Lab 19**: Insecure Direct Object References - Extracting User Accounts

![image-20211031224902895](C:/Users/tuandv/AppData/Roaming/Typora/typora-user-images/image-20211031224902895.png)

Đây là lab liên quan đến LFI. Tức là về cơ bản  chúng ta có thể khai thác lỗi tệp cục bộ của máy chủ web. Tệp /etc/passwd sẽ chứa tài khoản tên `root`. Vì:

![image-20211031225259165](C:/Users/tuandv/AppData/Roaming/Typora/typora-user-images/image-20211031225259165.png)

(Để ý kĩ phần url nhé). lỗi tại page=... khiến ta có thể truy xuất đến 1 tệp bất kì của server.





----



**Lab 20**: Insecure Direct Object References - Extracting User Accounts with Local File Inclusion

![image-20211031225457260](C:/Users/tuandv/AppData/Roaming/Typora/typora-user-images/image-20211031225457260.png)

(Nhìn lại bức ảnh lab 19). Ta dùng công cụ find để tìm xem tên người dùng nào xuất hiện: -> `ntp` 

![image-20211031225644260](C:/Users/tuandv/AppData/Roaming/Typora/typora-user-images/image-20211031225644260.png)





-----



**Lab 21**: Insecure Direct Object Reference - Web Shell with Local File Inclusion

![image-20211031225740889](C:/Users/tuandv/AppData/Roaming/Typora/typora-user-images/image-20211031225740889.png)

Cơ bản thì câu hỏi này liên nó bảo dùng pwd (mà pwd tức là in ra vị trí tại đâu). Thực ra đáp án là  /var/www/mutillidae luôn. Vì sao? Tự làm tay mới to nên tự tìm cách kết nối shell nhé haha :))



--------

Oke chuyển sang lab RFI (vẫn trong phần IDOR)

**Lab 22**: Insecure Direct Object Reference - Web Shell with Remote File Inclusion (RFI)

![image-20211031230429583](C:/Users/tuandv/AppData/Roaming/Typora/typora-user-images/image-20211031230429583.png)

Đề bài dài vờ lờ. À câu này lí thuyết => Đ/Á cuối



-----

Chuyển hướng mở.

**Lab 23**: Open Redirects - Part 1

![image-20211031230639721](C:/Users/tuandv/AppData/Roaming/Typora/typora-user-images/image-20211031230639721.png)

