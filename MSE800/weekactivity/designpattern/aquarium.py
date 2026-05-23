# week7 activity2
from abc import ABC


class GoldFish:
    number = 12
    def speak(self):
        print("I'm a GoldFish")


class Shark:
    number = 10
    def speak(self):
        print("I'm a Shark")

class FishFactory(ABC):
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)

        return cls._instance

    def create_fish(self,kind=None):
        if kind == "goldFish":
            # Correctly increment the class attribute
            GoldFish.number = GoldFish.number + 1
            return GoldFish()
        if kind == "shark":
            # Correctly increment the class attribute
            Shark.number = Shark.number + 1
            return Shark()

class Admin:
    def numberTheFishCount(self, kind = None):
        if kind=="goldFish":
            print("number of {0} is {1}".format(kind, str(GoldFish.number)))
        if kind == "shark":
            print("number of {0} is {1}".format(kind, str(Shark.number)))

if __name__ == "__main__":
    fish_factory = FishFactory()
    admin = Admin()

    # Get user input for the type of fish
    fish_type = input("Enter the type of fish to create (e.g., 'shark' or 'goldFish'): ")

    # Validate the input
    if fish_type in ["shark", "goldFish"]:
        print(f"\n--- Before creating a new {fish_type} ---")
        admin.numberTheFishCount(fish_type)
        
        # Create the new fish
        fish_factory.create_fish(fish_type)
        
        print(f"\n--- After creating a new {fish_type} ---")
        admin.numberTheFishCount(fish_type)
    else:
        print("Invalid fish type. Please enter 'shark' or 'goldFish'.")
