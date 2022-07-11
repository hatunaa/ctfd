# Modifying serialized data types

Sau khi login, header Cookie cũng lưu thông tin đối tượng dưới dạng serialization gồm 2 thuộc tính là: username và access_token

![image-20220711191828678](C:/Users/tuandv/AppData/Roaming/Typora/typora-user-images/image-20220711191828678.png)

Trong thử thách này chúng ta vẫn phải truy cập vào admin panel để xóa người dùng carlos. Trong description chỉ định rằng tên tài khoản của quản trị viên là administrator. 

Tiếp theo chúng ta sẽ xử lí access_token sửa đổi thuộc tính này để tận dụng lỗ hổng loose comparaison (so sánh lỏng lẻo) trong php.

Nói qua về lỗ hổng php loose comparaison đơn giản như sau:

+ sử dụng `==` hoặc `!=` : cả hai biến đều có cùng giá trị   => cả hai biến đều có cùng giá trị
+ sử dụng `===` hoặc `!==`: cả hai biến đều có cùng kiểu và cùng giá trị => chặt chẽ hơn

Ví dụ:

![image](https://user-images.githubusercontent.com/68894302/178265915-3efc04c7-ae40-4eec-9b08-967b7e26a030.png)

Nếu so sánh một chuỗi với 0 thì 'abcxy'=0 luôn trả lại giá trị đúng miễn là chuỗi không chứa số khác 0 ở đầu chuỗi. Như vậy nếu chúng ta so sánh giá trị chuỗi `access_token` với 0 thì có thể bypass trong trường hợp này. Trong [PHP serialize](https://www.php.net/manual/en/function.serialize.php) định nghĩa i chính là đại diện cho kiểu integer

![image](https://user-images.githubusercontent.com/68894302/178266200-f4ac76c3-1566-492f-8dd4-ff868bb468ed.png)

cookie mới ở dạng base64 decode như sau:

`O:4:"User":2:{s:8:"username";s:13:"administrator";s:12:"access_token";i:0;}`

Áp dụng thay đổi và gửi request đưa đến giao diện quản trị viên:

![image](https://user-images.githubusercontent.com/68894302/178266838-2ca76bfb-9744-4906-9a7a-bfe291257880.png)

Vào giao diện quản trị, xóa tài khoản carlos và challenge được giải quyết

![image](https://user-images.githubusercontent.com/68894302/178267124-2c5c4046-b13d-412a-86d1-7584aef9f681.png)

![image](https://user-images.githubusercontent.com/68894302/178267399-488c9ab0-b82c-4b5a-a792-962076448c1d.png)