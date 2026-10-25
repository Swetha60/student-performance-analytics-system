# Student Performance Analytics System

## Project Overview

The Student Performance Analytics System is a web-based application developed using Django and Python. It helps manage student information, academic records, attendance, and marks through a centralized interface.

<img width="1869" height="848" alt="Image" src="https://github.com/user-attachments/assets/35a82bfe-caf6-4a2a-ae54-7314484a5167" />

The main objective is to organize student academic data and make it easier to monitor student performance.

## Objectives

- Manage student and classroom information.
- Maintain subject and examination details.
- Record assessments and student marks.
- Record and manage student attendance.
- Display student-related summary information on the dashboard.
- Provide a simple interface for managing academic records.

## Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite
- **Development Environment:** Visual Studio Code
- **Version Control (optional):** Git and GitHub

## Main Modules

1. **Dashboard:** Displays summary information such as total students, classrooms, subjects, marks, and attendance records.
2. **Student Management:** Supports student record management.
3. **Academic Management:** Manages subjects, examinations, assessments, and marks.
4. **Attendance Management:** Records and manages student attendance.
5. **Analytics:** Provides student performance-related summaries or visualizations, depending on the implemented features.
6. **Django Admin:** Provides an administrative interface for managing registered model records.

## Installation and Setup

### 1. Clone or download the project

Download the project source code to your computer and open its root folder in VS Code.

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

On Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Django

```bash
python -m pip install django
```

If a `requirements.txt` file is available, install the project's dependencies using:

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open the following address in your browser:

http://127.0.0.1:8000/

## Testing

Before submission, verify the following:

- The application starts without errors.
- The dashboard displays correctly.
- Student records can be added, edited, and deleted, where implemented.
- Subjects, examinations, assessments, and marks pages work.
- Attendance can be recorded and saved.
- Navigation links open the correct pages.
- The Django system check completes successfully.

Run the system check with:

```bash
python manage.py check
```

## Future Enhancements

- Student performance prediction using machine learning.
- Advanced analytics and interactive charts.
- PDF and Excel report exports.
- Role-based access for teachers and students.
- Automated notifications for attendance and academic performance.

## Conclusion

The Student Performance Analytics System demonstrates how Django can be used to develop a centralized application for managing student information, academic records, marks, and attendance. It provides a foundation for future enhancements in educational data analytics.
