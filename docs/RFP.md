# Request for Proposal (RFP)
# Dunbar Veterinary Clinic Appointment System
## 1. Project Overview
Dunbar Veterinary Clinic is a local animal hospital. Currently, appointment bookings are managed manually using paper notebooks and phone calls. This causes missed appointments, double booking, and difficulty tracking pet medical history.
The clinic requires a lightweight desktop appointment management system to help receptionists manage pet appointments, record customer information, and view daily schedules.

## 2. Business Background
- Clinic name: Dunbar Veterinary Clinic
- Opening hours: 09:00 - 17:00
- Maximum daily appointments: 12
- Users: Clinic reception staff

## 3. Functional Requirements
1. Create new appointment: input pet name, owner name, contact information, appointment time, service type.
2. View all existing appointments.
3. Check appointment conflict: prevent double booking for the same time slot.
4. Delete or cancel existing appointments.
5. Load system configuration from config file.
6. Save appointment data locally.

## 4. Non-Functional Requirements
1. Usability: Simple text-based interface, receptionists can learn to operate within 30 minutes.
2. Reliability: System should not crash during daily operation.
3. Maintainability: Code stored in GitHub, use Git version control.
4. Testability: Unit tests are provided to verify core appointment creation function.

## 5. Deliverables
1. Python source code, stored in GitHub repository.
2. Unit test scripts.
3. System configuration file (JSON).
4. Configuration management report.
5. README documentation for system setup and running tests.

## 6. Project Timeline
- Week 1: Set up GitHub repository, folder structure, initial code.
- Week 2: Implement core appointment functions, write unit tests.
- Week 3: Complete documentation, final submission.

## 7. Acceptance Criteria
1. The system can successfully create valid appointments.
2. The system rejects duplicate time booking.
3. All unit tests pass.
4. All source code and documents are committed to GitHub repository.
