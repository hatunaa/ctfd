# [Burpsuite] lab #Authentication bypass via encryption oracle

## Description
This lab contains a logic flaw that exposes an encryption oracle to users. To solve the lab, exploit this flaw to gain access to the admin panel and delete Carlos. 

You can log in to your own account using the following credentials: wiener:peter

## Analysis

Giống như các lab trước, admin panel tồn tại dưới /admin
Chức năng bình luận cho phép để lại email của người dùng, khi nhập email tồn tại và email không tồn tại ta thấy phản hồi có sự khác nhau như sau:

```request
HTTP/1.1 302 Found
Location: /post/comment/confirmation?postId=2
Connection: close
Content-Length: 0
```

Và khi gửi email không tồn tại ví dụ: hacker.leet

```
HTTP/1.1 302 Found
Location: /post?postId=2
Set-Cookie: notification=6gnZux7RqYcxiimw2eYGXH1w4e7PPxdpF4toigfsdrQH8uCy4tbwWz0mf7%2bJFA%2bW; HttpOnly
Connection: close
Content-Length: 0
```

Trường notification của cookie được mã hóa, Khi paste giá trị `notification` vào GET /post?postId=x thì thấy có thông báo trong phản hồi: `Invalid email address: hacker.leet`

Cụm từ "Invalid email address: " có 23 kí tự. Và chúng ta nhận thấy rằng `eYmlaG%2bQQA0jKnCJT0Vw3zZ35Rs%2bZgPU57zOJPSqOSc%3d` có chứa các kí tự %2 và ở sau `Invalid email address` ta thấy thông báo có thể được giải mã.

Có một chức năng cũng có kiểu mã hóa giống như notification đó là stay-logged-in. Sau khi login, header của requests như sau:
```
GET /my-account HTTP/1.1
Host: ac121fb01f5bd63dc09f28b800cd00cd.web-security-academy.net
Cookie: session=SrgNVyGprrmRN1lPRx7Mi8sKmIVsG5NL; stay-logged-in=eYmlaG%2bQQA0jKnCJT0Vw3zZ35Rs%2bZgPU57zOJPSqOSc%3d
```
Có thể thấy rằng cách mã hóa của stay-logged-in và notification là rất giống nhau. 
Nếu chúng ta sử dụng một phương pháp mã hóa thì: 
+ POST /post/comment dùng để Encrypt
+ GET /post?postId={x} được dùng để Decrypt
+ notification trong phản hồi của POST /post/comment cũng được dùng để mã hóa

## Exploit
Gửi `email=administrator:1652097711395` tới encrypt. Văn bản được mã hóa bởi DECRYPT bằng cách sử dụng thông báo của param là: 
```
Invalid email address: administrator:1652097711395
```

Ngoài thông tin tài khoản cơ bản được mã hóa, "invalid email address: " cũng được encrypt

Invalid email address: Bao gồm 23 ký tự, gửi toàn bộ câu được mã hóa để giải mã

Thực hiện URL decode → base64 decode → xóa 23 bytes. 
Sau đó mã hóa ngược lại base64 encode → URL encode. Để kiểm tra xem văn bản được mã hóa có đúng hay không, thử giải mã.  Kết quả tìm thấy 500 Internal Server Error và thông báo 
``` 
Input length must be multiple of 16 when decrypting with paddedcipher
```

Trường đầu vào phải là bội số của 16 khi giải mã bằng giải thuật paddedcipher. Search google thì ra thuật toán phân nhóm  đã được sử dụng. Padding là một cách để lấy dữ liệu có thể là bội số của kích thước khối cho một mật mã và mở rộng nó ra sao cho đúng.
Vì thế 16x2-23, cần thêm 9 kí tự vào trước administrator để encrypt nhóm trước đó, nhóm `administrator:1652097711395` là nhóm sau cùng.
```
123456789administrator:1652097711395
```
Sau đó đưa giá trị notification vào phẩn decode và mã hóa như các bước ở trên. Mã cuối cùng là: 

```
%66%4c%4b%59%4d%76%63%6b%43%47%32%31%65%32%41%70%48%6b%6e%51%64%31%51%42%48%78%4a%74%49%4b%4d%4d%50%68%71%79%74%78%69%6d%65%37%59%3d
```
Dùng mã trên để thay thế giá trị của notification và chúng ta có phần mã hóa như sau
```
<header class="notification-header">
administrator:1652097711395         
</header>
```


