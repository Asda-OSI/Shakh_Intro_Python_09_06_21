# В компьютерной игре есть юниты (персонажи).
# Каждый юнит имеет такие характеристики:
# имя
# клан
# здоровье    (int от 1 до 100. Начальное значение 100)
# сила        (int от 1 до 10. Начальное значение 1)
# ловкость    (int от 1 до 10. Начальное значение 1)
# интелект    (int от 1 до 10. Начальное значение 1)
#
# Каждый юнит может лечиться (увеличить свое здоровье на 10 пунктов, максимум 100) - написать метод увеличения здаровья.
#
# Есть три типа юнитов - маги, лучники и рыцари.
# У магов есть дополнительная характеристика - тип магии (воздух, огонь, вода)
# У лучников есть дополнительная характеристика - тип лука (лук, арбалет)
# У рыцарей есть дополнительная характеристика - тип оружия (меч, топор, пика)
#
# Каждый юнит может увеличить свой базовый навык на 1 пункт, максимум 10.
# Маг увеличивает интелект.
# Лучник увеличивает ловкость.
# Рыцарь увеличивает силу.
# Написать метод увеличения базового навыка (в родительском классе).
#
# Предложить свою реализацию классов Unit, Mage, Archer, Knight.


class Unit:
    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self.health = 100
        self.mana = 100
        self.strength = 1
        self.agility = 1
        self.intelligence = 1
        self.type = None

    def increase_health(self):
        if self.mana >= 10:
            self.mana -= 10
            if self.health > 90:
                self.health = 100
            else:
                self.health = self.health + 10

    def ability(self):
        if self.mana >= 10:
            self.mana -= 10
            if self.type == 'Mage':
                if self.intelligence > 9:
                    self.intelligence = 10
                else:
                    self.intelligence += 1
            elif self.type == 'Archer':
                if self.agility > 9:
                    self.agility = 10
                else:
                    self.agility += 1
            elif self.type == 'Knight':
                if self.strength > 9:
                    self.strength = 10
                else:
                    self.strength += 1


class Mage(Unit):
    def __init__(self, name, clan, magic='Air'):
        super().__init__(name, clan)
        self.type = 'Mage'
        if magic == 'Fire' or magic == 'Air' or magic == 'Water':
            self.magic = magic
        else:
            self.magic = 'Air'


class Archer(Unit):
    def __init__(self, name, clan, bow_type='Bow'):
        super().__init__(name, clan)
        self.type = 'Archer'
        if bow_type == 'Bow' or bow_type == 'Crossbow':
            self.bow = bow_type
        else:
            self.bow = 'Bow'


class Knight(Unit):
    def __init__(self, name, clan, weapon='Sword'):
        super().__init__(name, clan)
        self.type = 'Knight'
        self.health = 10
        if weapon == 'Sword' or weapon == 'Ax' or weapon == 'Lance':
            self.weapon = weapon
        else:
            self.weapon = 'Sword'


knight = Knight('knight', 'another_clan', 'Lancer')
