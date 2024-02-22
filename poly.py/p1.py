class demo():
    def fun(self):
        print("IN DEMO:FUN")
class memo():
    def gun(self):
        print("IN MEMO:GUN")
def callfun(obj):
    if obj==obj1:
        obj.fun()
    else:
        obj.gun()
obj1=demo()
obj2=memo()
callfun(obj1)
