"""def hotelcost(days):
    return days*150
def travelcost(city):
    if city=="Chicago":
        return 183
    elif city=="London":
        return 222
    elif city=="Toronto":
        return 220
    elif city=="Tokyo":
        return 475
    else:
        print("Please enter a valid city")

def carcost(days):
    cost = days*150
    if days >= 7:
        return (cost - 50)
    elif days >= 3:
        return (cost - 20)
    return cost
def totalcost():
    city = input("Which city are you going to?")
    if city == "Toronto" or city== "Chicago" or city == "London" or city == "Tokyo":
        days = int(input("How many days?"))
        total = hotelcost(days) + travelcost(city) + carcost(days)
        print(total)
    else:
        print ("Please enter a valid city")
        totalcost()
totalcost()"""

"""letters = ['a', 'b', 'c', 'd', 'e', 'f']

sliced_list = letters[2:5]

print(sliced_list)"""

"""animals= ["ant", "bat", "cat", "dog"]

print(animals.index("cat"))

animals.insert(1, "snake")

print(animals)
animals.pop(2)
print(animals)
animals.remove("cat")
print(animals)
animals.sort()
print (animals)"""

def print(lis):
    print(lis[0])
          


