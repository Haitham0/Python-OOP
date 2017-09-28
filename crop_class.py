# Author: Haitham Mousa
# Version: 1.2
# All Rights reserved

import random


class Crop:
    ''' A Generic food crop '''

    # Constructor

    def __init__(self, growth_rate, light_need, water_need):
        # Set the attributes with inital value
        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"


        # the the above attributes are prefixed with an underscore to indicate
        # that they should not be accessed directly from outwith the class
    def need(self):
        # Return a dictionary containing the light and water need
        return {'light need': self._light_need, 'Water need': self._water_need}
    def Report(self):
        # Return a dictionary containing
        return {'Type':self._type, 'status': self._status, 'Growth': self._growth, 'Growth Rate': self._growth_rate}

    def updateStatus(self):
        if self._growth > 15:
            self._status = "Old"
        elif self._growth > 10:
            self._status = "Mature"
        elif self._growth > 5:
            self._status = "Young"
        elif self._growth > 0:
            self._status = "Seedling"
        elif self._growth == 0:
            self._status = "Seed"
    def grow(self, light, water):
        if light >= self._light_need and water >= self._water_need:
            self._growth += self._growth_rate
            #Increment days growing
            self._days_growing += 1
            # Update Status
            self.updateStatus()
            # Update Status is private

def auto_Grow(Crop, days):
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        Crop.grow(light, water)
def manual_Grow():
    print()


def display_menu():
    print("1. Grow Manually over 1 day")
    print("2. Grow Automatically over 30 days")
    print("Report Status")
    print("3. Exit Test program")
    print()
    print("Please select an option from the above menu")

def Get_menu_choice():
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Option selected: "))
            if 0 <= choice >= 4:
                option_valid = True
            else:
                print("Enter a valid option")
        except ValueError:
            print("Please enter a valid option")
    return choice


def managecorp():
    print("this is the crop management program")
    print()
    noexit = True
    while noexit:
        display_menu()
        option = Get_menu_choice()
        print()
        if option == 1:
            manual_Grow()
            print()
            break
        elif option == 2:
            auto_Grow()
            print()
            break
        elif option == 3:
            print(Crop.Report())
            print()
            break
        elif option == 4:
            noexit = False
            print()
        print("Thank you for using the Crop Management program")


def main():
    #instaniate the class
    new_crop1 = Crop(1, 4, 3)
 #   new_crop2 = Crop(2, 6, 9)
    # test to see whether it works or not
    print(new_crop1.need())
    print(new_crop1.Report())
    auto_Grow(new_crop1, 30)
    print(new_crop1.Report)
managecorp()

 #   print(new_crop2._status)
 #   print(new_crop2._light_need)
 #   print(new_crop2._water_need)

if __name__ == "__main__":
    main()