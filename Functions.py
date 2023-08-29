from Classes import Army, Economy
import random


def start_a_war(army1: Army, economy1: Economy, army2: Army, economy2: Economy) -> None:
    if army2.number_of_soldiers <= 0 and army1.number_of_soldiers == 0:
        print(f"Невозможно начать войну, так как во обеих странах нет солдат.")
        return

    elif army1.number_of_soldiers <= 0:
        print(f"Армия страны {army1.country_name} побеждает, так как в армии страны {army2.country_name} нет солдат.")
        army2.fights_total += 1
        army1.fights_total += 1
        army1.fights_won += 1
        return

    elif army2.number_of_soldiers <= 0:
        print(f"Армия страны {army2.country_name} побеждает, так как в армии страны {army1.country_name} нет солдат.")
        army2.fights_total += 1
        army1.fights_total += 1
        army2.fights_won += 1
        return

    soldiers_lost1 = random.randint(0, army1.number_of_soldiers)
    soldiers_lost2 = random.randint(0, army2.number_of_soldiers)

    result1 = (army1.number_of_soldiers + army1.possible_number_of_recruits -
               soldiers_lost1) * army1.army_strength * (army1.army_money if army1.army_money > 0 else 1)
    result2 = (army2.number_of_soldiers + army2.possible_number_of_recruits -
               soldiers_lost2) * army2.army_strength * (army2.army_money if army2.army_money > 0 else 1)

    army1.fights_total += 1
    army2.fights_total += 1

    army1.number_of_soldiers -= soldiers_lost1
    army2.number_of_soldiers -= soldiers_lost2

    army1.population -= soldiers_lost1
    army2.population -= soldiers_lost2
    economy1.population -= soldiers_lost1
    economy2.population -= soldiers_lost2

    army1.loss_of_money += soldiers_lost1 * 5
    army2.loss_of_money += soldiers_lost2 * 5
    army1.army_money += soldiers_lost2 * 5 - soldiers_lost1 * 5
    army2.army_money += soldiers_lost1 * 5 - soldiers_lost2 * 5

    if result1 > result2:
        army1.fights_won += 1
        army2.fights_lost += 1
        print(f"Армия страны {army1.country_name} побеждает.")
    else:
        army2.fights_won += 1
        army1.fights_lost += 1
        print(f"Армия страны {army2.country_name} побеждает.")
    print(f"Армия страны {army1.country_name} потеряла {soldiers_lost1} солдат.")
    print(f"Армия страны {army2.country_name} потеряла {soldiers_lost2} солдат.")


def recruit_soldiers(army: Army, economy: Economy, amount: int) -> None:
    if army.possible_number_of_recruits < amount:
        print("Недостаточно свободных людей для рекрутинга.")
    else:
        army.number_of_soldiers += amount
        economy.number_of_soldiers += amount
        army.army_money += amount * 5
        economy.economy_money -= amount * 5
        army.economy_money -= amount * 5
        print(f"{amount} солдат были рекрутированы.")


def retire_soldiers(army: Army, economy: Economy, amount: int) -> None:
    if army.number_of_soldiers < amount:
        print("Недостаточно солдат для отправки в отставку.")
    else:
        army.number_of_soldiers -= amount
        economy.number_of_soldiers -= amount
        army.army_money -= amount * 5
        economy.economy_money += amount * 5
        army.economy_money += amount * 5
        print(f"{amount} солдат были отправлены в отставку.")


def buy_upgrades(economy: Economy, amount: int) -> None:
    if economy.economy_money < amount * economy.upgrade_cost:
        print(f"Недостаточно денег для покупки улучшений.")
    else:
        economy.economy_money -= amount * economy.upgrade_cost
        economy.economy_money += amount * 1000
        print("Улучшения куплены.")


def create_country(taken_names) -> tuple:
    army = Army()
    economy = Economy()
    rows = ["country_name", "population", "number_of_soldiers", "economy_money", "army_money", "upgrade_cost", "general"]
    for row in rows:
        info = input(f"Заполнение поля {row}: ")
        if row == "country_name":
            while info in taken_names or not info.isalpha():
                print('Страна с данным именем уже существует или имя не валидно.')
                info = input('Заполнение поля country_name: ')
            setattr(army, 'country_name', info)
            setattr(economy, 'country_name', info)
        elif row != "general":
            while not info.isdigit():
                print(f'Невалидное значение для поля {row}.')
                info = input(f"Заполнение поля {row}: ")
            if hasattr(army, row): setattr(army, row, int(info))
            if hasattr(economy, row): setattr(economy, row, int(info))
        else:
            while not info.isalpha():
                print(f'Невалидное значение для поля {row}.')
                info = input(f"Заполнение поля {row}: ")
            setattr(army, row, info)
    print(f"Страна успешно создана.")
    return army, economy


def print_army_info(army: Army):
    print('Количество военных:', army.number_of_soldiers)
    print('Возможное количество рекрутов:', army.possible_number_of_recruits)
    print('Количество денег:', army.army_money)
    print('Общее количество битв:', army.fights_total)
    print('Количество выигранных битв:', army.fights_won)
    print('Количество проигранных битв:', army.fights_lost)
    print('Генерал:', army.general)
    print('Сила армии:', army.army_strength)
    print('Убыток денег:', army.loss_of_money)


def print_economy_info(economy: Economy):
    print('Население страны:', economy.population)
    print('Мирное население:', economy.civilians)
    print('Деньги на экономику:', economy.economy_money)
    print('Текущий доход:', economy.current_income)
    print('Количество улучшений:', economy.number_of_upgrades)
    print('Стоимость улучшения:', economy.upgrade_cost)


def print_country_info(army: Army):
    print('Население страны:', army.population)
    print('Количество военных:', army.number_of_soldiers)
    print('Мирное население:', army.civilians)
    print('Деньги на экономику:', army.economy_money)
    print('Деньги на армию:', army.army_money)
    print('Название страны:', army.country_name)
    print('Доход:', army.income)

