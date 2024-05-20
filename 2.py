class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Ресторан {self.restaurant_name} предлагает кухню типа {self.cuisine_type}.")

    def open_restaurant(self):
        print("Ресторан открыт!")

restaurant1 = Restaurant("Италиано", "итальянская")
restaurant2 = Restaurant("Суши-Мастер", "японская")
restaurant3 = Restaurant("СтейкХаус", "американская")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
