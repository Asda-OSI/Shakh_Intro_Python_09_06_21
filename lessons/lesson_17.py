class Unit:
    def __init__(self, name='none', clan='none'):
        self.name = name
        self.clan = clan
        self.hp = 100
        self._power = 1
        self._intelligence = 1
        self._dexterity = 1
        self._base_skill = 1

    def up_skill(self):
        self._base_skill += 1


class Mage(Unit):
    def __init__(self, name='none', clan='none', skill='storm'):
        super().__init__(name, clan)
        dict_skills = {
            'fire': 'fire',
            'water': 'water',
            'storm': 'storm'
        }
        self.skill = dict_skills[skill]

    @property
    def intelligence(self):
        self._intelligence = self._base_skill
        return self._intelligence


gendalf = Mage('Gendalf', 'Hummans', 'storm')
gendalf.up_skill()
print(gendalf.intelligence)

# class TD:
#     def __init__(self, q, w, e):
#         self.q = q
#         self.w = w
#         self._e = e
#
#     def __repr__(self):
#
