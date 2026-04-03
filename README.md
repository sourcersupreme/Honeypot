# Honeypot
This project is a basic low-interaction honeypot designed to capture unauthorized login attempts and log attacker activity.
Low-Interaction Honeypot System
📌 Overview

This project implements a low-interaction honeypot designed to simulate a login service and capture unauthorized access attempts. It helps in analyzing attacker behavior such as credential guessing and connection patterns.

🎯 Objectives
      
Monitor unauthorized login attempts

Capture attacker credentials

Log IP addresses and timestamps

Provide basic attack analysis

⚙️ Features

Fake login service (socket-based)

Real-time connection logging

Credential capture (username/password)

Log file storage for analysis

Lightweight and easy to deploy

🛠️ Tech Stack

Python 3

Socket Programming

File Handling

## 🚀 How to Run

### Step 1: Clone Repo

git clone https://github.com/yourusername/advanced-honeypot.git
cd advanced-honeypot

### Step 2: Install Dependencies

pip install -r requirements.txt

### Step 3: Run Honeypot Server (IMPORTANT)

python3 -m honeypot.server

### Step 4: Run Dashboard

cd dashboard
python3 app.py

### Step 5: Test

Open new terminal:
nc localhost 9999

Then open browser:
http://localhost:5000

⚠️ Note: Run using module mode (-m) to avoid import errors.
