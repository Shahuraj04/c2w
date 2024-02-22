class fun:
    def __del__(self):
        print("In destructor")
obj1=fun()
obj2=fun()
obj3=fun()
obj4=fun()
obj1=obj3
del obj2

