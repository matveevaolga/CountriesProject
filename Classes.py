from abc import ABC


class Country(ABC):
    def __init__(self, population: int = 0, number_of_soldiers: int = 0, economy_money: int = 0,
                 army_money: int = 0, country_name: str = 'Unknown') -> None:
        self.population = population
        self.number_of_soldiers = number_of_soldiers
        self.economy_money = economy_money
        self.army_money = army_money
        self.country_name = country_name
        self.income = self.economy_money

    @property
    def civilians(self):
        return self.population - self.number_of_soldiers


class Army(Country):
    def __init__(self, general: str = 'Unknown', **kwargs) -> None:
        super().__init__(**kwargs)
        self.general = general
        self.fights_total = 0
        self.fights_won = 0
        self.fights_lost = 0
        self.loss_of_money = 0

    @property
    def army_strength(self) -> float:
        return self.number_of_soldiers * (1 + self.fights_total / 100) * (2 + self.fights_won / 100)

    @property
    def possible_number_of_recruits(self) -> int:
        difference = self.population // 2 - self.civilians if self.population // 2 < self.civilians else 0
        return self.civilians + difference


class Economy(Country):
    def __init__(self, upgrade_cost: int = 0, **kwargs) -> None:
        super().__init__(**kwargs)
        self.upgrade_cost = upgrade_cost
        self.number_of_upgrades = 0

    @property
    def current_income(self) -> int:
        return self.income + self.number_of_upgrades * 1000
