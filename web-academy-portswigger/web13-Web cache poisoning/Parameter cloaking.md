## Parameter cloaking

Đầu tiên truy cập vào trang 

![image](https://user-images.githubusercontent.com/68894302/181160632-59c5160d-6e08-4a96-8034-d145c9760265.png)

Gửi request đến repeater

![image](https://user-images.githubusercontent.com/68894302/181160731-b6f92b23-b000-47af-b7b2-2fcff8fac24c.png)

Nếu chúng ta thêm một cache buster và gửi nó, nó sẽ được reflected trong phản hồi

![image](https://user-images.githubusercontent.com/68894302/181160911-f20c7254-eec9-4156-94d4-9f874235af52.png)

Nếu chúng ta thêm param utm_content thì nó cũng được phản ánh trong phản hồi

![image](https://user-images.githubusercontent.com/68894302/181161180-c1486deb-51a1-4280-bb66-31be6e3be92a.png)

Nếu thêm một tham số bổ sung bằng dấu chấm phẩy (__;__) thì nó không được reflected trong phản hồi mà bị loại ra khỏi cache key. Các param bổ sung có thể bị loại trừ khỏi cache key

![image](https://user-images.githubusercontent.com/68894302/181161432-884effef-ae67-476f-843a-1bb3b1236ba4.png)

Gửi yêu cầu tiếp theo đến repeater

![image](https://user-images.githubusercontent.com/68894302/181161718-7acae888-00f1-47e0-a18d-fc7185c72178.png)

Khi gửi nó có thể kiểm tra giá trị callback trong phản hồi

![image](https://user-images.githubusercontent.com/68894302/181161870-fb4886da-736d-4663-ad81-4e2d60bb2df7.png)

Nó sẽ được reflected nếu giá trị callback được thay đổi

![image](https://user-images.githubusercontent.com/68894302/181161972-4ad157b0-d8b5-4a21-98c0-c6c42014cced.png)

Loại trừ param callback bằng tham số utm_content, sau đó thêm param callback dùng dấy chấm phẩy để overwrite nó

![image](https://user-images.githubusercontent.com/68894302/181163358-dce5001e-09f9-4c21-8fde-e1b319bf37ec.png)

Challenge được giải quyết

![image](https://user-images.githubusercontent.com/68894302/181163421-6d7b87c1-d3df-441f-84cb-54f44422169c.png)