# Host validation bypass via connection state attack

Đôi khi các máy chủ chỉ thực hiện xác thực đối với yêu cầu đầu tiên mà chúng nhận được qua một kết nối mới. Trong trường hợp này có thể bỏ qua việc xác thực này bằng cách gửi yêu cầu đầu tiên như một yêu cầu bình thường, sau đó thực hiện một yêu cầu khác phía sau trên cùng 1 kết nối

Để thực hiện điều này, Burp Suite đã phát hành phiên bản 2022.8.1 có thêm tính năng nhóm các request thành 1 group và gửi nó trên cùng 1 kết nối

![image](https://user-images.githubusercontent.com/68894302/185840094-87ef424a-d447-4816-a276-7890d4bd4058.png)

Tuy nhiên cần chỉnh header Connection từ close thành keep-alive để giữ cho giao tiếp giữa các request liên tục được duy trì. 

Demo việc này chúng ta sẽ cùng làm một bài lab đơn giản trên Portswigger đó là [Host validation bypass via connection state attack](https://portswigger.net/web-security/host-header/exploiting/lab-host-header-host-validation-bypass-via-connection-state-attack). Đây là một bài lab với gợi ý có tồn tại lỗ hổng SSRF trong cơ chế xác thực Host header và địa chỉ IP ở phía local đề bài cho là 192.168.0.1. Nhưng ở đây mình sẽ thực hiện brute-force để tìm địa chỉ IP local này. Vì trong thực tế muốn thực trigger được lỗ hổng thì chúng ta phải đi tìm địa chỉ IP localhost trước.

Khi truy cập đến endpoint /admin thì server trả về status 404 Not Found. Có nghĩa là endpoint này không tồn tại, hoặc không được public ra ngoài internet? 

![image](https://user-images.githubusercontent.com/68894302/185841245-3899c335-9f7d-4887-b4ef-280d3c38cd78.png)

Theo Internet Engineering Task Force (IETF)  trong tài liệu [RFC-1918](https://datatracker.ietf.org/doc/html/rfc1918#section-3) thì các dải IP sau thuộc dải IP nội bộ

![image](https://user-images.githubusercontent.com/68894302/185842440-921988f9-9d03-4e55-9b1a-6b304b973fec.png)

Khi thử với địa chỉ IP 192.168.1.1 và truy cập đến path /admin thì phản hồi trả về 

![image](https://user-images.githubusercontent.com/68894302/185843214-f68fa3b3-aae3-4043-a235-b39281ac975a.png)

Redirect 301 (Moved permanently) là một mã trạng thái HTTP (response code HTTP) nhằm thông báo rằng các URL hoặc các trang web đã được chuyển hướng vĩnh viễn sang một URL hoặc một trang web khác. Có nghĩa là tất cả các giá trị của trang web hoặc URL gốc như hình ảnh, nội dung… sẽ được chuyển hết sang URL mới. Tức là gì, chúng ta đã có thể truy cập vào được nội bộ của ứng dụng.

Bây giờ việc cần làm là nhóm 2 request này lại với nhau, request đầu tiên là request bình thường, để connection ở trạng thái keep-alive ; request thứ 2 là request đến admin panel ở đây là /admin và địa chỉ IP của nó là 192.168.1.1. 

![image](https://user-images.githubusercontent.com/68894302/185844026-ee88a412-876f-472c-93ef-c292674d19e5.png)

Group 2 request này lại thành 1 nhóm và phối hợp trong 1 lần gửi 

Và đây là kết quả trả về trong tab thứ 2 (7). 

![image](https://user-images.githubusercontent.com/68894302/185844408-56bca353-f712-482a-8fba-91561809df60.png)

Một form xóa người dùng mà chỉ admin mới có quyền này, bao gồm csrf token, session để thực hiện. Thêm param csrf token vào và vì là submit form nên thay đổi http method thành POST

![image](https://user-images.githubusercontent.com/68894302/185845168-32fb3269-8fe4-46dc-8aa7-aa6fe5f8397b.png)

Và như vậy là người dùng carlos đã bị xóa, thử thách đã được giải quyết



