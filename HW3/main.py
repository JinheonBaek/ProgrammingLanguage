# try-except
# When import libraries, check library is already exist on you local enviroment. 
try:
    import re
    import datetime
except:
    print("re 또는 datetime library 가 없습니다.")
    print("실행 중 라이브러리가 존재하지 않아 예외처리가 발생하여 프로그램이 종료될 수 있습니다.")

class HomeAppliance(object):
    """
    Home Appliances Class, parent class to all other appliance classes.

    Attributes:
        __str__: Print name and created date of appliance.
        status: Print name, status and created date of appliance.
        start: Start appliance and update status of appliance to Start.
        end: End appliance and update status of appliance to Wait.
    """

    def __init__(self, name, status):
        self._name = name
        self._status = status
        self._created_at = datetime.datetime.now()

    def __str__(self):
        return "이름 - {0} / 등록 일자 - {1}".format(self._name, self._created_at)

    @property
    def status(self):
        return "이름 - {0} / 상태 - {1} / 등록 일자 - {2}".format(self._name, self._status, self._created_at)

    def start(self):
        self._status = "Start"

    def end(self):
        self._status = "Wait"
    
class WashingMachine(HomeAppliance):
    """
    WashingMachine Class, parent class is HomeAppliance class.

    WashingMachine shold have property about remaining-time of machine.

    Attributes:
        status: With basic status using status function of parent class, print additional info about remaining time.
        controller: Print options and control selected input of user on each state.
        start: Start Washing Machine with some time interval.
        update: Update state of wachine machine when finishes washing.
    """

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
        ## try - except
        ## Check user enters valid number about options.
        try:
            print("\n[세탁 옵션] \n1. 행굼\n2. 표준\n3. 강력 세탁\n0. 메인메뉴로 돌아가기\n")

            choice = int(input("세탁 옵션을 선택 해주세요: "))
            
            if choice == 0:
                return
            elif 1 <= choice <= 3:
                if self._status == "Wait": 
                    self.start(interval = 0.1 * choice)
                else: 
                    print("\n현재 세탁 진행 중입니다.\n세탁이 완료된 후 다음 세탁을 이용 부탁드립니다.")
            else:
                raise ValueError('입력하신 숫자의 범위가 잘못 되었습니다. 0 ~ 3 사이의 정수만 입력하셔야 합니다.')

        except ValueError as error:
            print(error)

    def start(self, interval):
        super(WashingMachine, self).start()
        self._started_at = datetime.datetime.now()
        self._interval = interval

    def update(self):
        finished_at = self._started_at + datetime.timedelta(minutes = self._interval)
        
        if (finished_at <= datetime.datetime.now()):
            self._status = "Wait"

class AirConditioner(HomeAppliance):
    """
    AirConditioner Class, parent class is HomeAppliance class.

    AirConditioner shold have property about temperature user want to set.

    Attributes:
        status: With basic status using status function of parent class, print additional info about target temperature.
        controller: Print options and control selected input of user on each state.
        start: Start AirConditioner with some target temperature.
        set_temperature: Set target temperature of Home between 18 and 30 with integer value. 
    """

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
        ## try - except
        ## Check user enters valid number about options.
        try:
            print("\n[에어컨 옵션] \n1. 에어컨 시작\n2. 에어컨 온도 조절\n3. 에어컨 종료\n0. 메인메뉴로 돌아가기\n")

            choice = int(input("에어컨 옵션을 선택 해주세요: "))
            
            if choice == 0:
                return
            elif choice == 1:
                if self._status == "Wait":
                    self.start()
                else:
                    print("\n현재 에어컨이 켜져있는 상태 입니다. 에어컨의 희망 온도는 {0} 입니다.".format(self._target_temperature))
            elif choice == 2:
                if self._status == "Wait":
                    print("\n현재 에어컨이 꺼져있는 상태 입니다. 에어컨을 킨 다음 이용 부탁드립니다.")
                else:
                    self.set_temperature()
            elif choice == 3:
                if self._status == "Wait":
                    print("\n현재 에어컨이 꺼져있는 상태 입니다.")
                else:
                    self.end()
            else:
                raise ValueError('입력하신 숫자의 범위가 잘못 되었습니다. 0 ~ 3 사이의 정수만 입력하셔야 합니다.')

        except ValueError as error:
            print(error)

    def start(self):
        super(AirConditioner, self).start()
        
        if self.set_temperature() == False:
            self._target_temperature = 24
            print("에어컨 온도 설정에 실패하여 에어컨을 기본온도(24도)로 시작하였습니다.")

    def set_temperature(self):
        ## try - except
        ## Check user enters valid number about temperature.
        try:
            print("\n에어컨 설정 온도 범위 (정수): 18 ~ 30")

            temperature = int(input("에어컨 온도를 설정 해주세요: "))
            
            if 18 <= temperature <= 30:
                self._target_temperature = temperature
                return True
            else:
                raise ValueError('입력하신 숫자의 범위가 잘못 되었습니다. 18 ~ 30 사이의 정수만 입력하셔야 합니다.')

        except ValueError as error:
            print(error)
            return False

