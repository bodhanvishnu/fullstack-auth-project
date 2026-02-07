#Fullstack Auth System (Flask + React)

A production-ready authentication and authorization system built with Flask and React, featuring JWT-based authentication, role-based access control (RBAC), and a secure deployment behind Nginx with HTTPS.
This project demonstrates end-to-end ownership: backend APIs, frontend integration, deployment, and infrastructure decisions.

#Live Demo

Frontend (HTTPS):
https://fullstack-auth.duckdns.org

#Tech Stack
#Backend
Python, Flask
Flask-JWT-Extended (access & refresh tokens)
MySQL
Gunicorn (WSGI server)
Nginx (reverse proxy)

#Frontend
React
Axios
React Router
Plain CSS (minimal, clean UI)
Infrastructure
DigitalOcean VPS
Nginx reverse proxy
HTTPS via Certbot (Let’s Encrypt)
DuckDNS (free domain)

#Features
Authentication
User signup and login
Password hashing
JWT access tokens
JWT refresh tokens
Protected routes using @jwt_required
Authorization (RBAC)
Roles stored as JWT claims
Role-based route protection via decorators
Admin-only endpoints
User-specific endpoints

#Frontend
Login and Signup pages
Dashboard with user profile
Admin dashboard with all users list
Protected routes based on authentication state
Token-based API access

#Deployment
Backend served via Gunicorn
Frontend served as a static build via Nginx
SSL termination at Nginx
Backend APIs proxied internally (/auth, /user, /admin)
No direct exposure of Gunicorn to the internet

#API Routes Overview
Auth
POST /auth/signup
POST /auth/login
POST /auth/refresh

User

GET /user/dashboard
GET /user/profile

Admin

GET /admin/dashboard
GET /admin/get-all-users

Architecture Overview
Browser (HTTPS)
   |
   v
Nginx (SSL termination)
   |
   +--> React build (static files)
   |
   +--> /auth, /user, /admin
            |
            v
        Gunicorn (Flask app)
            |
            v
          MySQL


Frontend never talks to raw IPs or ports
All API traffic goes through Nginx
Internal communication uses HTTP, external uses HTTPS

#Production Considerations & Trade-offs
This project was intentionally scoped to focus on correctness, clarity, and ownership before adding scale-oriented complexity.
Some production-level enhancements are intentionally documented but not yet implemented:

Database Connection Pooling
Currently using direct DB connections for simplicity.
In a higher-load environment, a connection pool (e.g., SQLAlchemy pooling) would be added to avoid exhausting MySQL connections.

Refresh Token Rotation & Revocation
Refresh tokens are implemented, but rotation and blacklist logic are not yet added.
In production, refresh tokens would be rotated and stored hashed server-side.

Centralized Error Handling
Error handling is explicit per route.
A global error handler would be added in a larger system for consistency.

Rate Limiting / Brute Force Protection
Not implemented yet, but would be added using middleware or a gateway-level solution.

These trade-offs were made deliberately to keep the system understandable and extensible.

Local Setup
Backend
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
gunicorn -w 4 -b 127.0.0.1:5006 app:app

Frontend
cd frontend
npm install
npm run build


Serve the build using Nginx.

#Why This Project
This project exists to demonstrate:
Understanding of authentication systems
Secure API design
Role-based authorization
Real-world deployment practices
Trade-off driven engineering decisions
It is designed to be easy to harden rather than over-engineered from day one.

Author
Built and deployed by Vishnu
Backend-leaning Full-Stack Developer (Flask, React)
