letter = '''Drear <|name|>
you are selected

Date: <|date|>
'''
name = input("Enter your Name : ")
date = input("Enter your Date : ")
print("\n")        #new line
letter = letter.replace("<|name|>", name)
letter= letter.replace("<|date|>", date)
print(letter)