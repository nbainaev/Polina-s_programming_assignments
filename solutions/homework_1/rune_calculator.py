"""
    Задача: Каждой руне соответствует число:
    a = 10
    b = 20
    c = 30
    Пользователь вводит последовательность рун (напр. "ac"). Вычислите сумму.
    
    Вычисления проводить в функции rune_calculator.
"""
a = 10
b = 20
c = 30

def rune_calculator(runes: str) -> int:
    """
        Функция для вычисления силы последовательности рун.

        Параметры
        ---------
        -runes: str\n
            Последовательность рун
        
        Возвращаемое значение
        --------------------
        -rune_strength: int\n
            Суммарная сила рун
    """
    rune_strength = 0
    for rune in runes:
        if rune == "a":
            rune_strength += a
        elif rune == "b":
            rune_strength += b
        else:
            rune_strength += c
    
    return rune_strength

string = input("введите последовательность рун:")
rune_strength = rune_calculator(string)
print(rune_strength)