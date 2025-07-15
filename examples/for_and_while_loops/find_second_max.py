import time

def find_max(list_: list):
    max_ = list_[0]
    second_max = list_[0]
    for value in list_[1:]:
        if value > max_:
            second_max = max_
            max_ = value
        
    return max_, second_max

start = time.time()
lst = list(map(float, input("Введите список через пробел: ").strip(" ").split(" ")))
max_, second_max = find_max(lst)
print("Второй максимум: ", second_max)

stop = time.time()
print(f"Выполнение заняло времени {stop - start:2f} с")