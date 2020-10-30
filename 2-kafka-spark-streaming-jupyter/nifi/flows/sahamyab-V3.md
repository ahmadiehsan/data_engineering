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

 - **name** : 'Extract Hashtags'

 - **pre**  : Processor 4
   - ***relation*** :  Success

 - **type** :  ExtractText

 - ***properties*** :

   -  "Hashtags": "`#(.*?)[\s\\n#\\"]`",
   -  "extract-text-enable-repeating-capture-group": "true"

  - ***settings***
    - **Automatically Terminate Relationships** : ALL



 ### Processor 6

 - **name** : CombineHashtagsToOneJsonField

 - **pre**  : Processor 5
   - ***relation*** :  Matched,UnMatched

 - **type** :  AttributesToJSON

 - ***properties*** :

   -  "attributes-to-json-regex": "`Hashtags[\.][1-9]`",

  - ***settings***
    - **Automatically Terminate Relationships** : ALL



 ### Processor 7

 - **name** : ConvertHashtagsToList
 - **pre**  : Processor 6
   - ***relation*** :  Success
 - **type** :  UpdateAttribute
 - ***properties*** :

   -  "Hashtags": "`${JSONAttributes:replaceAll('\"Hashtag.[1-9]\":',''):replace('{', '['):replace('}', ']')}`",
  - ***settings***
    - **Automatically Terminate Relationships** : ALL



 ### Processor 8

 - **name** : RemoveExtraNamesFromHashtagList
 - **pre**  : Processor 7
   - ***relation*** :  Success
 - **type** :  UpdateAttribute
 - ***properties*** :

   -  "Delete Attributes Expression": "JSONAttributes|Hashtags.[1-9]?"
   -   "Hashtags": "${Hashtags:replaceAll('\"Hashtags.[1-9]\":',''):replace('{', '['):replace('}', ']')}"
  - ***settings***
    - **Automatically Terminate Relationships** : ALL









 ### Processor 9

 - **name** : SetFinalJson

 - **pre**  : Processor 8
   - ***relation*** :  Success

 - **type** :  AttributesToJSON

 - ***properties*** :

   -  "Attributes List": "postId,sendTimePersian,senderUsername, sendTime, senderName,type,content,Hashtags"
   -  "Destination": "flowfile-content"

  - ***settings***
    - **Automatically Terminate Relationships** : ALL



 ### Processor 10

 - **name** : SaveTweetFile

 - **pre**  : Processor 9
   - ***relation*** :  Success

 - **type** :  PutFile

 - ***properties*** :
   - "Directory" : "/home/nifi/workspace/tweets"
   -  "Conflict Resolution Strategy" : "replace"

  - ***settings***
    - **Automatically Terminate Relationships** : ALL

