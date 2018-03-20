'''
Trip Calculator Script
'''

#car object
class Car:
	name = ""
	hwy_mpg = 0
	tank_size = 0
	fuel_type = ""

#trip object
class Trip:
	name = ""
	start_location = ""
	final_destination = ""
	cars = []
	legs = []
	total_fuel_cost = 0
	total_miles = 0
	total_lodging = 0
	total_trip_cost = 0

class Leg:
	point_a_name = ""
	point_b_name = ""
	total_distance = 0
	avg_fuel_prem_cost = 0
	avg_fuel_reg_cost = 0
	lodging_cost = 0


trip = Trip()
trip.name = input("Name of Trip: ")
trip.start_location = input("Start Location: ")
trip.final_destination = input("Final Destination: ")

numcars = int(input("Total number of cars: "))
while (len(trip.cars) < numcars):
	car = Car()
	car.name = input("Car name: ")
	car.hwy_mpg = int(input("Highway MPG: "))
	car.tank_size = float(input("Tank size: "))
	car.fuel_type = input("Fuel type: ")
	trip.cars.append(car)

numlegs = int(input("Enter the number of legs of the trip: "))
while (len(trip.legs) < numlegs):
	leg = Leg()
	leg.point_a_name = input("Point A Name: ")
	leg.point_b_name = input("Point B Name: ")
	leg.total_distance = int(input("Total Distance: "))
	leg.avg_fuel_reg_cost = float(input("Average Cost per Gallon of Regular Fuel: "))
	leg.avg_fuel_prem_cost = float(input("Average Cost per Gallon of Premium Fuel: "))
	leg.lodging_cost = float(input("Lodging Cost: "))
	trip.legs.append(leg)

trip.total_fuel_cost = 0

for c in trip.cars:
	for l in trip.legs:
		num_fuel_stops = (l.total_distance / (c.tank_size*c.hwy_mpg))
		if c.fuel_type == "regular":
			trip.total_fuel_cost += ((c.tank_size*l.avg_fuel_reg_cost)*num_fuel_stops)
		elif c.fuel_type == "premium":
			trip.total_fuel_cost += ((c.tank_size*l.avg_fuel_prem_cost)*num_fuel_stops)

print("Total Fueld Cost for Trip: ", trip.total_fuel_cost)
trip.total_miles = 0
for l in trip.legs:
	trip.total_miles += l.total_distance
print("Total Distance: ", trip.total_miles)

trip.total_lodging = 0
for l in trip.legs:
	trip.total_lodging += l.lodging_cost
print("Total Lodging Cost: ", trip.total_lodging)

trip.total_trip_cost = trip.total_fuel_cost + trip.total_lodging;
print("Trip Total: ", trip.total_trip_cost)

