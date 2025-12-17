class Person:
    """Base class for all people in the hospital (Inheritance Example)."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}"

class Doctor(Person):
    """Represents a doctor."""
    def __init__(self, name, age, specialty):
        super().__init__(name, age)
        self.specialty = specialty

    def get_details(self):
        # Polymorphism: Overriding the parent method
        return f"👨‍⚕️ Dr. {self.name} - Specialist in {self.specialty}"

class Patient(Person):
    """Represents a patient."""
    def __init__(self, name, age, ailment):
        super().__init__(name, age)
        self.ailment = ailment
        self.assigned_doctor = None

    def assign_doctor(self, doctor):
        self.assigned_doctor = doctor

    def get_details(self):
        doc_info = self.assigned_doctor.name if self.assigned_doctor else "None"
        return f"🤒 Patient: {self.name} (Ailment: {self.ailment}) -> Doctor: {doc_info}"

class HospitalManager:
    """Manages doctors and patients."""
    def __init__(self):
        self.doctors = []
        self.patients = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        print(f"✅ Doctor added: {doctor.name}")

    def admit_patient(self, patient):
        self.patients.append(patient)
        print(f"✅ Patient admitted: {patient.name}")

    def list_all(self):
        print("\n--- HOSPITAL STATUS ---")
        print("Doctors:")
        for d in self.doctors:
            print(d.get_details())
        print("\nPatients:")
        for p in self.patients:
            print(p.get_details())

if __name__ == "__main__":
    hospital = HospitalManager()
    
    # Create Staff
    d1 = Doctor("Berkan Bicen", 35, "Neurology")
    d2 = Doctor("House M.D.", 45, "Diagnostics")
    
    hospital.add_doctor(d1)
    hospital.add_doctor(d2)
    
    # Create Patients
    p1 = Patient("John Doe", 25, "Migraine")
    p1.assign_doctor(d1)
    
    hospital.admit_patient(p1)
    
    hospital.list_all()