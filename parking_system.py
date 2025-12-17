import datetime

# ==============================================================================
## SECTION 1: CUSTOM EXCEPTIONS (Exception Handling)
# (OOP Requirement: Inheritance is used to create a hierarchy of exceptions)
# ==============================================================================
class ParkingError(Exception):
    """Base exception class for all custom parking system errors."""
    pass

class DuplicatePlateError(ParkingError):
    """Exception raised when attempting to register an already existing plate."""
    pass

class FullLotError(ParkingError):
    """Exception raised when attempting to park a vehicle in a full lot."""
    pass

class VehicleNotParkedError(ParkingError):
    """Exception raised when attempting to remove a vehicle that is not currently parked."""
    pass

# ==============================================================================
## SECTION 2: CORE DATA CLASSES (Encapsulation and Composition)
# ==============================================================================

class Vehicle:
    """Represents a driver's vehicle."""
    
    def __init__(self, license_plate: str, vehicle_type: str):
        # Encapsulation: Attributes are protected (conventionally private).
        self._license_plate = self._validate_plate(license_plate)
        self._vehicle_type = vehicle_type
        
    @staticmethod
    def _validate_plate(plate):
        """Checks license plate validity and cleans it."""
        if not plate or not isinstance(plate, str):
            raise ValueError("License plate cannot be empty or invalid.")
        # Cleans spaces and converts to uppercase for internal consistency.
        return plate.upper().replace(" ", "")

    # Encapsulation: Getter method (@property) provides controlled access.
    @property
    def license_plate(self):
        """Returns the license plate."""
        return self._license_plate
        
    @property
    def vehicle_type(self):
        """Returns the vehicle type."""
        return self._vehicle_type
    
    def __str__(self):
        return f"Vehicle: {self.vehicle_type}, Plate: {self.license_plate}"

class Driver:
    """Represents a driver who applies for a parking pass."""
    
    def __init__(self, full_name: str, driver_id: str, vehicle: Vehicle):
        self._full_name = full_name
        self._driver_id = self._validate_id(driver_id)
        # Composition: The Driver object owns a reference to the Vehicle object.
        self._vehicle = vehicle
        
    @staticmethod
    def _validate_id(driver_id):
        """Validates the driver ID."""
        if not driver_id:
            raise ValueError("Driver ID cannot be empty.")
        return driver_id
        
    # Encapsulation: Getter methods (@property)
    @property
    def full_name(self):
        return self._full_name
        
    @property
    def driver_id(self):
        return self._driver_id

    @property
    def vehicle(self) -> Vehicle:
        """Returns the driver's vehicle object."""
        return self._vehicle
        
    def __str__(self):
        return f"Driver: {self.full_name} (ID: {self.driver_id}), {self.vehicle}"

# ==============================================================================
## SECTION 3: PASS CLASSES (Inheritance and Polymorphism)
# ==============================================================================

class ParkingPass:
    """The base class for all parking passes (Inheritance Base)."""
    
    def __init__(self, pass_id: str, driver: Driver, fee_rate: float):
        self._pass_id = pass_id
        self._driver = driver 
        self._fee_rate = fee_rate

    # Getter methods
    @property
    def driver(self) -> Driver:
        return self._driver

    @property
    def pass_id(self):
        return self._pass_id
        
    @property
    def fee_rate(self):
        return self._fee_rate

    # Polymorphism: Base method to be overridden
    def calculate_fee(self, hours_parked: float) -> float:
        """Calculates the parking fee based on the standard rate."""
        if hours_parked < 0:
             raise ValueError("Parked hours cannot be negative.")
        return hours_parked * self._fee_rate
        
    def __str__(self):
        return f"Standard Pass (ID: {self.pass_id}) - Rate: {self.fee_rate} TL/hour"


class StudentPass(ParkingPass):
    """Student parking pass (Inherits from ParkingPass)."""
    STUDENT_RATE = 2.0  # Rule: 2 TL/hour

    def __init__(self, pass_id: str, driver: Driver):
        # Inheritance: Calls the parent class constructor.
        super().__init__(pass_id, driver, self.STUDENT_RATE)

    # Polymorphism: Uses the parent's implementation (cheaper flat rate).
    def calculate_fee(self, hours_parked: float) -> float:
        return super().calculate_fee(hours_parked)
        
    def __str__(self):
        return f"Student Pass (ID: {self.pass_id}) - Rate: {self.fee_rate} TL/hour"


