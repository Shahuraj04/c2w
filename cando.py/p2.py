class vehicle:
    def __init__ (self,brand,model,year,speed):
        self.brand=brand
        self.model=model
        self.year=year
        self.speed=speed
    def accelerate(self):
        pass
    def brake(self):
        pass
    def honk(self):
        pass
class child(vehicle):
    def accelerate():
        pass
    def honk():
        pass
obj1=vehicle("BMW","GT3","2003","200 kmph")
obj2=child("BMW","GT3","2003","200 kmph")

