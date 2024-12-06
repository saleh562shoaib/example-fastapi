# خاص بتسهيل الاتصال بقاعدة البينات و بوست بحيث لا تحتاج الى الدخول والتعديل في الكود البرمجي
# (6) خاص بقاعدة بيانات الاستعلام 
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

# SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip_address/hostname>/<database_name>'
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Admin@localhost:5432/fastapi'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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