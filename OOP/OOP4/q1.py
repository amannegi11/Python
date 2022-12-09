class Parent:
    def __init__(self) -> None:
        self.num=100
    
class Child(Parent):

    def __init__(self) -> None:
        super().__init__()
        self.var=200
    def show(self):
        print(self.num)
        print(self.var)
son=Child()
son.show()
