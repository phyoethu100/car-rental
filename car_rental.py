import datetime 

class CarRental:

    def __init__(self, stock):
        self.stock = stock
    

    def display_cars(self):
        print(f"We currenly have {self.stock} cars available to rent.")
        return self.stock


    def rent_car_hour(self, car):
        if car < 0:
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
        if car < 0:
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

        if cars and rental_type and rental_time: 
            self.stock += cars
            time = datetime.datetime.now()
            rental_period = time - rental_time
        
            if rental_type == 1:
                bill = round(rental_period.seconds / 3600) * 5 * cars 
                    
            elif rental_type == 2:
                bill = round(rental_period.days) * 20 * cars 
                    
            elif rental_type == 3:
                bill = round(rental_period.days / 7) * 60 * cars
                
            if (3 <= cars <= 5):
                print("You are eligible for a promotion of 30% discount")
                bill = bill * 0.7

            print("Thanks for returning your car. Hope you enjoyed our service!")
            print(f"That would be {bill}")
                
            return bill

        else:
            print("Are you sure you rented a car with us?")
            return None
