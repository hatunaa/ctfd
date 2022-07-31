## Routing-based SSRF

Change the value of the Host header to localhost to see if we can access the local resource

![image](https://user-images.githubusercontent.com/68894302/182006665-708b8995-5471-4ddf-90c5-5e65c9af6f49.png)

The error may have been caused by `localhost` being blacklist. The most common internal IP address is 192.168.0.x  we see whatever they've setup machines on their network to see.

![image](https://user-images.githubusercontent.com/68894302/182006923-e154cd80-1b60-45fd-8b05-fc8de2c60a5f.png)

Brute-force to find exactly 4th octet 

![image](https://user-images.githubusercontent.com/68894302/182007021-e960eb1f-6723-4db7-8eae-fba2b99f3334.png)

Access the intranet with the address 192.168.0.67 forward to the path /admin

![image](https://user-images.githubusercontent.com/68894302/182007042-66c5bf6d-ebc9-4881-a91f-5a0872c03e72.png)

We can now access the admin panel without access control. 

![image](https://user-images.githubusercontent.com/68894302/182007316-f3fd2c06-eb27-4a1c-bf64-24f45c21e0da.png)

Show response in browser and delete user panel appears.

![image](https://user-images.githubusercontent.com/68894302/182007485-e083a795-31ee-4993-a000-ecaa3c2078e9.png)

User carlos has been deleted

![image](https://user-images.githubusercontent.com/68894302/182007442-93668c0e-a869-4c3b-a5ed-0e0c449db376.png)



![image](https://user-images.githubusercontent.com/68894302/182007524-f7a52096-0ec6-49a5-85a7-c80dc806c9ff.png)