import streamlit as st
from dotenv import load_dotenv
import os
from utils.message_generator import generate_message
from utils.whatsapp_sender import send_whatsapp_message

load_dotenv()

st.set_page_config(page_title="Wellness Whispers", layout="centered")

if "step" not in st.session_state:
    st.session_state.step = 1
if "user_data" not in st.session_state:
    st.session_state.user_data = {}

def next_step():
    st.session_state.step += 1

def prev_step():
    st.session_state.step -= 1

# Step 1 - Welcome Page
if st.session_state.step == 1:
    st.image("assets/logo.png", width=200)
    st.title("Welcome to Wellness Whispers")
    st.markdown("Your personalized daily motivation, straight to WhatsApp and Email based on your fitness journey.")
    if st.button("Get Started"):
        next_step()

# Step 2 - Basic Details
elif st.session_state.step == 2:
    st.subheader("Step 1: Tell us about yourself")
    name = st.text_input("Name")
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    age = st.number_input("Age", min_value=10, max_value=100)
    email = st.text_input("Email")
    phone = st.text_input("WhatsApp Number (with country code)", placeholder="+91XXXXXXXXXX")

    if st.button("Next"):
        st.session_state.user_data.update({
            "name": name,
            "gender": gender,
            "age": age,
            "email": email,
            "phone": phone
        })
        next_step()
    st.button("Back", on_click=prev_step)

# Step 3 - Preferences
elif st.session_state.step == 3:
    st.subheader("Step 2: Your Wellness Preferences")
    fitness_level = st.radio("Your Fitness Level", ["Beginner", "Intermediate", "Advanced"])
    goal = st.selectbox("Main Wellness Goal", ["Fat loss", "Stress relief", "Energy boost", "Mental clarity"])
    activity = st.multiselect("Preferred Activities", ["Yoga", "Walking", "Gym", "Meditation", "Cycling"])
    tone = st.selectbox("Motivational Style", ["Hard tone (Push me)", "Gentle", "Cheerful", "Spiritual"])
    delivery = st.radio("Delivery Method", ["WhatsApp", "Email", "Both"])
    time = st.time_input("Preferred Time for Daily Message")
    length = st.selectbox("Message Length", ["2 lines", "5 lines", "10 lines"])

    if st.button("Submit"):
        st.session_state.user_data.update({
            "fitness_level": fitness_level,
            "goal": goal,
            "activity": ", ".join(activity),
            "tone": tone,
            "delivery": delivery,
            "time": str(time),
            "length": length
        })
        next_step()
    st.button("Back", on_click=prev_step)

# Step 4 - Show Message and (optionally) Send
elif st.session_state.step == 4:
    st.success("You're all set!")
    st.write("Here's a sample motivational message just for you:")

    user = st.session_state.user_data
    message = generate_message(
        name=user["name"],
        goal=user["goal"],
        activity=user["activity"],
        tone=user["tone"],
        length=user["length"]
    )
    st.write(f"📨 **Motivation:**\n\n{message}")

    if "WhatsApp" in user["delivery"]:
        sent = send_whatsapp_message(user["phone"], message)
        if sent:
            st.success("Message sent to WhatsApp!")
        else:
            st.error("Failed to send WhatsApp message.")

    if st.button("Start Over"):
        st.session_state.step = 1
        st.session_state.user_data = {}