class Atm(object):
    def __init__(self,name,age,cardNumber,pinNumber):
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber
        self.name=name
        self.age=age


    def CashWithdrawl(self,name,age,cardNumber,pinNumber):
        print("withdrawl_done")

    def BalanceEnquiry(self,name,age,cardNumber,pinNumber):
        print("your_balance_is....")

s1=Atm("s1",14,"your card number here","your pin number here")
s1.CashWithdrawl("s1",14,"your card number here","your pin number here") 
s1.BalanceEnquiry("s1",14,"your pin number here","your card number here")

