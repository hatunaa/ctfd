# DOM-based vulnerabilities



## DOM là gì? 

The Document Object Model (DOM) là một biểu diễn phân cấp của trình duyệt web của các phần tử trên trang.  Các trang web có thể sử dụng JavaScript để thao tác các nút và đối tượng của DOM, cũng như các thuộc tính của chúng.  Bản thân  thao tác DOM không phải là một vấn đề.  Trên thực tế, nó là một phần  không thể thiếu trong cách thức hoạt động của các trang web hiện đại. Tuy nhiên, JavaScript xử lý dữ liệu không an toàn có thể kích hoạt nhiều cuộc tấn công khác nhau. Các lỗ hổng dựa trên DOM phát sinh khi một  trang web chứa JavaScript nhận một giá trị có thể kiểm soát được của kẻ  tấn công, được gọi là nguồn và chuyển nó vào một chức năng nguy hiểm, được gọi là sink.

## Các lỗ hổng tain-flow

Nhiều lỗ hổng dựa trên DOM có thể bắt nguồn từ các vấn đề với cách mã phía máy khách thao túng dữ liệu có thể kiểm soát của kẻ tấn công.               

Để khai thác hoặc giảm thiểu những lỗ hổng này, điều quan trọng là trước tiên bạn phải tự làm quen với những điều cơ bản về dòng chảy giữa các  source và phần sink.

> **Source**
>
> Source là một thuộc tính JavaScript chấp nhận dữ liệu có khả năng bị kẻ  tấn công kiểm soát.  Một ví dụ về nguồn là thuộc tính location.search vì nó đọc đầu vào từ chuỗi truy vấn, điều này tương đối đơn giản để kẻ tấn công kiểm soát.  Cuối cùng, bất kỳ tài sản nào có thể được kiểm soát  bởi kẻ tấn công đều là một nguồn tiềm năng.  Điều này bao gồm URL giới  thiệu (được hiển thị bởi chuỗi document.referrer), cookie của người dùng (được hiển thị bởi chuỗi document.cookie) và thông báo web.

>  **Sinks**
>
> Phần sinks là một hàm  JavaScript hoặc đối tượng DOM tiềm ẩn nguy hiểm có thể gây ra các hiệu  ứng không mong muốn nếu dữ liệu do kẻ tấn công kiểm soát được chuyển đến nó.  Ví dụ, hàm `eval()` là một sink vì nó xử lý đối số được chuyển cho nó dưới dạng JavaScript.  Một ví dụ về sinks HTML là `document.body.innerHTML`vì nó có khả năng cho phép kẻ tấn công đưa vào HTML độc hại và thực thi JavaScript tùy ý. 	     

Về cơ bản, các lỗ hổng dựa trên DOM phát sinh khi một trang  web chuyển dữ liệu từ nguồn đến sink, sau đó xử lý dữ liệu theo cách  không an toàn trong bối cảnh phiên của khách hàng.         

Nguồn phổ biến nhất là URL, thường được truy cập bằng đối tượng `location`.  Kẻ tấn công có thể xây dựng một liên kết để đưa nạn nhân đến một  trang dễ bị tấn công với trọng tải trong chuỗi truy vấn và các phần phân đoạn của URL.  Hãy xem xét đoạn mã sau:         

``` 
goto = location.hash.slice(1)
if (goto.startsWith('https:')) {
  location = goto;
}
```

Điều này dễ bị [DOM base open redirect](https://portswigger.net/web-security/dom-based/open-redirection) vì nguồn`location.hash` được xử lý theo cách không an toàn.  Nếu URL chứa phân đoạn băm bắt đầu bằng `https:`, mã này trích xuất giá trị của thuộc tính `location.hash` và đặt nó là đối tượng`location` của `window`.  Kẻ tấn công có thể khai thác lỗ hổng này bằng cách xây dựng URL sau:         

```
https://www.innocent-website.com/example#https://www.evil-user.net
```

Khi nạn nhân truy cập URL này, JavaScript đặt giá trị của thuộc tính vị  trí thành https://www.evil-user.net, tự động chuyển hướng nạn nhân đến  trang web độc hại.  Ví dụ: hành vi này có thể dễ dàng bị lợi dụng để  thực hiện một cuộc tấn công lừa đảo.

## Sources phổ biến

Dưới đây là các source điển hình có thể được sử dụng để khai thác nhiều lỗ hổng bảo mật:

``` 
document.URL
document.documentURI
document.URLUnencoded
document.baseURI
location
document.cookie
document.referrer
window.name
history.pushState
history.replaceState
localStorage
sessionStorage
IndexedDB (mozIndexedDB, webkitIndexedDB, msIndexedDB)
Database
```

## Phần sinks nào có thể dẫn đến lỗ hổng DOM-based?

Danh sách sau cung cấp tổng quan nhanh về các lỗ hổng dựa trên DOM phổ  biến và ví dụ về lỗi có thể dẫn đến từng lỗ hổng.  Để có danh sách đầy  đủ hơn về các phần chìm có liên quan, vui lòng tham khảo các trang dành  riêng cho lỗ hổng bảo mật bằng cách nhấp vào các liên kết bên dưới.

``` 
DOM-based vulnerability 			Example sink
DOM XSS LABS 						document.write()
Open redirection LABS 				window.location
Cookie manipulation LABS 			document.cookie
JavaScript injection 				eval()
Document-domain manipulation 		document.domain
WebSocket-URL poisoning 			WebSocket()
Link manipulation 					element.src
Web message manipulation 			postMessage()
Ajax request-header manipulation 	setRequestHeader()
Local file-path manipulation 		FileReader.readAsText()
Client-side SQL injection 			ExecuteSql()
HTML5-storage manipulation 			sessionStorage.setItem()
Client-side XPath injection 		document.evaluate()
Client-side JSON injection 			JSON.parse()
DOM-data manipulation 				element.setAttribute()
Denial of service 					RegExp() 
```

## Cách ngăn chặn các lỗ hổng DOM-based taint-flow 

Bạn không thể thực hiện bất kỳ hành động nào để loại bỏ hoàn toàn mối đe dọa từ các cuộc tấn công dựa trên DOM.  Tuy nhiên, nói chung, cách hiệu quả nhất để tránh các lỗ hổng dựa trên DOM là tránh cho phép dữ liệu từ bất kỳ nguồn không đáng tin cậy nào tự động thay đổi giá trị được  truyền đến bất kỳ bộ lưu nào.   

Nếu chức năng mong muốn của ứng dụng có nghĩa là hành vi này là không  thể tránh khỏi, thì biện pháp bảo vệ phải được thực hiện trong mã phía  máy khách.  Trong nhiều trường hợp, dữ liệu liên quan có thể được xác  thực trên cơ sở whitelist, chỉ cho phép nội dung được biết là an  toàn.  Trong các trường hợp khác, cần phải sanitize  hoặc mã hóa dữ liệu.  Đây có thể là một nhiệm vụ phức tạp và tùy thuộc vào ngữ cảnh mà dữ  liệu sẽ được chèn vào, có thể liên quan đến sự kết hợp của mã thoát  JavaScript, mã hóa HTML và mã hóa URL, theo trình tự thích hợp.