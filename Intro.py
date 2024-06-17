#2.1 Классы, объекты, экземпляры классов
# class Car:
#   model = "BMW"
#   engine = 1.6
#
# a = Car()
# b = Car()
#
# print(a.model)
# print(b.model)
#
# b.model = "VAZ"  # Изменяем значение атрибута model в ЭК
# b.color = 'white'  # Добавляем новый атрибут в ЭК
# print(b.model, b.color)  # Вывод: VAZ white
#
# class Contact:
#     name = 'Barak'
#     phone_number = '+1 202 345 4564'
# b =  Contact()
#
# class Animal:
#     pass
# lion = Animal()
# print(isinstance(lion, Animal))


#2.2 Атрибуты класса
# class Person:
#   name = 'Jared'
#   age = 30
#
# print(getattr(Person, 'salary', 'Нет такого атрибута'))
# print(getattr(Person, 'salary', 100))
#
# print(Person.__dict__)
#
# print(hasattr(Person, 'name'))
#
# print(Person.name)
# Person.name = 'Michail'
# print(Person.name)
#
# Person.money = 100
# Person.phone = '+1 202 777 xxx'
# print(Person.__dict__)
# print(Person.money)
# print(Person.phone)
#
# setattr(Person, 'money', 200)
# setattr(Person, 'phone', '+1 202 777 xxx')
# print(Person.__dict__)
# print()
# setattr(Person, 'name', 'Vasya')
# setattr(Person, 'age', '43')
# print(Person.__dict__)
#
# print(Person.__dict__)
# print()
# delattr(Person, 'age')
# print(Person.__dict__)
# print()
# del Person.money
# print(Person.__dict__)
#
# class Book:
#     name = '1984'
#     writer = 'Джордж Оруэлл'
#     pages = 213
#
# print(Book.name)
# print(Book.writer)
#
# print(getattr(Book, 'writer'))
# print(getattr(Book, 'pages'))
#
# setattr(Book, 'name', 'Скотный двор')
# setattr(Book, 'pages', 115)
#
# setattr(Book, 'rating', 8.7)
# Book.genre = 'dystopian'
#
# delattr(Book, 'pages')
# delattr(Book, 'writer')
# delattr(Book, 'rating')
# #del (Book.writer, Book.rating)
#
# class Cat:
#     name = 'Матроскин'
#     color = 'black'
# my_cat = Cat()
#
# class Empty:
#     pass
# my_list = [
#     ('apple', 23),
#     ('banana', 80),
#     ('cherry', 13),
#     ('date', 10),
#     ('elderberry', 4),
#     ('fig', 65),
#     ('grape', 5),
#     ('honeydew', 7),
#     ('kiwi', 1),
#     ('lemon', 10),
# ]
#
# for i in my_list:
#     setattr(Empty, i[0], i[1])
# [setattr(Empty, *tup) for tup in my_list]
# [setattr(Empty,i[0],i[1]) for i in my_list]
#
# class Duck:
#     weight = 5
#     height = 10
# def is_obj_has_attr(c, t):
#     return hasattr(c,t)
# if hasattr(Duck, 'weight'):
#     print('Атрибут age присутствует')
# print(is_obj_has_attr(Duck, 'weight'))
# print(is_obj_has_attr(Duck, 'name'))
# print(is_obj_has_attr(Duck, 'height'))
#
# class Person:
#     name = "John Smith"
#     age = 30
#     gender = "male"
#     address = "123 Main St"
#     phone_number = "555-555-5555"
#     email = "johnsmith@example.com"
#     is_employed = True
# #text = input().split()
# [print(f'{i}-YES' if getattr(Person, i.lower(), 0) else f'{i}-NO') for i in input().split()]
# for i in input().split():
#     if hasattr(Person, i.lower()):
#         print(f'{i}-YES')
#     else:
#         print(f'{i}-NO')
#
# for i in s:
#     print(f"{i}-{['NO', 'YES'][hasattr(Person, i.lower())]}")

#2.3 Атрибуты экземпляра класса
# class Person:
#     name = 'Ivan'
#     age = 30
#
# man = Person()    # Создаём ЭК и связываем его с переменной man
# print(man.age)    # Получаем текущее значение атрибута age в ЭК man
# man.money = 100   # Создаём в ЭК атрибут money со значением 100
# print(man.money)  # Получаем текущее значение атрибута money в ЭК man
# man.money = 250   # Изменяем текущее значение атрибута money в ЭК man на 250
# print(man.money)  # Получаем текущее значение атрибута money в ЭК man
# delattr(man, 'money')  # Удаляем атрибут money из ЭК
# print(hasattr(man, 'money'))  # Проверяем наличие атрибута money в ЭК man: False
#
# man = Person()
# print(man.__dict__)# Печатает пустой словарь: {}
# man.name = 'Alex'
# print(man.__dict__)# Печатает словарь: {'name': 'Alex'}
#
# man = Person()
# print('Атрибуты ЭК man:', man.__dict__)
# man.name = 'Alex'
# print('Атрибуты ЭК man:', man.__dict__)
# dude = Person()
# print('Атрибуты ЭК people:', dude.__dict__)
# dude.name = 'Sergey'
# print('Атрибуты ЭК people:', dude.__dict__)
#
# man = Person()
# man.name = 'Alex'
# print(Person.name, man.name) # Печатает «Ivan Alex»
# del man.name
# print(Person.name, man.name) # Печатает «Ivan Ivan»
#
# class SuperHero:
#     pass
# batman = SuperHero()
# batman.can_fly = False
# batman.damage = 175
#
# superman = SuperHero()
# superman.can_fly = True
# superman.damage = 285
# superman.alter_ego = 'Кларк Кент'
#
# class Config:
#     pass
# def create_instance(n: int) -> Config:
#     test = Config()
#     for i in range(1, n+1):
#         setattr(test, f'attribute{i}', f'value{i}')
#     return test
# # Ниже расположены проверки для функции create_instance
#
# config_2 = create_instance(2)
# assert isinstance(config_2, Config)
# assert config_2.__dict__ == {'attribute1': 'value1', 'attribute2': 'value2'}
# print('good')
#
#
# def create_instance(n: int) -> Config:
#     obj = Config()
#     obj.__dict__ = {f'attribute{i}': f'value{i}' for i in range(1, n + 1)}
#     return obj
#
#
# def create_instance(num):
#     obj = Config()
#     for i in range(1, num + 1):
#         obj.__dict__[f'attribute{str(i)}'] = f'value{str(i)}'
#     return obj

#2.4 Функции как атрибут класса

# class Car:
#     model = "BMW"
#     engine = 1.6
#     def drive():
#         print("Let's go")
# print(Car.__dict__)
# Car.drive()
# getattr(Car, 'drive')()
#
# class Car:
#   model = "BMW"
#   engine = 1.6
#   @staticmethod
#   def drive():
#     print("Let's go")
# a = Car()
# b = Car()
# Car.drive()
# getattr(Car, 'drive')()
# a.drive()
# b.drive()







print('test')