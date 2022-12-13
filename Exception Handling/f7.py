class SecurityError(Exception):

    def __init__(self,message):
        print(message)

    def logout(self):
        print('logout')





class Google:

    def __init__(self,name,email,password,device):
        self.name=name
        self.email=email
        self.password=password
        self.device=device

    def login(self,email,password,device):
        if device!=self.device:
            raise SecurityError('Something went wrong')
        if email==self.email and password ==self.password:
            print('Welcome')
        else:
            print('login error')



obj=Google("Aman",'aamjdbw@jwbdui','bdi#sxbbu','hdgwy')

try:
    obj.login('aamjdbw@jwbdui','bdi#sxbbu','hdgwp')
except SecurityError as e:
    e.logout()
else:
    print(obj.name)

finally:
    print('database connection closed')

