import random
import person, beverage

def make_random_order(menus):
    """
    Make random orders (between 1 and 9 beverages). \n
    This function uses random sampling with replacement.
    
    Return:
        list of sampled beverages (not instanced yet)
    """
    return random.choices(list(menus.values()), k = random.randrange(1, 10))

def processCustomerOrder(employee, customer, menus):
    """
    Process customer with one selected employee. \n
    """

    ## Selected employee sets current customer
    employee.currentCustomer = customer
    
    ## Customer requests menu using get_menu() function
    ### In this setting, get_menu() return only true
    if customer.get_menu():
        employee.print_menu(menus = menus)

    ## Customer makes order with order list randomly produced
    customer.make_order(make_random_order(menus))
    ## Print time of the ordered beverages.
    ## After that, print price of the ordered beverages.
    print("소요시간은 {}초 입니다.".format(employee.get_time(customer = employee.currentCustomer)))
    print("주문하신 음료에 대한 가격은 {}원 입니다.".format(employee.get_price(customer = employee.currentCustomer)))

def main():
    ## employee list (our cafe shop has four employees)
    employeeList = [
        person.Employee('창기'),
        person.Employee('재용'),
        person.Employee('건형'),
        person.Employee('은혁')
    ]

    ## Beverage menus (out cafe shop has below beverages)
    menus = {
        'Americano': beverage.Americano,
        'CafeLatte': beverage.CafeLatte,
        'Cappuccino': beverage.Cappuccino,
        'VanillaLatte': beverage.VanillaLatte,
        'CafeMocha': beverage.CafeMocha,
        'CaramelMaki': beverage.CaramelMaki,
        'HotChocolate': beverage.HotChocolate,
        'MintChocolate': beverage.MintChocolate
    }

    ## Customer Queue
    ### Using append, new customer is comming
    ### Using customerList[1:], dequeue customer that ordered beverages
    customerList = []

    ## Customer '시우' comes into the cafe
    customerList.append(person.Customer('시우'))

    ## Process the customer in the queue.
    for customer in customerList:
        processCustomerOrder(random.choice(employeeList), customer, menus)
        customerList = customerList[1:]

    ## Customer '소영', '진헌', '하윤' come into the cafe
    customerList.append(person.KoreaUniver('소영'))
    customerList.append(person.KoreaUniver('진헌'))
    customerList.append(person.Youth('하윤'))

    ## Process the customer in the queue.
    for customer in customerList:
        processCustomerOrder(random.choice(employeeList), customer, menus)
        customerList = customerList[1:]

    ## Customer '민준', '예준' come into the cafe
    customerList.append(person.Customer('민준'))
    customerList.append(person.Youth('예준'))

    ## Process the customer in the queue.
    for customer in customerList:
        processCustomerOrder(random.choice(employeeList), customer, menus)
        customerList = customerList[1:]

if __name__ == '__main__':
    main()
