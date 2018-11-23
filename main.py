import datetime

class HomeAppliance(object):
    def __init__(self, name, status):
        self._name = name
        self._status = status
        self._created_at = datetime.datetime.now()

    def __str__(self):
        return "가전제품 이름 - {0} / 가전제품 등록 일자 - {1}".format(self._name, self._created_at)

    @property
    def status(self):
        return "가전제품 이름 - {0} / 가전제품 상태 - {1} / 가전제품 등록 일자 - {2}".format(self._name, self._status, self._created_at)

    def start(self):
        self._status = "Start"

    def end(self):
        self._status = "Wait"
    
class WashingMachine(HomeAppliance):
    def __init__(self):
        super(WashingMachine, self).__init__("세탁기", "Wait")
        self._started_at = datetime.datetime.now()
        self._interval = 0

    @property
    def status(self):
        self.update()
        basic_status = super(WashingMachine, self).status
        
        if self._status == "Wait":
            return basic_status
        else:
            finished_at = self._started_at + datetime.timedelta(minutes = self._interval)
            return basic_status + ' / 잔여 시각 - {0}'.format(finished_at - datetime.datetime.now())

    def controller(self):
        try:
            print("[세탁 옵션] \n1. 행굼\n2. 표준\n3. 강력 세탁\n0. 메인메뉴로 돌아가기")

            choice = int(input("세탁 옵션을 선택 해주세요: "))
            
            if choice == 0:
                return
            elif 1 <= choice <= 3:
                if self._status == "Wait": 
                    self.start(interval = 0.1 * choice)
                else: 
                    print("현재 세탁 진행 중입니다.\n세탁이 완료된 후 다음 세탁을 이용 부탁드립니다.")
            else:
                raise ValueError('Input number range error')

        except ValueError as e:
            print(e)

    def start(self, interval):
        self._status = "Start"
        self._started_at = datetime.datetime.now()
        self._interval = interval

    def update(self):
        finished_at = self._started_at + datetime.timedelta(minutes = self._interval)
        
        if (finished_at <= datetime.datetime.now()):
            self._status = "Wait"

class AirConditioner(HomeAppliance):
    def __init__(self):
        super(AirConditioner, self).__init__("에어컨", "Wait")
        self._target_temperature = 0

    @property
    def status(self):
        basic_status = super(AirConditioner, self).status
        
        if self._status == "Wait":
            return basic_status
        else:
            return basic_status + ' / 현재 설정 온도 - {0}'.format(self._target_temperature)

    def controller(self):
        try:
            print("[에어컨 옵션] \n1. 에어컨 시작\n2. 에어컨 온도 조절\n3. 에어컨 종료\n0. 메인메뉴로 돌아가기")

            choice = int(input("에어컨 옵션을 선택 해주세요: "))
            
            if choice == 0:
                return
            elif choice == 1:
                if self._status == "Wait":
                    self.start()
                else:
                    print("현재 에어컨이 켜져있는 상태 입니다. 에어컨의 희망 온도는 {0} 입니다.".format(self._target_temperature))
            elif choice == 2:
                if self._status == "Wait":
                    print("현재 에어컨이 꺼져있는 상태 입니다. 에어컨을 킨 다음 이용 부탁드립니다.")
                else:
                    self.set_temperature()
            elif choice == 3:
                if self._status == "Wait":
                    print("현재 에어컨이 꺼져있는 상태 입니다.")
                else:
                    self.end()
            else:
                raise ValueError('Input number range error')

        except ValueError as e:
            print(e)

    def start(self):
        self._status = "Start"
        
        if self.set_temperature() == False:
            self._target_temperature = 24
            print("에어컨 온도 설정에 실패하여 에어컨을 기본온도(24도)로 시작하였습니다.")

    def set_temperature(self):
        try:
            print("에어컨 설정 온도 범위 (정수): 18 ~ 30")

            temperature = int(input("에어컨 온도를 설정 해주세요: "))
            
            if 18 <= temperature <= 30:
                self._target_temperature = temperature
                return True
            else:
                raise ValueError('Input number range error')

        except ValueError as e:
            print(e)
            return False

