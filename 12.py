def Zadacha_12_1():
    class Restraurant:
        def __init__(self, restraurant_name='', cuisine_type='', restraurant_rating=0):
            self.restraurant_name = restraurant_name
            self.cuisine_type = cuisine_type
            self.restraurant_rating = restraurant_rating

        def describe_restraurant(self):
            print(f'Название ресторана: {self.restraurant_name}')
            print(f'Тип кухни: {self.cuisine_type}')

        def update_rating(self, restraurant_rating):
            self.restraurant_rating = restraurant_rating
            print(f'Новый рейтинг ресторана - {restraurant_rating}*')

        def open_restaurant(self):
            print('Ресторан открыт!')

    class IceCreamStand(Restraurant):
        flavors = ['пломбир', 'сливочное', 'молочное', 'фруктовый лёд', 'эскимо']

        def ice_cream_varieties(self):
            print(self.flavors)

    newIceCreamStand = IceCreamStand()
    newIceCreamStand.ice_cream_varieties()


#Zadacha_12_1()


def Zadacha_12_2():
    class Restraurant:
        def __init__(self, restraurant_name='', cuisine_type='', restraurant_rating=0):
            self.restraurant_name = restraurant_name
            self.cuisine_type = cuisine_type
            self.restraurant_rating = restraurant_rating

        def describe_restraurant(self):
            print(f'Название ресторана: {self.restraurant_name}')
            print(f'Тип кухни: {self.cuisine_type}')

        def update_rating(self, restraurant_rating):
            self.restraurant_rating = restraurant_rating
            print(f'Новый рейтинг ресторана - {restraurant_rating}*')

        def open_restaurant(self):
            print('Ресторан открыт!')

    class IceCreamStand(Restraurant):
        flavors = ['пломбир', 'фруктовый лёд', 'эскимо']
        location = ''
        working_hours = ''

        def ice_cream_varieties(self):
            print(self.flavors)

        def add_flavor(self, value):
            self.flavors.append(value)

        def remove_flavor(self, value):
            try:
                self.flavors.remove(value)
            except:
                print('Такого сорта нет в наличии')

        def is_flavor_exist(self, value):
            print('Такой сорт есть в наличии') if value in self.flavors else print('Такого сорта нет в наличии')

    class Plombier(IceCreamStand):
        cone_size = '1'

        def ice_cream_cone_size(self):
            print(self.cone_size)

    class Fruit_Ice(IceCreamStand):
        ice_flavor = 'Лимонный'

        def fruit_ice_flavor(self):
            print(self.ice_flavor)

    class Popsicle(IceCreamStand):
        chocolate_variety = 'Молочный'

        def popsicle_chocolate_variety(self):
            print(self.chocolate_variety)

    newIceCreamStand = IceCreamStand()

    newIceCreamStand.working_hours = str(input('Введите время открытия и закрытия заведения\n'))
    newIceCreamStand.location = str(input('Введите описание локации заведения\n'))

    newIceCreamStand.add_flavor(str(input('Введите новый сорт мороженного\n')))
    newIceCreamStand.remove_flavor(str(input('Введите сорт мороженного, который необходимо удалить\n')))
    newIceCreamStand.is_flavor_exist(str(input('Введите сорт мороженного, который необходимо проверить\n')))
    newIceCreamStand.ice_cream_varieties()

    newPlombier = Plombier()
    newPlombier.ice_cream_cone_size()

    newFruit_Ice = Fruit_Ice()
    newFruit_Ice.fruit_ice_flavor()

    newPopsicle = Popsicle()
    newPopsicle.popsicle_chocolate_variety()


#Zadacha_12_2()


def Zadacha_12_3():
    import tkinter as tk

    class Restraurant:
        def __init__(self, restraurant_name='', cuisine_type='', restraurant_rating=0):
            self.restraurant_name = restraurant_name
            self.cuisine_type = cuisine_type
            self.restraurant_rating = restraurant_rating

        def describe_restraurant(self):
            print(f'Название ресторана: {self.restraurant_name}')
            print(f'Тип кухни: {self.cuisine_type}')

        def update_rating(self, restraurant_rating):
            self.restraurant_rating = restraurant_rating
            print(f'Новый рейтинг ресторана - {restraurant_rating}*')

        def open_restaurant(self):
            print('Ресторан открыт!')

    class IceCreamStand(Restraurant):
        flavors = ['пломбир', 'фруктовый лёд', 'эскимо']
        location = ''
        working_hours = ''

        def ice_cream_varieties(self):
            print(self.flavors)

        def add_flavor(self, value):
            self.flavors.append(value)

        def remove_flavor(self, value):
            try:
                self.flavors.remove(value)
            except:
                print('Такого сорта нет в наличии')

        def is_flavor_exist(self, value):
            print('Такой сорт есть в наличии') if value in self.flavors else print('Такого сорта нет в наличии')

    newIceCreamStand = IceCreamStand()
    flavor_txt = ''.join(f'{i+1}) {val}\n' for i, val in enumerate(newIceCreamStand.flavors))
    window = tk.Tk()
    window.title("Лавка с мороженным")
    cnv = tk.Canvas(window, width=500, height=500, background='Pink')
    cnv.pack()
    cnv.create_rectangle(100, 100, 400, 300, fill='White', outline='Pink')
    cnv.create_text(250, 200, text=flavor_txt, font=('Arial', 20), fill='Black')
    cnv.mainloop()


#Zadacha_12_3()