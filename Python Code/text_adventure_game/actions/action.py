def get_random_action(self):
    import random
    from characters.mage import Mage
    from characters.warrior import Warrior

    actions = []
    if isinstance(self, Mage):
        actions = ['attack1', 'attack2', 'heal', 'defend']
    elif isinstance(self, Warrior):
        actions = ['attack1', 'attack2', 'defend']
    return random.choice(actions)