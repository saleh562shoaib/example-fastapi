# fast api يمكنك التعلم من قوقل اكتب
# HTTP request methods تصفحه
# pydantic تصفحه 
# pydantic خاص بالتحقق من البيانات
# http://127.0.0.1:8000/docs اكتبه في google لترى مشروعك
# postgresSQL . pgAdmin عليك معرفتهم
# postgres data typs ابحث فيه
# bigint vs int عليك معرفة الفرق بينهم
# Psycopg documentation تصفحه
# print() تذكر هذا خاص بالطباعة هنا
# sql alchemy تصفحه
# RETURNING * يرجع لك القيمة في بوستغريس
# db: Session = Depends(get_db) لاستحضار البينات
# db.query(models.Post).all() لاستحضار ملف الاكواد
# response_model=schemas.Post هو استيراد لملف الاسكيمة
# مع ال db انسى اي دي الذي هنا
# pip install passlib[bcrypt] تصفحه ونزله 
# posts and users تم تقل كل واحد فيهم الى ملفه الخاص
# http://127.0.0.1:8000 هو نفسه {{URL}} في postman في البيئة الافتراضية
# لارسال ريكويست الخاص بي في براوسر الخاص بي fetch('http://localhost:8000/').then(res => res.josn()).then(console.log) الى السيرفر
# حمل  git وادخل لل github ثم اكتب الذي تحت على حدى
# -----------------------------------------------------
# اكتب هذا في terminal
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/saleh562shoaib/example-fastapi.git
# git push -u origin main
# -----------------------------------------------------------

# render ابحث عنه وحمله و اعرف كل شئ عنه لكي تحمل طبيقك على السيرفير وبعدها تعلم  ونشرهheroku
# ولا تحميل ملفين . nginx , gunicorn.server

# vw ubuntu عليك تعلمه لاحقا ومعرفة كل شئ عنه 


# from fastapi import FastAPI #, Response, status, HTTPException,Depends 
# from fastapi.params import Body  
# from pydantic import BaseModel
# from passlib.context import CryptContext # انقلهم لملف خاص بهم 
# from typing import Optional, List  
# from random import randrange
# from app import main
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time
# from sqlalchemy.orm import Session 
# from sqlalchemy.sql.functions import mode
# from . import models #, schemas, utils
# from .database import engine #, get_db
# from .routers import post, user, auth


# (7)
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # انقلهم لملف خاص بهم 
 # (6)
# models.Base.metadata.create_all(bind=engine)

# app = FastAPI()

# خاصة بادخال المعلومات
# ستستبدله ب PostCreate
#(1) لصناعة بوست جديد
# Body هو مثل لكن يكتب هنا
# يقبل انواع البيانات
# حتى لو حذف هناك سيظهر هنا
# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True
    # rating: Optional[int] = None 

# (6) قواعد البينات
# سيتم نقله الى ملف database في الاخير
# while True:

#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='Admin',
#         cursor_factory=RealDictCursor)# لتشغيل البينات
#         cursor = conn.cursor()
#         print("Database connection was succesfully!")
#         break
#     except Exception as error:
#         print("connecting to database faild")
#         print("Error: ", error)
#         time.sleep(2)

# (3) لتحديد الصفحة الذي تريد لااي دي
# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1 }, {"title": 
# "favorite foode", "content": "I  like pizza" , "id": 2}]


#(3)
# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p
        
# # (4)
# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i

# posts 1
# app.include_router(post.router) # خاص بجلب احد الملفين

# users 2
# app.include_router(user.router) # خاص بجلب احد الملفين

# auth 
# app.include_router(auth.router) 

##################################################################


# posts 1

#(0)البداية
# @app.get("/")# هذه الصفحة: هذه هي البنية الاساسية للكود وهنا يوضع المسار
# async def root():بنية الصفحة 
#     return {"message":"Hello World"}اظهار مكونات البنية منسق

# #(2) لتحديد المسار والاظهار
# @app.get("/")
# def root():
    # return {"message":"Hello World"}

# # postCreate سنقوم بحذفه لان هناك بوست اسمه
# # هذا فقط للتاكد اذا كان قواعد البينات تعمل
# # (6) هذا مثل مثبت لقاعدة البينات وظهوره مباشرة في الوسيط بوست مان بدون الحاجة ل cursor.execute...
# # @app.get("/sqlalchemy")
# # def test_posts(db: Session = Depends(get_db)):
#     # posts = db.query(models.Post).all() # 1 
#     # posts = db.query(models.Post)
#     # print(posts) #3
#     # return {"status": "success"}1
#     # return {"data": posts}
#     # return {"data":"successfull"}


