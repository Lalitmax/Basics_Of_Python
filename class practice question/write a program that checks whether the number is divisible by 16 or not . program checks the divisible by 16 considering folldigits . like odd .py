#  254176 
# 693408
num = int(input("Enter the number : "))

place_ftpd = num%10000
last_four_digit =place_ftpd//1000

if(last_four_digit%2==0):
    place_ttpd =num%1000
    last_three_digit =place_ttpd//100
    total =(last_four_digit*last_three_digit)+num%100
    if(total%16==0):
        print("{} (even) is divisible by 16".format(num))
    else:
        print("{} (even) not divisible by 16".format(num))
else:
    place_ttpd = num%1000
    place_ttpd +=8
    last_three_digit =place_ttpd//100
    total = (last_three_digit*4)+place_ttpd%100
    if(total%16==0):
        print("{} (odd) is divisible by 16".format(num))
    else:
      
        print("{} (odd) not divisible by 16".format(num))
