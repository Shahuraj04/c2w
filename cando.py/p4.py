class parent:
    def __init__(self,x):
        self.x=x

    def instmethod(self):
        print("IN PARENT INSTANCE METHOD")
class child(parent):
    def instmethod(self):
         print("IN CHILD INSTANCE METHOD")
obj1=child(2)
obj1.instmethod()
        

