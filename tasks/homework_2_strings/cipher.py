"""
Задача 2: Шифр замены
Условие:
Дана строка.
-Замените все буквы "к" на "@"
-Переведите в верхний регистр
-Выделите подстроку от индекса 2 до 7
-Соберите результат в формате: "Сообщение: [РЕЗУЛЬТАТ] | Длина: [ДЛИНА_СТРОКИ]"
-Используйте методы replace(), upper(), срезы, len() и f-строки.
"""
s = "Кошка сбежала!"
s_ = s[2:7].upper().replace("К", "@")
print(f"Сообщение: {s_} | Длина: { len(s_)}")