class Boiler(HomeAppliance):
    """
    Boiler Class, parent class is HomeAppliance class.

    Boiler shold have property about temperature user want to set.

    Attributes:
        status: With basic status using status function of parent class, print additional info about target temperature.
        controller: Print options and control selected input of user on each state.
        start: Start Boiler with some target temperature.
        set_temperature: Set target temperature of Home between 18 and 30 with integer value. 
    """

    def __init__(self):
        super(Boiler, self).__init__("보일러", "Wait")
        self._target_temperature = 0

    @property
    def status(self):
        basic_status = super(Boiler, self).status
        
        if self._status == "Wait":
            return basic_status
        else:
            return basic_status + ' / 현재 설정 온도 - {0}'.format(self._target_temperature)

    def controller(self):
        ## try - except
        ## Check user enters valid number about options.
        try:
            print("\n[보일러] \n1. 보일러 시작\n2. 보일러 온도 조절\n3. 보일러 종료\n0. 메인메뉴로 돌아가기\n")

            choice = int(input("보일러 옵션을 선택 해주세요: "))
            
            if choice == 0:
                return
            elif choice == 1:
                if self._status == "Wait":
                    self.start()
                else:
                    print("\n현재 보일러가 켜져있는 상태 입니다. 보일러의 희망 온도는 {0} 입니다.".format(self._target_temperature))
            elif choice == 2:
                if self._status == "Wait":
                    print("\n현재 보일러가 꺼져있는 상태 입니다. 보일러를 킨 다음 이용 부탁드립니다.")
                else:
                    self.set_temperature()
            elif choice == 3:
                if self._status == "Wait":
                    print("\n현재 보일러가 꺼져있는 상태 입니다.")
                else:
                    self.end()
            else:
                raise ValueError('입력하신 숫자의 범위가 잘못 되었습니다. 0 ~ 3 사이의 정수만 입력하셔야 합니다.')

        except ValueError as error:
            print(error)

    def start(self):
        super(Boiler, self).start()

        if self.set_temperature() == False:
            self._target_temperature = 24
            print("보일러 온도 설정에 실패하여 보일러를 기본온도(24도)로 시작하였습니다.")

    def set_temperature(self):
        ## try - except
        ## Check user enters valid number about temperature.
        try:
            print("\n보일러 설정 온도 범위 (정수): 18 ~ 30")

            temperature = int(input("보일러 온도를 설정 해주세요: "))
            
            if 18 <= temperature <= 30:
                self._target_temperature = temperature
                return True
            else:
                raise ValueError('입력하신 숫자의 범위가 잘못 되었습니다. 18 ~ 30 사이의 정수만 입력하셔야 합니다.')

        except ValueError as error:
            print(error)
            return False

