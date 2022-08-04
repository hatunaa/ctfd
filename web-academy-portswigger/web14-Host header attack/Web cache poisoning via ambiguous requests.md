## Web cache poisoning via ambiguous requests

The header **`X-Cache`** in the response could be very useful as it may have the value __miss__ when the request wasn't cached and the value __hit__ when it is cached

<<<<<<< HEAD
![image-20220731024714976](https://user-images.githubusercontent.com/68894302/182420347-02bf60f2-977b-4408-a2e3-c1e8b49813f2.png)
=======
![image-20220731024714976](https://user-images.githubusercontent.com/68894302/182009970-d525312c-cfb2-4e4f-ae2a-d3a9866b4d99.png)
>>>>>>> 12d207656df7fdf0d4d97bfc655e2e4018ad45d3

Unable to change Host header

![image](https://user-images.githubusercontent.com/68894302/181980667-d87a933f-70ed-4c5d-8e0a-5ef3a01168dd.png)

Using header X-Forwarded-Host to poison cache but it doesn't seem to work.

![image](https://user-images.githubusercontent.com/68894302/181989478-c058df8b-f684-4f4a-9f72-bd5199d0b887.png)

Add a second Host header and send the request and we see that host reflected in the cache along with endpoint **`resources/js/tracking.js`**

![image](https://user-images.githubusercontent.com/68894302/181994457-0d970d69-5fe1-4632-ad2e-64f6abf12a4a.png)

Change the second Host header to the exploit server address and the endpoint to __/resources/js/tracking.js __ 

![image](https://user-images.githubusercontent.com/68894302/181994492-00b4b32d-5e38-4056-a83b-b9d854781a71.png)

After change

![image](https://user-images.githubusercontent.com/68894302/181995256-cb0a8176-44d4-4542-b000-8d34c2465ec6.png)

The exploit server has been cached

![image](https://user-images.githubusercontent.com/68894302/181994662-38354d37-818a-4f15-b5fb-81579688b471.png)

send requests until it's cached, then reload home page

![image](https://user-images.githubusercontent.com/68894302/181995477-fc106cbc-4e71-4d1f-a40c-025f60d624b2.png)
