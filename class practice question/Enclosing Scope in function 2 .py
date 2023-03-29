a = "global variable"
def method():
    a="nonlocal variable"
    def function():
        nonlocal a
        a="dfsdfj"
        print(a)
    function()
    print(a)

method()
print(a)