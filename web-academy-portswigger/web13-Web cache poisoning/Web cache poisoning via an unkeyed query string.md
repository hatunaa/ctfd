# Web cache poisoning via an unkeyed query string

Yêu cầu của bài này là làm cho trang web thực hiện hàm alert(1). Khi truy vấn trên URL chúng ta thấy rằng nó cache lại sau khi thêm trường header Origin để sửa đổi. 

![image](https://user-images.githubusercontent.com/68894302/180707310-1dd742bb-7d68-48b7-b375-a671897cf9ff.png)

Trên burp chúng ta gửi requests đến khi cache chuyển sang hit, escape ra khỏi tag `link` và chèn vào đó javascript

![image](https://user-images.githubusercontent.com/68894302/180707537-f865d943-7f69-461c-a243-645595f371c9.png)

Sau đó thì alert() được thực thi.