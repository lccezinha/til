import math

class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients


    def __repr__(self):
        return f"Pizza({self.ingredients})"

    # Acts like a factory method
    @classmethod
    def flavor_one(cls):
        return cls(10, ['ingredient_1', 'ingredient_2'])

    @classmethod
    def flavor_two(cls):
        return cls(10, ['ingredient_3', 'ingredient_4'])

    @classmethod
    def flavor_three(cls):
        return cls(10, ['ingredient_5', 'ingredient_6'])

    def area(self):
        return self._circle_area(self.radius)

    @staticmethod
    def _circle_area(r):
        return r ** 2 * math.pi

pizza = Pizza(10, ['ingredient_10', 'ingredient_20'])
print(pizza)

print(Pizza.flavor_one())
print(Pizza.flavor_two())
print(Pizza.flavor_three())
print(pizza.area())
print(Pizza._circle_area(5))