def print_result(func):
    def pr(*args):
        func(*args)
        print(func.__name__ + ":")
        a = func(*args)
        if type(a) is dict:
            for key, value in a.items():
                print(key, ' = ', value)
        elif type(a) is list:
            for i in range(0, len(a)):
                print(a[i])
        else:
            print(a)
        return a
    return pr


@print_result
def test_1():
    return 1

@print_result
def test_2():
    return 'iu5'

@print_result
def test_3():
    return {'a': 1, 'b': 2}

@print_result
def test_4(b):
    return b

if __name__ == '__main__':
    print('!!!!!!!!')
    b = [1, 2]
    test_1()
    test_2()
    test_3()
    test_4(b)
