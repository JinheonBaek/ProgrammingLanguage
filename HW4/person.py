class Person(object):
    """
    Person Class, parent class to all other person classes.

    Attributes:
        name: person name.
    """
    def __init__(self, name):
        self._name = name

    def __str__(self):
        ## Getter of the person name.
        return self._name

class Customer(Person):
    """
    Customer Class, parent class is a Person class.

    Attributes:
        Using super method, set name of the person.
        Make orderList with blank (that variable will be used to hold list of order instance).
    """
    def __init__(self, name):
        super(Customer, self).__init__(name)
        self._orderList = []

    @property
    def orderList(self):
        ## Getter of the customer's order list
        return self._orderList

    def get_menu(self):
        ## Whether customer wants are not menu list
        ### In this setting, customer only returns True,
        ### But if we set return variable as False, menu is not printed to the customer.
        return True

    def make_order(self, orderList):
        ## Customer makes order with parameter orderList
        ### Instance all orderList, and customer holds instanced order list.
        ### After instantiation, print orders of the customer.
        self._orderList = [order() for order in orderList]
        self.print_order()

    def print_order(self):
        ## Print orders of the customer
        ### In self.orderList, duplicate beverages are listed with different memory address,
        ### And using name of the each beverage, makes orderList countable.
        orderList = [order.name for order in self.orderList]
        
        for order in set(orderList):
            print("{} {}잔".format(order, orderList.count(order)), end=" ")
        print("주세요.\n")

class KoreaUniver(Customer):
    """
    KoreaUniver Class, parent class is a Customer class.

    Distinguish Korea University Student with others using class name. (instance.__class__)
    """
    pass

class Youth(Customer):
    """
    Youth Class, parent class is a Customer class.

    Distinguish Youth with others using class name. (instance.__class__)
    """
    pass

class Employee(Person):
    """
    Employee Class, parent class is a Person class.

    Attributes:
        Using super method, set name of the person.
        Init currentCustomer None (this variable will be used to hold current customer is who)
    """
    def __init__(self, name):
        super(Employee, self).__init__(name)
        self._currentCustomer = None

    @property
    def currentCustomer(self):
        ## Getter of the current customer
        return self._currentCustomer

    @currentCustomer.setter
    def currentCustomer(self, customer):
        ## Setter of the current customer,
        ### After set current customer, print employee name to current customer
        self._currentCustomer = customer
        
        print("\n{}님 안녕하세요, 전 주문을 도와드릴 바리스타 {}입니다.".format(customer, self))

    def print_menu(self, menus):
        ## Print menus of the coffe shop
        ### parameter menus has list of the menus,
        ### And print menu in list(menus) using class variable (class.description).
        print("\n저희 문벅스 고려대점의 메뉴와 가격, 그리고 소요시간은 다음과 같습니다.")
        print("*****" * 12)
        for menu in menus:
            print(menus[menu].description)
        print("*****" * 12)

    def get_time(self, customer):
        ## Return sum of the time to make all beverages that customer requests.
        return sum([order.time for order in customer.orderList])

    def get_price(self, customer):
        ## Return sum of the price of all beverages that customer requests.
        ### If customer is a Korea University Student, set discount_rate 0.2
        ### If customer is a Youth, set discount_rate 0.3
        ### Others, set discount_rate 0
        discount_rate = 0

        if (customer.__class__ == KoreaUniver): 
            print("고려대생 할인이 적용되었습니다.")
            discount_rate = 0.2
        elif (customer.__class__ == Youth): 
            print("청소년 할인이 적용되었습니다.")
            discount_rate = 0.3

        return (int(sum([(order.price * (1 - discount_rate)) for order in customer.orderList])))