class AirCleaner(HomeAppliance):
    """
    AirCleaner Class, parent class is HomeAppliance class.

    Attributes:
        controller: Print options and control selected input of user on each state. 
    """

    def __init__(self):
        super(AirCleaner, self).__init__("공기청정기", "Wait")

    def controller(self):
        ## try - except
        ## Check user enters valid number about options.
        try:
            print("\n[공기청정기] \n1. 공기청정기 시작\n2. 공기청정기 종료\n0. 메인메뉴로 돌아가기\n")

            choice = int(input("공기청정기 옵션을 선택 해주세요: "))
            
            if choice == 0:
                return
            elif choice == 1:
                if self._status == "Wait":
                    self.start()
                else:
                    print("\n현재 공기청정기가 켜져있는 상태 입니다.")
            elif choice == 2:
                if self._status == "Wait":
                    print("\n현재 공기청정기가 꺼져있는 상태 입니다.")
                else:
                    self.end()
            else:
                raise ValueError('입력하신 숫자의 범위가 잘못 되었습니다. 0 ~ 2 사이의 정수만 입력하셔야 합니다.')

        except ValueError as error:
            print(error)
    
class Menu():
    """
    Menu Class, control all of user inputs about create, read, update, delete appliances. 

    Attributes:
        __str__: Print main menu.
        print_choice: Print user's choice about menu to notify that you select that menu.
        select: Select function that control user's choice about main-menu.
        print_appliances: Print each appliance (or appliance status) contained on appliances list.
        add_appliance: Add appliance on list that holds set of appliances based on the user's input about appliance number.
        delete_appliance: Delete one appliance on list that holds set of appliances based on the uesr's input about appliance number.
        check_appliance_status: Print status of all appliance on list.
        change_appliance_status: Change one appliance on list that holds set of appliances based on the user's input about appliance number.
    """
    
    def __init__(self):
        self._display_string = "\n[메뉴]\n1. 가전제품 등록하기\n2. 가전제품 등록 해제하기\n3. 가전제품 상태 확인하기\n4. 가전제품 상태 변경하기\n0. 프로그램 종료하기\n"
        self._select = None
        self._choices = {
            0: lambda: print("\n프로그램을 종료합니다. \n이용해 주셔서 감사합니다."),
            1: lambda: print("\n*** 가전제품 등록하기를 선택 하셨습니다. ***\n"),
            2: lambda: print("\n*** 가전제품 등록 해제하기를 선택 하셨습니다. ***\n"),
            3: lambda: print("\n*** 가전제품 상태 확인하기를 선택 하셨습니다. ***\n"),
            4: lambda: print("\n*** 가전제품 상태 변경하기를 선택 하셨습니다. ***\n")
        }
        self._appliances = {
            1: WashingMachine,
            2: AirConditioner,
            3: Boiler,
            4: AirCleaner
        }

    def __str__(self):
        return self._display_string

    def print_choice(self, choice = False):
        if choice == False: 
            choice = self._select
        
        action = self._choices.get(choice)
        action()

    def select(self):
        ## try - except
        ## Check user enters valid number about options.
        try:
            choice = int(input("메뉴를 선택해주세요: "))
            
            if 0 <= choice <= 4:
                self._select = choice
                return (self._select, False)
            else:
                raise ValueError('입력하신 숫자의 범위가 잘못 되었습니다. 0 ~ 4 사이의 정수만 입력하셔야 합니다.')

        except ValueError as error:
            return (error, True)

    def print_appliances(self, appliances, status=False):
        print("\n현재 등록된 가전제품 목록")
        for index, appliance in enumerate(appliances):
            print(index, appliance.status if status == True else appliance, sep = '. ')

    def add_appliance(self, appliances):
        print("\n[가전제품 목록]\n1. 세탁기\n2. 에어컨\n3. 보일러\n4. 공기청정기\n")
        
        ## try - except
        ## Check user enters valid number about options.
        try:
            choice = int(input("추가하실 가전제품 목록을 선택 해주세요: "))
            
            if 1 <= choice <= 4:
                appliance = self._appliances.get(choice)
                appliances.append(appliance())
                self.print_appliances(appliances)
            else:
                raise ValueError('입력하신 숫자의 범위가 잘못 되었습니다. 1 ~ 4 사이의 정수만 입력하셔야 합니다.')

        except ValueError as error:
            print(error)

    def delete_appliance(self, appliances):
        if not appliances:
            print("\n현재 등록된 가전제품이 없습니다.\n가전제품을 먼저 등록 해주시기 바랍니다.")
            return

        ## try - except
        ## Check user enters valid number about options.
        try:
            self.print_appliances(appliances)
            choice = int(input("\n제거하실 가전제품 번호를 선택 해주세요: "))
            
            if 0 <= choice < len(appliances):
                appliances.pop(choice)
                self.print_appliances(appliances)
            else:
                raise ValueError('입력하신 숫자의 범위가 잘못 되었습니다. 0 ~ {} 사이의 정수만 입력하셔야 합니다.'.format(len(appliances) - 1))

        except ValueError as error:
            print(error)


    def check_appliance_status(self, appliances):
        if not appliances:
            print("\n현재 등록된 가전제품이 없습니다.\n가전제품을 먼저 등록 해주시기 바랍니다.")
            return

        self.print_appliances(appliances = appliances, status = True)

    
    def change_appliance_status(self, appliances):
        if not appliances:
            print("\n현재 등록된 가전제품이 없습니다.\n가전제품을 먼저 등록 해주시기 바랍니다.")
            return

        self.print_appliances(appliances = appliances, status = True)

        ## try - except
        ## Check user enters valid number about options.
        try:
            choice = int(input("\n상태를 변경하실 가전제품 번호를 선택 해주세요: "))
            
            if 0 <= choice < len(appliances):
                appliances[choice].controller()
                self.print_appliances(appliances = appliances, status = True)
            else:
                raise ValueError('입력하신 숫자의 범위가 잘못 되었습니다. 0 ~ {} 사이의 정수만 입력하셔야 합니다.'.format(len(appliances) - 1))

        except ValueError as error:
            print(error)

