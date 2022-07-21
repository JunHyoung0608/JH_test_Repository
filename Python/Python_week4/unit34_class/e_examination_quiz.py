class Annie:
    def __init__(self, *args):
        self.health = args[0]
        self.mana = args[1]
        self.ap = args[2]

    def tibbers(self):
        self.attack = float(self.ap) * 0.65 + 400.0
        print('티버: 피해량 {0}'.format(self.attack))

data = list(map(float, input().split()))
annie = Annie(*data)
annie.tibbers