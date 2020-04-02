class Employee():
    amount= 2
    def __init__(self,first,last,pay):
        self.first= first
        self.last= last
        self.pay= pay
    def email(self):
        return "{}.{}@gmail.com".format(self.first,self.last)
    def fullName(self):
        return "{} {}".format(self.first,self.last)
    def pay(self):
        self.pay= int(self.pay* self.amount)

