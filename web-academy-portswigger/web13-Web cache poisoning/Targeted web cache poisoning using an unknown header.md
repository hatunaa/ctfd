# Targeted web cache poisoning using an unknown header

Đầu tiên chúng ta sẽ xác định unkeyed inputs bằng cách dùng Param Miner trên Burpsuite, đây là công cụ mạnh có thể scan header để thực hiện poison cache thay vì thử bằng cách thủ công khá lâu.

1. Xác định unkeyed inputs là X-Host

​	![image](https://user-images.githubusercontent.com/68894302/180639030-f8ee6748-b0ef-44c7-a36d-62ead6965878.png)

2. Thêm header `X-Host` cùng giá host example để thử thì host đấy được inject vào nội dung phản hồi, có vẻ như poisonning thành công

   ![image](https://user-images.githubusercontent.com/68894302/180639148-3c5d0f6c-c41c-45e2-9581-52b410b83f27.png)

Header Vary trong response để xác định máy người dùng truy cập từ môi trường nào để xác định người dùng khác nhau. Vậy chúng ta có thể thực thi bằng cách thực thi javascript trong comment để người dùng dính chưởng, sau đó check trong log server exploit để xem user-agent của họ là bao nhiêu, thông qua sự khác nhau giữa các địa chỉ IP

Như với hình ảnh bên dưới, địa chỉ IP 171.251.237.87 là ip của chúng ta đang truy cập, còn địa chỉ ip 10.0.3.186 là từ ip của victim. 

![image](https://user-images.githubusercontent.com/68894302/180639269-07aeb2dd-1f74-472e-a899-3baef22c241e.png)

![image](https://user-images.githubusercontent.com/68894302/180639330-e9b5b98f-bdb1-40ef-8c4d-5faddf720c63.png)

Chúng ta sẽ lấy được User-agent ở đây và replace vào header request, sau đó gửi request để X-Cache chuyển sang hit là chúng ta đã giải quyết challenge này.

<img src="https://user-images.githubusercontent.com/68894302/180639385-f819ca30-092d-4ece-a651-6cab41589d91.png" alt="image" style="zoom:80%;" />