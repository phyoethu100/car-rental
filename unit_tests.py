import unittest, datetime
from car_rental import CarRental 
from customer import Customer 

class CarRentalTest(unittest.TestCase):

    def test_display_cars(self):
        car1 = CarRental()
        car2 = CarRental(100)
        car3 = CarRental(-1)

        self.assertEqual(car1.display_cars(), 0)
        self.assertEqual(car2.display_cars(), 100)
        self.assertEqual(car3.display_cars(), 0)



    def test_rent_hourly_zero_num(self):
        car = CarRental(10)
        self.assertEqual(car.rent_car_hour(0), None)


    def test_rent_hourly_negative_num(self):
        car = CarRental(10)
        self.assertEqual(car.rent_car_hour(-1), None)


    def test_rent_hourly_greater_than_stock(self):
        car = CarRental(10)
        self.assertEqual(car.rent_car_hour(12), None)
    

    def test_rent_hourly_positive_num(self):
        car = CarRental(10)
        hour = datetime.datetime.now().hour
        self.assertEqual(car.rent_car_hour(5).hour, hour)
    
    
     
    def test_rent_daily_zero_num(self):
        car = CarRental(10)
        self.assertEqual(car.rent_car_daily(0), None)


    def test_rent_daily_negative_num(self):
        car = CarRental(10)
        self.assertEqual(car.rent_car_daily(-1), None)


    def test_rent_daily_greater_than_stock(self):
        car = CarRental(10)
        self.assertEqual(car.rent_car_daily(12), None)
    

    def test_rent_daily_positive_num(self):
        car = CarRental(10)
        hour = datetime.datetime.now().hour
        self.assertEqual(car.rent_car_daily(5).hour, hour)
    


    def test_rent_weekly_zero_num(self):
        car = CarRental(10)
        self.assertEqual(car.rent_car_weekly(0), None)


    def test_rent_weekly_negative_num(self):
        car = CarRental(10)
        self.assertEqual(car.rent_car_weekly(-1), None)


    def test_rent_weekly_greater_than_stock(self):
        car = CarRental(10)
        self.assertEqual(car.rent_car_weekly(12), None)
    

    def test_rent_weekly_positive_num(self):
        car = CarRental(10)
        hour = datetime.datetime.now().hour
        self.assertEqual(car.rent_car_weekly(5).hour, hour)




unittest.main()
