def gun():
    print("GUN")
def run(y):
    print("RUn")
    y()
def fun(x):
    print("FUN")
    x()
fun(run(gun))
