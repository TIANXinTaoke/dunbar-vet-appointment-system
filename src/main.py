"""
Dunbar Veterinary Appointment System
Language school related vet booking system for assignment
"""
from datetime import datetime

class Appointment:
    def __init__(self, pet_name, owner_name, contact, appointment_time, service_type):
        self.pet_name = pet_name
        self.owner_name = owner_name
        self.contact = contact
        self.appointment_time = appointment_time
        self.service_type = service_type

    def __str__(self):
        return f"[{self.appointment_time}] Pet:{self.pet_name}, Owner:{self.owner_name}, Service:{self.service_type}"


class VetAppointmentSystem:
    def __init__(self):
        self.appointment_list = []

    def create_appointment(self, pet_name, owner_name, contact, appointment_time, service_type):
        new_app = Appointment(pet_name, owner_name, contact, appointment_time, service_type)
        self.appointment_list.append(new_app)
        return new_app

    def list_all_appointments(self):
        if not self.appointment_list:
            print("No appointments found.")
            return
        for item in self.appointment_list:
            print(item)


if __name__ == "__main__":
    system = VetAppointmentSystem()
    print("=== Dunbar Vet Appointment System ===")
    # Demo data
    system.create_appointment(
        pet_name="Mimi",
        owner_name="Tom",
        contact="tom@example.com",
        appointment_time="2026-10-01 10:00",
        service_type="General Checkup"
    )
    system.list_all_appointments()
