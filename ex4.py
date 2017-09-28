my_name = 'Joe Shuttlewood'
my_age = 26
my_height = 6*12+2 #Hopefully this will put my height in to inches for me. Yep, it works!
my_weight = 200
my_eyes = 'blue'
my_hair = 'blonde'
is_heavy = my_weight > 3000 #when I use this variable further on this will return 'False'. Flattering.
my_height_in_cm = my_height * 2.5
my_weight_in_kg = my_weight // 2.2 #I had 'my_height / 2.2' here originally but it returned a float with 13 decimal places, looking at the documentation you can do 'integer division' with '//' which will always round down.
test_weight_in_kg = my_weight / 2.2 #I am going to try calling the result of this function as an integer, which hopefully will return 90 or 91. A second method of the above.

print(f"Let's talk about {my_name}.")
print(f"He is {my_height} inches tall, which is {my_height_in_cm} centimeters.") #this works correctly as above.
print(f"He's {my_weight} pounds heavy, which is {my_weight_in_kg} kilograms.")
print(f"It is {is_heavy} that he is overweight.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")

total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
print (int(test_weight_in_kg)) #this should hopefully return 90.
