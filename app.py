import streamlit as st
from firebase_config import auth  # Import Firebase authentication
import pyrebase

# Firebase authentication
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_email" not in st.session_state:
    st.session_state.user_email = ""

# Sidebar navigation
st.sidebar.title("Navigation")

if not st.session_state.logged_in:
    page = st.sidebar.radio(" ", ["Login", "Register", "Forgot Password"])
else:
    page = st.sidebar.radio(
        " ",
        ["Home", "Check Heart Rate", "Relaxation", "Consult Professional", "About Us", "Dashboard"],
        index=5,  # Default to Dashboard
    )

# Login Function
def login():
    st.title("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            st.session_state.logged_in = True
            st.session_state.user_email = user["email"]
            st.success("Logged in successfully!")
            st.rerun()
        except Exception as e:
            st.error("Invalid credentials. Please try again.")

# Register Function
def register():
    st.title("Register")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    
    if st.button("Register"):
        if password == confirm_password:
            try:
                auth.create_user_with_email_and_password(email, password)
                st.success("Account created successfully! Please login.")
                st.session_state.logged_in = False
                st.rerun()
            except Exception as e:
                st.error("Registration failed. Email may already exist or password is too weak.")
        else:
            st.error("Passwords do not match. Please try again.")

# Forgot Password Function
def forgot_password():
    st.title("Forgot Password")
    email = st.text_input("Enter your registered email")
    if st.button("Reset Password"):
        try:
            auth.send_password_reset_email(email)
            st.success("Password reset email sent. Check your inbox.")
        except Exception as e:
            st.error("Error sending password reset email. Please check your email address.")

# Logout Function
def logout():
    st.session_state.logged_in = False
    st.session_state.user_email = ""
    st.rerun()

# Pages after login
def home():
    st.title("🏠 Home")
    st.write("Welcome to Edge AI Health Monitoring!")

def check_heart_rate():
    st.title("💓 Check Heart Rate")
    st.write("This page will analyze your heart rate in real-time.")

def relaxation():
    st.title("🧘 Relaxation")
    st.write("Guided relaxation techniques and exercises.")

def consult_professional():
    st.title("👨‍⚕️ Consult a Professional")
    st.write("Schedule an appointment or get expert advice.")

def about_us():
    st.title("ℹ️ About Us")
    st.write("Learn more about the Edge AI Health Monitoring project.")

def dashboard():
    st.title("Edge AI Health Monitoring")
    st.subheader("Welcome to Dashboard")
    st.write(f"Logged in as: {st.session_state.user_email}")
    if st.button("Logout"):
        logout()

# Render the selected page
if not st.session_state.logged_in:
    if page == "Login":
        login()
    elif page == "Register":
        register()
    elif page == "Forgot Password":
        forgot_password()
else:
    if page == "Home":
        home()
    elif page == "Check Heart Rate":
        check_heart_rate()
    elif page == "Relaxation":
        relaxation()
    elif page == "Consult Professional":
        consult_professional()
    elif page == "About Us":
        about_us()
    elif page == "Dashboard":
        dashboard()
