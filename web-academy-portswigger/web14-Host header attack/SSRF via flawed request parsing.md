## SSRF via flawed request parsing

Change Host header to 192.168.0.x. After brute-force we get the IP address 192.168.0.82

![image](https://user-images.githubusercontent.com/68894302/182009357-7dc6e341-8fdb-466e-badd-e90d77cb78ca.png)

Replace `GET /` to `GET myID.web-security-academy.net/`   and we have successfully accessed the internal resource.

![image](https://user-images.githubusercontent.com/68894302/182009387-1e9689be-fa01-44e6-8369-5e51542fdb7d.png)

To delete user we need csrf token and username

![image](https://user-images.githubusercontent.com/68894302/182009393-f7caae2b-816b-42d4-82b7-87b7bab977e7.png)

Change method to POST, our body data will consist of csrf and username.

![image](https://user-images.githubusercontent.com/68894302/182009428-b471943a-9dd8-418c-82b0-5984bfa5d0dc.png)

Status 302 redirect shows that user carlos has been successfully deleted. Completed challenge

![image](https://user-images.githubusercontent.com/68894302/182009518-af756a4d-0127-47a5-b7f3-34b502e68966.png)