class PasswordManager():
    """
    PasswordManager Class, set password when user first runs software and compare when user create, update, delete appliances.  

    Attributes:
        set_password: Set password based on some rules (영문 대 소문자, 숫자 / 4 ~ 16 자).
        compare_password: Compare password based on two passwords (class holds and passed by parameter).
        password_check: With this function, system can check whether user know or not a system password.
    """

    def __init__(self):
        self._password = None
        self.set_password()
    
    def set_password(self):
        print("\n가전제품을 등록, 수정, 해제하기 위해서는 별도의 비밀번호가 필요합니다.")
        print("4~16자 영문 대 소문자, 숫자 만을 사용하셔야 합니다.")
        
        while True:
            ## try - except
            ## Check user enters valid password for the rule.
            try: 
                password = input("\n사용하실 비밀번호를 입력해주세요: ")

                if re.match(r'[A-Za-z0-9]{4,16}', password) is not None:
                    (start, end) = re.match(r'[A-Za-z0-9]{4,16}', password).span()
                    
                    ## 공백 입력을 방지하기 위해서 (Ex. 0123456 0123 입력 방지)
                    if password[start:end] == password:
                        self._password = password
                        break

                raise ValueError('비밀번호는 4~16자 영문 대 소문자, 숫자 만을 사용하셔야 합니다.')
            
            except NameError as error:
                raise NameError('Python re library 를 설치 해주세요.')
                
            except ValueError as error:
                print(error)

    def compare_password(self, password):
        if (self._password == password): return True
        else: return False

    def password_check(self):
        password = input("비밀번호를 입력해주세요: ")

        if self.compare_password(password): return True
        
        print("\n비밀번호가 일치하지 않습니다.")
        return False

def main():
    print("\n내 집 가전제품 관리 소프트웨어 입니다. :)")
    print("모든 메뉴는 '정수'로 입력하셔야 하며, 입력값에 따라 예외처리가 발생할 수 있습니다.")
    input("계속 진행하시려면 엔터를 입력 해주세요.")

    ## try - except
    ## Syntax to prepare for possible errors.
    try: 
        menu = Menu()
        pw_manager = PasswordManager()

        appliances = []

        while True:
            print("\n" + "*****" * 10)
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

            print("\n" + "*****" * 10 + "\n")
    
    except Exception as error:
        print("\n아래 에러가 발생하여 프로그램을 종료합니다.")
        print(error)

if __name__ == '__main__':
    main()
