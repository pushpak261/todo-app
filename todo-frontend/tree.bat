@echo off
echo Creating Project Structure...

mkdir src
mkdir src\api
mkdir src\context
mkdir src\components
mkdir src\pages

type NUL > src\api\client.js
type NUL > src\api\authApi.js
type NUL > src\api\todoApi.js

type NUL > src\context\AuthContext.jsx

type NUL > src\components\ProtectedRoute.jsx

type NUL > src\pages\LoginPage.jsx
type NUL > src\pages\SignupPage.jsx
type NUL > src\pages\DashboardPage.jsx
type NUL > src\pages\ProfilePage.jsx

type NUL > src\App.jsx
type NUL > src\main.jsx

echo Done!
pause
