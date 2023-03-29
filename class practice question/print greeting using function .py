# First methods
def greet1(host,uni,guest):
    print(" i am {}. i am your host".format(host))
    print("Hello Mr. {} Welcome to {}".format(guest,uni))


# second methods
def greet2(host,uni,*guest):
    print("i am {}. i am your host ".format(host))

    for i in guest:
        print("Hello Mr. {} Welcome to {}".format(i,uni))


greet1("sajay", "Chitkara university", "lalit")
greet2("gourab tiwari","Chitkara university ","lalit","rahul","saroj","mukesh")