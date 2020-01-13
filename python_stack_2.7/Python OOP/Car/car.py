class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.mph_adder().mpg_adder().display_all()

    def mph_adder(self):
        self.speed = "{}mph".format(self.speed)
        return self

    def mpg_adder(self):
        self.mileage = "{}mpg".format(self.mileage)
        return self

    def display_all(self):
        print "Price: {}".format(self.price)
        print "Speed: {}".format(self.speed)
        print "Fuel: {}".format(self.fuel)
        print "Mileage: {}".format(self.mileage)
        print "Tax: {}".format(self.tax)
        print ""
        return self

car_a = Car(2000, 35, "Full", 15)
# car_a.mph_adder().mpg_adder().display_all()

car_b = Car(2000, 5, "Not Full", 105)
# car_b.mph_adder().mpg_adder().display_all()

car_c = Car(2000, 15, "Kind of Full", 95)
# car_c.mph_adder().mpg_adder().display_all()

car_d = Car(2000, 25, "Full", 25)
# car_d.mph_adder().mpg_adder().display_all()

car_e = Car(2000, 45, "Empty", 25)
# car_e.mph_adder().mpg_adder().display_all()

car_f = Car(20000000, 35, "Empty", 15)
# car_f.mph_adder().mpg_adder().display_all()

