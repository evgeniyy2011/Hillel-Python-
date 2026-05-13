# ДЗ 6.2. Конвертер із числа в дату

value = int(input("Enter any number (seconds) between 0 - 8640000 - "))
if value >= 0 and value < 8640000:
    day, time_s = divmod(value, 86400)
    hours, m = divmod(time_s, 3600)
    minutes, sec = divmod(m, 60)
    if str(day)[-2:] in ("11", "12", "13", "14"):
        end = "днів"
    elif str(day)[-1] == "2" or str(day)[-1] == "3" or str(day)[-1] == "4":
        end = "дні"
    elif str(day)[-1] == "1":
        end = "день"
    else:
        end = "днів"
    print(
        f"{day} {end}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(sec).zfill(2)}"
    )
