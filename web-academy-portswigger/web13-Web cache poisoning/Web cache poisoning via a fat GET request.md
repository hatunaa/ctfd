# Web cache poisoning via a fat GET request

Trong response thì có đoạn js call đến __setCountryCookie __ 

![image](https://user-images.githubusercontent.com/68894302/181214157-bfe41486-7ae8-4584-85eb-6e7d9d39572e.png)

Khi thêm một param callback với giá trị khác thì giá trị của nó đã ghi đè lên giá trị ban đầu

![image](https://user-images.githubusercontent.com/68894302/181214949-402f163a-ddb4-49d5-9bd5-159cd9a57b33.png)

Thêm tham số vào body của request và send cho đến khi nó được lưu vào cache

![image](https://user-images.githubusercontent.com/68894302/181215236-733e7f1e-3cd7-4d97-b552-eb2213f0c32c.png)

Clear challenge 

![image](https://user-images.githubusercontent.com/68894302/181215360-12bc855f-7c34-447f-9ccf-3dad9c634826.png)