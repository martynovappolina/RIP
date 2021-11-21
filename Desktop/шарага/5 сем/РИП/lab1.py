import sys
import math

def get_coef(index, prompt):
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt)
        coef_str = input()
    # Переводим строку в действительное число
    coef = float(coef_str)
    return coef


def get_roots(a, b, c):
    result = []
    if a != 0:
        D = b*b - 4*a*c
        if D == 0.0:
            root = -b / (2.0*a)

            if root > 0:
                result.append(math.sqrt(root))
                result.append(-math.sqrt(root))

        elif D > 0.0:
            sqD = math.sqrt(D)
            root1 = (-b + sqD) / (2.0*a)
            root2 = (-b - sqD) / (2.0*a)

            if root1 > 0:
                result.append(math.sqrt(root1))
                result.append(-math.sqrt(root1))

            if root2 > 0:
                result.append(math.sqrt(root2))
                result.append(-math.sqrt(root))
    else:
        if b != 0:
            root = -c / b
            if root > 0:
                result.append(math.sqrt(root))
                result.append(-math.sqrt(root))
        else:
            root = 'любое число'
            result.append(root)

    return result


def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a,b,c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Нет корней')
    elif len_roots == 1:
        if roots[0] == 'любое число':
            print('Х может быть любым числом')
        else:
            print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {}, {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {}, {}, {} и {}'.format(roots[0], roots[1], roots[3], roots[4]))
    

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# qr.py 1 0 -4