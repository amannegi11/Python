class Atm:
# static variable define outside of methods
    __counter=1

    def __init__(self) -> None:
        # instance variable define inside methods
        self.pin=1112
        self.balance=1000
        self.cid=Atm.__counter # static variable using (class.static_variable) 
        Atm.__counter+=1
        #self.main()
    
    #utility functions (no need to create object for it)
    @staticmethod
    def get():
        return Atm.__counter
        #access it by using class.__variable(Atm.__counter)
    
    def main(self):
        user=input('''Hello sir how can i help you?
        1. Press 1 to know your current balance
        2. Press 2 to change your pin
        3. Press 3 for withdraw money
         ''')
        if user==1:
            self.cb()
        elif user==2:
            self.cp()
        else:
            self.wm()
           
    def cb(self):
        Pin=int(input('Enter your pin'))
        if Pin==self.pin:
            print(f"Your current balance is {self.balance}")
        else:
            print("Incorrect pin")
        self.main()
    def cp(self):
        Pin=int(input('Enter current pin'))
        if Pin==self.pin:
            New_pin=int(input('Enter new pin'))
            self.pin=New_pin
        else:
            print('Incorrect pin')
        self.main()
    def wm(self):
        Pin=int(input('Enter current pin'))
        if Pin==self.pin:
            amount=int(input('Enter amount'))
            if amount<=self.balance:
                print(f"here is your amount {amount} remaining balance in your account is {self.balance-amount}")
            else:
                print('Not sufficient balance')
        else:
            print('Incorrect pin')
        self.main()


obj1=Atm()
obj2=Atm()
obj3=Atm()
obj4=Atm()

print(obj2.id)
print(obj4.id)
print(obj3.id)
print(obj1.id)
print(Atm._Atm__count)
