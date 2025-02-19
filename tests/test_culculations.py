# mytest.py => test_culculations.py غيره لهذاالاسم
# mytest.py ثم ارجعه لاسمه الاصلي بعد الانتهاء من الاختبار
# test_culculations.py ثم ارجعه لاسمه الاصلي بعد الانتهاء من الاختبار
# pytest -v -s
# يجب ان يكون الحساب متوافق في كلا الملفين الخاص بالحساب
# pytest --disable-warnings -v -x
import pytest
from app.culculations import add, subtract, multiply, divde, BankAccount, InsufficientFound


@pytest.fixture
def zero_bank_account():
    print("creating empty bank account")
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("num1, num2, expected", [
    (3, 2, 5),
    (7, 1, 8),
    (12, 4, 16)
])
def test_add(num1, num2, expected): #1
# # def fjyggiio():
    print("testting add function")
#     # sum = add(5, 3)
#     # assert sum == 8 #1
    # assert add(5, 3) == 8 #2
    assert add(num1, num2) == expected

# testing_add()

def test_add2(): 
    assert add(4, 2) == 6


def test_subtract():
    # assert subtract(9, 4) == 5
    assert subtract(9, 4) == 5

def test_multiply():
    assert multiply(4, 3) == 12

def test_divde():
    assert divde(20, 5) == 4

def test_bank_set_initial_amount(bank_account):
    # bank_account = BankAccount(50)
    assert bank_account.balance == 50

def test_bank_defualt_amount(zero_bank_account):
    # bank_account = BankAccount()
    print("testing my bank account")
    # assert bank_account.balance == 0 #1
    assert zero_bank_account.balance == 0

def test_Withdraw(bank_account):
    # bank_account = BankAccount(50)
    bank_account.Withdraw(20)
    assert bank_account.balance == 30

def test_deposit(bank_account):
    # bank_account = BankAccount(50)
    bank_account.deposit(30)
    assert bank_account.balance == 80

def test_collect_interest(bank_account):
    # bank_account = BankAccount(50)
    bank_account.collect_interest()
    # assert bank_account.balance == 55 #1
    assert round(bank_account.balance, 6) == 55


@pytest.mark.parametrize("deposited, Withdraw, expected", [
    (200, 100, 100),
    (50, 10, 40),
    (1200, 200, 1000)
    # (10, 50, -40)
])
# def test_bank_transaction(zero_bank_account):
def test_bank_transaction(zero_bank_account, deposited, Withdraw, expected):
    zero_bank_account.deposit(deposited) #(200)كان
    zero_bank_account.Withdraw(Withdraw) #(100)كان
    assert zero_bank_account.balance == expected #100كان

def test_insufficient_funds(bank_account):
    # with pytest.raises(Exception):
    with pytest.raises(InsufficientFound):
        bank_account.Withdraw(200)