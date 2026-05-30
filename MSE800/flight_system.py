# flight_system.py

class Flight:
    """
    Parent class representing a general flight.
    Contains attributes and methods common to all types of flights.
    """
    def __init__(self, flight_number, origin, destination, departure_time):
        # Shared attributes for all flights
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.airline = "Air New Zealand"  # Default airline for all flights

    def display_flight_details(self):
        """
        Shared method to display the core details of any flight.
        This method is intended to be inherited by subclasses.
        """
        print(f"--- Flight Information ---")
        print(f"Airline: {self.airline}")
        print(f"Flight Number: {self.flight_number}")
        print(f"From: {self.origin} To: {self.destination}")
        print(f"Departure: {self.departure_time}")


class DomesticFlight(Flight):
    """
    Subclass representing a domestic flight within New Zealand.
    It inherits from the Flight class and adds specific attributes and methods.
    """
    def __init__(self, flight_number, origin, destination, departure_time, aircraft_type):
        # --- INHERITANCE ---
        # Call the constructor of the parent class (Flight) to initialize shared attributes.
        super().__init__(flight_number, origin, destination, departure_time)
        
        # --- SUBCLASS SPECIFIC ATTRIBUTE ---
        # Attribute specific to domestic flights
        self.aircraft_type = aircraft_type
        self.is_koru_club_available = self.check_koru_club_status()

    def check_koru_club_status(self):
        """
        Subclass specific method.
        Determines if Koru Club is available based on the origin airport.
        """
        # A simple check for major NZ airports
        major_airports = ["Auckland", "Wellington", "Christchurch", "Dunedin"]
        return self.origin in major_airports

    def display_flight_details(self):
        """
        --- METHOD OVERRIDING ---
        This method overrides the parent's display_flight_details method.
        It first calls the parent method to display shared details,
        and then adds its own specific information.
        """
        # Call the parent class's method to print the general flight details
        super().display_flight_details()
        
        # Now, print the details specific to the DomesticFlight subclass
        print(f"Aircraft: {self.aircraft_type}")
        print(f"Koru Club Available at Origin: {'Yes' if self.is_koru_club_available else 'No'}")
        print(f"--------------------------")
