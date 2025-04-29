from abc import ABC,abstractmethod

class Accoount:
    listOfAccounts = []

    def __init__(self,name,accountNumber,password,type):
        self.name = name
        self.accountNumber = accountNumber
        self.password = password
        self.type = type

        self.balance = 0
        Accoount.listOfAccounts.append(self)

    def changeInformation(self,newName):
        self.newName = newName

    def changeInformation(self,name,password):
        self.name = name
        self.password = password

    def depositeAmount(self,amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Faild to deposite!")
    
    def withdrowAmount(self,amount):
        if amount > 0 and amount < self.balance:
            self.balance -= amount
        else:
            print("Faild to withdrow!")

    def getBalance(self):
        return self.balance
    
    @abstractmethod
    def showInformation(self):
        pass


class SavingsAccount(Accoount):
    def __init__(self, name, accountNumber, password, type, intrestRate):
        self.intrestRate = intrestRate
        super().__init__(name, accountNumber, password, type)





myAccount = Accoount("Tasnim Rahman",100012,1234,"savings")

myAccount.depositeAmount(1000)
print(myAccount.getBalance())

