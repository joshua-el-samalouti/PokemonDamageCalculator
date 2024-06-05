import math


class Pokemon:
    def __init__(self, dex_id, species, name, base_xp, height, weight, ability, moves, types,
                 base_stats, lvl, nature, iv, ev):
        self.dex_id = dex_id
        self.species = species
        self.name = name
        self.base_xp = base_xp
        self.height = height
        self.weight = weight
        self.ability = ability
        self.moves = moves
        self.types = types
        self.base_stats = base_stats
        self.eva = 1
        self.acc = 1
        if lvl < 1 or lvl > 100:
            raise ValueError("Level must be between 1 and 100")
        else:
            self.lvl = lvl
        if any(iv) < 0 or any(iv) > 31:
            raise ValueError("IV must be between 0 and 31")
        else:
            self.iv = iv
        if any(ev) < 0 or any(ev) > 255:
            raise ValueError("EV must be between 0 and 255")
        elif sum(ev) > 508:
            raise ValueError("Total EV cannot exceed 508")
        else:
            self.ev = ev
        natures = {'hardy': 0,
                   'lonely': 1,
                   'brave': 2,
                   'adamant': 3,
                   'naughty': 4,
                   'bold': 5,
                   'docile': 6,
                   'relaxed': 7,
                   'impish': 8,
                   'lax': 9,
                   'timid': 10,
                   'hasty': 11,
                   'serious': 12,
                   'jolly': 13,
                   'naive': 14,
                   'modest': 15,
                   'mild': 16,
                   'quiet': 17,
                   'bashful': 18,
                   'rash': 19,
                   'calm': 20,
                   'gentle': 21,
                   'sassy': 22,
                   'careful': 23,
                   'quirky': 24}
        if nature in natures.keys():
            self.nature = nature
            nat_val = natures[nature]
            nat_vals = [int(math.floor(nat_val/5))+1, (nat_val % 5)+1]
        else:
            raise ValueError('\''+nature+'\' is not a valid nature')
        self.stats = []
        if dex_id == 292:
            self.stats[0] = 1
        else:
            self.stats[0] = ((((2 * self.base_stats[0] + self.iv[0] + (self.ev[0] / 4)) * self.lvl) / 100)
                             + self.lvl + 10)
        for i in range(1, 6):
            self.stats[i] = (((2 * self.base_stats[i] + self.iv[i] + (self.ev[i] / 4)) * self.lvl) / 100) + 5
        self.stats[nat_vals[0]] = self.stats[nat_vals[0]] * 1.1
        self.stats[nat_vals[1]] = self.stats[nat_vals[1]] * 0.9
        self.hp = self.stats[0]
        self.pha = self.stats[1]
        self.phd = self.stats[2]
        self.spe = self.stats[3]
        self.spa = self.stats[4]
        self.spd = self.stats[5]
        self.status = 0
        self.item = 0
        # TODO Leveling: EV Yield, Leveling Rate, Evolution
        # TODO Pokédex: Description
        # TODO Breeding: Egg Groups, Hatch Time
        # TODO Catching: Catch Rate
        # TODO Expanded Info: Egg Groups
        # TODO Development: Abilities, Learnable Abilities
    pass



