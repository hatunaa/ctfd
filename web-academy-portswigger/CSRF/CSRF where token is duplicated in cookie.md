# CSRF where token is duplicated in cookie

Sau khi đăng nhập và thay đổi địa chỉ email của người dùng wiener quan sát thấy có sự trùng lặp mã csrf

![image](https://user-images.githubusercontent.com/68894302/173715652-aa9f010e-0654-4624-b8e1-cb755ce7d376.png)

Chúng ta thấy CSRF token xuất hiện 2 lần: trong phần body và cookie. Và trong challenge này chúng ta cũng thấy có thể control chức năng tìm kiếm bằng giá trị Set-Cookie để lấy phản hồi Cookie từ máy chủ

![image](https://user-images.githubusercontent.com/68894302/173716770-09b15f59-75d9-45b4-93b7-3a74129f7e35.png)

Sau khi thay đổi token CSRF bằng một giá trị bất kì thấy rằng vẫn có thể thay đổi địa chỉ email thành công![image](https://user-images.githubusercontent.com/68894302/173715886-597ff594-7f58-4e8d-9928-9e02e6c66ecd.png)

Ở đây chúng ta có thể hiểu rằng máy chủ backend theo dõi các token CSRF bình thường, chỉ sử dụng cookie làm tuyến phòng thủ bổ sung. Máy chủ backend không thực hiện bất kì theo dõi csrf nào và chỉ xác minh token csrf trong body bằng với token csrf trong cookie được đặt cùng thời điểm đó.

Mã thông báo CSRF được gắn với cookie không phải session nên chúng ta có thể lạm dụng nó để thao túng giá trị csrf token

POC CSRF như sau

![image](https://user-images.githubusercontent.com/68894302/173718109-d98a0055-f21a-4367-ad17-21a66fafb1a3.png)

