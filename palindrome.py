print(">> Progame Chech Palindrome <<")
s=input("Enter integer number(4 digit) : " )
number1 = s[0:1]
number2 = s[1:2]
number3 = s[2:3]
number4 = s[3:4]
if (number1 == number4 and number2 == number3)  :
    print(f"You number {s},is palindrome. ")
else:
    print(f"You number is{s},is not palindrome. ")

