from abc import ABC, abstractmethod

class Burger(ABC):

    @abstractmethod
    def prepare(self):
        pass

class VeggieBurger(Burger):
    def prepare(self):
        return "Veggie Burger"
    
class ChickenBurger(Burger):
    def prepare(self):
        return "Chicken Burger"

class Restaurant(ABC):
    def order_burger(self, burger_type):
        burger = self.create_burger(burger_type)
        burger.prepare()

    @abstractmethod
    def create_burger(self, burger_type):
        pass

class BurgerFactory(Restaurant):
    def create_burger(self, burger_type):
        if burger_type == "Veggie":
            return VeggieBurger()
        elif burger_type == "Chicken":
            return ChickenBurger()
        else:
            return None
        
# Driver code
if __name__ == "__main__":
    factory = BurgerFactory()
    burger = factory.order_burger("Veggie")
    print(burger)
    burger = factory.order_burger("Chicken")
    print(burger)
    burger = factory.order_burger("Fish")
    print(burger)