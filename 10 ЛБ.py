def Zadacha_10_1():
    import json
    with open("10 лаба.json", "r", encoding="utf-8") as file:
        a = json.load(file)
        result = ''
        for i in a['products']:
            if i['available'] == True:
                avail = 'В наличии'
            else:
                avail = 'Нет в наличии!'
            result += f'Название: {i["name"]}\nЦена: {i["price"]}\nВес: {i["weight"]}\n{avail}\n\n'
        print(result)


def Zadacha_10_2():
    import json
    with open("10 лаба.json", "r+", encoding="utf-8") as file:
        a = json.load(file)

        b = {'name': input(str('Введите название продукта: ')),
             'price': input(str('Введите стоимость продукта: ')),
             'available': input(str('Введите наличие продукта(да, если есть в наличии): ')).lower() == 'да',
             'weight': input(str('Введите вес продукта: '))}
        a['products'].append(b)

        result = ''
        for i in a['products']:
            avail = 'В наличии' if i['available'] else 'Нет в наличии!'
            result += f'Название: {i["name"]}\nЦена: {i["price"]}\nВес: {i["weight"]}\n{avail}\n\n'
        print(result)
        file.truncate(0)
        file.seek(0)
        json.dump(a, file, ensure_ascii=False)


def Zadacha_10_3():
    with open ('en-ru.txt', 'r', encoding= 'utf-8') as file:
        txt = file.read()

    txt_list = txt.split('\n')
    dct = {}
    for i in txt_list:
        i = i.split(' - ')
        dct[i[1]] = i[0]
    print(sorted(dct.keys()))

    txt_out = ''
    for i in sorted(dct.keys()):
        txt_out += f'{i} - {dct[i]}\n'

    print(txt_out)
    open('ru-en.txt', 'w', encoding='utf-8').write(txt_out)


