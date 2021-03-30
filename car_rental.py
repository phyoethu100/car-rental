import datetime 

class CarRental:

    def __init__(self, stock=0):
        self.stock = stock
    

    def display_cars(self):
        print(f"We currently have {self.stock} cars available to rent.")
        return self.stock


    def rent_car_hour(self, car):
        if car <= 0:
            print("The number of cars should be positive")
        
        elif car > self.stock:
            print(f"Sorry! We currently have {self.stock} cars available to rent.")
            return None

        else:
            time = datetime.datetime.now()
            print(f"You have rented {car} car(s) on an hourly basis at {time.hour} hours")
            print("You will be charged at $20 for each hour per car")
            print("Have a fun ride!")
        
        self.stock -= car
        return time
    

    def rent_car_daily(self, car):
        if car <= 0:
            print("The number of cars should be positive")
            
        elif car > self.stock:
            print(f"Sorry! We currently have {self.stock} cars available to rent")
            return None

        else:
            time = datetime.datetime.now()
            print(f"You have rented {car} car(s) on an hourly basis at {time.hour} hours")
            print("You will be charged at $100 for each day per car")
            print("Have a fun ride!")
            
        self.stock -= car
        return time
    

    def rent_car_weekly(self, car):
        if car <= 0:
            print("The number of cars should be positive")
            
        elif car > self.stock:
            print(f"Sorry! We currently have {self.stock} cars available to rent")
            return None

        else:
            time = datetime.datetime.now()
            print(f"You have rented {car} car(s) on an hourly basis at {time.hour} hours")
            print("You will be charged at $500 for each week per car")
            print("Have a fun ride!")
            
        self.stock -= car
        return time
        

    def return_cars(self, request):
        cars, rental_type, rental_time = request
        bill = 0
        rent = ""

        if cars and rental_type and rental_time: 
            self.stock += cars
            time = datetime.datetime.now()
            rental_period = time - rental_time
        
            if rental_type == 1:
                rent = "Hourly base"
                bill = round(rental_period.seconds / 3600) * 20 * cars 
                    
            elif rental_type == 2:
                rent = "Daily base"
                bill = round(rental_period.days) * 100 * cars 
                    
            elif rental_type == 3:
                rent = "Weekly base"
                bill = round(rental_period.days / 7) * 500 * cars
                
            if (3 <= cars <= 5):
                print("You are eligible for a promotion of 30% discount")
                bill = bill * 0.7

            print("Thank you for returning the car. Have a nice day!")
            print(f"\nThe bill would be ${bill}")
            print("Do you want to pay with cash or credit card?")

            try: 
                payment = int(input("Enter 1 for cash and 2 for credit card: "))
            except ValueError:
                print("Please enter a number!")

            if payment == 1:
                print("Thank you for your payment! Here is your receipt...")
                print("\n--------------------------------------------------")
                print("\t\tCAR RENTAL SHOP")
                print(f"\tCars rented: {cars}")
                print(f"\tRental type: {rent}")
                print(f"\tRented on: {rental_time}")
                print(f"\tReturned on: {time}")
                print(f"\tTotal bill: ${bill}")
                print("\tPayment type: cash")
                print(f"\tPaid on: {time}")
                print("\tThank you!")
                print("--------------------------------------------------")
        
            elif payment == 2:
                credit = input("Enter your credit card number: ")

                if 18 > len(credit) > 14: 
                    print("Thank you for your payment! Here is your receipt...")
                    print("\n--------------------------------------------------")
                    print("\t\tCAR RENTAL SHOP")
                    print(f"\tCars rented: {cars}")
                    print(f"\tRental type: {rent}")
                    print(f"\tRented on: {rental_time}")
                    print(f"\tReturned on: {time}")
                    print(f"\tTotal bill: ${bill}")
                    print("\tPayment type: credit card")
                    print(f"\tPaid on: {time}")
                    print("\tThank you!")
                    print("--------------------------------------------------")
                else:
                    print("Please enter the valid credit card number!")
            
            else: 
                print("Please enter 1 or 2 only!")

            return bill

        else:
            print("Are you sure you rented a car with us?")
            return None
