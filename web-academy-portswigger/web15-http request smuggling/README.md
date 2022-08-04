# Lỗ hổng HTTP Requests smuggling

Các trang web hiện đại bao gồm các chain systems, tất cả đều giao tiếp qua HTTP. Kiến trúc nhiều tầng này nhận các HTTP request từ nhiều người dùng khác nhau và định tuyến chúng qua một kết nối TCP/TLS duy nhất

![image](https://user-images.githubusercontent.com/68894302/182902903-d455b44d-f410-454e-8012-d87b808b78ce.png)

Tuy nhiên, nhiều khi các request chỉ xác thực phía Front-end mà bỏ qua xác thực phía back-end khiến cho máy chủ back-end không biết nơi mỗi message kết thúc (message ở đây là toàn bộ request) dẫn đến việc hacker có thể gửi một message không rõ ràng được hiểu là hai request riêng biệt bởi back-end

![image](https://user-images.githubusercontent.com/68894302/182903778-ddbc7ee1-7ffc-46f0-89c4-509f47d3f6a2.png)

Điều này cung cấp cho kẻ tấn công khả năng thêm nội dung tùy ý khi bắt đầu yêu cầu của người dùng hợp pháp tiếp theo. Trong cách tấn công này smuggled content sẽ được gọi là __prefix__ và được đánh dấu bằng màu da cam

Ví dụ front-end ưu tiên header Content-Length đầu tiên và back-end ưu tiên thứ hai. Từ quan điểm của back-end, luồng TCP có thể trông giống như sau:

![image](https://user-images.githubusercontent.com/68894302/182904876-040098ad-3904-4854-88c9-7644e933b44b.png)

Front-end sẽ forward dữ liệu màu xanh lam và da cam trước khi đưa ra phản hồi. Điều này làm cho back-end socket bị poisoning với dữ liệu màu da cam. hi yêu cầu hợp pháp màu xanh lá cây đến, nó sẽ được thêm vào nội dung màu cam, gây ra phản hồi không mong muốn.

Trong ví dụ này, 'G' được chèn vào sẽ làm hỏng yêu cầu của người dùng màu xanh lá cây và họ có thể sẽ nhận được phản hồi dọc theo dòng "Unknown method GPOST".

Trong real world, kỹ thuật Content-Length kép hiếm khi hoạt động vì nhiều hệ thống từ chối hợp lý các yêu cầu có nhiều tiêu đề độ dài nội dung. Thay vào đó, chúng ta sẽ tấn công các hệ thống bằng cách sử dụng mã hóa phân đoạn - đã có thông số kỹ thuật [RFC2616](https://datatracker.ietf.org/doc/html/rfc2616#section-4.4): 

"__If a message is received with both a Transfer-Encoding header field and a Content-Length header field, the latter MUST be ignored__ "

(Nếu nhận được thông báo có cả trường header Transfer-Encoding (TE) và Content-Length (CL), thì trường sau đó PHẢI bị bỏ qua)

...

-----

Refer [James Kettle](https://portswigger.net/research/james-kettle)     

https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn

