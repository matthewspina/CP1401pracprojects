from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def drive_taxi(taxis, taxi_chosen):
    car = taxis[taxi_chosen]
    distance_driven = int(input("Drive how far?"))
    car.drive(distance_driven)
    return car


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    menu = ("q)uit, c)hoose, d)rive")
    choice = str(input(menu)).lower()
    bill = 0
    while choice != "q":
        if choice == "c":
            i = 0
            for taxi in taxis:
                print("{} - {}".format(i, taxi))
                i += 1
            taxi_chosen = int(input("Choose taxi: "))
            print("Bill to date: ${}".format(bill))
        elif choice == "d":
            taxi_car = drive_taxi(taxis, taxi_chosen)
            bill += taxi_car.get_fare()
            print("Your {} trip cost ${}\nBill to date: {} ".format(taxi_car.name,taxi_car.get_fare(),bill))
        else:
            print("Invalid option")
        choice = str(input(menu)).lower()
    print("Total trip cost: ${}".format(bill))
    i = 0
    for taxi in taxis:
        print("{} - {}".format(i, taxi))
        i += 1


main()
