def Zadacha_9_1():
    from PIL import Image, ImageFilter
    from pathlib import Path
    Path('filters/').mkdir(exist_ok=True)
    for i in Path('Исходники/').iterdir():
        image = Image.open(str(i))
        image_new = image.filter(ImageFilter.SHARPEN)
        image_new.save('filters/' + str(i)[-5] + '_filtered.jpg')


def Zadacha_9_2():
    from PIL import Image, ImageFilter
    from pathlib import Path
    Path('filters/').mkdir(exist_ok=True)
    for i in list(Path('Исходники/').glob('*.jpg')) + list(Path('Исходники/').glob('*.png')):

        image = Image.open(str(i))
        image_new = image.filter(ImageFilter.SHARPEN)
        image_new.save('filters/' + str(i)[-5] + '_filtered.jpg')


def Zadacha_9_3():
    from pathlib import Path
    a = Path('9_3.csv').read_text()
    print(f'Исходный текст: \n{a}\n')

    b = a.split('\n')[1:4]
    print(f'Массив из исходного текста: \n{b}\n')

    result = 0
    itog = ''
    for i in b:
        c = i.split(',')
        result += int(c[1]) * int(c[2])
        itog += f'{c[0]} - {c[1]} шт. за {c[2]}руб.\n'
    itog += f'Итоговая стоимость: {result} руб.'
    print(itog)