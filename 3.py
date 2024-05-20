class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, initial_rating):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = initial_rating

    def describe_restaurant(self):
        print(f"Ресторан {self.restaurant_name} предлагает кухню типа {self.cuisine_type}. Рейтинг: {self.rating}")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг ресторана {self.restaurant_name} обновлен: {self.rating}")

restaurant = Restaurant("La Bella", "итальянская", 4.5)
restaurant.describe_restaurant()

new_rating = 4.8
restaurant.update_rating(new_rating)
restaurant.describe_restaurant()
