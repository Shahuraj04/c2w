class Demo:
    def __init__(self):
        print("IN CONSTRUCTOR")
    def __del__(self):
        print("IN DESTRUCTOR")
def fun():
    print("IN FUN")
    obj=Demo()
    print("END OF FUN")
    return obj
retObj=fun()
print("END CODE")