# # (2)
# @app.get("/posts", response_model=List[schemas.Post])#اذا كان المسار متشابه فانه يظهر الاول في الترتيب في الصفحات
# # def get_posts():1
# def get_posts(db: Session = Depends(get_db)):
#     # posts = cursor.execute("""SELECT * FROM posts""")1
#     # posts = cursor.fetchone() # 2 خاص بالجلب المعلومات اما واحد او بعض او الكل
#     # print(posts)3
#     posts = db.query(models.Post).all()
#     # return {"data": "this is your posts"}1
#     # return {"data": my_posts}2
#     # return {"data": posts}1
#     return posts

# #(1)
# # @app.post("/createposts")1
# # @app.post("/posts", status_code=status.HTTP_201_CREATED)2
# @app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
# # def create_posts(payload: dict = Body(...)):1
# # def create_posts(post: Post):1
# def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
#     # print(payload)1
#     # print(new_post)2
#     # print(new_post.title)3 # لجلب عنصر واحد
#     # print(new_post.published)4 # لجلب عنصر واحد
#     # print(new_post.rating)5 # لجلب عنصر واحد
#     # print(post) #6 لجلب عنصر واحد
#     # print(post.dict())6
#     # post_dict = post.dict()7# متغير جديد نضع فيه الكلاس 
#     # post_dict["id"] = randrange(0, 1000000)7
#     # my_posts.append(post_dict)7
#     # cursor.execute(f"INSERT INTO posts (title, content, published) VALUES ({post.title}, {post.content}, 
#                         # {post.published}")# 1 يمكنك جعله كنص فقطمثل الطريقة السابقة في صناعة بوست
#     # cursor.execute(""" INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""",
#     #                 (post.title, post.content, post.published)) #
#     # new_post  = cursor.fetchone()#
#     # conn.commit()# # لحفظ التغيرات لتظهر في البوست مان التغيرات في البينات
#     # print(**post.dict()) # هو سيظهر نفس النتيجة الكود الذي تحت بدل من الكود الذي تحت بنجمتين
#     # new_post = models.Post(title=post.title, content=post.content, published=post.published)1
#     new_post = models.Post(**post.dict())
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post) # لا تنسى عليك الحفظ التغيرات في كل مرة
#     # return {"message: "succesfully created posts"}1
#     # return {"new_post": f"title {payload['title']} content {payload['content']}"}# 2 لاظهار القاموس
#     # return {"data": "new post"}# 3 بدل ان يكون مجرد نص سيصبح القاموس مكانه تحت
#     # return {"data": post}4
#     # return {"data": post_dict}5
#     # return {"data": new_post}6
#     return new_post

# # هذا فقط للتاكد اذا كان حذف العنصر تعمل يعني تجربة
# # # (4): تعيد احدث واخر صفحة مع اي دي ويجب ان يكون فوق الرقم (3)
# # @app.get("/posts/latest")
# # def get_latest_post():
# #     post = my_posts[len(my_posts)-1]
# #     return {"detail": post}

# #(3) هنا سنقوم فيها بجعل الخطا يظهر اذا كان اي دي خاطئ
# @app.get("/posts/{id}", response_model=schemas.Post)
# # def get_post(id: int):#1 يمكنك كتابة نوع البيانات تحت وظبعايختلف اظهار البينات بينهما
# # def get_post(id: str):#2 يمكنك كتابة نوع البيانات تحت وظبعايختلف اظهار البينات بينهما
# # def get_post(id: int, response: Response, ):#3 هذه الخاصية لاظهار الاخطاء مثل ال status 
# def get_post(id: int, db: Session = Depends(get_db)):#4 هذه الخاصية لاظهار الاخطاء مثل ال status 
#     # print(id)1
#     # print(type(id))2
#     # post = find_post(int(id))3
#     # cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id)))4
#     # test_post = cursor.fetchone()1
#     # post = cursor.fetchone()2
#     post = db.query(models.Post).filter(models.Post.id == id).first()
#     # print(post)
#     # print(test_post)1
#     # post = find_post(id)1
#     # print(post)1
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} was not found")
#         # response.status_code = 404 # 1
#         # response.status_code = status.HTTP_404_NOT_FOUND # 2 نفس الشئ التي فوق لتعرف نوع اتش تي تي بي الذي لديك
#         # return {'massage': f"post with id {id} was not found"}2
#     # return {"post_detail": f"Here is post {id}"}1
#     # return {"post_detail": post}1
#     return  post