class StaffPass(ParkingPass):
    """Staff parking pass (Inherits from ParkingPass). Rule: FIRST 1 HOUR IS FREE."""
    STAFF_RATE = 3.0  # Rule: 3 TL/hour

    def __init__(self, pass_id: str, driver: Driver):
        # Inheritance: Calls the parent class constructor.
        super().__init__(pass_id, driver, self.STAFF_RATE)

    # Polymorphism: OVERRIDE of the calculate_fee method
    def calculate_fee(self, hours_parked: float) -> float:
        """Calculates the staff fee, applying the first 1 hour free rule."""
        
        if hours_parked < 0:
             raise ValueError("Parked hours cannot be negative.")
        
        # Rule: First 1 hour is free for staff
        if hours_parked <= 1.0:
            return 0.0
        
        # Charge only for the hours exceeding 1.0
        chargeable_hours = hours_parked - 1.0
        return chargeable_hours * self.fee_rate
        
    def __str__(self):
        return f"Staff Pass (ID: {self.pass_id}) - Rate: {self.fee_rate} TL/hour (First hour free)"

# ==============================================================================
## SECTION 4: PARKING LOT MANAGEMENT CLASS (ParkingLot)
# ==============================================================================

class ParkingLot:
    """Manages the physical parking Lot."""
    
    def __init__(self, name: str, capacity: int):
        self._name = name
        self._capacity = self._validate_capacity(capacity)
        # Encapsulation: Internal collection (Plate -> Entry Time)
        self._parked_vehicles = {} 
        
    @staticmethod
    def _validate_capacity(capacity):
        """Checks that capacity is positive."""
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer.")
        return capacity

    @property
    def name(self):
        return self._name

    @property
    def capacity(self):
        return self._capacity
        
    # Encapsulation: Controlled access to the internal collection
    def is_full(self) -> bool:
        """Checks if the parking lot is full."""
        return len(self._parked_vehicles) >= self._capacity
        
    def is_parked(self, license_plate: str) -> bool:
        """Checks if the specified plate is currently parked."""
        # Clean plate before checking.
        return license_plate.upper().replace(" ", "") in self._parked_vehicles

    def add_vehicle(self, license_plate: str):
        """Adds the vehicle to the lot and records the entry time."""
        plate = license_plate.upper().replace(" ", "")

        if self.is_full():
            # Exception Handling: Raises FullLotError if the lot is full.
            raise FullLotError(f"ERROR: '{self.name}' parking lot is full. Capacity reached.")
            
        if self.is_parked(plate):
             raise ParkingError(f"ERROR: Vehicle with plate ({plate}) is already parked.")

        # Record entry time
        self._parked_vehicles[plate] = datetime.datetime.now()
        print(f"✅ {plate} successfully parked. (Entry Time Recorded)")

    def remove_vehicle(self, license_plate: str) -> datetime.datetime:
        """Removes the vehicle from the lot and returns the entry time."""
        plate = license_plate.upper().replace(" ", "")

        if not self.is_parked(plate):
            # Exception Handling: Raises VehicleNotParkedError if the vehicle is not found.
            raise VehicleNotParkedError(f"ERROR: Vehicle with plate ({plate}) not found among parked vehicles.")
            
        # Remove the plate and return the entry time.
        entry_time = self._parked_vehicles.pop(plate)
        print(f"✅ {plate} successfully removed from the lot.")
        return entry_time
        
    def get_parked_plates(self):
        """Returns a copy of the plates of actively parked vehicles."""
        return list(self._parked_vehicles.keys())

# ==============================================================================
## SECTION 5: MAIN CONTROL CLASS (ParkingSystem)
# ==============================================================================

