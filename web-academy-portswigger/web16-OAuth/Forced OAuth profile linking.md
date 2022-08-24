## Forced OAuth profile linking

Có 2 lựa chọn để đăng nhập là dùng username và mật khẩu truyền thống hoặc cách thứ hai là đăng nhập qua OAuth

![image](https://user-images.githubusercontent.com/68894302/186358960-85a0fa9c-e20b-4d5d-9265-e56421579316.png)

Đăng nhập bằng username:password là wiener:peter

![image](https://user-images.githubusercontent.com/68894302/186359847-5e6f89ea-ea9c-4d00-a790-f476295eb3d3.png)

Thử tiếp với chức năng đăng nhập bằng OAuth

![image](https://user-images.githubusercontent.com/68894302/186360287-5d13cadf-df8a-4884-9beb-918ac570354c.png)

Xem lại history trong tab Proxy

![image](https://user-images.githubusercontent.com/68894302/186361238-02b80aec-16e4-4dc5-a2a9-1546d7fb9f66.png)

Đây là các thông số bên client application gửi yêu cầu đến OAuth để yêu cầu quyền truy cập vào tài nguyên. Nhưng ở đây thấy thiếu tham số state.
Tham số state có thể duy trì dữ liệu giữa người dùng được chuyển hướng đến máy chủ ủy quyền và quay lại một lần nữa. Đây là một giá trị duy nhất vì nó đóng vai trò như một cơ chế bảo vệ CSRF nếu nó chứa một giá trị duy nhất hoặc ngẫu nhiên cho mỗi yêu cầu. 

![image](https://user-images.githubusercontent.com/68894302/186399349-555ca5d4-ba19-4171-ae0e-eed54d93004f.png)

Drop request để đánh cắp mã code này, sau đó dùng nó để tạo một iframe trên exploit server của chúng ta để chuyển sau khi phân phối đoạn mã độc này đến người dùng tiếp theo thì sau khi chúng ta đăng nhập sẽ vào được giao diện của người đó, ở đây là admin

![image](https://user-images.githubusercontent.com/68894302/186403515-93588c4c-4d9f-4a40-854a-fda56b5fea48.png)

Quay trở lại đăng nhập bằng mạng xã hội chúng ta đã vào được giao diện quản trị

![image](https://user-images.githubusercontent.com/68894302/186403680-1b38105b-93ab-45ee-b474-af5b6cdcb209.png)

Hoàn thành thử thách

![image](https://user-images.githubusercontent.com/68894302/186403806-305f96e3-f3d2-47f1-bdbc-6510358965db.png)

