# Basic server-side template injection

Điểm có thể inject template tại vị trí __/?message__  với __<%= 7*7 %> __ chúng ta có thể xác định rằng có thể thực thi SSTI, ngoài ra sau khi thử một số tag thì chúng ta cũng có thể thực thi được xss, nhưng ở bài này không yêu cầu khai thác lỗi xss nên chúng ta có thể bỏ qua

Sau khi thử với __config__ thì thấy thông báo lỗi trả về từ ứng dụng

![image](https://user-images.githubusercontent.com/68894302/179418784-521af489-d16b-46ca-9914-05801260f32b.png)

=> xác định ứng dụng đang sử dụng Ruby trong phần backend. Dùng kĩ thuật để đọc file trong Ryby chúng ta có __Dir.entries('/')__ để list ra các thư mục

![image](https://user-images.githubusercontent.com/68894302/179418858-8c795efd-c08f-4294-854d-7cc7fafbebad.png)

Tìm thấy file__morale.txt__ trong thư mục /home/carlos/

![image](https://user-images.githubusercontent.com/68894302/179418993-7539d175-b73a-411e-a997-7e753186bd6c.png)

Tiến hành xóa file này.

![image](https://user-images.githubusercontent.com/68894302/179419021-08bdebac-e575-4191-9248-9bf7b8b1c097.png)