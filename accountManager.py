from account import Account
import datetime, time

class AccountManager:
    def __init__(self):
        self.accounts : list[Account] = []
    def makeTest(self):
        newAccount = Account("Test")
        newAccount.addTransaction("123", time.mktime(datetime.datetime.now().timetuple()), "test", 10)
        newAccount.addTransaction("233", 1730739476419, "test", 10)
        newAccount.addTransaction("12223", 1730739476419, "test", 10)
        print(newAccount.transactions)
        self.accounts.append(newAccount)