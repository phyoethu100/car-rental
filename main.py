from car_rental import CarRental 
from customer import Customer 

def main():
    cars_rental = CarRental(300)
    customer = Customer()

    print("\n\tWELCOME TO CAR RENTAL SHOP!\n")

    while True:
        print("""
        ======== Car Rental Shop ========
        1. Display available cars
        2. Rent a car on an hourly basis: $20 
        3. Rent a car on a daily basis: $100
        4. Rent a car on a weekly basis: $500
        5. Return a car
        6. Exit
        """)

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number!")
            continue
        
        if choice == 1:
            cars_rental.display_cars()
        
        elif choice == 2:
            customer.rental_time = cars_rental.rent_car_hour(customer.rent_cars())
            customer.rental_type = 1

        elif choice == 3:
            customer.rental_time = cars_rental.rent_car_daily(customer.rent_cars())
            customer.rental_type = 2

        elif choice == 4:
            customer.rental_time = cars_rental.rent_car_weekly(customer.rent_cars())
            customer.rental_type = 3

        elif choice == 5:
            customer.bill = cars.return_cars(customer.return_cars())
            customer.cars, customer.rental_type, customer.rental_time = 0,0,0    

        elif choice == 6: 
            break
        
        else: 
            print("Please enter a choice between 1-6 only!")
    
    print("Thank you for using our car rental system!")


main() 