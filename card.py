class Card:
    def __init__(self, kind, name, cost = None, subtype = None):
        self.kind = kind
        self.name = name
        self.owner = None

        self.cost = cost
        self.subtype = subtype
        self.power = power
        self.toughness = toughness
        self.effect = effect

        self.attacked = False
        self.blocked = False

    def __str__(self):
        return '{} {}'.format(self.name, self.cost)

    def __repr__(self):
        return '{}'.format(self.name)

class Permanent(Card):
    def __init__(self):
        self.tapped = False

    def tap(self):
        self.tapped = True

    def untap(self):
        self.tapped = False

class Land(Permanent, color = None, ability = None):
    def tap_for_mana(self):
        created_mana = Mana(color)
        return created_mana

class Creature(Card, ):


class Sorcery(Card, effect):


class Intant(Card, effect):

class Artifact(Card,):

class Creature(Card,):
#deck = []
#for _ in range(20):
#    deck.append(Card('land', "Land"))
#for _ in range(6):
#    deck.append(Card('creature', "Bear", 2, 2))
#for _ in range(6):
#    deck.append(Card('creature', "Knight", 3, 3))
#for _ in range(4):
#    deck.append(Card('creature', "Elemental", 4, 4))
#for _ in range(2):
#    deck.append(Card('creature', "Vampire", 5, 5))
#    deck.append(Card('creature', "Dragon", 6, 6))

def find_by_name(zone, name):
    chosen_card = None
    for card in zone:
        if card.name == name:
            chosen_card = card
            break
    else:
        print("Did not find " + name + " in the zone.")
    return chosen_card
