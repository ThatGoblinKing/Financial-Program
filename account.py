import pandas
class Account:
    def __init__(self, name):
        self.name = name
        self.transactions = pandas.DataFrame(columns=['Epoch', 'Category', 'Amount'], index=['ID'])
    def addTransaction(self, id : str, unix : float, category : str, amount : int):
        self.transactions.loc[id] = [unix, category, amount]