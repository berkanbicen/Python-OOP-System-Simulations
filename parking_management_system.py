import datetime
from abc import ABC, abstractmethod
from typing import Dict, Optional

# ==============================================================================
## SECTION 1: CUSTOM EXCEPTIONS (Domain Driven Errors)
# ==============================================================================
class ParkingError(Exception):
    """Base class for all parking system exceptions."""
    pass

class DuplicatePlateError(ParkingError):
    """Raised when a plate is already registered."""
    pass

class FullLotError(ParkingError):
    """Raised when the parking lot is at capacity."""
    pass

class VehicleNotParkedError(ParkingError):
    """Raised when a vehicle is not found in the lot."""
    pass

# ==============================================================================
## SECTION 2: CORE ENTITIES (Encapsulation)
# ==============================================================================

class Vehicle:
    def __init__(self, license_plate: str, vehicle_type: str):
        self._license_plate = self.sanitize_plate(license_plate)
        self._vehicle_type = vehicle_type
        
    @staticmethod
    def sanitize_plate(plate: str) -> str:
        """Cleans and standardizes the license plate format."""
        if not plate or not isinstance(plate, str):
            raise ValueError("Invalid license plate format.")
        return plate.upper().replace(" ", "")

    @property
    def license_plate(self) -> str:
        return self._license_plate

    def __str__(self) -> str:
        return f"[{self.license_plate}] - {self._vehicle_type.capitalize()}"

class Driver:
    def __init__(self, full_name: str, driver_id: str, vehicle: Vehicle):
        self._full_name = full_name
        self._driver_id = driver_id
        self._vehicle = vehicle 

    @property
    def full_name(self) -> str:
        return self._full_name

    def __str__(self) -> str:
        return f"Driver: {self.full_name} | {self._vehicle}"

# ==============================================================================
## SECTION 3: PASS LOGIC (Polymorphism & Abstraction)
# ==============================================================================

class ParkingPass(ABC):
    def __init__(self, pass_id: str, driver: Driver, fee_rate: float):
        self._pass_id = pass_id
        self._driver = driver 
        self._fee_rate = fee_rate

    @abstractmethod
    def calculate_fee(self, hours_parked: float) -> float:
        """Calculate the specific fee based on pass type."""
        pass

class StudentPass(ParkingPass):
    STUDENT_RATE = 2.0  # TL/hour

    def __init__(self, pass_id: str, driver: Driver):
        super().__init__(pass_id, driver, self.STUDENT_RATE)

    def calculate_fee(self, hours_parked: float) -> float:
        return max(0.0, hours_parked * self._fee_rate)

class StaffPass(ParkingPass):
    STAFF_RATE = 3.0  # TL/hour

    def __init__(self, pass_id: str, driver: Driver):
        super().__init__(pass_id, driver, self.STAFF_RATE)

    def calculate_fee(self, hours_parked: float) -> float:
        # Rule: First 1 hour is free for staff
        chargeable_hours = max(0.0, hours_parked - 1.0)
        return chargeable_hours * self._fee_rate

# ==============================================================================
## SECTION 4: MANAGEMENT (Business Logic)
# ==============================================================================

class ParkingSystem:
    def __init__(self, lot_name: str, capacity: int):
        self._name = lot_name
        self._capacity = capacity
        self._parked_vehicles: Dict[str, datetime.datetime] = {}
        self._drivers: Dict[str, Driver] = {}
        self._passes: Dict[str, ParkingPass] = {}

    def register_driver(self, name: str, d_id: str, plate: str, v_type: str):
        vehicle = Vehicle(plate, v_type)
        self._drivers[vehicle.license_plate] = Driver(name, d_id, vehicle)
        print(f"✅ Registration Successful: {self._drivers[vehicle.license_plate]}")

    def issue_pass(self, plate: str, p_type: str):
        clean_plate = Vehicle.sanitize_plate(plate)
        driver = self._drivers.get(clean_plate)
        if not driver:
            raise ParkingError("Driver must be registered first!")
        
        pass_id = f"PASS-{clean_plate}-{datetime.datetime.now().strftime('%M%S')}"
        if p_type.lower() == 'student':
            self._passes[clean_plate] = StudentPass(pass_id, driver)
        else:
            self._passes[clean_plate] = StaffPass(pass_id, driver)
        print(f"🎫 Pass Issued: {p_type.upper()}")

    def process_entry(self, plate: str):
        clean_plate = Vehicle.sanitize_plate(plate)
        if clean_plate not in self._passes:
            raise ParkingError("No active pass found!")
        if len(self._parked_vehicles) >= self._capacity:
            raise FullLotError("The parking lot is full.")
        
        self._parked_vehicles[clean_plate] = datetime.datetime.now()
        print(f"🚀 Entry Successful: {clean_plate}")

    def process_exit(self, plate: str):
        clean_plate = Vehicle.sanitize_plate(plate)
        if clean_plate not in self._parked_vehicles:
            raise VehicleNotParkedError("Vehicle is not in the lot.")
        
        entry_time = self._parked_vehicles.pop(clean_plate)
        duration = (datetime.datetime.now() - entry_time).total_seconds() / 3600.0
        fee = self._passes[clean_plate].calculate_fee(duration)
        
        print(f"\n💰 Exit Processed: {clean_plate}")
        print(f"⏱️ Duration: {duration:.2f} hours | Total Fee: {fee:.2f} TL")

# ==============================================================================
## MAIN LOOP
# ==============================================================================

if __name__ == "__main__":
    sys = ParkingSystem("OSTIM TechnoPark", 10)
    
    while True:
        print(f"\n--- {sys._name} Management System ---")
        print("1. Register | 2. Issue Pass | 3. Entry | 4. Exit | 5. Shutdown")
        choice = input("Select an option: ")
        
        try:
            if choice == '1':
                sys.register_driver(input("Name: "), input("ID: "), input("Plate: "), "Car")
            elif choice == '2':
                sys.issue_pass(input("Plate: "), input("Type (student/staff): "))
            elif choice == '3':
                sys.process_entry(input("Plate: "))
            elif choice == '4':
                sys.process_exit(input("Plate: "))
            elif choice == '5':
                print("Shutting down the system...")
                break
        except Exception as e:
            print(f"⚠️ Operation Failed: {e}")
