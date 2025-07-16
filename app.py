# import streamlit as st
# import pandas as pd
# import os
# from datetime import datetime
# import base64
#
# # st.set_page_config(page_title="Γ & Ν - Πρόσκληση", layout="centered")
# # Κλήση με το όνομα του αρχείου εικόνας σου
#
# # -- CSS για background εικόνα
# def set_background(png_file):
#     with open(png_file, "rb") as f:
#         data = f.read()
#         encoded = base64.b64encode(data).decode()
#
#     css = f"""
#     <style>
#     .stApp {{
#         background-image: url("data:image/png;base64,{encoded}");
#         background-size: cover;
#         background-position: center;
#         background-repeat: no-repeat;
#         background-attachment: fixed;
#     }}
#     </style>
#     """
#     st.markdown(css, unsafe_allow_html=True)
#
# set_background("Nikolis.png")
#
# # Κενό για να "κατέβουν" οι χάρτες πιο κάτω από τις υπογραφές
# st.markdown("<div style='height:150px;'></div>", unsafe_allow_html=True)
#
# st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
# lang = st.radio("🌐", ["Ελληνικά", "English"], horizontal=True, label_visibility="collapsed")
# st.markdown("</div>", unsafe_allow_html=True)
#
# texts = {
#     "Ελληνικά": {
#         "church": "⇢ [Εκκλησία](https://share.google/Cs77mCBaMYn2HUTXV)",
#         "venue": "⇢ [Κέντρο](https://share.google/qKdLDqAhLqE8AKYy7)",
#         "select_name": "Διάλεξε το όνομά σου",
#         "adults": "Ενήλικες;",
#         "kids_0_3": "Παιδιά 0-3 ετών:",
#         "kids_3_plus": "Παιδιά άνω των 3:",
#         "upload_photos": "📸 Θες να ανεβάσεις φωτογραφίες από τον γάμο μας;",
#         "submit": "✅ Υποβολή",
#         "success": "✅ Η υποβολή έγινε με επιτυχία! Ευχαριστούμε πολύ! 💖"
#     },
#     "English": {
#         "church": "⇢ Church: [View on Map](https://share.google/Cs77mCBaMYn2HUTXV)",
#         "venue": "⇢ Venue: [View on Map](https://share.google/qKdLDqAhLqE8AKYy7)",
#         "select_name": "Choose your name",
#         "adults": "Adults",
#         "kids_0_3": "Children aged 0-3:",
#         "kids_3_plus": "Children over 3:",
#         "upload_photos": "📸 Want to upload photos from our wedding?",
#         "submit": "✅ Submit",
#         "success": "✅ Submitted successfully! Thank you so much! 💖"
#     }
# }
#
# guest_list = ["Αλέξανδρος Παπαδόπουλος", "Μαρία Κωνσταντίνου", "Γιάννης & Ελένη", "Άλλο..."]
# col1, col2 = st.columns(2)
# with col1:
#     st.markdown(texts[lang]["church"])
# with col2:
#     st.markdown(texts[lang]["venue"])
#
# name = st.selectbox(texts[lang]["select_name"], guest_list)
# adults = st.number_input(texts[lang]["adults"], min_value=1, max_value=10, value=1)
# kids_0_3 = st.number_input(texts[lang]["kids_0_3"], min_value=0, max_value=10, value=0)
# kids_3_plus = st.number_input(texts[lang]["kids_3_plus"], min_value=0, max_value=10, value=0)
#
import streamlit as st
import pandas as pd
import os
from datetime import datetime
import base64

# Background image function
def set_background(png_file):
    with open(png_file, "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data).decode()

    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    a {{
        color: #586c82 !important;  /* Custom pink color */
        font-weight: bold;
        font-size: 18px;
        text-decoration: none;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

set_background("Nikolis.png")

# Add spacing
st.markdown("<div style='height:150px;'></div>", unsafe_allow_html=True)

# Center language selection
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
lang = st.radio("🌐", ["Ελληνικά", "English"], horizontal=True, label_visibility="collapsed")
st.markdown("</div>", unsafe_allow_html=True)

texts = {
    "Ελληνικά": {
        "church": '<a href="https://share.google/Cs77mCBaMYn2HUTXV" target="_blank">⇢ Εκκλησία</a>',
        "venue": '<a href="https://share.google/qKdLDqAhLqE8AKYy7" target="_blank">⇢ Κέντρο</a>',
        "select_name": "Διάλεξε το όνομά σου",
        "adults": "Ενήλικες;",
        "kids_0_3": "Παιδιά 0-3 ετών:",
        "kids_3_plus": "Παιδιά άνω των 3:",
        "upload_photos": "📸 Θες να ανεβάσεις φωτογραφίες από τον γάμο μας;",
        "submit": "Υποβολή",
        "success": "Ευχαριστούμε πολύ, ανυπομονούμε!!"
    },
    "English": {
        "church": '<a href="https://share.google/GFpw6TkvB1dCoJOIP" target="_blank">⇢ Church: View on Map</a>',
        "venue": '<a href="https://share.google/h0IKsQ0Srz0cUvfJy" target="_blank">⇢ Venue: View on Map</a>',
        "select_name": "Choose your name",
        "adults": "Adults",
        "kids_0_3": "Children aged 0-3:",
        "kids_3_plus": "Children over 3:",
        "upload_photos": "📸 Want to upload photos from our wedding?",
        "submit": "Submit",
        "success": "Can't wait for this day!!"
    }
}

guest_list = ["Αλέξανδρος Παπαδόπουλος", "Μαρία Κωνσταντίνου", "Γιάννης & Ελένη", "Άλλο..."]

# Centered links
st.markdown(f"<div style='text-align: center;'>{texts[lang]['church']} &nbsp;&nbsp;&nbsp; {texts[lang]['venue']}</div>", unsafe_allow_html=True)

# Form layout
with st.form("attendance_form"):
    name = st.selectbox(texts[lang]["select_name"], guest_list)
    adults = st.number_input(texts[lang]["adults"], min_value=1, max_value=10, value=1)
    kids_0_3 = st.number_input(texts[lang]["kids_0_3"], min_value=0, max_value=10, value=0)
    kids_3_plus = st.number_input(texts[lang]["kids_3_plus"], min_value=0, max_value=10, value=0)

    submitted = st.form_submit_button(texts[lang]["submit"])

    if submitted:
        # Ensure the wedding_table directory exists
        os.makedirs("wedding_table", exist_ok=True)

        # Define the file path
        filename = os.path.join("wedding_table", "guest_responses.csv")

        # Create new row of data
        new_data = pd.DataFrame([{
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Name": name,
            "Adults": adults,
            "Kids_0_3": kids_0_3,
            "Kids_3_plus": kids_3_plus
        }])

        # Save or append to CSV
        if os.path.exists(filename):
            existing = pd.read_csv(filename)
            combined = pd.concat([existing, new_data], ignore_index=True)
        else:
            combined = new_data
        combined.to_csv(filename, index=False)
        st.success(texts[lang]["success"])
