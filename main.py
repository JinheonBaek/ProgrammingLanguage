class HomeAppliance(object):
    def __init__(self):
        self._status = None

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status
    
class WashingMachine(HomeAppliance):
    def __init__(self):
        self._status = None

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

class AirConditioner(HomeAppliance):
    def __init__(self):
        self._status = None

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

class Boiler(HomeAppliance):
    def __init__(self):
        self._status = None

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

class AirCleaner(HomeAppliance):
    def __init__(self):
        self._status = None

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

class Menu():
    def __init__(self):
        self._display_string = '''
[메뉴]
1. 가전제품 등록하기
2. 가전제품 등록 해제하기
3. 가전제품 상태 확인하기
4. 가전제품 상태 변경하기
0. 프로그램 종료하기
'''
        self._select = None
        self._choices = {
            1: self.add_appliance,
            2: self.del_appliance,
            3: self.check_appliance_status,
            4: self.change_appliance_status
        }

    def print_choice(self, choice = False):
        if choice == False: 
            choice = self._select
        
        action = self._choices.get(choice)
        action()

    def select(self):
        try:
            choice = int(input("메뉴를 선택해주세요: "))
            
            if 0 <= choice <= 4:
                self._select = choice
                return self._select
            else:
                raise ValueError

        except ValueError:
            return None

    def add_appliance(self):
        print("Add Appliance")

    def del_appliance(self):
        print("Delete Appliance")

    def check_appliance_status(self):
        print("Check Appliance Status")
    
    def change_appliance_status(self):
        print("Change Appliance Status")

    def __str__(self):
        return self._display_string


"""
Guide function that prints guideline of this software.
"""
def show_guideline():
    print("Guide")

def set_password():
    print("Set Master Password")

    return "1"

def main():
    show_guideline()
    password = set_password()
    
    menu = Menu()
    appliances = []

    while True:
        print(menu)

        choice = menu.select()

        if choice == 0:
            break
        elif choice == None:
            print("Input Number Error")
        else:
            menu.print_choice()
    
    # print("Hello world")
    # test = Boiler()
    # test.status = '1'
    # print(test.status)


if __name__ == '__main__':
    main()