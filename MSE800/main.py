from database import create_table, create_steak_table, create_restaurant_table
from student_manager import add_student, view_students, search_student, delete_student
from steak_manager import add_steak, view_steaks, delete_steak
from restaurant_manager import add_restaurant, view_restaurants, delete_restaurant

def student_menu():
    """Manages operations for the student table."""
    while True:
        print("\n==== 🎓 Student Manager ====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by Name")
        print("4. Delete Student by ID")
        print("5. Back to Main Menu")
        choice = input("Select an option (1-5): ")

        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            gender = input("Enter gender: ")
            add_student(name, age, gender)
        elif choice == '2':
            students = view_students()
            print("\n--- All Students ---")
            for student in students:
                print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Gender: {student[3]}")
        elif choice == '3':
            name = input("Enter name to search: ")
            students = search_student(name)
            print(f"\n--- Search Results for '{name}' ---")
            for student in students:
                print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Gender: {student[3]}")
        elif choice == '4':
            student_id = int(input("Enter student ID to delete: "))
            delete_student(student_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

def steak_menu():
    """Manages operations for the steak table."""
    while True:
        print("\n==== 🥩 Steak Manager ====")
        print("1. Add Steak")
        print("2. View All Steaks")
        print("3. Delete Steak by ID")
        print("4. Back to Main Menu")
        choice = input("Select an option (1-4): ")

        if choice == '1':
            weight = float(input("Enter weight (oz): "))
            price = float(input("Enter price ($): "))
            add_steak(weight, price)
        elif choice == '2':
            steaks = view_steaks()
            print("\n--- All Steaks ---")
            for steak in steaks:
                print(f"ID: {steak[0]}, Weight: {steak[1]} oz, Price: ${steak[2]:.2f}")
        elif choice == '3':
            steak_id = int(input("Enter steak ID to delete: "))
            delete_steak(steak_id)
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

def restaurant_menu():
    """Manages operations for the restaurant table."""
    while True:
        print("\n==== 🍽️ Restaurant Manager ====")
        print("1. Add Restaurant")
        print("2. View All Restaurants")
        print("3. Delete Restaurant by ID")
        print("4. Back to Main Menu")
        choice = input("Select an option (1-4): ")

        if choice == '1':
            name = input("Enter name: ")
            location = input("Enter location: ")
            boss = input("Enter boss's name: ")
            waiters = int(input("Enter number of waiters: "))
            boss_id = int(input("Enter boss's ID: "))
            add_restaurant(name, location, boss, waiters, boss_id)
        elif choice == '2':
            restaurants = view_restaurants()
            print("\n--- All Restaurants ---")
            for r in restaurants:
                print(f"ID: {r[0]}, Name: {r[1]}, Location: {r[2]}, Boss: {r[3]}, Waiters: {r[4]}, Boss ID: {r[5]}")
        elif choice == '3':
            restaurant_id = int(input("Enter restaurant ID to delete: "))
            delete_restaurant(restaurant_id)
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

def main():
    # Initialize all tables when the application starts
    create_table()
    create_steak_table()
    create_restaurant_table()

    while True:
        print("\n==== 🌟 Main Menu 🌟 ====")
        print("1. Manage Students 🎓")
        print("2. Manage Steaks 🥩")
        print("3. Manage Restaurants 🍽️")
        print("4. Exit")
        choice = input("Select a manager (1-4): ")

        if choice == '1':
            student_menu()
        elif choice == '2':
            steak_menu()
        elif choice == '3':
            restaurant_menu()
        elif choice == '4':
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
