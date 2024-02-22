def outer():
    message="OUTER FUNCTION"
    def inner():
        return message
    return inner
if __name__ == "__main__":
    inner_func=outer()
    result=inner_func()
    print(result)
