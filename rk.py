# используется для сортировки
from operator import itemgetter

class CD:
    """cd-диск"""
    def __init__(self, id, capacity, recording_layer_type, lib_id):
        self.id = id
        self.capacity = capacity
        self.recording_layer_type = recording_layer_type
        self.lib_id = lib_id

class CD_lib:
    """библиотека cd-дисков"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class LibDisk:
    def __init__(self, lib_id, disk_id):
        self.lib_id = lib_id
        self.disk_id = disk_id

# библиотеки cd-дисков
libs = [
    CD_lib(1, 'CDDB'),
    CD_lib(2, 'Dacal CD Library'),
    CD_lib(3, 'Proceed')
]

# диски
disks = [
    CD(1, 650, 'Cyanine', 1),
    CD(2, 702, 'Cyanine', 1),
    CD(3, 790, 'Cyanine', 1),
    CD(4, 870, 'Cyanine', 2),
    CD(5, 650, 'Phthalocyanine', 2),
    CD(6, 650, 'Phthalocyanine', 2),
    CD(7, 702, 'Phthalocyanine', 3),
    CD(8, 702, 'Phthalocyanine', 3),
    CD(9, 650, 'Phthalocyanine', 4),
    CD(10, 650, 'Phthalocyanine', 4)
]

lib_disks = [
    LibDisk(1, 1),
    LibDisk(1, 2),
    LibDisk(1, 3),
    LibDisk(2, 4),
    LibDisk(2, 5),
    LibDisk(2, 6),
    LibDisk(3, 7),
    LibDisk(3, 8),
    LibDisk(4, 9),
    LibDisk(4, 10),
]

def main():
    # Соединение данных один-ко-многим
    one_to_many = [(e.recording_layer_type, e.capacity, d.name)
                   for d in libs
                   for e in disks
                   if e.lib_id == d.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(d.name, ed.lib_id, ed.disk_id)
                         for d in libs
                         for ed in lib_disks
                         if d.id == ed.lib_id]

    many_to_many = [(e.recording_layer_type, e.capacity, lib_name)
                    for lib_name, lib_id, disk_id in many_to_many_temp
                    for e in disks if e.id == disk_id]

    print('Задание А1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(res_11)

    print('\nЗадание А2')
    res_12_unsorted = []
    # Перебираем все библиотеки
    for d in libs:
        # Список дисков в библиотеке
        d_disks = list(filter(lambda i: i[2] == d.name, one_to_many))
        # Если библиотека не пустая
        if len(d_disks) > 0:
            # ёмкости дисков в библиотеке
            d_capacitys = [capacity for _, capacity, _ in d_disks]
            # суммарная ёмкость дисков в библиотеке
            d_capacitys_sum = sum(d_capacitys)
            res_12_unsorted.append((d.name, d_capacitys_sum))

    # Сортировка по суммарной ёмкости
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\nЗадание А3')
    res_13 = {}
    # Перебираем все библиотеки
    for d in libs:
        if 'Library' in d.name:
            # Список дисков в библиотеке
            d_disks = list(filter(lambda i: i[2] == d.name, many_to_many))
            # только тип записывающего слоя
            d_disks_id = [x for x, _, _ in d_disks]
            # Добавляем результат в словарь
            # ключ - библиотека, значение - список id
            res_13[d.name] = d_disks_id

    print(res_13)


if __name__ == '__main__':
    main()
