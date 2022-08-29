## SSRF via OpenID dynamic client registration

> This lab allows client applications to dynamically register themselves with the [OAuth](https://portswigger.net/web-security/oauth) service via a dedicated registration endpoint. Some client-specific  data is used in an unsafe way by the OAuth service, which exposes a  potential vector for SSRF.        
>
> To solve the lab, craft an [SSRF attack](https://portswigger.net/web-security/ssrf) to access `http://169.254.169.254/latest/meta-data/iam/security-credentials/admin/` and steal the secret access key for the OAuth provider's cloud environment.        
>
> You can log in to your own account using the following credentials: `wiener:peter`        







![image](https://user-images.githubusercontent.com/68894302/187126609-288b1576-ec41-41a2-92d4-2312a21d58c5.png)



![image](https://user-images.githubusercontent.com/68894302/187127926-a38d7f6d-9632-43d6-bb94-285bbd26a0a7.png)



![image](https://user-images.githubusercontent.com/68894302/187126609-288b1576-ec41-41a2-92d4-2312a21d58c5.png)

![image](https://user-images.githubusercontent.com/68894302/187127926-a38d7f6d-9632-43d6-bb94-285bbd26a0a7.png)

![image](https://user-images.githubusercontent.com/68894302/187127997-43786a96-69f3-4071-b6f8-40dbb5dfbabc.png)

![image](https://user-images.githubusercontent.com/68894302/187128014-2cb7b0cd-cec8-4da3-b682-a7eef67884fa.png)

![image](https://user-images.githubusercontent.com/68894302/187128108-469b48e3-18c3-4388-a044-20c7b6589d18.png)

![image](https://user-images.githubusercontent.com/68894302/187128214-4ce66f90-d5af-4c1e-bb3e-a815e21a6a26.png)

![image](https://user-images.githubusercontent.com/68894302/187128517-ba48916d-0df8-42c6-b3ce-286524bb6ee4.png)

![image](https://user-images.githubusercontent.com/68894302/187128588-41b4fbf5-7fcc-4ca5-9455-6008388bbc37.png)

![image](https://user-images.githubusercontent.com/68894302/187128617-189119bb-341f-4193-9000-4cfd0749b3a5.png)



