# ZecPath Job Portal API

## Project Description

ZecPath is a Job Portal REST API developed using Django and Django REST Framework. It provides APIs for Employers and Candidates to manage job postings and applications.

## Technologies Used

- Python 3.14
- Django 6.0.7
- Django REST Framework
- SQLite3
- python-dotenv

## Features

- Custom User Model
- Employer Registration
- Candidate Registration
- Job Management
- Job Application Management
- REST APIs

## Project Structure

```
zecpath/
│── app/
│── zecpath_project/
│── manage.py
│── requirements.txt
│── README.md
│── .gitignore
```

## Installation

```bash
git clone https://github.com/Adhithyan-vs-03/zecpath_project.git

cd zecpath

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/jobs/ | List Jobs |
| POST | /api/jobs/create/ | Create Job |
| GET | /api/user-test/ | Test API |

## Author

**Adhithyan VS**