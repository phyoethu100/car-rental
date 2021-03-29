import unittest
from car_rental import CarRental 
from customer import Customer 

class CarRentalTest(unittest.TestCase):

    def test_display_cars(self):
        car1 = CarRental()
        car2 = CarRental(100)

        self.assertEqual(car1.display_cars(), 0)
        self.assertEqual(car2.display_cars(), 100)


    def test_rent_hourly_negative_num(self):
        car = CarRental(10)
        self.assertEqual(car.rent_car_hour(-1), None)


    def test_rent_hourly_zero_num(self):
        car = CarRental(10)
        self.assertEqual(car.rent_car_hour(0), None)


    def test_rent_hourly_positive_num(self):
        car = CarRental(10)
        hour = datetime.now().hour
        self.assertEqual(car.rent_car_hour(2).hour, hour)


    def test_rent_hourly_invalid_positive(self):
        car = CarRental(10)
        self.assertEqual(car.rent_car_hour(11), None)




unittest.main()