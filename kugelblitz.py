from PIL import Image
import streamlit as st
import pandas as pd
import os
from io import BytesIO
import io
import base64

st.set_page_config(page_title="Kugelblitz Club Page", layout="wide")


# Configurations
 Simple password protection
PASSWORD = "kugelblitz123"  # <-- Change this to a secure password

# Data storage (for simple use, in-memory; can be adapted to file/database)
if 'club_data' not in st.session_state:
    st.session_state.club_data = pd.DataFrame(columns=[
        "Name", "Batch", "Course", "Phone", "Email", "Position", "Picture"
    ])

# Function to upload and store image
def save_image(uploaded_file):
    return uploaded_file.getvalue()

# Sidebar form with password
with st.sidebar:
    st.header("🔒 Admin Access")
    password = st.text_input("Enter password", type="password")
    
    if password == PASSWORD:
        st.success("Access granted")
        
        with st.form("club_member_form", clear_on_submit=True):
            name = st.text_input("Name")
            batch = st.text_input("Batch")
            course = st.text_input("Course")
            phone = st.text_input("Phone Number")
            email = st.text_input("Email")
            position = st.selectbox("Position in Club", ["President", "Vice President", "Core Team", "Member", "Other"])
            picture = st.file_uploader("Upload Picture", type=["jpg", "jpeg", "png"])
            
            submitted = st.form_submit_button("Submit / Update Entry")
            
            if submitted:
                if name and batch and course and phone and email and position and picture:
                    # Check if entry exists
                    existing = st.session_state.club_data['Name'] == name
                    if existing.any():
                        st.session_state.club_data.loc[existing, :] = [name, batch, course, phone, email, position, save_image(picture)]
                        st.success("Entry updated!")
                    else:
                        new_entry = {
                            "Name": name,
                            "Batch": batch,
                            "Course": course,
                            "Phone": phone,
                            "Email": email,
                            "Position": position,
                            "Picture": save_image(picture)
                        }
                        st.session_state.club_data = st.session_state.club_data.append(new_entry, ignore_index=True)
                        st.success("New entry added!")
                else:
                    st.error("Please fill all fields and upload a picture.")

# Main page display
def display_member(member):
    st.image(BytesIO(member['Picture']), width=150)
    st.subheader(member['Name'])
    st.write(f"📚 {member['Course']} ({member['Batch']})")
    st.write(f"📞 {member['Phone']}")
    st.write(f"📧 {member['Email']}")

# Separate columns for hierarchy
president = st.session_state.club_data[st.session_state.club_data['Position'] == "President"]
vp = st.session_state.club_data[st.session_state.club_data['Position'] == "Vice President"]
others = st.session_state.club_data[~st.session_state.club_data['Position'].isin(["President", "Vice President"])]

# Display President
st.header("👑 President")
if not president.empty:
    for idx, member in president.iterrows():
        display_member(member)
else:
    st.info("No President added yet.")

# Display Vice President
st.header("🎖️ Vice President")
if not vp.empty:
    for idx, member in vp.iterrows():
        display_member(member)
else:
    st.info("No Vice President added yet.")

# Display Core Team and Others
st.header("🚀 Core Team Members")
if not others.empty:
    for idx, member in others.iterrows():
        with st.expander(member['Position'] + ": " + member['Name']):
            display_member(member)
else:
    st.info("No core team members added yet.")


