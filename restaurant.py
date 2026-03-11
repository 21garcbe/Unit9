class Restaurant:
    def __init__(self, restaurant_name, number_served=0):
        self.restaurant_name = restaurant_name
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"The restaurant is a {self.restaurant_name} restaurant.")

    def open_restaurant(self):
        print("The restaurant is now open!")

    def set_number_served(self, number_served):
        """Set the number of customers that have been served."""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Add the given amount to the number of customers served."""
        self.number_served += additional_served    
    
#Test Restaurant class with olive garden object
olive_garden = Restaurant('Olive Garden')
print(olive_garden.restaurant_name)
olive_garden.set_number_served(5)
print(olive_garden.number_served)
olive_garden.increment_number_served(5)
print(olive_garden.number_served)

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, flavors):
        super().__init__(restaurant_name)
        self.flavors = flavors

    def display_flavors(self):
        print("The ice cream stand offers the following flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")


