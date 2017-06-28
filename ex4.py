# -*- coding: utf-8 -*-
cars=100
space_in_a_car=4.0
drivers=30
passegers=90
car_not_driven=cars-drivers
car_driven=drivers
carpool_capacity=car_driven*space_in_a_car
average_passengers_per_car=passegers/car_driven

print "There are", cars,"cars available"
print "There are only", drivers, "drivers available"
print "We can transport",carpool_capacity,"people today"
print "We need to put about",average_passengers_per_car, "in each car."
