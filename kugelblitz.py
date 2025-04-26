import streamlit as st
import pandas as pd
import os
from io import BytesIO

st.set_page_config(page_title="Kugelblitz Club Page", layout="wide")
st.image("https://assets.science.nasa.gov/dynamicimage/assets/science/astro/universe/2023/09/main_image_star-forming_region_carina_nircam_final-5mb.jpg?w=2000&h=1158&fit=crop&crop=faces%2Cfocalpoint", caption="A Kugelblitz is a theoretical, highly dense concentration of energy, specifically light or heat, that collapses into a black hole due to the warping of spacetime. It's a black hole formed not from matter, but from intensely focused energy, potentially created by a powerful laser pulse. ", use_container_width=True)

# Configurations

st.title("Kugelblitz")
st.image("data:image/jpeg;base64,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", caption="President", use_container_width=True)
# Simple password protection
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


