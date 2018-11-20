"""
Guide function that prints guideline of this software.
"""
def guide():
    print("Guide")

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

def main():
    guide()
    print("Hello world")
    test = Boiler()
    test.status = '1'
    print(test.status)


if __name__ == '__main__':
    main()