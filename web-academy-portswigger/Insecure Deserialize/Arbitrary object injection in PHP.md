# Arbitrary object injection in PHP

View source code chúng ta thấy gợi ý sau

![image](https://user-images.githubusercontent.com/68894302/178032140-17122f93-0eba-405c-aaa6-aad59d012d2f.png)

Sau khi truy cập vào entrypoint` /libs/CustomTemplate.php` thì không có gì cả, thông thường với một bài ctf bằng ngôn ngữ PHP thì chúng ta sẽ dùng `~` ở cuối file để truy cập source code

> /libs//CustemTemplate.php~

Mở code trong trình editor để phân tích cho rõ hơn

![image](https://user-images.githubusercontent.com/68894302/178042160-cbb3751f-b6bd-42da-bbad-901c080c0867.png)

Thông thường với một bài PHP deserialize thì phải có một trong hai phương thức sau: **__wakeup()**, **__destruct()**  thường được gọi là magic method (phương thức ma thuật) để xử lí dữ liệu người dùng, người dùng có thể chèn dữ liệu tùy ý vào hàm `unserialize()`.

Chúng ta cùng phân tích một chút về đoạn code trên:

+ __construct() như một hàm khởi tạo mỗi khi đối tượng CustomTemplate được tạo ra. Biến $lock_file_paht sẽ bằng biến $template_file_path +'.lock' .
+ hai hàm isTemplateLocked sẽ kiểm tra lock_file_path có tồn tại hay không, nếu tồn tại thì trả về true, hàm getTemplate trả về nội dung của template_file_path thành một string 
+ hàm saveTemplate() gọi đến hàm isTemplateLocked nếu tồn tại thì tiếp tục kiểm tra:
  	+ Nếu lock_file_path không rỗng thì nó sẽ ném ra một ngoại lệ không thể ghi đè vào file đó
  	+ Nếu $template không thể write được vào template_file_path thì nó cũng ném ra một ngoại lệ
+ destruct() được gọi khi đối tượng bị khi không có tham chiếu nào đến đối tượng nữa hay nói gọn là đối tương bị phá hủy.

Chúng ta sẽ chú ý hơn vào destruct() và làm cách nào để inject được string `/home/carlos/morela.txt ` Nếu file chúng ta nhập vào tồn tại thì nó sẽ gọi đến unlink() để xóa file này.

Vậy thì làm thế nào để inject vào file này trong khi $lock_file_path được khởi tạo với `.lock` ở cuối. 

## Khai thác

Cookie sẽ trả về cho chúng ta ở dạng serialize như sau:

![image](https://user-images.githubusercontent.com/68894302/178037324-dd7ad5ff-9820-4f7c-8c78-6bd5395e0af7.png)

Như vậy chúng ta có thể dễ dàng thay đổi đối tượng và các thuộc tính của nó sau đó chuyển tiếp request.

Payload:

`O:14:"CustomTemplate":1:{s:14:"lock_file_path";s:23:"/home/carlos/morale.txt";}`

Giải thích một chút các phần tử trong payload này như sau:

+ O:14:"CustomTemplate":1: đối tượng CustomTemplate với chiều dài 14 kí tự, có 1 thuộc tính 
+ s:14:"lock_file_path";s:23:"/home/carlos/morale.txt" : thuộc tính lock_file_path có độ dài 14 kí tự và giá trị của nó là /home/carlos/morale.txt dài 23 kí tự

<<<<<<< HEAD
![image](https://user-images.githubusercontent.com/68894302/178042456-3a547f59-e799-48c6-a479-01fa8854e6ba.png)
=======
![image](https://user-images.githubusercontent.com/68894302/178042456-3a547f59-e799-48c6-a479-01fa8854e6ba.png)
>>>>>>> 4c410c5dce1ead8d9dafcbefbe4d8c229374d4ab
