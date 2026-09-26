# Configuration Management Report
## Project: Dunbar Veterinary Clinic Appointment System

### 1. Introduction
This report describes the configuration management strategy used for the Dunbar vet appointment system project. Git and GitHub are used as the version control tool to manage all source code, test files and project documents.

### 2. Configuration Items (CIs)
All items tracked under version control:
1. Source code: `src/main.py`
2. Test code: `tests/test_appointment.py`
3. Configuration file: `config/config.json`
4. Project documents: `docs/RFP.md`, `docs/ConfigurationManagementReport.md`
5. Repository settings: `.gitignore`, `README.md`

### 3. Version Control Strategy
- Branch: Only `main` branch is used for this assignment.
- Commit rule: Each commit has a clear message describing changes.
- `.gitignore` file: Exclude temporary files, cache files, log files, avoid committing unnecessary files.

### 4. Change Control Process
1. Developer modifies files locally.
2. Run unit tests to verify changes work correctly.
3. Use `git add` to stage modified configuration items.
4. Use `git commit` to create a local commit with descriptive message.
5. Use `git push` to upload changes to GitHub remote repository.
6. Review GitHub repository to confirm all files are updated.

### 5. Repository Structure
