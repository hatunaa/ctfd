+ Check achievable values through query:

  `{__schema{types{name,fields{name}}}}`

  ![image](https://user-images.githubusercontent.com/68894302/181878694-d4af19dd-1e7a-4d83-ace1-0d2d1a4cc54e.png)

+ Create comments through mutation and flag can be extracted

  `{"query":"mutation{createComment(userId:1,nudeId:1,postId:1,comment:\"testing1337\"){nude{id,flag}}}"}`

  ![image](https://user-images.githubusercontent.com/68894302/181878643-e09f40fa-da94-4e47-87ae-3e8b1f31ddc1.png)

+ However, maybe `nudeId` is not suitable. Let's change the value for it to `nudeId=2` and bùmmm:

  ![image](https://user-images.githubusercontent.com/68894302/181879061-1b8c5073-0d72-424f-aa9a-be8038e391bc.png)

  

  