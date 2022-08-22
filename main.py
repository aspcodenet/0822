from car import Car
import string
import random

allCars = []

def initialize():
    for x in range(0,1000000):
        regno = random.choice(string.ascii_uppercase) \
            +  random.choice(string.ascii_uppercase) \
            +  random.choice(string.ascii_uppercase) \
            +  random.choice(string.digits)    \
            +  random.choice(string.digits)    \
            + random.choice(string.ascii_uppercase + string.digits)
        car = Car(regno, "")
        allCars.append(car)

def GetCarByRegNo(regno:str):
    for car in allCars:
        if car.Regno == regno:
            return car
    return None

def main():    
    initialize()
    while True:
        x = input("Ange regno:")
        car = GetCarByRegNo(x)
        if car == None:
            print("Finns ej")
        else:
            print("Träff")

if __name__ == "__main__":
    main()
