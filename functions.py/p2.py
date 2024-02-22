def fun():
    print("START FUN")
    yield 10
    yield 20
    yield 30
    print("END fun")
for i in fun():
    print(i)

