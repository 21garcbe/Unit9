from restaurant import Restaurant
from restaurant import IceCreamStand

texas_roadhouse = Restaurant('Texas Roadhouse')
print(texas_roadhouse.restaurant_name)
texas_roadhouse.set_number_served(10)
print(texas_roadhouse.number_served)
texas_roadhouse.increment_number_served(15)
print(texas_roadhouse.number_served)

#Test ice cream stand class with Jeni's Ice Cream Object
jenis_stand = IceCreamStand("Jeni's Ice Cream", ["Chocolate", "Coffee", "Lavender"])
print(f"This is not a restaurant, its a {jenis_stand.restaurant_name} ice cream stand.")
jenis_stand.display_flavors()
