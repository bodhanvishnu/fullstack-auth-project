# Fullstack Authentication System (Flask + React)

This project is a production-ready authentication system built using **Flask** for the backend and **React** for the frontend. It implements **JWT-based authentication** along with **role-based access control (RBAC)** and follows a clean, modular backend structure.

The backend is deployed using **Gunicorn** on a DigitalOcean server, and the application is live.

Live application:  
http://159.65.145.247:3001/

---

## Why this project

Most applications need a solid authentication layer before anything else.  
This project focuses on building that foundation properly:

- Clear separation between authentication, authorization, and business logic
- Token-based auth suitable for frontend-backend separation
- A structure that can scale as features grow

The goal was to build something realistic, not a demo-only project.

---

## Core Features

### Backend (Flask)
- JWT-based authentication
- Role-Based Access Control (RBAC)
- Modular architecture using routes, services, and utilities
- Centralized auth and role validation logic
- Designed for extension (more roles, permissions, or services)

### Frontend (React)
- Login and signup flow
- Token-based session handling
- Protected routes based on authentication state
- Communicates with Flask APIs

---

## Tech Stack

- Backend: Flask (Python)
- Frontend: React
- Authentication: JWT
- Deployment: Gunicorn
- Server: DigitalOcean

---

## Project Structure

fullstack-auth-project/
├── backend/
│ ├── app.py
│ ├── routes/ # API routes (auth, user)
│ ├── services/ # Business logic
│ ├── utils/ # Auth & RBAC helpers
│ └── db/ # Database connections
├── frontend/
│ ├── src/ # React source code
│ ├── public/
│ ├── package.json
│ └── package-lock.json
└── .gitignore


## Running Locally

### Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py

#Frontend
cd frontend
npm install
npm start


The frontend runs on http://localhost:3000 and communicates with the Flask backend via APIs.

#Deployment

The backend is deployed on a DigitalOcean server using Gunicorn for production serving.
The application is live at:

http://159.65.145.247:3000/

Future Improvements

This project can be extended with:

Refresh tokens

Password reset flow

More granular permissions

Rate limiting

Audit logging


