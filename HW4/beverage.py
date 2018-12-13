class Beverage(object):
    """
    Beverage Class, parent class to all other beverage classes.

    Attributes:
        name: beverage name.
        price: beverage price.
        time: time it takes to make beverage.
    """
    def __init__(self, name, price, time):
        self._name = name
        self._price = price
        self._time = time

    @property
    def name(self):
        ## Getter of the beverage name
        return self._name
    
    @property
    def price(self):
        ## Getter of the beverage price
        return self._price

    @property
    def time(self):
        ## Getter of the beverage time takes to make
        return self._time

class Americano(Beverage):
    """
    Americano Class, parent class is a Beverage class.

    description is a class variable that represent beverage info. \n
    Using super method, set name, price and time of the beverage.
    """
    description = "아메리카노의 가격은 3000원, 소요시간은 10초 입니다."

    def __init__(self):
        super(Americano, self).__init__("아메리카노", 3000, 10)

class CafeLatte(Beverage):
    """
    CafeLatte Class, parent class is a Beverage class.

    description is a class variable that represent beverage info. \n
    Using super method, set name, price and time of the beverage.
    """
    description = "카페라떼의 가격은 3500원, 소요시간은 12초 입니다."

    def __init__(self):
        super(CafeLatte, self).__init__("카페라떼", 3500, 12)

class Cappuccino(Beverage):
    """
    Cappuccino Class, parent class is a Beverage class.

    description is a class variable that represent beverage info. \n
    Using super method, set name, price and time of the beverage.
    """
    description = "카푸치노의 가격은 4000원, 소요시간은 13초 입니다."

    def __init__(self):
        super(Cappuccino, self).__init__("카푸치노", 4000, 13)

class VanillaLatte(Beverage):
    """
    VanillaLatte Class, parent class is a Beverage class.

    description is a class variable that represent beverage info. \n
    Using super method, set name, price and time of the beverage.
    """
    description = "바닐라라떼의 가격은 4000원, 소요시간은 13초 입니다."

    def __init__(self):
        super(VanillaLatte, self).__init__("바닐라라떼", 4000, 13)

class CafeMocha(Beverage):
    """
    CafeMocha Class, parent class is a Beverage class.

    description is a class variable that represent beverage info. \n
    Using super method, set name, price and time of the beverage.
    """
    description = "카페모카의 가격은 4500원, 소요시간은 15초 입니다."

    def __init__(self):
        super(CafeMocha, self).__init__("카페모카", 4500, 15)

class CaramelMaki(Beverage):
    """
    CaramelMaki Class, parent class is a Beverage class.

    description is a class variable that represent beverage info. \n
    Using super method, set name, price and time of the beverage.
    """
    description = "카라멜 마끼아또의 가격은 4500원, 소요시간은 15초 입니다."

    def __init__(self):
        super(CaramelMaki, self).__init__("카라멜마끼아또", 4500, 15)

class HotChocolate(Beverage):
    """
    HotChocolate Class, parent class is a Beverage class.

    description is a class variable that represent beverage info. \n
    Using super method, set name, price and time of the beverage.
    """
    description = "핫초코의 가격은 4000원, 소요시간은 10초 입니다."

    def __init__(self):
        super(HotChocolate, self).__init__("핫초코", 4000, 10)

class MintChocolate(Beverage):
    """
    MintChocolate Class, parent class is a Beverage class.

    description is a class variable that represent beverage info. \n
    Using super method, set name, price and time of the beverage.
    """
    description = "민트초코의 가격은 4500원, 소요시간은 12초 입니다."

    def __init__(self):
        super(MintChocolate, self).__init__("민트초코", 4500, 12)