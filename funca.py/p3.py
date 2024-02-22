def add(x):
    def inner(y):
        return x*y
    return inner
if __name__ == "__main__":
    obj=add(3)
    result=obj(7)
    print(result)
