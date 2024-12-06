# posts?limit=2&skip=1&search=something%20beaches 
#  prefix خاص باختصارات منها انها تختصر عليك عناء كتابة اسم الروت في كل خاصية
#  مثله سنقوم بدراسة مثل الذي قي الذي في غوغل محل كتابة اليو ار ال ال المسار مكان الذي تكتب ما تريد
# سنقوم بطباعة كل ما يتعلق باوامر  votes %
# حولنا results ل posts بعدها
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter 
from sqlalchemy.orm import Session 
from typing import List, Optional  
from sqlalchemy import func
from .. import models, schemas, oauth2
from ..database import  get_db

# +  /id  /posts/{id} يمكنك اضافة هذا ايضا مع الزائد
router = APIRouter(
    prefix="/posts", 
    tags=['Posts'] # يجعل الهذا الملف في مجموعته الخاصة في google fastapi
)

#(0)البداية
# @app.get("/")# هذه الصفحة: هذه هي البنية الاساسية للكود وهنا يوضع المسار
# async def root():بنية الصفحة 
#     return {"message":"Hello World"}اظهار مكونات البنية منسق

#(2) لتحديد المسار والاظهار
# @router.get("/")
# def root():
#     return {"message":"Hello World"}

# postCreate سنقوم بحذفه لان هناك بوست اسمه
# هذا فقط للتاكد اذا كان قواعد البينات تعمل
# (6) هذا مثل مثبت لقاعدة البينات وظهوره مباشرة في الوسيط بوست مان بدون الحاجة ل cursor.execute...
# @app.get("/sqlalchemy")
# def test_posts(db: Session = Depends(get_db)):
    # posts = db.query(models.Post).all() # 1 
    # posts = db.query(models.Post)
    # print(posts) #3
    # return {"status": "success"}1
    # return {"data": posts}
    # return {"data":"successfull"}

# $ current_user كان user_id
# (2)
# @router.get("/", response_model=List[schemas.Post])1#اذا كان المسار متشابه فانه يظهر الاول في الترتيب في الصفحات
@router.get("/", response_model=List[schemas.PostOut])#اذا كان المسار متشابه فانه يظهر الاول في الترتيب في الصفحات
# @router.get("/")2#اذا كان المسار متشابه فانه يظهر الاول في الترتيب في الصفحات
# def get_posts():1
# def get_posts(db: Session = Depends(get_db))1:
# def get_posts(db: Session = Depends(get_db), current_user: # $
# int = Depends(oauth2.get_current_user)):2
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""): # limit  خاص بتحديد الحد الاقصى لجبلب العناصر يوضع هكذا في اليوست posts?limit=5
    # posts = cursor.execute("""SELECT * FROM posts""")1
    # posts = cursor.fetchone() # 2 خاص بالجلب المعلومات اما واحد او بعض او الكل
    # print(posts)3
    # print(search)
    # posts = db.query(models.Post).all() #1
    # posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()2

    results = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    
    results = list(map(lambda x : x._mapping, results))
    # print(results)
    # posts = db.query(models.Post).filter(models.Post.owner_id == current_user.id).all()2
    # return {"data": "this is your posts"}1
    # return {"data": my_posts}2
    # return {"data": posts}1
    # return posts #2
    return  results

#(1)
# @app.post("/createposts")1
# @app.post("/posts", status_code=status.HTTP_201_CREATED)2
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
# def create_posts(payload: dict = Body(...)):1
# def create_posts(post: Post):1
# def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):# 1
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user:
int = Depends(oauth2.get_current_user)):# 3 # $
# def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), 
    # get_current_user: int = Depends(oauth2.get_current_user)):#2  خاص ب oauth2 
    # print(payload)1
    # print(new_post)2
    # print(new_post.title)3 # لجلب عنصر واحد
    # print(new_post.published)4 # لجلب عنصر واحد
    # print(new_post.rating)5 # لجلب عنصر واحد
    # print(post) #6 لجلب عنصر واحد
    # print(post.dict())6
    # post_dict = post.dict()7# متغير جديد نضع فيه الكلاس 
    # post_dict["id"] = randrange(0, 1000000)7
    # my_posts.append(post_dict)7
    # cursor.execute(f"INSERT INTO posts (title, content, published) VALUES ({post.title}, {post.content}, 
                        # {post.published}")# 1 يمكنك جعله كنص فقطمثل الطريقة السابقة في صناعة بوست
    # cursor.execute(""" INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""",
    #                 (post.title, post.content, post.published)) #
    # new_post  = cursor.fetchone()#
    # conn.commit()# # لحفظ التغيرات لتظهر في البوست مان التغيرات في البينات
    # print(**post.dict()) # هو سيظهر نفس النتيجة الكود الذي تحت بدل من الكود الذي تحت بنجمتين
    # new_post = models.Post(title=post.title, content=post.content, published=post.published)1
    # print(current_user.id) # $ هذا نقلناه تحت
    # print(current_user.email) # 1 $ 
    # new_post = models.Post(**post.dict())1
    new_post = models.Post(owner_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post) # لا تنسى عليك الحفظ التغيرات في كل مرة
    # return {"message: "succesfully created posts"}1
    # return {"new_post": f"title {payload['title']} content {payload['content']}"}# 2 لاظهار القاموس
    # return {"data": "new post"}# 3 بدل ان يكون مجرد نص سيصبح القاموس مكانه تحت
    # return {"data": post}4
    # return {"data": post_dict}5
    # return {"data": new_post}6
    return new_post

