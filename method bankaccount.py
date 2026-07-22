class bankaccount:
    def __init__(self,account_number,holder_name):
        self.account_number =account_number
        self.holder_name =holder_name
class savings_account(bankaccount):  
    def __init__(self,account_number,holder_name,balance):
     super(self,account_number,holder_name)
     self.balance=balance
    def display_balance(self):
        print("balance",self.balance)
class onlinebanking(savings_account):
    def __init__(self,account_number,holder_name,balance):
      super(self,account_number,holder_name,balance)  
    def check_balance(self):
        print("account_details")
        print("account_number:self.account_number")
        print("")
bankaccount("o12345","rasool").display_bankaccount()
savings_account(20000).display_savingsaccount()
onlinebanking(20000).display_onlinebanking()