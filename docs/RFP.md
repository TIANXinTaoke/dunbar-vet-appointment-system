# Request for Proposal (RFP)
Project: Dunbar Veterinary Clinic Appointment Management System

## 1. Introduction and Background
Dunbar Veterinary Clinic is a mixed‑practice rural veterinary clinic located in Boonah, Queensland. The clinic currently manages appointments by paper‑based appointment book and green farm‑visit diary. The existing VetLedger4 software only supports invoicing and medication recording and cannot handle appointment scheduling. Manual recording causes double‑booking, missed appointments and human‑error data loss.

This project aims to procure software‑related tools and supporting services to build a lightweight appointment management system. The system must work without continuous internet connection because local network outages occur frequently in Boonah. The system will manage client records, animal records, property records, in‑clinic consultations and farm visit appointments.

Project objective: Deliver an offline‑first appointment system to replace manual paper booking records.

## 2. Scope of Work
### Project Description
Develop a local‑run appointment management system for Dunbar Veterinary Clinic. The system supports creating, searching, modifying and cancelling two types of appointments: fixed‑15‑minute in‑clinic consultations and variable‑duration farm property visits. Client, animal and property information shall be stored locally. No cloud‑only dependency is allowed.

### Deliverables expected from vendor
1. Complete Python source code for appointment management system.
2. Unit test scripts to verify core business logic.
3. External library list and installation guidance.
4. System configuration file for clinic parameters.
5. README document containing setup, run and test instructions.
6. No requirement for cloud hosting deployment; system runs locally on clinic Windows PCs.

### Timelines
- Week 1: Environment setup, project structure design
- Week 2: Implement core functions and unit testing
- Week 3: Final document completion and project hand‑over
Final delivery deadline: 28 September 2026

## 3. Technical Requirements
### Functional Requirements
1. Create, search and update client information.
2. Record animal profiles linked to corresponding clients.
3. Record farm property information for large‑animal farm visits.
4. Create two appointment types: 15‑minute in‑clinic consultation; variable‑time farm visit linked to property.
5. Modify and cancel appointments; cancelled appointments shall remain in records rather than being deleted.
6. List daily appointments for clinic consultation and farm visits.
7. Load clinic parameters from external JSON configuration file.

### Non‑Functional Requirements
1. Offline capability: The system must operate fully without internet access.
2. Usability: Text‑based interface; clinic staff can master basic operations within 30 minutes.
3. Reliability: No data loss when application restarts.
4. Maintainability: Source code managed by Git version‑control with clear commit messages.
5. Testability: Automated unit tests cover core appointment‑creation logic.

### Integration Requirements
This system shall NOT integrate with VetLedger4 in this project phase. No third‑party API integration required.

## 4. Proposal Guidelines
### Submission Instructions
Vendor shall provide access to a public Git repository containing full source code and documentation. All deliverables must be stored within the repository.

### Format
Source code: Python `.py` files; configuration: JSON; documentation: Markdown files readable on GitHub.

### Deadline
Proposal submission deadline: 21 September 2026. Final system delivery: 28 September 2026.

## 5. Evaluation Criteria
### Selection Process
Proposals will be reviewed against technical requirement completeness, offline‑working capability, test coverage and documentation quality.

### Criteria
1. Functional completeness (40%): meets all functional requirements for client, animal and two‑type‑appointment management.
2. Off‑line support (25%): system runs fully without internet connection.
3. Testing quality (20%): existence and pass‑rate of unit tests.
4. Documentation quality (15%): readability of README and project documents.

### Weighting
Weights shown above. Proposal failing offline‑working requirement will be rejected directly.

## 6. Vendor Information
### Company Overview
Vendor is a software‑development service provider providing custom lightweight desktop application for small‑rural‑business customers.

### Experience and Qualifications
Vendor shall have experience building local‑first Python desktop applications for small‑business clients. Experience working for veterinary or rural‑service organisations is preferred.

### References
Vendor shall provide two past client references for similar local‑application projects.

## 7. Cost Proposal
### Pricing Structure
Total fixed‑price project cost: AUD 3200.
Breakdown:
- Source‑code development: AUD 2400
- Unit‑test development and debugging: AUD 500
- Project documentation delivery: AUD 300

No ongoing annual licence fee. Software owned fully by Dunbar Veterinary Clinic upon final payment.

### Payment Terms
- 40% deposit upon contract signature
- 50% payment after successful system demonstration
- 10% final payment on final delivery acceptance

## 8. Terms and Conditions
### Contract Terms
All intellectual property of delivered source code transfers to Dunbar Veterinary Clinic after full payment. Vendor shall provide 30‑day bug‑fix support after hand‑over.

### Legal Requirements
Delivered software must comply with Australian privacy requirements for storing client personal and contact information.

## 9. Additional Information
### Q&A Sessions
Virtual Q&A session available on 14 September 2026 for vendor questions.

### Contact Information
Contact person: Dr Simone Valdez, Dunbar Veterinary Clinic.

## 10. Appendices
### Supporting Documents
1. Dunbar Veterinary Clinic background and interview notes.
2. Paper appointment‑book sample reference.

### Glossary
- In‑clinic consultation: Fixed 15‑minute appointment inside clinic consulting rooms.
- Farm visit: Variable‑duration on‑site service to rural property.
