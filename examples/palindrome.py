"""
    Условие:
    Проверьте, является ли строка палиндромом (игнорируя пробелы, регистр и знаки препинания).
    Пример:
    "А роза упала на лапу Азора" → True.
"""

string = input("Введите строку: ")

string = string.lower()
new_string = ""
for char in string:
    if char.isalpha():
        new_string += char

print(new_string == new_string[::-1])