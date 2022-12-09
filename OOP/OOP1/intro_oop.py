# l=[11,12]
# print(type(l))

#pascal case hello worls class helloworld


class Atm:
    # constructor is a special function which does not need to call explicitly
    def __init__(self):
        self.pin=""
        self.balance=0
        self.menu()
        # print('hello')
    
    def menu(self):
        user_input=input("""
        Hi how can i help you?
        1. Press 1 to create pin 
        2. Press 2 to change pin
        3. Press 3 to check Balance
        4. Press 4 to withdraw
        5. Anything else to exit
        """)
        # print('negi')

        if user_input=="1":
            #create pin
            self.create_pin()
        elif user_input=="2":
            #change pin
            self.change_pin()
        elif user_input=="3":
            #check Balance
            self.check_balance()
        elif user_input=="4":
            # withdraw
            self.withdraw_money()
        else:
            pass
            # exit
    def create_pin(self):
        user_pin=input('enter your pin')
        self.pin=user_pin

        user_balance=int(input('enter balance'))
        self.balance=user_balance

        print('pin crated successfully')
        self.menu()
    def change_pin(self):
        old_pin=input('enter current pin')
        if old_pin==self.pin:
            #let him change the pin
            new_pin=input('enter the new pin')
            self.pin=new_pin
            print('pin changed successfully')
            self.menu()
        else:
            print('nahi karne denge')
            self.menu()
    def check_balance(self):
        pin=input('Enter your pin')
        if pin==self.pin:
            print('your balance is', self.balance)
        else:
            print('wrong pin')
        self.menu()
    def withdraw_money(self):
        pin=input('enter your pin')
        if pin==self.pin:
            amount=int(input('Enter the amount'))
            if amount<=self.balance:
                self.balance=self.balance-amount
                print('Withdrawal successful balance is',self.balance)
                
            else:
                print('Not sufficient balance')
        else:
            print('wrong pin')
        self.menu()


obj=Atm()

