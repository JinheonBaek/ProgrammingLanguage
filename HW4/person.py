class Person(object):
    def __init__(self, name, nickname):
        self._name = name
        self._nickname = nickname

class Customer(Person):
    pass

class KoreaUniver(Customer):
    pass

class Youth(Customer):
    pass

class Employee(Person):
    def __init__(self, name, nickname):
        super(Employee, self).__init__(name, nickname)