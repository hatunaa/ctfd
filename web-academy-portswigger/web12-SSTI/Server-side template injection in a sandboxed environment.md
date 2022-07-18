## Server-side template injection in a sandboxed environment

__Description__:

To solve the lab, break out of the sandbox to read the file `my_password.txt` from Carlos's home directory

__finding template engine__

Template engine đang được sử dụng là Freemaker

![image](https://user-images.githubusercontent.com/68894302/179453967-989e0b39-7764-48fd-a02c-b2da2b8422b6.png)

nhưng ở đây chúng ta không thể thực thi mã tùy ý được, mà sẽ dựa vào lớp Object chain với hàm có sẵn với mọi object như getClass()

![image](https://user-images.githubusercontent.com/68894302/179453775-19744be6-64f8-42ef-8658-d5ead7de83fe.png)

Chuyển các kí tự sang bytes sang ascii ta được

![image](https://user-images.githubusercontent.com/68894302/179454993-9e58a10c-9ba5-4d77-836f-5609bdd64c23.png)

Như vậy đã đọc thành công file __/etc/passwd__. Vì bài yêu cầu chúng ta đọc file __my_password.txt__ từ thư mục chính của Carlos nên chúng ta sẽ thay đổi file trong 

![image](https://user-images.githubusercontent.com/68894302/179455256-f7526420-0c26-4d20-84bd-ac33b4df266f.png)

![image](https://user-images.githubusercontent.com/68894302/179455349-bc0c6655-bd5c-4196-a2a7-bb65dc7a33b4.png)

![image](https://user-images.githubusercontent.com/68894302/179455382-0bed4747-0cc2-4f75-b547-6c9d1b8c7133.png)