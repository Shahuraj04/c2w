def outer():
    def inner1(a,b):
        print("In INNER1")
        return a-b
    def inner2(obj):
        print("INNER 2")
        print(obj)
        return inner2
    retInner1=inner1(10,4)
    retInner2=inner2(retInner1)
    return retInner2
if __name__ == '__main__':
    retObj=outer()
    print(retObj)