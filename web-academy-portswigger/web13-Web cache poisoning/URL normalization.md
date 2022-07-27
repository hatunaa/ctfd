## URL normalization

Ở challenge này thì người dùng có thể gửi cho victim một URL để khi victim nhấp vào thì javascript sẽ được thực thi, cụ thể là hàm alert

Khi chúng ta thử một endpoint bất kì không tồn tại thì response trả về NOT Found trong thẻ `<p>` như sau:
![image](https://user-images.githubusercontent.com/68894302/181234506-7a27e435-14ef-49ba-977b-111d464d78f4.png)Sau khi thêm `</p>` thì ta thấy đoạn script được phản ánh trong res:

![image](https://user-images.githubusercontent.com/68894302/181234763-ea485241-cc3a-41a1-b335-3a552f9bbe15.png)

Điều đó cho thấy mặc dù endpoint không tồn tại nhưng sau đó javascript vẫn được thực thi

Gửi URL đó cho victim, trong trường hợp này chúng ta nên gửi toàn bộ payload qua burp mới có thể thực thi được, vì sau khi gửi bằng trình duyệt thì các kí tự đặc biệt có thể đã bị encodeURL

![image](https://user-images.githubusercontent.com/68894302/181235135-daf11cd2-bace-413e-a615-93f04995dc5a.png)

Và clear challenge này.

![image](https://user-images.githubusercontent.com/68894302/181235196-f74ce357-e55a-49b6-98a8-d18a05e93f34.png)