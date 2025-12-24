# 🏗️ Object-Oriented System Simulations

A comprehensive collection of console-based system simulations designed to demonstrate advanced **Software Architecture** and **Object-Oriented Programming (OOP)** principles in Python.

## 🚀 Architectural Vision
This repository moves beyond simple scripting to showcase professional software engineering patterns. The goal is to build scalable, maintainable, and robust backend logic.

### Key Technical Pillars:
- **Abstraction (ABC):** Leveraged Python's `abc` module to define strict interfaces, preventing improper instantiation of base entities.
- **Polymorphism:** Implemented dynamic behavior for various roles (e.g., Student vs. Staff fee logic) through method overriding.
- **Encapsulation:** Protected core data integrity using property decorators and protected attributes.
- **Robust Error Handling:** Designed a hierarchy of custom exceptions (BankingError, ParkingError) to ensure system stability.
- **Type Hinting:** Applied PEP 484 standards across all modules for improved code clarity and IDE support.

---

## 📂 Projects Overview

### 1. 🏎️ Parking Management System
**File:** `parking_management_system.py`
A simulation for urban parking facilities featuring role-based logic.
- **Highlight:** Uses polymorphism to calculate different fee rates for Students and Staff members.
- **Tech Stack:** ABC, Encapsulation, Custom Exception Handling.

### 2. 🏥 Hospital Management (Trauma Team Edition)
**File:** `hospital_management_system.py`
A **Cyberpunk 2077** themed medical management system.
- **Highlight:** Manages complex relationships between Ripperdocs (Doctors) and Patients with specific neural/cyberware conditions.
- **Context:** Features Night City legends like Viktor Vektor and V.

### 3. 💳 ATM Management (Arasaka Banking)
**File:** `atm_management_system.py`
A high-security financial terminal simulation focused on transaction integrity.
- **Highlight:** Strict authentication layers and secure credit-chip (balance) management.
- **Security:** Implements `InsufficientFundsError` and `InvalidPinError` for realistic banking flow.

---

## 🧪 Quick Start & Demo
To explore the simulations with pre-registered data, use these credentials:

| System | Serial ID / Plate | PIN / Type | Notes |
| :--- | :--- | :--- | :--- |
| **ATM** | `77-V` | `2077` | High-priority Arasaka account |
| **Hospital** | `PAT-77` | `Relic` | Consult with Viktor Vektor |
| **Parking** | `06 BB 66` | `Student` | Testing role-based fee logic |

---

## 👨‍💻 Author
**Berkan Biçen** *Software Engineering Student @ OSTIM Technical University*

---
