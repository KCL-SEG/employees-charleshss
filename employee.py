"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, pay, payType, hours, commission, commissionType, contractNum):
        self.name = name
        self.pay = pay
        self.payType = payType
        self.hours = hours
        self.commission = commission
        self.commissionType = commissionType
        self.contractNum = contractNum
        self.totalPay = 0

    def get_pay(self):
        if (self.commissionType == None):
            if (self.payType == "s"):
                self.totalPay = self.pay
            else:
                self.totalPay = self.pay * self.hours
        elif (self.commissionType == "b"):
            if (self.payType == "s"):
                self.totalPay = self.pay + self.commission
            else:
                self.totalPay = (self.pay * self.hours) + self.commission
        else:
            if (self.payType == "s"):
                self.totalPay = self.pay + (self.commission * self.contractNum)
            else:
                self.totalPay = (self.pay * self.hours) + (self.commission * self.contractNum)

        return self.totalPay

    def get_pay_type(self):
        return self.payType

    def __str__(self):
        output = ""
        if (self.commissionType == None):
            if (self.payType == "s"):
                output = self.name + " works on a monthly salary of "+ str(self.pay)+".  Their total pay is "+ str(self.totalPay)+"."
            else:
                output = self.name + " works on a contract of "+ str(self.hours)+" hours at "+ str(self.pay)+"/hour.  Their total pay is "+ str(self.totalPay)+"."
        elif (self.commissionType == "b"):
            if (self.payType == "s"):
                output = self.name + " works on a monthly salary of "+ str(self.pay)+" and receives a bonus commission of "+ str(self.commission)+".  Their total pay is "+ str(self.totalPay)+"."
            else:
                output = self.name + " works on a contract of "+ str(self.hours)+" hours at "+ str(self.pay)+"/hour and receives a bonus commission of "+ str(self.commission)+".  Their total pay is "+ str(self.totalPay)+"."
        else:
            if (self.payType == "s"):
                output = self.name + " works on a monthly salary of "+ str(self.pay)+ " and receives a commission for "+ str(self.contractNum)+" contract(s) at "+ str(self.commission)+"/contract.  Their total pay is "+ str(self.totalPay)+"."
            else:
                #"Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract. Their total pay is 4410."
                output = self.name + " works on a contract of "+ str(self.hours)+" hours at "+ str(self.pay)+"/hour and receives a commission for "+ str(self.contractNum)+" contract(s) at "+ str(self.commission)+"/contract.  Their total pay is "+ str(self.totalPay)+"."

        return output

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000, "s", None, None, None, None)
print(str(billie))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 25, "h", 100, None, None, None)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, "s", None, 200, "c", 4,)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 25, "h", 150, 220, "c", 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, "s", None, 1500, "b", None)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 30, "h", 120, 600, "b", None)
