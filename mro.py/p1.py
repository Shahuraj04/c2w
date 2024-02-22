class Grandparent():
    def show(self):
        print("IN GRANDPARENT")
class parent1(Grandparent):
    def show(self):
        print("IN PARENT 1")
class parent2(Grandparent):
    def show(self):
        print("IN PARENT 2")
class child(parent2,parent1):
    def printt(self):
        
        super().show()
obj=child()
obj.printt()
#print(child.mro())    
obj2=child.mro()
'''
classnames = [cls.__name__ for cls in child.__mro__[1:]]
for name in classnames:
    print(name)
'''
for i in obj2:

    print(i)
    for j in i:
        print(j)
print()




