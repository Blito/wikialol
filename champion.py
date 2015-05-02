from decimal import *

class Champion:
    def __init__(self, data_la, data_na = None, data_eu = None):
        stats = data_la['stats']
        self.disp_name = data_la['name']
        self.ms = stats['movespeed']
        self.range = stats['attackrange']
        self.attack_delay = stats['attackspeedoffset']
        self.as_base = str(Decimal(0.625 / (1 + self.attack_delay)).quantize(Decimal('1.000')))
        self.dam_base = stats['attackdamage']
        self.arm_base = stats['armor']
        self.mr_base = stats['spellblock']
        self.hp_base = stats['hp']
        self.mp_base = stats['mp']
        self.hp5_base = stats['hpregen']
        self.mp5_base = stats['mpregen']
        self.as_lvl = stats['attackspeedperlevel']
        self.dam_lvl = stats['attackdamageperlevel']
        self.arm_lvl = stats['armorperlevel']
        self.mr_lvl = stats['spellblockperlevel']
        self.hp_lvl = stats['hpperlevel']
        self.mp_lvl = stats['mpperlevel']
        self.hp5_lvl = stats['hpregenperlevel']
        self.mp5_lvl = stats['mpregenperlevel']
        self.image = self.disp_name.replace('.', '').replace(' ', '') + 'Square.png'
        self.title = data_la['title']
        self.herotype = data_la['tags'][0]
        self.alttype = str((len(data_la['tags']) > 1 and data_la['tags'][1]) or '')
        self.rangetype = ''
        self.date = ''
        self.patch = ''
        self.health = data_la['info']['defense']
        self.attack = data_la['info']['attack']
        self.spells = data_la['info']['magic']
        self.difficulty = data_la['info']['difficulty']
        self.ip = ''
        self.rp = ''
    #     if data_na and data_eu:
    #         self.__spells = {'Q': Spell(data_la['spells'][0], data_na['spells'][0], data_eu['spells'][0]),
    #                         'W': Spell(data_la['spells'][1], data_na['spells'][1], data_eu['spells'][1]),
    #                         'E': Spell(data_la['spells'][2], data_na['spells'][2], data_eu['spells'][2]),
    #                         'R': Spell(data_la['spells'][3], data_na['spells'][3], data_eu['spells'][3])}
    #         self.passive = Passive(data_la['passive'], data_na['passive'], data_eu['passive'])
    #     else:
    #         self.__spells = {'Q': Spell(data_la['spells'][0],
    #                         'W': Spell(data_la['spells'][1],
    #                         'E': Spell(data_la['spells'][2],
    #                         'R': Spell(data_la['spells'][3]}
    #         self.passive = Passive(data_la['passive'])
    #
    # def get_spell(self, key):
    #     return self.__spells[key.upper()]
