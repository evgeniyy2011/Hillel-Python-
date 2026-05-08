# ДЗ 5.2. Модифікувати калькулятор

while True:
    numb_one = float(input("Enter first number = "))
    deystvie = input("enter character ( +, -, /, *)")
    numb_two = float(input("Enter second number = "))
    if deystvie == "+":
        print(numb_one + numb_two)
    elif deystvie == "-":
        print(numb_one - numb_two)
    elif deystvie == "*":
        print(numb_one * numb_two)
    elif deystvie == "/":
        if numb_two == 0:
            print("Forbiden devided on 0 !")
        else:
            print(numb_one / numb_two)
    ask = input("Do you want again?")
    if ask.lower() == "y" or ask.lower() == "yes":
        continue
    else:
        break
