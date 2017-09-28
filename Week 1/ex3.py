cars = 100 #this line defines 'cars' as an integer, 100.
space_in_a_car = 4.0 #this line defines 'space_in_a_car' as a float, 4.0.
drivers = 30
#testing a comment in a line above a variable.
passengers = 90
cars_not_driven = cars - drivers #this line defines 'cars_not_driven' as 70, this will change if we redefine 'cars' or 'drivers'
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car #this line multiplies an integer by a float, will it return a float?
average_passengers_per_car = passengers / cars_driven #I think this line conatined the intentional typo, missing the 's' from 'passengers'.

print("There are", cars, "cars available.") #this should print 'There are 100 cars available.' as it uses the 'car' variable I defined earlier as 100.
print("There are only", drivers, "drivers available.") #as above, but this line uses 'drivers'.
print("There will be", cars_not_driven, "empty cars today.") #I'm overcommenting.
print("We can transport", carpool_capacity, "people today.") #As predicted above, the variable 'carpool_capacity' does return a float.
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
#I have now scrolled down the document and realised the intentional typo was supposed to return an error and I should've located it from that.
#As commented above if I were to define 'space_in_a_car' as 4 instead of 4.0, it would return an integer of 120, instead of a float of 120.0.
