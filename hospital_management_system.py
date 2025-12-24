import datetime
from abc import ABC, abstractmethod
from typing import Dict, List, Optional

# ==============================================================================
## SECTION 1: CUSTOM EXCEPTIONS (Domain-Specific Error Architecture)
# ==============================================================================
class HospitalError(Exception):
    """Base exception class for all hospital-related errors."""
    pass

class PersonNotFoundError(HospitalError):
    """Raised when a specific doctor or patient ID cannot be found."""
    pass

class AssignmentError(HospitalError):
    """Raised when a medical assignment fails logic checks."""
    pass

# ==============================================================================
## SECTION 2: CORE ENTITIES (Abstraction & Inheritance)
# ==============================================================================

class Person(ABC):
    """
    Abstract Base Class for all hospital personnel and patients.
    Ensures architectural integrity by preventing direct instantiation.
    """
    def __init__(self, name: str, age: int, person_id: str):
        self._name = name
        self._age = age
        self._person_id = person_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def person_id(self) -> str:
        return self._person_id

    @abstractmethod
    def get_summary(self) -> str:
        """Polymorphic method to be implemented by specialized subclasses."""
        pass

class Doctor(Person):
    """Represents a medical specialist (Ripperdoc in Night City terms)."""
    def __init__(self, name: str, age: int, doctor_id: str, specialty: str):
        super().__init__(name, age, doctor_id)
        self._specialty = specialty

    def get_summary(self) -> str:
        # Polymorphism: Specific formatting for Doctor entities
        return f"👨‍⚕️ Dr. {self.name} (Specialty: {self._specialty}) [ID: {self.person_id}]"

class Patient(Person):
    """Represents a person receiving medical care."""
    def __init__(self, name: str, age: int, patient_id: str, ailment: str):
        super().__init__(name, age, patient_id)
        self._ailment = ailment
        self._assigned_doctor: Optional[Doctor] = None

    def assign_doctor(self, doctor: Doctor):
        """Encapsulation: Controlled access to set the doctor reference."""
        self._assigned_doctor = doctor

    def get_summary(self) -> str:
        # Polymorphism: Specific formatting for Patient entities
        doc_info = self._assigned_doctor.name if self._assigned_doctor else "WAITING FOR ASSIGNMENT"
        return f"🤒 Patient: {self.name} | Condition: {self._ailment} | Assigned to: {doc_info}"

# ==============================================================================
## SECTION 3: SYSTEM MANAGEMENT (Business Logic Layer)
# ==============================================================================

class HospitalSystem:
    """Central orchestrator for medical staff and patient data."""
    def __init__(self, hospital_name: str):
        self._name = hospital_name
        self._doctors: Dict[str, Doctor] = {}
        self._patients: Dict[str, Patient] = {}

    def add_doctor(self, name: str, age: int, d_id: str, specialty: str):
        new_doctor = Doctor(name, age, d_id, specialty)
        self._doctors[d_id] = new_doctor
        print(f"✅ Medical Staff Registered: {new_doctor.name}")

    def admit_patient(self, name: str, age: int, p_id: str, ailment: str):
        new_patient = Patient(name, age, p_id, ailment)
        self._patients[p_id] = new_patient
        print(f"✅ Patient Admitted to Trauma Team: {new_patient.name}")

    def assign_patient_to_doctor(self, p_id: str, d_id: str):
        patient = self._patients.get(p_id)
        doctor = self._doctors.get(d_id)

        if not patient:
            raise PersonNotFoundError(f"CRITICAL: Patient ID {p_id} not found in database.")
        if not doctor:
            raise PersonNotFoundError(f"CRITICAL: Specialist ID {d_id} not found in database.")

        patient.assign_doctor(doctor)
        print(f"🤝 Linked: {patient.name} is now under the supervision of {doctor.name}")

    def display_status(self):
        """Prints the current overview of the entire facility."""
        print(f"\n{'='*20} {self._name.upper()} STATUS {'='*20}")
        print("\n[ACTIVE MEDICAL STAFF]")
        for doc in self._doctors.values():
            print(doc.get_summary())
        
        print("\n[HOSPITALIZED PATIENTS]")
        for pat in self._patients.values():
            print(pat.get_summary())
        print(f"\n{'='*55}")

# ==============================================================================
## SECTION 4: MAIN EXECUTION (Welcome to Night City)
# ==============================================================================

if __name__ == "__main__":
    # Initializing the Cyberpunk-themed hospital
    trauma_center = HospitalSystem("Night City Trauma Team Center")

    try:
        print("🌐 Syncing with Arasaka Medical Network...")
        
        # Adding Medical Staff (Famous Ripperdocs & Netrunners)
        trauma_center.add_doctor("Viktor Vektor", 45, "DOC-001", "Cyberware Surgery")
        trauma_center.add_doctor("Lucy Kushinada", 21, "DOC-002", "Neural-Link Repair")
        trauma_center.add_doctor("Finger's Ripperdoc", 55, "DOC-003", "Black Market Tech")

        print("\n📥 Processing Urgent Admissions...")
        
        # Admitting Patients (Night City Legends)
        trauma_center.admit_patient("V (Vincent)", 27, "PAT-77", "Relic Corruption")
        trauma_center.admit_patient("Jackie Welles", 30, "PAT-88", "Gunshot Wounds")
        trauma_center.admit_patient("Johnny Silverhand", 99, "PAT-00", "Engram Defragmentation")

        # System Assignments
        print("\n🛠️ Automating Physician Assignments...")
        trauma_center.assign_patient_to_doctor("PAT-77", "DOC-001") # V assigned to Viktor
        trauma_center.assign_patient_to_doctor("PAT-00", "DOC-002") # Johnny assigned to Lucy

        # Final Overview
        trauma_center.display_status()

    except HospitalError as e:
        print(f"❌ DATABASE BREACH/ERROR: {e}")
    except Exception as e:
        print(f"⚠️ UNHANDLED SYSTEM CRASH: {e}")
