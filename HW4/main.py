import random
import person, beverage

def make_random_order(menus):
    return random.choices(list(menus.values()), k = random.randrange(1, 10))

def processCustomerOrder(employ, customer, menus):
    employ.currentCustomer = customer
    
    if customer.get_menu():
        employ.print_menu(menus = menus)

    customer.make_order(make_random_order(menus))
    print("소요시간은 {}초 입니다.".format(employ.get_time(customer = employ.currentCustomer)))
    print("주문하신 음료에 대한 가격은 {}원 입니다.".format(employ.get_price(customer = employ.currentCustomer)))

def main():
    employList = [
        person.Employee('창기'),
        person.Employee('재용'),
        person.Employee('건형'),
        person.Employee('은혁')
    ]

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
    customerList = []

    ## Customer '시우' comes into the cafe
    customerList.append(person.Customer('시우'))

    for customer in customerList:
        processCustomerOrder(random.choice(employList), customer, menus)
        customerList = customerList[1:]

    ## Customer '소영', '진헌', '하윤' come into the cafe
    customerList.append(person.KoreaUniver('소영'))
    customerList.append(person.KoreaUniver('진헌'))
    customerList.append(person.Youth('하윤'))

    for customer in customerList:
        processCustomerOrder(random.choice(employList), customer, menus)
        customerList = customerList[1:]

    ## Customer '민준', '예준' come into the cafe
    customerList.append(person.Customer('민준'))
    customerList.append(person.Youth('예준'))

    for customer in customerList:
        processCustomerOrder(random.choice(employList), customer, menus)
        customerList = customerList[1:]

if __name__ == '__main__':
    main()
