class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

        self.cars = {1: 0, 2: 0, 3: 0}

    def addCar(self, carType: int) -> bool:
        num = self.cars.get(carType) + 1
        if 1 == carType:
            if num > self.big:
                return False
        elif 2 == carType:
            if num > self.medium:
                return False
        else:
            if num > self.small:
                return False

        self.cars[carType] = num
        return True



# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)