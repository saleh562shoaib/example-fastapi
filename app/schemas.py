# وظيفة هذا الملف انه يقوم بأختيار صحة البينات وتعريف النماذج وقابلية الصيانة
# هنا يتبع اسلوب التوريث
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True    

class PostCreate(PostBase):
    pass


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        from_attributes = True


# class Post(BaseModel):
class Post(PostBase):
    id: int
    # title: str
    # content: str
    # published: bool
    created_at: datetime
    owner_id: int
    owner: UserOut # هذا الكلاس الذي تحت عليك وضعه فوق حتى يتعدى الخطأ هاذا خاص بدمج كل الخواص في مخرج واحد

    class Config:
        from_attributes = True

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

# class UserOut(BaseModel):
#     id: int
#     email: EmailStr
#     created_at: datetime
#     class Config:
#         from_attributes = True

class UserLogen(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel): # [@]
    access_token: str
    token_type: str

class TokenData(BaseModel): # [@]
    id: Optional[int] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1) # هذا خاص بجلب عدد الاعمدة او الصفوف الذي تحدد له
    

# class PostUpdate(PostBase):


# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True

# class CreatePost(BaseModel):
#     title: str
#     content: str
#     published: bool = True 


# class UpdatePost(BaseModel):
#     published: bool 

