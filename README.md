# Unified Python Application Suite
**A dual-application project featuring a secure Password Manager and an interactive Pokémon Tracker.**

This repository contains two interconnected Python projects built to demonstrate foundational programming logic, secure data handling, and backend architecture.

## 🚀 Key Features

### 1. Secure Password Manager
* **Authentication:** Implemented a robust login system with password hashing.
* **Security:** Features a three-strike lockout mechanism for failed login attempts and an email OTP recovery system.
* **Local Storage:** Utilizes SQLite for secure, local credential storage.

### 2. Interactive Pokémon Application
* **API Integration:** Connects to external APIs (like PokéAPI) to fetch and parse live data.
* **Data Management:** Uses SQLite to store structured user data and team configurations.
* **Unified Flow:** Shares authentication architecture with the Password Manager for a seamless user experience.

## 🛠️ Tech Stack & Libraries
* **Language:** Python
* **Database:** SQLite
* **Key Libraries & Modules:**
  * `flask`: For routing and building the foundational web application interface.
  * `hashlib`: For secure password hashing and verification.
  * `smtplib` & `email.message`: To structure and manage the email OTP recovery system.
  * `requests`: For handling RESTful API calls to fetch live Pokémon data.
  * `sqlite3`: For local database queries and storage.
  * `random`: For algorithmic generation within the application logic
  
## 🚧 Work in Progress: Web Integration
While the core backend logic and database architecture are fully functional, this project is currently serving as my bridge into full-stack web development.
I am actively working on migrating the terminal-based flows into a browser-based web application using **Flask**. 
Currently, the basic routing (`app.py`) and UI scaffolding (`templates/` and `static/`) are in development.
My next steps involve fully connecting the SQLite database functions to the web front-end to create a seamless UI.

## ⚙️ Configuration & Setup
For security reasons, all database files (`.db`) and hardcoded credentials have been removed from this public repository. 

To run the Email OTP Recovery system locally:
1. Open `pokemon_password_recovery.py`.
2. Replace `YOUR_EMAIL_HERE@gmail.com` with a valid sender email address.
3. Replace `YOUR_APP_PASSWORD_HERE` with a generated App Password (if using Gmail).
