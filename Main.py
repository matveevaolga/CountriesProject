import Functions

countries = {}
commands = {1: 'Создать страну', 2: 'Информация о стране', 3: 'Информация об экономике страны',
            4: 'Информация об армии страны', 5: 'Начать войну', 6: 'Рекрутировать солдат',
            7: 'Отправить солдат в отставку', 8: 'Купить улучшения', 9: 'Выйти'}


def country_choice(taken_n=-1) -> int:
    print('Выберите страну:')
    for numb, name in zip(range(1, len(countries) + 1), countries.keys()):
        print(numb, ': ', name, sep='')
    n = input()
    while not n.isdigit() or int(n) not in range(1, len(countries) + 1) or n == taken_n:
        print('Неверный номер страны.')
        n = input('Выберите страну: ')
    return int(n) - 1


while True:
    print('Выберите номер команды: ')
    for numb, comm in commands.items():
        print(numb, ': ', comm, sep='')
    command = input()
    if not len(countries) and command != '1':
        print('Вы еще не создали ни одной страны.')
        continue
    match command:
        case '1':
            army, country = Functions.create_country(list(countries.keys()))
            countries[army.country_name] = [army, country]
        case '2':
            n = country_choice()
            country = list(countries.keys())[n]
            Functions.print_country_info(countries[country][0])
        case '3':
            n = country_choice()
            country = list(countries.keys())[n]
            Functions.print_economy_info(countries[country][1])
        case '4':
            n = country_choice()
            country = list(countries.keys())[n]
            Functions.print_army_info(countries[country][0])
        case '5':
            if len(countries) == 1:
                print(f'Стране {list(countries.keys())[0]} не с кем воевать.')
                continue
            print('Выбор первой воюющей страны:')
            n1 = country_choice()
            army1, economy1 = countries[list(countries.keys())[n1]]
            print('Выбор второй воюющей страны:')
            n2 = country_choice(n1)
            army2, economy2 = countries[list(countries.keys())[n2]]
            Functions.start_a_war(army1, economy1, army2, economy2)
        case '6':
            n = country_choice()
            country = list(countries.keys())[n]
            amount = input('Введите количество солдат для рекрутинга: ')
            while not amount.isdigit():
                print('Невалидное количество солдат для рекрутинга.')
                amount = input('Введите количество солдат для рекрутинга: ')
            army, economy = countries[country]
            Functions.recruit_soldiers(army, economy, int(amount))
        case '7':
            n = country_choice()
            country = list(countries.keys())[n]
            amount = input('Введите количество солдат для отправки в отставку: ')
            while not amount.isdigit():
                print('Невалидное количество солдат для отправки в отставку.')
                amount = input('Введите количество солдат для отправки в отставку: ')
            army, economy = countries[country]
            Functions.retire_soldiers(army, economy, int(amount))
        case '8':
            n = country_choice()
            country = list(countries.keys())[n]
            amount = input('Введите количество улучшений: ')
            while not amount.isdigit():
                print('Невалидное количество улучшений.')
                amount = input('Введите количество улучшений: ')
            Functions.buy_upgrades(countries[country][1], int(amount))
        case '9':
            break
        case _:
            print('Неверный номер команды.')
