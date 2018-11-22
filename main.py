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

class PasswordManager():
    def __init__(self):
        self._password = None
    
    def set_password(self, password):
        self._password = password

    def compare_password(self, password):
        if (self._password == password):
            return True
        else:
            return False
    


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
            0: lambda: print("\n프로그램을 종료합니다. \n이용해 주셔서 감사합니다."),
            1: lambda: print("\n가전제품 등록하기를 선택 하셨습니다."),
            2: lambda: print("\n가전제품 등록 해제하기를 선택 하셨습니다."),
            3: lambda: print("\n가전제품 상태 확인하기를 선택 하셨습니다."),
            4: lambda: print("\n가전제품 상태 변경하기를 선택 하셨습니다.")
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
                return (self._select, False)
            else:
                raise ValueError('Input number range error')

        except ValueError as e:
            return (e, True)

    def add_appliance(self, appliances):
        print("[가전제품 목록]")
        print("1. 세탁기")
        print("2. 에어컨")
        print("3. 보일러")
        print("4. 공기청정기")

        try:
            choice = int(input("추가하실 가전제품 목록을 선택 해주세요: "))
            
            if choice == 1:
                appliances.append(WashingMachine())
            elif choice == 2:
                appliances.append(AirConditioner())
            elif choice == 3:
                appliances.append(Boiler())
            elif choice == 4:
                appliances.append(AirCleaner())
            else:
                raise ValueError('Input number range error')

        except ValueError as e:
            print(e)



    def delete_appliance(self):
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


def main():
    show_guideline()
    
    menu = Menu()
    pw_manager = PasswordManager()
    
    appliances = []

    while True:
        print(menu)

        (message, err_detected) = menu.select()

        if err_detected == True:
            print(message)
        else:
            menu.print_choice(choice = message)

            if message == 0:
                break
            if message == 1:
                menu.add_appliance(appliances)
                print(appliances)



    
    # print("Hello world")
    # test = Boiler()
    # test.status = '1'
    # print(test.status)


if __name__ == '__main__':
    main()