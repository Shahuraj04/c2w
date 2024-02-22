def outer(flag):
    def inner():
        return "THIS IS TRUE." if flag else "THIS IS FAlSE."
    return inner
if __name__ == "__main__":
    true_function=outer(True)
    false_function=outer(False)
    print(true_function())
    print(false_function())
