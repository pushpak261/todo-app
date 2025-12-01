# Full Stack TODO Application  
### React + FastAPI + MongoDB + JWT Authentication  

## Overview
This is a secure, full–stack task management system that allows users to:
- Create an account  
- Authenticate using JWT  
- Create todo items  
- Mark todos as completed  
- Delete todos  
- View personal profile  
- Logout  

Each user only has access to their own todo items. User data is completely isolated.

---

## Key Features

### Authentication
- Signup and Login using email and password  
- JWT based authentication  
- Protected backend endpoints  
- Authentication state handled using React Context  

### Todo Management
- Add new todos  
- Toggle todo completion status  
- Delete todos  
- All todos stored per user  

### User Profile
- Displays registered name and email  
- Logout functionality  

### UI / UX
- Centered responsive design  
- Clear input forms  
- Status notifications  
- Loading state indicators  

---

# System Architecture

React (Frontend)
      |
      |  Uses JWT Token
      V
FastAPI (Backend)
      |
      | Performs CRUD operations
      V
MongoDB Database

---

# Project Structure

## Frontend (React)
todo-frontend/  
  src/  
    api/  
      client.js  
      authApi.js  
      todoApi.js  
    components/  
      Header.jsx  
      ProtectedRoute.jsx  
    context/  
      AuthContext.jsx  
    pages/  
      LoginPage.jsx  
      SignupPage.jsx  
      DashboardPage.jsx  
      ProfilePage.jsx  
    App.jsx  
    main.jsx  
    style.css  

## Backend (FastAPI)
todo-backend/  
  app/  
    routers/  
      auth_router.py  
      todo_router.py  
    schemas/  
      user_schema.py  
      todo_schema.py  
    services/  
      user_service.py  
      todo_service.py  
    repositories/  
      user_repository.py  
      todo_repository.py  
    core/  
      security.py  
      config.py  
      dependencies.py  
    db/  
      mongodb.py  
    main.py  

---

# Installation & Setup

## Step 1: Clone Repository
git clone <your-repository-link>

---

## Step 2: Backend Setup (FastAPI)
cd todo-backend  
pip install -r requirements.txt  
uvicorn app.main:app --reload  

Backend will run at:  
http://127.0.0.1:8000  

---

## Step 3: Frontend Setup (React)
cd todo-frontend  
npm install  
npm run dev  

Frontend will run at:  
http://localhost:<port>  

---

# API Endpoints

### Authentication APIs
Method | Endpoint | Description  
POST | /auth/signup | Register user  
POST | /auth/login | Authenticate and return JWT  
GET | /users/me | Get authenticated user  

### Todo APIs
Method | Endpoint | Description  
GET | /todos/ | List all todos for user  
POST | /todos/ | Create new todo  
PATCH | /todos/{id} | Update todo completion  
DELETE | /todos/{id} | Delete todo  

---

# JWT Authentication Flow

1. User logs in  
2. Backend returns JWT token  
3. Frontend stores token in localStorage  
4. Each protected request includes:  
   Authorization: Bearer <token>  
5. Backend verifies token  
6. User identity is confirmed  

---

# Security Implementation
- Passwords are hashed  
- JWT is required for protected endpoints  
- Users cannot access or modify other users’ data  
- Database filters records using user ID  

---

# Testing (Postman or Thunder Client)

### Request: Signup
POST /auth/signup  
Body:  
{  
  "full_name": "Test User",  
  "email": "test@mail.com",  
  "password": "123"  
}

### Request: Login
POST /auth/login  
Body:  
{  
  "email": "test@mail.com",  
  "password": "123"  
}

Response:  
{  
  "access_token": "JWT_TOKEN",  
  "token_type": "bearer"  
}

---

# Learning Outcomes
- Building frontend authentication with React  
- Using Context API for global state  
- Designing backend APIs in FastAPI  
- Implementing JWT authentication  
- Using MongoDB for persistent storage  
- Structuring a full–stack application  
- Clean UI and maintainable code architecture  

---

# Author
Pushpak Rajendra Pandharpatte  
Full Stack Developer  
React | FastAPI | Python | MongoDB  

---

# Conclusion
This project demonstrates the implementation of a complete full–stack application using React for the frontend and FastAPI for the backend, with MongoDB as the database. The system includes secure user authentication, todo management, and a clean and efficient UI with proper state management and backend validation.
