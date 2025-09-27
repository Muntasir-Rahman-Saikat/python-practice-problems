def guess():
    actual_number=6

    while True:
        a = int(input("Enter a number between 1 and 9: "))
        if a>8 or a<4:
             print("higher")
        elif (a>=4 and a<=8) and a!=actual_number:
            print("Almost there")
        elif a==actual_number:
            print("Your guess is correct")
            break
guess()