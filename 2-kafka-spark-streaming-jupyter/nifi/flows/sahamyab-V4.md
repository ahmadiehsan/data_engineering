 ### Processor 11

 - **name** : ReplaceDoubleQutesInHashtagList

 - **pre**  : Processor 9
   - ***relation*** :  Success

 - **type** :  ReplaceText

 - ***properties*** :
   -  "Search Value": "`\\\"`"
   -  "Replacement Value": "`'`'"

  - ***settings***
    - **Automatically Terminate Relationships** : ALL



 ### Processor 12

 - **name** : ConvertHashtagStringToList
 - **pre**  : Processor 11       
   - ***relation*** :  Success
 - **type** :  ReplaceText  
 - ***properties*** :
   -  "Search Value": " `\"Hashtags\"\:\s*\"\[.*\]\"` "
   -  "Replacement Value": "`"Hashtags":${Hashtags}` "   
  - ***settings***
    - **Automatically Terminate Relationships** : ALL





 ### Processor 13

 - **name** : SaveToElasticsearch

 - **pre**  : Processor 12

   - ***relation*** :  Success

 - **type** :  PutElasticsearchHttp

 - ***properties*** :

              "Identifier Attribute": "postId",
               "type": "_doc",
               "index": "sahamyab",
               "**Elasticsearch URL**": "http://elasticsearch:9200",

  - ***settings***

    - **Automatically Terminate Relationships** : ALL