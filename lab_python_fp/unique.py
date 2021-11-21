import random
# import gen_random

def gen_random(begin, end, num_count):
    rand = []
    for i in range(0, num_count):
        rand.append(random.randint(begin, end))
    return rand

class Unique(object):
    def __init__(self, items, **kwargs):
        self.elements = {}
        ignore_case = kwargs.get('ignore_case')

        if ignore_case is None:
            ignore_case = False
        elif not isinstance(ignore_case, bool):
            raise Exception("ignore_case parameter is not Boolean")

        for item in items:
            if ignore_case is True and isinstance(item, str):
                item = item.lower()

            self.elements[item] = item

    def __next__(self):
        return next(self.elements)

    def __iter__(self):
        return iter(self.elements)
    # def __init__(self, items, **kwargs):
    #     self.used_elements = set()
    #     self.data = items
    #     self.index = 0
    #
    #     if 'ignore_case' not in kwargs:
    #         self.ignore_case = False
    #     else:
    #         self.ignore_case = kwargs['ignore_case']
    #
    # def __iter__(self):
    #     return self
    #
    # def __next__(self):
    #     while True:
    #         if self.index >= len(self.data):
    #             raise StopIteration
    #         else:
    #             current = self.data[self.index]
    #             self.index = self.index + 1
    #             if self.ignore_case:
    #                 if current.lower() not in self.used_elements:
    #                     self.used_elements.add(current.lower())
    #                     return current
    #             else:
    #                 if current not in self.used_elements:
    #                     self.used_elements.add(current)
    #                     return current


def main():
    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    data2 = gen_random(1, 3, 10)
    data3 = ['abb', 'Abb', 'b', 'B', 'a', 'A', 'b', 'B']

    for val in Unique(data1):
        print(val)
    print('')

    for val in Unique(data2):
        print(val)
    print('')

    for val in Unique(data3, ignore_case=False):
        print(val)
    print('')

    for val in Unique(data3, ignore_case=True):
        print(val)

if __name__ == "__main__":
    main()