class Boiler(HomeAppliance):
    def __init__(self):
        super(Boiler, self).__init__("보일러", "Wait")
        self._target_temperature = 0

    @property
    def status(self):
        basic_status = super(AirConditioner, self).status
        
        if self._status == "Wait":
            return basic_status
        else:
            return basic_status + ' / 현재 설정 온도 - {0}'.format(self._target_temperature)

    def controller(self):
        try:
            print("[보일러] \n1. 보일러 시작\n2. 보일러 온도 조절\n3. 보일러 종료\n0. 메인메뉴로 돌아가기")

            choice = int(input("보일러 옵션을 선택 해주세요: "))
            
            if choice == 0:
                return
            elif choice == 1:
                if self._status == "Wait":
                    self.start()
                else:
                    print("현재 보일러가 켜져있는 상태 입니다. 보일러의 희망 온도는 {0} 입니다.".format(self._target_temperature))
            elif choice == 2:
                if self._status == "Wait":
                    print("현재 보일러가 꺼져있는 상태 입니다. 보일러를 킨 다음 이용 부탁드립니다.")
                else:
                    self.set_temperature()
            elif choice == 3:
                if self._status == "Wait":
                    print("현재 보일러가 꺼져있는 상태 입니다.")
                else:
                    self.end()
            else:
                raise ValueError('Input number range error')

        except ValueError as e:
            print(e)

    def start(self):
        self._status = "Start"
        
        if self.set_temperature() == False:
            self._target_temperature = 24
            print("보일러 온도 설정에 실패하여 보일러를 기본온도(24도)로 시작하였습니다.")

    def set_temperature(self):
        try:
            print("보일러 설정 온도 범위 (정수): 18 ~ 30")

            temperature = int(input("보일러 온도를 설정 해주세요: "))
            
            if 18 <= temperature <= 30:
                self._target_temperature = temperature
                return True
            else:
                raise ValueError('Input number range error')

        except ValueError as e:
            print(e)
            return False

class AirCleaner(HomeAppliance):
    def __init__(self):
        super(AirCleaner, self).__init__("공기청정기", "Wait")

    def controller(self):
        try:
            print("[공기청정기] \n1. 공기청정기 시작\n2. 공기청정기 종료\n0. 메인메뉴로 돌아가기")

            choice = int(input("공기청정기 옵션을 선택 해주세요: "))
            
            if choice == 0:
                return
            elif choice == 1:
                if self._status == "Wait":
                    self.start()
                else:
                    print("현재 공기청정기가 켜져있는 상태 입니다.")
            elif choice == 2:
                if self._status == "Wait":
                    print("현재 공기청정기가 꺼져있는 상태 입니다.")
                else:
                    self.end()
            else:
                raise ValueError('Input number range error')

        except ValueError as e:
            print(e)

class PasswordManager():
    def __init__(self):
        self._password = None
        self.set_password()
    
    def set_password(self):
        password = input("비밀번호를 입력해주세요: ")
        self._password = password

    def compare_password(self, password):
        if (self._password == password):
            return True
        else:
            return False

    def password_check(self):
        pass
        # password = input("비밀번호를 입력해주세요: ")

        # if self.compare_password(password):
        #     print("통과")
        #     return True
        # else:
        #     print("통과 X")
        #     return False
    
class Menu():
    def __init__(self):
        self._display_string = "[메뉴]\n1. 가전제품 등록하기\n2. 가전제품 등록 해제하기\n3. 가전제품 상태 확인하기\n4. 가전제품 상태 변경하기\n0. 프로그램 종료하기"
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

    def delete_appliance(self, appliances):
        if not appliances:
            print("Appliances list is empty")
            return
        
        print("[현재 등록되어 있는 가전제품 목록]")

        for index, appliance in enumerate(appliances):
            print(index, appliance, sep = '. ')

        try:
            choice = int(input("제거하실 가전제품 번호를 선택 해주세요: "))
            
            if 0 <= choice < len(appliances):
                appliances.pop(choice)
            else:
                raise ValueError('Input number range error')

        except ValueError as e:
            print(e)


    def check_appliance_status(self, appliances):
        if not appliances:
            print("Appliances list is empty")
            return

        print("Check Appliance Status")

        for index, appliance in enumerate(appliances):
            print(index, appliance.status, sep = '. ')

    
    def change_appliance_status(self, appliances):
        if not appliances:
            print("Appliances list is empty")
            return

        print("Change Appliance Status")
        self.check_appliance_status(appliances)

        try:
            choice = int(input("상태를 변경하실 가전제품 번호를 선택 해주세요: "))
            
            if 0 <= choice < len(appliances):
                appliances[choice].controller()
            else:
                raise ValueError('Input number range error')

        except ValueError as e:
            print(e)

    def __str__(self):
        return self._display_string

def main():
    menu = Menu()
    pw_manager = PasswordManager()

    appliances = []

    while True:
        print(menu)

        (message, err_detected) = menu.select()

        if err_detected == True:
            print(message)
            continue
        
        menu.print_choice(choice = message)

        if message == 0:
            break
        elif message == 1:
            if (pw_manager.password_check() == False): continue
            menu.add_appliance(appliances)
        elif message == 2:
            if (pw_manager.password_check() == False): continue
            menu.delete_appliance(appliances)
        elif message == 3:
            menu.check_appliance_status(appliances)
        elif message == 4:
            if (pw_manager.password_check() == False): continue
            menu.change_appliance_status(appliances)

if __name__ == '__main__':
    main()