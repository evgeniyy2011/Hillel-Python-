# ДЗ 3.1. Найпростіший калькулятор

ins_one = float(input("Vvedite chislo -"))
action = input("Vvedite deystvie (*,+,-,/ -")
ins_two = float(input("Vvedite chislo -"))
if action == "*":
    print(ins_one * ins_two)
elif action == "+":
    print(ins_one + ins_two)
elif action == "-":
    print(ins_one - ins_two)
elif action == "/":
    if ins_two == 0:
        print("ALARM - delit na 0 nelza!!!!")
    else:
        print(ins_one / ins_two)
