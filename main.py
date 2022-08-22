from car import Car
import string
import random
from timeit import default_timer

allCars = {}

def initialize():
    for x in range(0,1000000):
        regno = random.choice(string.ascii_uppercase) \
            +  random.choice(string.ascii_uppercase) \
            +  random.choice(string.ascii_uppercase) \
            +  random.choice(string.digits)    \
            +  random.choice(string.digits)    \
            + random.choice(string.ascii_uppercase + string.digits)
        car = Car(regno, "")
        allCars[regno] = car

def GetCarByRegNo(regno:str):
    if not regno in allCars:
        return None
    return allCars[regno]
    # for car in allCars:
    #     if car.Regno == regno:
    #         return car
    # return None

def main():    
    timeStart = default_timer()
    initialize()
    timeEnd =  default_timer()
    print("Init tog ", timeEnd-timeStart)

    # print(allCars[3].Regno)
    # print(allCars[999999].Regno)
    while True:
        x = input("Ange regno:")
        timeStart = default_timer()
        car = GetCarByRegNo(x)
        timeEnd =  default_timer()
        print("Det tog ", timeEnd-timeStart)
        if car == None:
            print("Finns ej")
        else:
            print("Träff")

if __name__ == "__main__":
    main()
