class Customer:

    def __init__(self):
        self.cars = 0
        self.rental_type = 0
        self.rental_time = 0
        self.bill = 0 

    
    def rent_cars(self):
        try: 
            cars = int(input("How many cars do you want to rent? "))
        except ValueError:
            print("Please enter a number!")
            return -1

        if cars < 1:
            print("Number of cars should be more than zero!")
            return -1

        else:
            self.cars = cars 
        
        return self.cars


    def return_cars(self):
        if self.cars and self.rental_type and self.rental_time:
            return self.cars, self.rental_type, self.rental_time
        else:
            return 0,0,0