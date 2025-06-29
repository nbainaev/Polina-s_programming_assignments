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
        if runes == "a":
            rune_strength += a
        elif runes == "b":
            rune_strength += b
        else:
            rune_strength += c
        string = input("введите последовательность рун:")
        rune_strength = rune_calculator(string)
    return rune_strength

# Тут нужно прочитать входные данные и вывести суммарную силу рун