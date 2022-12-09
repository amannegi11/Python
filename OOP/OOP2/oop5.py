class Atm:

    def __init__(self) -> None:
        self._pin=1112
        self.__balance=1000
        self.main()
    
    def get(self):
        return self.__balance
    
    def set(self,new_value):
        if type(new_value)==int or type(new_value)==float:
                self.__balance=new_value    
        else:
            ...
    def main(self):
        user=int(input('''Hello sir how can i help you?
        1. Press 1 to know your current balance
        2. Press 2 to change your pin
        3. Press 3 for withdraw money
         '''))
        if user==1:
            self.cb()
        elif user==2:
            self.cp()
        else:
            self.wm()
           
    def cb(self):
        Pin=int(input('Enter your pin'))
        if Pin==self.__pin:
            print(f"Your current balance is {self.__balance}")
        else:
            print("Incorrect pin")
        self.main()
    def cp(self):
        Pin=int(input('Enter current pin'))
        if Pin==self.__pin:
            New_pin=int(input('Enter new pin'))
            self.__pin=New_pin
        else:
            print('Incorrect pin')
        self.main()
    def wm(self):
        Pin=int(input('Enter current pin'))
        if Pin==self.__pin:
            amount=int(input('Enter amount'))
            if amount<=self.__balance:
                print(f"here is your amount {amount} remaining balance in your account is {self.__balance-amount}")
            else:
                print('Not sufficient balance')
        else:
            print('Incorrect pin')
        self.main()

obj=Atm()
print(obj._pin)