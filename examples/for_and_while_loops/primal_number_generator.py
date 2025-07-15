def primal_number_gen(n: int) -> list:
    if N < 2:
        return None
    else:
        primals = [2]
        for number in range(3, N + 1):
            for primal in primals:
                if number % primal == 0:
                    break
            else:
                primals.append(number)
        
        return primals

N = int(input("Введите число: "))
primals = primal_number_gen(N)
if primals is not None:
    print(f"Список простых числел до {N}: {' '.join(map(str, primals))}")
else:
    print(f"Простых числел до {N} не нашлось!")
