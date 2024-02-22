class Human:
    def __init__(self,name,age):
        print("IN DEMO CONSTRUCTOR")
        self.name=name
        self.age=age
    def information(self):
        print("NAME IS :",self.name)
        print("AGE IS:",self.age)
name=input("ENTER NAME:")
age=int(input("ENTER AGE:"))

if __name__ == '__main__':
    obj1=Human(name,age)
    obj1.information()
