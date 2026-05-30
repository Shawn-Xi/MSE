# flight_demonstration.py
from flight_system import DomesticFlight

def run_flight_demonstration():
    """
    Main function to demonstrate the single inheritance flight system.
    """
    print("==== Air New Zealand Domestic Flight System ====\n")

    # --- Creating an Instance of the Subclass ---
    # This creates a DomesticFlight object. Notice it requires arguments for both
    # the parent class (Flight) and its own specific attributes.
    flight_nz535 = DomesticFlight(
        flight_number="NZ535",
        origin="Auckland",
        destination="Wellington",
        departure_time="10:00 AM",
        aircraft_type="Airbus A320"  # This is the subclass-specific attribute
    )

    # --- Accessing Inherited and Specific Methods ---
    # The display_flight_details() method is called on the DomesticFlight object.
    # This will execute the overridden method in the DomesticFlight class,
    # which in turn calls the parent method.
    flight_nz535.display_flight_details()

    # --- Another Example ---
    flight_nz801 = DomesticFlight(
        flight_number="NZ801",
        origin="Nelson",
        destination="Christchurch",
        departure_time="2:30 PM",
        aircraft_type="ATR 72"
    )
    flight_nz801.display_flight_details()


if __name__ == "__main__":
    run_flight_demonstration()
