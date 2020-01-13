class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayinfo(self):
        print "This bike costs {}, maximum speed flatlines at {}, and the total miles ridden are {}".format(self.price, self.max_speed, self.miles)
        return self
    
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    
    def reverse(self):
        print "Reversing"
        self.miles -= 5
        return self


new_bike_a = Bike(33333, 133)
new_bike_b = Bike(66666, 166)
new_bike_c = Bike(99999, 199)
# print new_bike_a
# print new_bike_a.price
# print new_bike_a.max_speed
# print new_bike_a.miles
# new_bike_a.displayinfo()
# new_bike_a.ride()
# new_bike_a.reverse()

new_bike_a.ride().ride().ride().reverse().displayinfo()
new_bike_b.ride().ride().reverse().reverse().displayinfo()
new_bike_c.reverse().reverse().reverse().displayinfo()

