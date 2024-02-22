def outer():
    def inner():
        return"INNER"
    return inner()
ans=outer()
print(ans)
