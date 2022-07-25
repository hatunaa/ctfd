## Web cache poisoning with an unkeyed cookie

1. Phản hồi yêu cầu được cache trong header Set-Cookie như sau:

   ![image](https://user-images.githubusercontent.com/68894302/180500046-4e7e04e3-6ca4-4093-b40e-c9904cbf75d7.png)

2.  Xác định điểm có thể nhiễm độc cache tại vị trí fehost, từ đây có thể dễ dàng escape ra khỏi json data

   ![image-20220723012059351](C:/Users/tuandv/AppData/Roaming/Typora/typora-user-images/image-20220723012059351.png)

3. Thực thi javascript, hàm alert popup lên là giải quyết challenge

   ![image](https://user-images.githubusercontent.com/68894302/180500629-0bea8357-cf6d-440b-9e5f-737162e91d6b.png)