# هذا فقط للتاكد اذا كان حذف العنصر تعمل يعني تجربة
# # (4): تعيد احدث واخر صفحة مع اي دي ويجب ان يكون فوق الرقم (3)
# @app.get("/posts/latest")
# def get_latest_post():
#     post = my_posts[len(my_posts)-1]
#     return {"detail": post}

#(3) هنا سنقوم فيها بجعل الخطا يظهر اذا كان اي دي خاطئ
# @router.get("/{id}", response_model=schemas.Post)1
@router.get("/{id}", response_model=schemas.PostOut)
# def get_post(id: int):#1 يمكنك كتابة نوع البيانات تحت وظبعايختلف اظهار البينات بينهما
# def get_post(id: str):#2 يمكنك كتابة نوع البيانات تحت وظبعايختلف اظهار البينات بينهما
# def get_post(id: int, response: Response, ):#3 هذه الخاصية لاظهار الاخطاء مثل ال status 
# def get_post(id: int, db: Session = Depends(get_db)):#4 هذه الخاصية لاظهار الاخطاء مثل ال status 
def get_post(id: int, db: Session = Depends(get_db), current_user:
int = Depends(oauth2.get_current_user)):#5  # $
    # print(id)1
    # print(type(id))2
    # post = find_post(int(id))3
    # cursor.execute("""SELECT * FROM posts WHERE id = %s """, (str(id)))4
    # test_post = cursor.fetchone()1
    # post = cursor.fetchone()2
    # post = db.query(models.Post).filter(models.Post.id == id).first()

    post =  db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()

    # print(post)
    # print(test_post)1
    # post = find_post(id)1
    # print(post)1
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} was not found")
    
    # if post.owner_id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=
    #     "Not authorzed to perform requested action")

        # response.status_code = 404 # 1
        # response.status_code = status.HTTP_404_NOT_FOUND # 2 نفس الشئ التي فوق لتعرف نوع اتش تي تي بي الذي لديك
        # return {'massage': f"post with id {id} was not found"}2
    # return {"post_detail": f"Here is post {id}"}1
    # return {"post_detail": post}1
    return  post

# (4) خاص لحذف العنصر
# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)1
@router.delete("/{id}")
# def delete_post(id: int,  db: Session = Depends(get_db))1:
def delete_post(id: int,  db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):# $
    # deleteing post
    # find the index in the array that has required ID
    # my_posts.pop(index)
    # cursor.execute("""DELETE FROM posts WHERE id = %s returning * """, (str(id),))#1
    # deleted_post = cursor.fetchone()#2
    # conn.commit()#3
    deleted_post =  db.query(models.Post).filter(models.Post.id == id)

    post = deleted_post.first()
    # index = find_index_post(id)

    # if index == None:1
    # if deleted_post.first() == None:1
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with id: {id} dose not exist")

    if post.owner_id != current_user.id: # الخاصية الجديد مع بوست
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=
        "Not authorzed to perform requested action")

    deleted_post.delete(synchronize_session=False)
    db.commit()

    # my_posts.pop(index)1 # pop وظيفته هو حذف العنصر وارجاعه
    # return {'message': 'post was seccesfully deleted'}1
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# (5) خاص بتغير العنصر وتبديله
# @app.put("/posts/{id}")1
@router.put("/{id}", response_model=schemas.Post)
# def update_post(id: int, post: Post, db: Session = Depends(get_db)):1
# def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db))2:
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db), current_user:# $
int = Depends(oauth2.get_current_user)):
    # print(id)1
    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s  WHERE id = %s
    #  RETURNING * """, (post.title, post.content, post.published, str(id)))#1
    # updated_post = cursor.fetchone()#2
    # conn.commit()#3
    post_query =  db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    # index = find_index_post(id)1
    # if index == None:1
    # if updated_post == None:1
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with id: {id} dose not exist")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=
        "Not authorzed to perform requested action") 
    
    # post_query.update({'title': 'hey this is my updated title', 'content': 'hey this is my updated content'},
    # synchronize_session=False)1
    
    post_query.update(updated_post.dict(), synchronize_session=False) # هو نقسه الذي فوق

    db.commit()

    # post_dict = post.dict() #
    # post_dict['id'] = id #
    # my_posts[index] = post_dict #
    # return {'message': 'updated post'}1
    # return {'data': post_dict}2
    # return {'data': updated_post}3
    # return {'data': 'succesful'}4
    # return {'data': post_query.first()}5
    return  post_query.first()