class ParkingSystem:
    """Central control class managing all driver, pass, and parking operations."""
    
    def __init__(self, lot_name: str, lot_capacity: int):
        # Composition: ParkingSystem owns a ParkingLot object.
        self._parking_lot = ParkingLot(lot_name, lot_capacity)
        
        # Encapsulation: Internal collections. Plate is the key.
        self._registered_drivers = {} # Plate -> Driver object
        self._issued_passes = {}     # Plate -> ParkingPass object (Polymorphic collection)

    # --- HELPER METHODS ---

    def _get_driver_by_plate(self, plate: str) -> Driver:
        """Returns the Driver object by plate, raises error if not found."""
        clean_plate = plate.upper().replace(" ", "")
        
        if clean_plate not in self._registered_drivers:
            raise ParkingError(f"ERROR: No driver or pass registered for plate ({clean_plate}). Registration is required first!")
        return self._registered_drivers[clean_plate]

    # --- CORE FUNCTIONAL METHODS (Menu Functions) ---

    def register_driver_and_vehicle(self, name: str, driver_id: str, plate: str, v_type: str):
        """Registers a new driver and vehicle in the system."""
        plate = plate.upper().replace(" ", "")
        
        if plate in self._registered_drivers:
            # Exception Handling: Raises DuplicatePlateError.
            raise DuplicatePlateError(f"ERROR: Plate ({plate}) is already registered in the system.")
        
        vehicle = Vehicle(plate, v_type)
        driver = Driver(name, driver_id, vehicle)
        
        self._registered_drivers[plate] = driver
        print(f"\n✅ Driver and Vehicle Registration Successful: {driver}")

    def issue_pass(self, plate: str, pass_type: str):
        """Issues a pass to a registered driver."""
        plate = plate.upper().replace(" ", "")
        
        try:
            driver = self._get_driver_by_plate(plate)
        except ParkingError as e:
            # Prevent issuing a pass to an unregistered driver
            raise e
            
        if plate in self._issued_passes:
            raise ParkingError(f"ERROR: A {self._issued_passes[plate].__class__.__name__} pass has already been issued for plate ({plate}).")

        pass_id = f"{plate}-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        if pass_type.lower() == 'student':
            new_pass = StudentPass(pass_id, driver) # Inheritance
        elif pass_type.lower() == 'staff':
            new_pass = StaffPass(pass_id, driver) # Inheritance
        else:
            raise ValueError("Invalid pass type. Must be 'student' or 'staff'.")
            
        self._issued_passes[plate] = new_pass
        print(f"\n✅ Pass Successfully Issued: {new_pass}")

    def park_vehicle(self, plate: str):
        """Parks a vehicle in the parking lot."""
        plate = plate.upper().replace(" ", "")
        
        try:
            if plate not in self._issued_passes:
                 raise ParkingError(f"ERROR: Vehicle with plate ({plate}) does not have an active parking pass. An active pass is required for entry.")
                 
            # Delegation to the ParkingLot class
            self._parking_lot.add_vehicle(plate)
            
        # Exception Handling: Catch errors raised by ParkingLot and display them to the user
        except ParkingError as e:
            print(f"\n🔴 Parking Operation Failed: {e}")

    def remove_vehicle_and_fee(self, plate: str, entry_time_override: datetime.datetime = None):
        """Removes the vehicle from the lot and calculates the fee (Polymorphism)."""
        plate = plate.upper().replace(" ", "")
        
        try:
            # 1. Remove the vehicle from ParkingLot and get entry time
            entry_time = self._parking_lot.remove_vehicle(plate)
            
            # Calculate parking duration
            exit_time = datetime.datetime.now()
            if entry_time_override:
                entry_time = entry_time_override
                
            parked_duration = exit_time - entry_time
            # Convert duration to hours (float)
            hours_parked = parked_duration.total_seconds() / 3600.0

            # 2. Retrieve the relevant ParkingPass object
            parking_pass = self._issued_passes.get(plate)
            
            # 3. Calculate the fee (Polymorphism in action)
            # When calculate_fee is called, the specific rule (Student/Staff) is applied.
            fee = parking_pass.calculate_fee(hours_parked)
            
            print("\n==============================================")
            print(f"💰 Vehicle Exit Information: {plate}")
            print(f"   Entry Time: {entry_time.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"   Exit Time: {exit_time.strftime('%Y-%m-%d %H:%M:%S')}")
            # Duration rounded to 2 decimal places
            print(f"   Duration: {hours_parked:.2f} hours ({int(parked_duration.total_seconds())} seconds)")
            print(f"   Pass Type: {parking_pass.__class__.__name__} ({parking_pass.fee_rate} TL/hour)")
            print(f"   **TOTAL FEE: {fee:.2f} TL**")
            print("==============================================")
            
        # Exception Handling: Catch errors and display them
        except ParkingError as e:
            print(f"\n🔴 Vehicle Removal Operation Failed: {e}")
        except Exception as e:
            print(f"\n❌ Unexpected Error Occurred: System failure detected: {e}. Please report this issue.")

    def list_active_passes(self):
        """Lists all active passes in the system."""
        print("\n--- Active Passes and Drivers ---")
        if not self._issued_passes:
            print("No active passes are currently registered in the system.")
            return

        for plate, card in self._issued_passes.items():
            driver = self._registered_drivers.get(plate)
            
            park_status = "Parked" if self._parking_lot.is_parked(plate) else "Not Parked"
            
            print(f"| {plate} | {card.pass_id} | {card.__class__.__name__} | Driver: {driver.full_name} | Status: {park_status}")
        print("---------------------------------")


    # --- MENU AND PROGRAM FLOW ---

    def _show_menu(self):
        """Prints the menu to the screen."""
        print("\n\n=== Ostim TechnoPark Smart Parking Management System ===")
        parked_count = len(self._parking_lot.get_parked_plates())
        print(f"Lot Capacity: {parked_count}/{self._parking_lot.capacity} (Available: {self._parking_lot.capacity - parked_count})")
        print("1. Register Driver and Vehicle")
        print("2. Issue Parking Pass")
        print("3. Park a Vehicle")
        print("4. Remove a Vehicle and Calculate Fee")
        print("5. List All Active Passes")
        print("6. Exit")
        return input("Enter your choice (1-6): ")

    def run_menu(self):
        """Runs the main program loop."""
        while True:
            choice = self._show_menu()
            
            try:
                if choice == '1':
                    print("\n--- Driver and Vehicle Registration ---")
                    name = input("Full Name: ")
                    driver_id = input("ID/Staff Number: ")
                    plate = input("License Plate (e.g., 06 BB 66): ")
                    v_type = input("Vehicle Type (car/motorcycle): ")
                    self.register_driver_and_vehicle(name, driver_id, plate, v_type)
                    
                elif choice == '2':
                    print("\n--- Pass Issuance ---")
                    plate = input("Plate to issue pass for: ")
                    pass_type = input("Pass Type (student/staff): ")
                    self.issue_pass(plate, pass_type)
                    
                elif choice == '3':
                    print("\n--- Vehicle Parking ---")
                    plate = input("Plate to park: ")
                    self.park_vehicle(plate)
                    
                elif choice == '4':
                    print("\n--- Vehicle Removal and Fee Calculation ---")
                    plate = input("Plate to remove: ")
                    # Note: For the take-home exam, you should use real time. 
                    # The entry_time_override parameter is only for debugging/testing
                    self.remove_vehicle_and_fee(plate) 
                    
                elif choice == '5':
                    self.list_active_passes()
                    
                elif choice == '6':
                    # Formal Exit Message
                    print("\n👋 Exiting the Parking Management System.")
                    print("Thank you for using the system. Allah'a emanet ol.")
                    break
                    
                else:
                    print("Invalid choice. Please enter a number between 1 and 6.")
            
            # Exception Handling: Catch all user input errors and custom exceptions
            except (ParkingError, ValueError) as e:
                print(f"\n🔴 Operation Error: {e}")
            except Exception as e:
                print(f"\n❌ Unexpected General Error: An unhandled exception occurred: {e}. Please try again.")

# ==============================================================================
## PROGRAM EXECUTION (MAIN BLOCK)
# ==============================================================================

if __name__ == "__main__":
    # Program entry point: Create the Parking System object
    LOT_NAME = "Ostim TechnoPark"
    LOT_CAPACITY = 10
    
    print(f"🚦 {LOT_NAME} Management System is starting...")
    parking_system = ParkingSystem(LOT_NAME, LOT_CAPACITY)
    
    # Run the main menu
    parking_system.run_menu()