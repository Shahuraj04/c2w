def outer():
    def inner():
        return "HELLO,C2W"
    return inner
    print("OUTER")
if __name__ == "__main__":
    result=outer()()
    print(result)
