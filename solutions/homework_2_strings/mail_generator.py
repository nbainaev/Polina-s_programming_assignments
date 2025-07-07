"""
Задача 5: Генератор email
Условие:
Пользователь вводит имя и фамилию (раздельно). Сгенерируйте email:

-Первые 3 буквы имени (строчные)
-Точку
-Фамилию в нижнем регистре (без пробелов)

@mail.com
Проверьте длину email (должна быть не менее 12 символов).
Используйте срезы, lower(), strip(), len(), f-строки.
"""
name = input("Введите ваше имя и фамилию:").strip(" ").lower()
name_2 = name[:3]
index = name.find(" ")
name_3 = name[index + 1:]
simbol_1 = "."
simbol_2 = "@mail.com"
if len(name_2 + simbol_1 +name_3 + simbol_2) >= 12:
    print(f"{name_2}{simbol_1}{name_3}{simbol_2}")