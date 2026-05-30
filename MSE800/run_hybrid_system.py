# run_hybrid_system.py
from flight_system import AirNZManagedFlight

def main():
    """
    Main function to demonstrate the hybrid inheritance flight system.
    """
    print("==== Demonstrating Hybrid Inheritance in Flight System ====\n")

    # --- Creating an Instance of the Final Subclass ---
    # This object will trigger the __init__ chain of all parent classes.
    # The MRO (Method Resolution Order) determines the call sequence.
    managed_flight = AirNZManagedFlight(
        flight_number="NZ101",
        origin="Auckland",
        destination="Los Angeles",
        stopover_country="Fiji",
        aircraft_type="Boeing 787-9 Dreamliner",
        is_koru_flight=True
    )

    # --- Calling Methods from Different Parent Classes ---
    # The object `managed_flight` has access to methods from all its ancestors.
    
    # Method from Flight (top-level parent)
    print(f"\nAirline Info: {managed_flight.get_airline_info()}")

    # Method from InternationalFlight
    managed_flight.check_visa_requirements()

    # Method from DomesticFlight (called via MRO in display_full_details)
    # Note: display_route in DomesticFlight is simpler, but it's the one that gets called
    # because of the MRO: AirNZManagedFlight -> DomesticFlight -> InternationalFlight -> ...
    
    # Method from AirNZManagedFlight itself
    managed_flight.display_full_details()

    # You can see the MRO by uncommenting the line below
    # print("\nMethod Resolution Order (MRO):")
    # print(AirNZManagedFlight.mro())


if __name__ == "__main__":
    main()
