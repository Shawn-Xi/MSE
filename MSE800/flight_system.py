# flight_system.py

class Flight:
    """
    Top-level parent class representing a generic flight.
    """
    def __init__(self, flight_number, airline="Air New Zealand"):
        print("-> Initializing Flight")
        self.flight_number = flight_number
        self.airline = airline

    def get_airline_info(self):
        """Returns the airline name."""
        return f"This flight is operated by {self.airline}."

    def display_flight_id(self):
        """Displays the unique flight identifier."""
        print(f"Flight ID: {self.airline} {self.flight_number}")


class DomesticFlight(Flight):
    """
    Inherits from Flight. Represents a flight within a single country.
    """
    def __init__(self, flight_number, origin, destination, **kwargs):
        print("--> Initializing DomesticFlight")
        # --- MULTILEVEL INHERITANCE ---
        # Pass relevant arguments up to the parent (Flight)
        super().__init__(flight_number=flight_number, **kwargs)
        self.origin = origin
        self.destination = destination

    def calculate_domestic_fare(self, base_fare=100):
        """Calculates a simple fare for a domestic flight."""
        return base_fare * 1.15  # Add 15% tax

    def display_route(self):
        """Displays the flight's route."""
        print(f"Route: {self.origin} -> {self.destination}")


class InternationalFlight(Flight):
    """
    Inherits from Flight. Represents a flight between different countries.
    """
    def __init__(self, flight_number, origin, destination, stopover_country, **kwargs):
        print("--> Initializing InternationalFlight")
        # --- MULTILEVEL INHERITANCE ---
        super().__init__(flight_number=flight_number, **kwargs)
        self.origin = origin
        self.destination = destination
        self.stopover_country = stopover_country

    def check_visa_requirements(self):
        """Checks if a visa is required for the stopover."""
        if self.stopover_country:
            print(f"Visa check required for stopover in {self.stopover_country}.")
        else:
            print("This is a direct international flight.")

    def display_route(self):
        """Displays the international flight's route, including stopovers."""
        route = f"Route: {self.origin} -> "
        if self.stopover_country:
            route += f"{self.stopover_country} -> "
        route += self.destination
        print(route)


class AirNZManagedFlight(DomesticFlight, InternationalFlight):
    """
    --- HYBRID INHERITANCE ---
    Inherits from both DomesticFlight and InternationalFlight.
    This class represents a final, fully-managed flight with specific operational details.
    
    Method Resolution Order (MRO) will be:
    AirNZManagedFlight -> DomesticFlight -> InternationalFlight -> Flight -> object
    """
    def __init__(self, flight_number, origin, destination, stopover_country=None, aircraft_type=None, is_koru_flight=False):
        print("---> Initializing AirNZManagedFlight")
        # --- HANDLING THE DIAMOND PROBLEM ---
        # We explicitly call the __init__ of the next class in the MRO that has the attributes we need.
        # In this case, InternationalFlight's __init__ is more comprehensive.
        # The `**kwargs` pattern is not used here to show the explicit call.
        super().__init__(
            flight_number=flight_number, 
            origin=origin, 
            destination=destination, 
            stopover_country=stopover_country
        )
        self.aircraft_type = aircraft_type
        self.is_koru_flight = is_koru_flight

    def assign_aircraft(self, aircraft_type):
        """Assigns a specific aircraft to the flight."""
        self.aircraft_type = aircraft_type
        print(f"Aircraft {self.aircraft_type} assigned to flight {self.flight_number}.")

    def display_full_details(self):
        """Displays a complete summary of the managed flight."""
        print(f"\n--- Full Flight Details for {self.flight_number} ---")
        self.display_flight_id()  # Inherited from Flight
        
        # The MRO ensures display_route() from DomesticFlight is called first.
        # We can call the InternationalFlight one explicitly if needed.
        self.display_route() 
        
        if self.stopover_country:
            self.check_visa_requirements() # Inherited from InternationalFlight
        
        print(f"Aircraft: {self.aircraft_type}")
        print(f"Koru Club Access: {'Yes' if self.is_koru_flight else 'No'}")
        print("--------------------------------------------------")
