

# Reflected XSS protected by very strict CSP, with dangling markup attack

>  Mức độ: Expert

Mô tả:

> This lab using a strict [CSP](https://portswigger.net/web-security/cross-site-scripting/content-security-policy) that blocks outgoing requests to external web sites.        
>
> To solve the lab, first perform a [cross-site scripting](https://portswigger.net/web-security/cross-site-scripting) attack that bypasses the CSP and exfiltrates a simulated victim user's [CSRF token](https://portswigger.net/web-security/csrf/tokens) using Burp Collaborator. You then need to change the simulated user's email address to `hacker@evil-user.net`. 	
>
> You must label your vector with the word "Click" in order to induce the simulated user to click it. For example: 	
>
> You can log in to your own account using the following credentials: `wiener:peter` 	

1.Step by step

