# يمثل هيكل قاعدة البينات
# db.query لا تنسى عليك الحفظ التغيرات في كل مرة
# (6) هنا وكانك تصنع جدولك مثل الذي في بوستغريس
# حتى لو حذف الجدول في بوست غريس  اذا قمت بحفظ هذا ب فيمكنك اعادة الجدول من جدبد ب التحديث ctrl + s
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey 
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base


class Post(Base):
    __tablename__= "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE', default=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False) # user_id سنقوم بنقس حركته لكن هنا

    owner = relationship("User") # هذا الكود يضع يوزر وكل خصائصه هنا


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)# ملاحظة لا يمكنك وضع نفس الايميل
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                         nullable=False, server_default=text('now()'))
    # phone_number = Column(String) # لن يظهر في فواهد البينات ابحث اكثر عن هذا
    


class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True, )
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True, )