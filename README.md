Edge AI Health Monitoring - Frontend

Overview

This repository contains the frontend of the Edge AI Health Monitoring system built with Streamlit and integrated with Firebase Authentication.

The backend will be developed separately and integrated via API calls.

Features

User Authentication (Login, Register, Forgot Password) using Firebase

Dashboard with Navigation

Live Heart Rate Monitoring (To be integrated with backend)

Relaxation Guidance

Consult a Professional

Technologies Used

Python

Streamlit

Firebase Authentication (pyrebase4)

OpenCV (for future real-time video processing)

Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/SUJAN199394/edge-ai-frontend

2️⃣ Create a Virtual Environment (Recommended)

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3️⃣ Install Required Dependencies

pip install -r requirements.txt

4️⃣ Set Up Firebase Authentication

1. Create a Firebase project in Firebase Console.

2. Go to Project Settings → Service Accounts → Generate Private Key.

3. Save the key as firebase_config.json in the project root.

4. Update firebase_config.py with the correct credentials.

5️⃣ Run the Application

streamlit run app.py

 License

This project is licensed under the MIT License.
