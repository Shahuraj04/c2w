class parent:
    def __init__(self):
        pass
    @classmethod
    def clsmethod(cls):

        pass
    @staticmethod
    def statmethod():
        pass
    def normalfun(self):
        pass
class child(parent):
    pass
obj1=child()
obj1.clsmethod()
obj1.statmethod()
obj1.normalfun()

