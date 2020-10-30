### Processor 1

- **name** : GetTweets

- **pre**  : -

- **type** :  InvokeHttp

- ***properties*** :

  - **Remote URL** : https://www.sahamyab.com/guest/twiter/list?v=0.1

 - ***settings***

    - **Automatically Terminate Relationships** : ALL
    
- ***scheduling***
  
  - **Run Schedule ** : 60 sec
  
  
  
### Processor 2

 - **name** : SplitTweets
   
 - **pre**  : Processor 1
   
   - ***relation*** :  Response
   
 - **type** :  SplitJson

 - ***properties*** :
   
   - **JsonPath Expression** : $.items[*]
   
  - ***settings***

    - **Automatically Terminate Relationships** : ALL
    
     
    



 ### Processor 3

 - **name** : ExtractAttributes

 - **pre**  : Processor 2
- ***relation*** :  Split
   
 - **type** :  EvaluateJsonPath

 - ***properties*** :

   - "Destination": "flowfile-attribute"
   - "senderName": "$.senderName"
   - "sendTimePersian": "$.sendTimePersian"
   - "postId": "$.id"
   - "type": "$.type"
   - "content": "$.content"
   - "senderUsername": "$.senderUsername"
   -  "sendTime": "$.sendTime"

  - ***settings***

    - **Automatically Terminate Relationships** : ALL




 ### Processor 4

 - **name** : UpdateTweetFileName

 - **pre**  : Processor 3
   - ***relation*** :  Matched

 - **type** :  UpdateAttribute

 - ***properties*** :

   -  "filename": "${postId:append('.json')}"

  - ***settings***

    - **Automatically Terminate Relationships** : ALL





 ### Processor 5

 - **name** : SetFinalJson

 - **pre**  : Processor 4
   - ***relation*** :  Success

 - **type** :  AttributesToJSON

 - ***properties*** :

   -  "Attributes List": "postId,sendTimePersian,senderUsername, sendTime, senderName,type,content"
   -  "Destination": "flowfile-content"

  - ***settings***
    - **Automatically Terminate Relationships** : ALL



 ### Processor 6

 - **name** : SaveTweetFile

 - **pre**  : Processor 5
   - ***relation*** :  Success

 - **type** :  PutFile

 - ***properties*** :
   - "Directory" : "/home/nifi/workspace/tweets"
   -  "Conflict Resolution Strategy" : "replace"

  - ***settings***
    - **Automatically Terminate Relationships** : ALL