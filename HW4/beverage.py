class Beverage(object):
    def __init__(self, name, price, time):
        self._name = name
        self._price = price
        self._time = time
    
    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self._price

    @property
    def time(self):
        return self._time

class Americano(Beverage):
    def __init__(self):
        super(Americano, self).__init__("아메리카노", 3000, 10)

class CafeLatte(Beverage):
    def __init__(self):
        super(CafeLatte, self).__init__("카페라떼", 3500, 12)

class Cappuccino(Beverage):
    def __init__(self):
        super(Cappuccino, self).__init__("카푸치노", 4000, 13)

class VanillaLatte(Beverage):
    def __init__(self):
        super(VanillaLatte, self).__init__("바닐라라떼", 4000, 13)

class CafeMocha(Beverage):
    def __init__(self):
        super(CafeMocha, self).__init__("카페모카", 4500, 15)

class CaramelMaki(Beverage):
    def __init__(self):
        super(CaramelMaki, self).__init__("카라멜 마끼아또", 4500, 15)

class HotChocolate(Beverage):
    def __init__(self):
        super(HotChocolate, self).__init__("핫초코", 4000, 10)

class MintChocolate(Beverage):
    def __init__(self):
        super(MintChocolate, self).__init__("민트초코", 4500, 12)