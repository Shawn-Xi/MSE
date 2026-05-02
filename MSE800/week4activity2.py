from w4a2user import Rectangle

def main():
    """Main function to run the land dimension calculator."""
    print("==== 🏞️ Land Dimension Calculator ====")
    
    # Create an instance of the Rectangle class
    land = Rectangle()
    
    # Get user input for dimensions
    land.input_dimensions()
    
    # Calculate and display the area and perimeter
    if land.length > 0 and land.width > 0:
        area = land.calculate_area()
        perimeter = land.calculate_perimeter()
        
        print(f"\n--- Calculation Results ---")
        print(f"Area of the land: {area:.2f} square units")
        print(f"Perimeter of the land: {perimeter:.2f} units")

if __name__ == "__main__":
    main()
