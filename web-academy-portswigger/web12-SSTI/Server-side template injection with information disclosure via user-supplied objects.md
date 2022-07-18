# Server-side template injection with information disclosure via user-supplied objects

__Yêu cầu__: 

Retrieve the secret key linked to the framework used by the server. The identifiers of a user account are given: `content-manager:C0nt3ntM4n4g3r`.

__Finding template engine__

Challenge này cho phép chúng ta thực hiện chỉnh sửa template, dùng `{{7*7}}` để kiểm tra kết quả có trả về kết quả 49 hay không

![image](https://user-images.githubusercontent.com/68894302/179439258-c12ea2ac-e4fd-4cf7-93b1-00e682b31842.png)

Nhưng sau khi preview thì thông báo lỗi trả về từ server

![image](https://user-images.githubusercontent.com/68894302/179439343-10aa14b7-91e5-41d7-bb15-0c81c5f5ef9a.png)Từ đoạn traceback này chúng ta thấy ứng dụng đang sử dụng template của Django (Python)

__Exploit__

Sử dụng payload sau để đọc đầu ra của trình debug

![image](https://user-images.githubusercontent.com/68894302/179440216-7d4b7496-45ca-4a86-ac3b-16e1f348bd06.png)

Đọc secret key từ đối tượng __settings__ có sẵn bằng `{{settings.SECRET_KEY}}`

![image](https://user-images.githubusercontent.com/68894302/179440446-4558a872-ed77-4d36-83b2-4eaddea7e6e4.png)

Dùng giá trị key đó để solve challenge

![image](https://user-images.githubusercontent.com/68894302/179440485-656a7559-f911-4885-b1da-873e16ccc3e6.png)