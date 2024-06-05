from pokemon import Pokemon


class Bulbasaur(Pokemon):

    def __init__(self, name, ability, moves, lvl, nature, iv, ev):
        super().__init__(1, 'Bulbasaur', name, 64, 0.7, 6.9, ability, moves,
                         ['Grass', 'Poison'], [45, 49, 49, 45, 65, 65], lvl, nature, iv, ev)
        pass
    pass


class Ivysaur(Pokemon):

    def __init__(self, name, ability, moves, lvl, nature, iv, ev):
        super().__init__(2, 'Ivysaur', name, 142, 1.0, 13.0, ability, moves,
                         ['Grass', 'Poison'], [60, 62, 63, 60, 80, 80], lvl, nature, iv, ev)
        pass
    pass


class Venusaur(Pokemon):

    def __init__(self, name, ability, moves, lvl, nature, iv, ev):
        super().__init__(3, 'Venusaur', name, 236, 2.0, 100.0, ability, moves,
                         ['Grass', 'Poison'], [80, 82, 83, 80, 100, 100], lvl, nature, iv, ev)
        pass
    pass


class Charmander(Pokemon):

    def __init__(self, name, ability, moves, lvl, nature, iv, ev):
        super().__init__(4, 'Charmander', name, 62, 0.6, 8.5, ability, moves,
                         ['Fire'], [39, 52, 43, 65, 60, 50], lvl, nature, iv, ev)
        pass
    pass


class Charmeleon(Pokemon):

    def __init__(self, name, ability, moves, lvl, nature, iv, ev):
        super().__init__(5, 'Charmeleon', name, 142, 1.1, 19.0, ability, moves,
                         ['Fire'], [58, 64, 58, 80, 80, 65], lvl, nature, iv, ev)
        pass
    pass


class Charizard(Pokemon):

    def __init__(self, name, ability, moves, lvl, nature, iv, ev):
        super().__init__(6, 'Charizard', name, 240, 1.7, 90.5, ability, moves,
                         ['Fire', 'Flying'], [78, 84, 78, 100, 109, 85], lvl, nature, iv, ev)
        pass
    pass


class Squirtle(Pokemon):

    def __init__(self, name, ability, moves, lvl, nature, iv, ev):
        super().__init__(7, 'Squirtle', name, 63, 0.5, 9.0, ability, moves,
                         ['Water'], [44, 48, 65, 43, 50, 64], lvl, nature, iv, ev)
        pass
    pass


class Wartortle(Pokemon):

    def __init__(self, name, ability, moves, lvl, nature, iv, ev):
        super().__init__(8, 'Wartortle', name, 142, 1.0, 22.5, ability, moves,
                         ['Water'], [59, 63, 80, 58, 65, 80], lvl, nature, iv, ev)
        pass
    pass


class Blastoise(Pokemon):

    def __init__(self, name, ability, moves, lvl, nature, iv, ev):
        super().__init__(9, 'Blastoise', name, 239, 1.6, 85.5, ability, moves,
                         ['Water'], [79, 83, 100, 78, 85, 105], lvl, nature, iv, ev)
        pass
    pass
