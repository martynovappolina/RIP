from operator import itemgetter

class File:
    def __init__(self, id, name, size, catalog_id):
        self.id = id
        self.name = name
        self.size = size
        self.catalog_id = catalog_id

class Catalog:
    def __init__(self, id, name, count):
        self.id = id
        self.name = name
        self.count = count

class FileCatalog:
    def __init__(self, catalog_id, file_id):
        self.catalog_id = catalog_id
        self.file_id = file_id

# Каталоги файлов
catalogs = [
    Catalog(1, 'Word', 3),
    Catalog(2, 'Excel', 2),
    Catalog(3, 'Paint', 6)
]

# Файлы
files = [
    File(1, 'Остров', 3, 1),
    File(2, 'Продукты', 2, 2),
    File(3, 'Домовой', 1, 3),
    File(4, 'Докладной', 1, 1),
    File(5, 'Проездной', 2, 3)
]

files_catalogs = [
    FileCatalog(1, 1),
    FileCatalog(2, 2),
    FileCatalog(3, 3),
    FileCatalog(1, 4),
    FileCatalog(3, 5),
]

def main():
    # Соединение один ко многим
    one_to_many = [(f.name, f.size, c.name, c.count)
                    for c in catalogs
                    for f in files
                    if f.catalog_id == c.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(c.name, f.catalog_id, f.file_id)
                         for c in catalogs
                         for f in files_catalogs
                         if c.id == f.catalog_id]

    many_to_many = [(f.name, catalog_name)
                    for catalog_name, catalog_id, file_id in many_to_many_temp
                    for f in files if f.id == file_id]

    print('Задание Д1')
    res_11 = list(filter(lambda x: x[0].endswith('ой'), one_to_many))
    for i in res_11:
        print("Файл: {}, Каталог: {}".format(i[0], i[2]))

    print('\nЗадание Д2')
    res_12_unsorted = []
    for c in catalogs:
        fs = list(filter(lambda i: i[2] == c.name, one_to_many))
        if len(fs) > 0:
            sizes = [size for _, size, _, _ in fs]
            sizes_mean = sum(sizes)/len(fs)
            res_12_unsorted.append((c.name, sizes_mean))

    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\nЗадание Д3')
    res_13 = {}

    for c in catalogs:
        if c.name.lower().startswith('w'):
            fs = list(filter(lambda i: i[1] == c.name, many_to_many))
            f_name = [x for x, _ in fs]
            res_13[c.name] = f_name

    print(res_13)

if __name__ == '__main__':
    main()