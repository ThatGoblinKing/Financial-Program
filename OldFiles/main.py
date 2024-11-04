import os
import launchFileInit
import globals as gb
from controller import ControllerInstance


controller = ControllerInstance()

os.system("cls")

while not gb.DOEXIT:
	controller.update()

'''
ACTIONS:
Show Accounts
Show Transaction History
	- Total
	- Per account
Account Actions
	- Deposit
	- Withdraw
	- Transfer
Display balance of all accounts
'''