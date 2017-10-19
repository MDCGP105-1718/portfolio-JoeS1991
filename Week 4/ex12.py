nights = int(input("How many nights are you staying? "))
fclass = input("Which flight class are you taking, economy, premium, business, or first? ")
NewYork = 2000
Auckland = 790
Venice = 154
Glasgow = 65
economy = 1.0
premium = 1.3
business = 1.6
first = 1.9

def hotelCost(x):
    x * 70
    return x

def planeTicket(fclass,city):
    x = city * fclass
    return x

def carCost(days):
    cost = 30 * days
    if days >= 3 and days < 7:
        cost = cost - 30
    elif days >= 7:
        cost = cost - 50
    else:
        cost = cost
    return cost

def totalCost(city,days):
    cost = hotelCost(days) + planeTicket(fclass,city) + carCost(days)

print(totalCost(NewYork,nights))