# # (4) خاص لحذف العنصر
# # @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)1
# @app.delete("/posts/{id}")
# def delete_post(id: int,  db: Session = Depends(get_db)):
#     # deleteing post
#     # find the index in the array that has required ID
#     # my_posts.pop(index)
#     # cursor.execute("""DELETE FROM posts WHERE id = %s returning * """, (str(id),))#1
#     # deleted_post = cursor.fetchone()#2
#     # conn.commit()#3
#     deleted_post =  db.query(models.Post).filter(models.Post.id == id)
#     # index = find_index_post(id)

#     # if index == None:1
#     if deleted_post.first() == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with id: {id} dose not exist")

#     deleted_post.delete(synchronize_session=False)
#     db.commit()

#     # my_posts.pop(index)1 # pop وظيفته هو حذف العنصر وارجاعه
#     # return {'message': 'post was seccesfully deleted'}1
#     return Response(status_code=status.HTTP_204_NO_CONTENT)

# # (5) خاص بتغير العنصر وتبديله
# # @app.put("/posts/{id}")1
# @app.put("/posts/{id}", response_model=schemas.Post)
# # def update_post(id: int, post: Post, db: Session = Depends(get_db)):1
# def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db)):
#     # print(id)1
#     # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s  WHERE id = %s
#     #  RETURNING * """, (post.title, post.content, post.published, str(id)))#1
#     # updated_post = cursor.fetchone()#2
#     # conn.commit()#3
#     post_query =  db.query(models.Post).filter(models.Post.id == id)
#     post = post_query.first()
#     # index = find_index_post(id)1
#     # if index == None:1
#     # if updated_post == None:1
#     if post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with id: {id} dose not exist")
    
#     # post_query.update({'title': 'hey this is my updated title', 'content': 'hey this is my updated content'},
#     # synchronize_session=False)1
    
#     post_query.update(updated_post.dict(), synchronize_session=False) # هو نقسه الذي فوق

#     db.commit()

#     # post_dict = post.dict() #
#     # post_dict['id'] = id #
#     # my_posts[index] = post_dict #
#     # return {'message': 'updated post'}1
#     # return {'data': post_dict}2
#     # return {'data': updated_post}3
#     # return {'data': 'succesful'}4
#     # return {'data': post_query.first()}5
#     return  post_query.first()

############################################################################

# users 2


# (7) عبارة عن جدول جديد صفحة جديدة كل شئ جديد غير جدول البوستس
# @app.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
# def create_user(user:schemas.UserCreate, db: Session = Depends(get_db)):

#     #hash the password - user.password
#     # hashed_password = pwd_context.hash(user.password) # خاص بجعل كلمة المرور مشفرة
#     hashed_password = utils.hash(user.password) #نفس الذي فوق 
#     user.password = hashed_password
#     new_user = models.User(**user.dict())
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     return new_user

# @app.get('/users/{id}',  response_model=schemas.UserOut)
# def get_user(id: int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} dose not exist")
    
#     return user

###################################################################
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import main
from . import models
from .database import engine 
from .routers import post, user, auth, vote
from .config import settings

# سنقوم بنقله الى ملف config.py
# from pydantic_settings import BaseSettings

# class Settings(BaseSettings):
#     # database_password: str = "localhost"
#     # database_password: str 
#     path: int
#     database_username: str = "postgres"
#     secret_key: str = "122uhouedh9e8yfh3o"

# settings = Settings()

print(settings.database_username)

# models.Base.metadata.create_all(bind=engine) # يتم حذفه بعد وضع alembic

app = FastAPI()

# origins = ["https://www.google.com", "https://www.youtube.com"] # هذا الذي تحت مع هذا خاص بارسال الاي بي اي خاص يك للسرفير
origins = ["*"] # كل سيرفرات

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# posts 1
app.include_router(post.router) # خاص بجلب احد الملفين

# users 2
app.include_router(user.router) # خاص بجلب احد الملفين

# auth 
app.include_router(auth.router)

# vote 
app.include_router(vote.router) 


@app.get("/")
def root():
    return {"message":"Hello World"}



    # return {"message":"Hello World!"} # في درس ال test_users.py يجب ان يكون الكود قبل اضافته  ان يكون على الشكل الذي تريده 








