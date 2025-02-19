# هناك اخطاء في الاختبار عليك حل مشكلتها عليك معرفة pytest وكيفية استخدامها
# Requests: HTTP for Humans تصفحها
def add(num1: int, num2: 2):
    return num1 + num2 

def subtract(num1: int, num2: 2):
    return num1 - num2

def multiply(num1: int, num2: 2):
    return num1 * num2

def divde(num1: int, num2: 2):
    return num1 / num2



class InsufficientFound(Exception):
    pass

class BankAccount():
    def __init__(self, starting_balance=0):
        self.balance = starting_balance #  -1 لا يجب زيادة او تنقيص هي لا يصح

    def deposit(self, amount):
        self.balance += amount

    def Withdraw(self, amount):
        if amount > self.balance:
            # raise Exception("Insufficient funds in account") # لن يعمل الاختبار اذا اليغيته
            raise InsufficientFound("Insufficient funds in account") # لن يعمل الاختبار اذا اليغيته
            # raise ZeroDivisionError() # هذا سيظهر لك خطا في الاختبار         
        self.balance -= amount

    def collect_interest(self):
        self.balance *= 1.1

