

class All:
    def test(self, player):  
        return True


class Not:
    def __init__(self, matcher):
        self._matcher = matcher

    def test(self, player):
        return not self._matcher.test(player)


class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)
        return player_value < self._value

class Or:
    def __init__(self, *funktiota):
        self._funktioita = funktiota

    def test(self, player):
        for funktio in self._funktioita:
            if funktio.test(player):
                return True
        return False
