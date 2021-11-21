def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for i in range(0, len(items)):
            print(items[i][args[0]])
    else:
        items_1 = {}
        for i in range(0, len(items)):
            for j in range(0, len(args)):
                items_1[args[j]] = (items[i][args[j]])
            print(items_1)

def main():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
        {'title': 'Кровать', 'price': 1800, 'color': 'red'},
        {'title': 'Часы настенные', 'price': 500, 'color': 'blue'},
        {'title': 'Шкаф', 'price': 1000, 'color': 'brown'}
    ]

    field(goods, 'title')
    print('')
    field(goods, 'title', 'price')
    print('')
    field(goods, 'title', 'price', 'color')

if __name__ == "__main__":
    main()