from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

def main():
    taxis = [Taxi("Prius",100),SilverServiceTaxi("Limo",100,2),SilverServiceTaxi("Hummer",200,4)]
    print ("Let's drive!")
    menu = ("q)uit, c)hoose, d)rive")
    choice = str(input(menu)).lower()
    while choice != "q":
        if choice == "c":
            i = 0
            for taxi in taxis:
                print("{} - {}".format(i,taxi))
                i += 1

        elif choice == "d":
            print("oi")
        else:
            print("Invalid option")
        choice = str(input(menu)).lower()
    print("goodbye")


main()