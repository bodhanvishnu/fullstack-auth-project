Flask JWT RBAC Backend

A Flask backend project implementing JWT authentication and role-based access control (RBAC).

This project focuses on building authentication and authorization in a clean, understandable way using Flask and MySQL.

Features

User signup and login

JWT-based authentication

Role-based access (USER / ADMIN)

Admin-only protected routes

Clean separation of routes and services

MySQL integration using raw SQL

Tech Stack

Python, Flask

Flask-JWT-Extended

MySQL (PyMySQL)

Werkzeug (password hashing)

Project Structure
app.py
db/         # database connection
services/   # user-related DB logic
routes/     # auth, user, admin routes
utils/      # RBAC decorator

API Overview

Auth

POST /auth/signup

POST /auth/login

User

GET /user/dashboard

GET /user/profile

Admin

GET /admin/dashboard

GET /admin/all-users-list

Running Locally
pip install -r requirements.txt
python app.py


Server runs on:

http://localhost:5006

Notes

JWT contains user ID and role

Access control is enforced at route level

.env is not committed

Future Improvements

Refresh tokens

Frontend integration

Deployment setup

This project was built to understand real-world backend authentication and authorization patterns.
