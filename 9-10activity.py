from restaurant import Restaurant

texas_roadhouse = Restaurant('Texas Roadhouse')
print(texas_roadhouse.restaurant_name)
texas_roadhouse.set_number_served(10)
print(texas_roadhouse.number_served)
texas_roadhouse.increment_number_served(15)
print(texas_roadhouse.number_served)