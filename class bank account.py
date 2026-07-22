class bankaccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def showbalance(self):
        print(f"{self.name}s balance's{self.balance}")
s1=bankaccount("rasool",100000)
s2=bankaccount("sravanthi",10000000)
s1.showbalance()
s2.showbalance()
                       
