
def safe_input_float(string_):
    while True:
        try:
            num = float(input(string_))

            if num <= 1 and num >= 0:
                break
            else:
                print('Коэффициент должен быть: 0 <= коэф <= 1\n')
                raise ValueError
        except ValueError:
            pass
    return num

def print_list_strats(res):

    print('')

    print('Рекомендуемые стратегии: ', end='')
    for item in res:
        print(' {}{} '.format('A', item + 1), end='')

    print('\n')

def print_list_probs(res):

    print('')

    print('Вероятности: ', end='')
    i = 0
    for item in res:
        print(' {}{} = {} '.format('Q', i + 1, item), end='')
        i += 1

    print('')

def get_model(choice):

    matrix = None
    probs = None

    if choice == 1:
        matrix = [
            [5, 7, 10],
            [7, 8, 6],
            [9, 8, 4]
        ]
        probs = [0.7, 0.2, 0.1]

    # старый первый пример из ворда
    elif choice == 2:
        matrix = [
            [15, 25, 20],
            [60, 20, 35],
            [25, 75, 45],
            [75, 5, 40]
        ]
        probs = [0.3, 0.1, 0.6]
    elif choice == 3:
        matrix = [
            [15, 25, 20],
            [60, 20, 35],
            [25, 75, 45],
            [75, 5, 40]
        ]
        probs = [0.5, 0.4, 0.1]

    # пример 1 из ворда
    elif choice == 4:
        matrix = [
            [15, 25, 50],
            [60, 20, 35],
            [25, 30, 45],
            [75, 5, 40]
        ]
        probs = [0.3, 0.2, 0.5]
    elif choice == 5:
        matrix = [
            [15, 25, 50],
            [60, 20, 35],
            [25, 30, 45],
            [75, 5, 40]
        ]
        probs = [0.5, 0.4, 0.1]

    # пример 2 из ворда
    elif choice == 6:
        matrix = [
            [8, 9, 10, 11],
            [11, 10, 7, 8],
            [13, 8, 14, 7]
        ]
        probs = [0.1, 0.7, 0.1, 0.1]
    elif choice == 7:
        matrix = [
            [8, 9, 10, 11],
            [11, 10, 7, 8],
            [13, 8, 14, 7]
        ]
        probs = [0.25, 0.25, 0.25, 0.25]


    return matrix, probs


