# nested function 
def outer():
    first_num=1
    def inner():
        first_num=0
        second_num=1
        print("inner - second_num is ",second_num)
    inner()
    print("outer - First_num is ",first_num)

outer()
