## Basic password reset poisoning

Login with account credentials: `wiener:peter`. We see there is a function to change the password. 

If we change the Host header to URL of Burp collab, we see that there are requests sent to it.

Ok from this we can infer Host header to be our exploit server. Now change username 

![image](https://user-images.githubusercontent.com/68894302/181941194-26e205a9-cb00-4bce-80aa-5075e66139c3.png)

Check log in exploit server __/log__

![image](https://user-images.githubusercontent.com/68894302/181942305-c6bb92e7-b85d-4132-b440-2e8af1d73fd4.png)

IP 10.0.4.184 can be accessed from internal server. In order to change the user password, we need the password token. It's pretty easy to change the **`carlos`** user's password

![image](https://user-images.githubusercontent.com/68894302/181944567-51e7e83c-af66-41f2-aece-078cf9aae6e4.png)

Status **`302 Found`** redirect  status response code indicates that the resource requested has been temporarily moved to  the URL given by the [`Location`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Location) header.

We can login with `account:carlos`  and `password:123`

![image](https://user-images.githubusercontent.com/68894302/181946399-b1040043-3524-45d8-b15a-bf6ef6106ddc.png)

So this challenge has been solved. I'm trying to write some problems I can solve in English, sorry for my poor Engrisk.

