def outer():
    def inner():
        return "GREETINGS FROM INNER FUNC"
    return inner()
if __name__ == "__main__":
    result=outer()
    print(result)
