class Person(object):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name

class Customer(Person):
    def __init__(self, name):
        super(Customer, self).__init__(name)
        self._orderList = []

    @property
    def orderList(self):
        return self._orderList

    def make_order(self, orderList):
        self._orderList = [order() for order in orderList]
        self.print_order()

    def get_menu(self):
        return True

    def print_order(self):
        orderList = [order.name for order in self.orderList]
        
        for order in set(orderList):
            print("{} {}잔".format(order, orderList.count(order)), end=" ")
        print("주세요.\n")

class KoreaUniver(Customer):
    pass

class Youth(Customer):
    pass

class Employee(Person):
    def __init__(self, name):
        super(Employee, self).__init__(name)
        self._currentCustomer = None

    @property
    def currentCustomer(self):
        return self._currentCustomer

    @currentCustomer.setter
    def currentCustomer(self, customer):
        self._currentCustomer = customer
        
        print("\n{}님 안녕하세요, 전 주문을 도와드릴 바리스타 {}입니다.".format(customer, self))

    def print_menu(self, menus):
        print("\n저희 문벅스 고려대점의 메뉴와 가격, 그리고 소요시간은 다음과 같습니다.")
        print("*****" * 12)
        for menu in menus:
            print(menus[menu].description)
        print("*****" * 12)

    def get_time(self, customer):
        return sum([order.time for order in customer.orderList])

    def get_price(self, customer):
        discount_rate = 1

        if (customer.__class__ == KoreaUniver): 
            print("고려대생 할인이 적용되었습니다.")
            discount_rate = 0.8
        elif (customer.__class__ == Youth): 
            print("청소년 할인이 적용되었습니다.")
            discount_rate = 0.7

        return (int(sum([(order.price * discount_rate) for order in customer.orderList])))

