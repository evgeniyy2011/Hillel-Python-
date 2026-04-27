# 1. Квадрат числа.

chislo = int(input("Vvedite chislo - "))
print(f"Vashe chislo - {chislo**2}")


# 2. “Середнє трьох чисел”
# Програма запитує три числа і виводить їх середнє арифметичне.

chislo_1 = int(input("Vvedite chislo 1 -  "))
chislo_2 = int(input("Vvedite chislo 2 -  "))
chislo_3 = int(input("Vvedite chislo 3 -  "))
total = (chislo_1 + chislo_2 + chislo_3) / 3
print(total)


# 3. “Перетворення хвилин у години”
# Користувач вводить кількість хвилин. Програма виводить, скільки це годин і хвилин.

minutes = int(input("Vvedite minytu - "))
a, b = divmod(minutes, 60)
print(f"{a} години {b} хвилини")


# 4. “Розрахунок знижки”
# Користувач вводить ціну товару і розмір знижки у %.
# Програма виводить кінцеву ціну.

cina = int(input("Vvedite ciny - "))
znuzhka = int(input("Vvedite znuzky % - "))
print(f"Ціна зі знижкою: {cina *(1-znuzhka/100)}")


# 5. “Остання цифра числа”
# Користувач вводить ціле число, програма виводить його останню цифру.

chislo = int(input("Vvedite chislo - "))
print(chislo % 10)


# 6. “Периметр прямокутника”
# Користувач вводить довжину і ширину. Програма виводить периметр.

dovguna = int(input("Vvedite dovguny priamokytnuka - "))
shuruna = int(input("Vvedite shuruna priamokytnuka - "))
perimetr = (dovguna + shuruna) * 2
print(f"Периметр {perimetr}")



# 7. Виведення числа в стовпчик
# Написати програму, яка просить користувача ввести 4-х значне число з клавіатури, після чого друкує на екрані стовпчик цифр, з якого це число складається. Наприклад, користувач вводить 1234, а програма виводить:

chislo = int(input("Vvedite 4-x znachnoe chislo - "))
print(chislo // 1000)
print((chislo // 100) % 10)
print((chislo // 10) % 10)
print(chislo % 10)
