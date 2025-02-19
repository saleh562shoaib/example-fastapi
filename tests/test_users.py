# api/conftest.py/test_something.py ابحث عنه
#  تم نقله الى ملف  database.py  خاص بالتست
# #  وظيفة هذا الملف هو اختبار نقاط النهاية
# # pytest -v -s tests\test_users.py
# pytest tests\test_users.py -v -s
# # pytest --disable-warnings -v tests\test_users.py -s -x
# عليك ان تحذف او تنظف قاعدة البينات في اجراء اي عملية لحماية من التكرار البينات
# fastapi_test قاعدة بيانات جديدة خاصة بالاختبار نفس القاعدة التي فوق تطبق عليها
# from fastapi.testclient import TestClient
# import pytest
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from app.main import app
import pytest
from jose import jwt
from app import schemas
# from app.config import settings
# from app.database import get_db
# from app.database import Base
# from alembic import command
# from .database import client, session # conftest.py بعد صنعه
from app.config import settings
# #  --------------------------------------------------
#  جزء من اكواد الخاصة بملف ال database.py
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Admin@localhost:5432/fastapi_test'
# SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'

# engine = create_engine(SQLALCHEMY_DATABASE_URL)

# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

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
# app.dependency_overrides[get_db] = overrid_get_db انه تحت

#  ----------------------------------------------------
# client = TestClient(app) #يمنك حذف بعد وضعه في الدالة


#  opps!
# @pytest.fixture
# def session():
#     Base.metadata.drop_all(bind=engine) # قبل تفعيل الكود 
#     Base.metadata.create_all(bind=engine) # بعد تفعيل الكود
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

#  opps!
# @pytest.fixture
# def client(session):
    # return TestClient(app) #1
    # Base.metadata.drop_all(bind=engine) # قبل تفعيل الكود انهم فوق الان في الدالة
    # Base.metadata.create_all(bind=engine) # قبل تفعيل الكود انهم فوق الان في الدالة
    # def overrid_get_db():
    #     try:
    #         yield session
    #     finally:
    #         session.close()
    # app.dependency_overrides[get_db] = overrid_get_db
    # # command.upgrade("head")
    # yield TestClient(app)
    # command.downgrade("base")

#  conftest.py بعد صنعه نقلناه فيه
# @pytest.fixture(scope="module")
# def test_user(client):
#     user_data = {"email": "sanjeev567111@gmail.com","password": "password123"}

#     res = client.post("/users/", json=user_data)

#     assert res.status_code == 201
#     # print(res.json())
#     new_user = res.json()
#     new_user['password'] = user_data['password']
#     return new_user

# --------------------------------------------------------
# def test_root(client): # لن يضاف الحقل المرتين عليك اضافة هذا  client
#     res = client.get("/")
#     print(res.json().get("message"))
#     assert res.json().get("message") == "Hello World"
#     assert res.status_code == 200
# -------------------------------------------------------


def test_create_user(client): # لن يضاف الحقل المرتين عليك اضافة هذا  client
    res = client.post("/users/", json={"email": "hello123@gmail.com", "password": "password123"})
    new_user = schemas.UserOut(**res.json())
    # assert res.json().get("email") == "hello123@gmail.com"
    assert new_user.email == "hello123@gmail.com"
    # print(res.json())
    assert res.status_code == 201 # هؤلاء الارقام خاصين ببوست مان

# scope معه سيعمل
# def test_login_user(client, test_user): # لن يضاف الحقل المرتين عليك اضافة هذا  client
def test_login_user(test_user, client): # لن يضاف الحقل المرتين عليك اضافة هذا  client
    # res = client.post("/login", data={"username": "hello123@gmail.com", "password": "password123"})
    res = client.post("/login", data={"username": test_user['email'], "password": test_user['password']})
    # print(res.json())
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id: str = payload.get("user_id")
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == 'bearer'
    assert res.status_code == 200

@pytest.mark.parametrize("email, password, status_code", [
    ('wrongemail@gmail.com', 'password123', 403),
    ('sanjeev@gmail.com', 'wrongpassword', 403),
    ('wrongemail@gmail.com', 'wrongpassword', 403),
    (None, 'password123', 403),
    ('sanjeev@gmail.com', None, 403)
])
# def test_incorrect_login(test_user2, client):
def test_incorrect_login(test_user2, client, email, password, status_code):
    # res = client.post("/login", data={"username": test_user2["email"], "password": "wrongpassword"})
    res = client.post("/login", data={"username": email, "password": password})

    # assert res.status_code == 403
    assert res.status_code == status_code
    # assert res.json().get('detail') == 'Invalid Credentals'







