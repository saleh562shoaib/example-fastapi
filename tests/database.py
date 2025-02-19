#  وظيفة هذا الملف هو اختبار نقاط النهاية
# pytest -v -s tests\test_users.py
# pytest --disable-warnings -v tests\test_users.py -s
# scope ابحث عنه
# الترتيب مهم اي الدوال
from fastapi.testclient import TestClient
import pytest 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.main import app
# from app import schemas
from app.config import settings
from app.database import get_db
from app.database import Base
from alembic import command
#  --------------------------------------------------
#  جزء من اكواد الخاصة بملف ال database.py
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Admin@localhost:5432/fastapi_test'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# بديله هو opps!
# Base.metadata.create_all(bind=engine)

# Base = declarative_base()

# بديله هو opps!
# def overrid_get_db():
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# بديله هو opps!
# app.dependency_overrides[get_db] = overrid_get_db

#  ----------------------------------------------------
# client = TestClient(app) #يمنك حذف بعد وضعه في الدالة

#  opps!
@pytest.fixture()
# @pytest.fixture(scope="module") مع test_user يمكنك حذفه scope= "module"
def session():
    print("my session fixture ran")
    Base.metadata.drop_all(bind=engine) # قبل تفعيل الكود 
    Base.metadata.create_all(bind=engine) # بعد تفعيل الكود
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

#  opps!
@pytest.fixture()
# @pytest.fixture(scope="module") مع test_user يمكنك حذفه scope= "module"
def client(session):
    # return TestClient(app) #1
    # Base.metadata.drop_all(bind=engine) # قبل تفعيل الكود 
    # Base.metadata.create_all(bind=engine) # بعد تفعيل الكود
    def overrid_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = overrid_get_db
    # command.upgrade("head")
    yield TestClient(app)
    # command.downgrade("base")