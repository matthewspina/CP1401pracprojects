from prac_08.silver_service_taxi import SilverServiceTaxi

def main():
    new_car1 = SilverServiceTaxi("Hummer",100,2)
    print(new_car1)
    new_car1.drive(18)
    print(new_car1)
    print(new_car1.get_fare())

main()