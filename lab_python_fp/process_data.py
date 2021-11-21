import json

from cm_timer import cm_timer_1
from gen_random import gen_random
from print_result import print_result
from unique import Unique

path = './data_light.json'

with open(path, encoding='utf-8') as f:
    data = json.load(f)

@print_result
def f1(data):
    return sorted((Unique((i["job-name"] for i in data), ignore_case = True)), key=lambda x: x.lower())

@print_result
def f2(data):
    return list(filter(lambda x: x.startswith('программист'), data))

@print_result
def f3(data):
    return list(map(lambda x: x + ' с опытом Python', data))

@print_result
def f4(data):
    data_sal = zip(data, gen_random(len(data), 100000, 200000))
    return list(map(lambda x: x[0] + ', зарплата: ' + str(x[1]) + 'руб', data_sal))

def main():
    with cm_timer_1():
        f4(f3(f2(f1(data))))

if __name__ == '__main__':
    main()
