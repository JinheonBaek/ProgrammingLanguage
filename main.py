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
        self.choices = {
            "1": self.something
        }

"""
Guide function that prints guideline of this software.
"""
def showGuideline():
    print("Guide")

def setPassword():
    print("Set Master Password")

def showMenu():
    print("Print Menu")

def init():
    showGuideline()
    setPassword()

def main():
    init()

    while(1):
        showMenu()

        controlValue = input("메뉴를 선택해주세요: ")

        print(controlValue)
        
        break
    
    # print("Hello world")
    # test = Boiler()
    # test.status = '1'
    # print(test.status)


if __name__ == '__main__':
    main()