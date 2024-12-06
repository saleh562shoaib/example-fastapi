# environment varaibale عليك الدخول اليه وتغير المسار 
# py -3 example.py و echo %MY_DB_URL% اكتبهم في التيرمينال

import os 

path = os.getenv("MY_DB_URL")
print(path)

# ###################################################

# قبل اضافة ال votes
# results

{
    "Post": {
        "content": "hello",
        "created_at": "2024-11-08T00:51:42.974812+03:00",
        "title": "something something beaches",
        "id": 22,
        "published": true,
        "owner_id": 10
    },
    "votes": 0
},

# بعد اضافة ال votes
# posts


{
    "title": "post1",
    "content": "sdfsdf",
    "published": true,
    "id": 3,
    "created_at": "2024-11-04T00:27:02.152238+03:00",
    "owner_id": 2,
    "owner": {
        "id": 2,
        "email": "candy@gnail.com",
        "created_at": "2024-10-18T01:00:32.321195+03:00"
    }
},
