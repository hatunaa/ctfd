# CSRF where token is tied to non-session cookie

Trong quá trình đăng nhập, mọi mã thông báo tồn tại từ trước đều bị vô hiệu (ít nhất là đối với cùng một đường dẫn truy cập. Vì vậy, một thông tin đăng nhập trong trình duyệt và một trong ứng dụng di động thì được, nhưng hai phiên trình duyệt đồng thời thì không).

Khi đăng xuất, mã thông báo cho phiên hiện tại bị vô hiệu. Thời gian tồn tại của mã thông báo có thể bị giới hạn, vì vậy, thỉnh thoảng mã thông báo trong một phiên có thể được trao đổi. Tất nhiên, điều này đòi hỏi ứng dụng phải đảm bảo rằng người dùng không bị gián đoạn

 Sau khi thay đổi email cho wiener một vài lần, qua một số lần đăng nhập và đăng xuất, chúng ta thấy rằng các mã thông báo csrf không thay đổi. Ngoài ra cookie là csrfKey chúng ta có thể control được qua chức năng tìm kiếm

![image](https://user-images.githubusercontent.com/68894302/173713735-ae0ab37d-0445-451f-b230-8376fa890d23.png)

csrfKey cũng không thay đổi, nên chúng ta sẽ thấy vấn đề lỗi ở đây đó là không ràng buộc với session hiện tại. Tiếp theo chúng ta sẽ tìm hiểu xem mã thông báo csrf có ràng buộc với người dùng không thì thấy rằng sau khi thay thay thế csrf token của wiener vào người dùng carlos chúng ta vẫn có thể đổi được email người dùng. 

Các bước exploit như sau:

+ gen 1 form html để thay đổi email
+ Sử dụng CSRF token hiện có nhưng còn hiệu lực(drop request)
+ Tính năng auto-submit

 POC CSRF payload như sau:

![image](https://user-images.githubusercontent.com/68894302/173714135-5d060de1-4fcc-4c13-b49d-60bf705d28a0.png)

Tại sao lại là img tag? Vì trong trường hợp này chúng ta cần một tính năng tự động submit. Khi người dùng không load ảnh thì nó vẫn thực hiện các event bên trong.

![image](https://user-images.githubusercontent.com/68894302/173714637-a558b4f8-d681-4691-8439-0178daef223e.png)