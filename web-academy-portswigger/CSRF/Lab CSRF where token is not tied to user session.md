# Lab: CSRF where token is not tied to user session

**Mức độ:** *PRACTITIONER*

---

**Mô tả**

This lab's email change functionality is vulnerable to CSRF. It uses tokens to try to prevent CSRF attacks, but they aren't  integrated into the site's session handling system.        

To solve the lab, use your exploit server to host an HTML page that uses a [CSRF attack](https://portswigger.net/web-security/csrf) to change the viewer's email address.        

You have two accounts on the application that you can use to help design your attack. The credentials are as follows:        

-  `wiener:peter`            
- `carlos:montoya`            

---

**Các bước**





