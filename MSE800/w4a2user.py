class Rectangle:
    def __init__(self):
        self.length = 0
        self.width = 0

    def input_dimensions(self):
        """Prompts the user to input the dimensions of the rectangle."""
        try:
            self.length = float(input("Enter the length of the rectangular land: "))
            self.width = float(input("Enter the width of the rectangular land: "))
        except ValueError:
            print("Invalid input. Please enter numeric values for dimensions.")
            self.length = 0
            self.width = 0

    def calculate_area(self):
        """Calculates the area of the rectangle."""
        return self.length * self.width

    def calculate_perimeter(self):
        """Calculates the perimeter of the rectangle."""
        return 2 * (self.length + self.width)
