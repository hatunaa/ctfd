# Reflected XSS with AngularJS sandbox escape without strings

>  Độ khó: Expert

Description:

> This lab uses [AngularJS](https://portswigger.net/web-security/cross-site-scripting/contexts/angularjs-sandbox) in an unusual way where the `$eval` function is not available and you will be unable to use any strings in AngularJS.  
>
>  To solve the lab, perform a [cross-site scripting](https://portswigger.net/web-security/cross-site-scripting) attack that escapes the sandbox and executes the `alert` function without using the `$eval` function.        

---

1.Step by step

Tìm kiếm `<></script>*()'&"{=}[]` và sau đó view-source chúng ta thấy nó đã được reflected vào trong code angularJS như sau:

```javascript
<script>angular.module('labApp'[]).controller('vulnCtrl',
	function($scope, $parse) {
        $scope.query = {};
        var key = 'search';
        $scope.query[key] = '&lt;&gt;&lt;/script&gt;*()&apos;&&quot;{=}[]';
        $scope.value = $parse(key)($scope.query);
});
</script>
```

Từ đó ta rút ra các tự không bị filter là `} { () = [] /` 

2.Giới thiệu AngularJS

AngularJS là một khuôn khổ phía  máy khách MVC được viết bởi Google.  Với Angular, các trang HTML bạn  nhìn thấy qua view-source hoặc Burp chứa 'ng-app' thực sự là các mẫu và  sẽ được hiển thị bởi Angular.  Điều này có nghĩa là nếu đầu vào của  người dùng được nhúng trực tiếp vào một trang, ứng dụng có thể dễ bị  chèn mẫu phía máy khách.  Điều này đúng ngay cả khi đầu vào của người  dùng được mã hóa HTML và bên trong một thuộc tính. 

Đầu vào văn bản {{1 + 1}} được đánh giá bởi Angular, sau đó hiển thị đầu ra: 2. 

Nó có nghĩa là bất kỳ ai có thể chèn dấu ngoặc nhọn kép đều có thể thực hiện các biểu thức Angular, khi được kết hợp với sandbox escape, chúng ta có thể thực thi JavaScript tùy ý

Hai đoạn mã sau cho thấy bản  chất của lỗ hổng. Trang đầu tiên tự động nhúng đầu vào của người dùng,  nhưng không dễ bị XSS vì nó sử dụng [htmlspecialchars ](http://php.net/manual/en/function.htmlspecialchars.php)để HTML mã hóa đầu vào: 

``` javascript
<html>
<body>
<p>
<?php
$q = $_GET['q'];
echo htmlspecialchars($q,ENT_QUOTES);
?>
</p>
</body>
</html>
```

Đoạn code thứ hai gần như giống hệt  nhau, nhưng việc inject Angular có nghĩa là nó có thể được khai thác bằng  cách chèn một biểu thức Angular và với sandbox escape, chúng ta  có thể lấy thực thi mã Javascript tùy ý . 

``` javascript
<html ng-app>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.4.7/angular.js"></script>
</head>
<body>
<p>
<?php
$q = $_GET['q'];
echo htmlspecialchars($q,ENT_QUOTES);?>
</p>   
</body>
</html>
```

Và ở trong thử thách này chúng ta cũng thấy phiên bả đang dùng là angular_1.4.4 là phiên bản cũ có chứa lỗ hổng.

![image](https://user-images.githubusercontent.com/68894302/172321176-173cb0a6-c699-407f-8e9f-bff38515d2ca.png)



3.Khai thác

Trong cheatsheet XSS thì chúng ta thấy rằng hầu hết các vector đề chứa dấu `'` chỉ có payload cuối cùng là không chứa

=> có thể dựa vào vertor này để tạo payload giải quyết thử thách

![image](https://user-images.githubusercontent.com/68894302/172321930-e5a24179-ca59-41e6-bfe0-cc20eddfb212.png)

Chúng ta có thể sử dụng việc ghi đè các hàm Javascript  gốc bằng cách sử dụng Angular expression. Vấn đề là biểu thức Angular  không hỗ trợ các câu lệnh hàm hoặc biểu thức hàm, vì vậy chúng ta sẽ không  thể ghi đè hàm bằng bất kỳ giá trị nào. Nhưng sử dụng `String.fromCharCode` thì có thể. Bởi vì hàm được gọi từ phương thức String constructor chứ không phải thông qua string literal (chuỗi kí tự).

Việc tránh các string nên chúng ta sẽ sử dụng chuyển đổi. Sử dụng phương thức JavaScript String fromCharCode() để chuyển đổi chuỗi  payload thành charCode

Nếu như box ở đầu bị thoát, chúng ta sẽ không thể ghi chuỗi.  Làm thế nào để chúng ta viết payload  JavaScript `<script>alert(1)</script>`?  

Chúng ta cần break ra khỏi  AngularJS sandbox  bằng cách sử dụng phương thức toString(), lấy  prototype string và ghi đè nó bằng cách join charAt dưới  dạng một mảng (charAt%3d []. join) và URL encode kí tự `=`. Sau đó chuyển đổi mảng vào bộ lọc `orrderBy` và đặt đối số cho bộ lọc để tạo chuyển đổi. 

Bằng cách ghi đè hàm bằng kỹ thuật [] .join, chúng ta có hàm charAt () trả về tất cả các ký tự đã được gửi đến nó. 

Ví dụ dưới đây để chuyển đổi mảng kí tự thành mảng charCode

![image](https://user-images.githubusercontent.com/68894302/172360968-166a08c6-c8a0-4de0-8978-f7510269d885.png)

[link](https://jsfiddle.net/tuandv16/5ay6ztos/23/)

Form để bypass AngularJS sandbox như sau:

```javascript
1&toString().constructor.prototype.charAt%3d[].join;[1]|orderBy:toString().constructor.from
CharCode(value1,value2,value3,...value_n)=1
```

Bây giờ có thể thay thế giá trị các giá trị fromCharCode bằng mảng kết quả và nó sẽ như thế này:

```javascript
?search=1&toString().constructor.prototype.charAt%3d[].join;[2]|orderBy:toString().constructor.fromCharCode(120,61,97,108,101,114,116,40,49,41)=2
```

![image](https://user-images.githubusercontent.com/68894302/172363035-3859058c-6ea6-4c2f-be7b-5a8d2df8e659.png)
