
def counter(lst: list, elem: int) -> int:
    count = 0
    for value in lst:
        if value == elem:
            count += 1
    return count

lst = list(map(int, input("Введите список через пробел: ").strip(" ").split(" ")))
element = int(input("Введите число, которое нужно подсчитать: "))

count = counter(lst=lst, elem=element)
print(f"Число {element} встретилось {count} раз(а)")
