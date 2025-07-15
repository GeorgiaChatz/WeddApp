import streamlit as st
import pandas as pd
import os
from datetime import datetime
import base64

# st.set_page_config(page_title="Γ & Ν - Πρόσκληση", layout="centered")
# Κλήση με το όνομα του αρχείου εικόνας σου

# -- CSS για background εικόνα
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
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

set_background("Nikolis.png")

# Κενό για να "κατέβουν" οι χάρτες πιο κάτω από τις υπογραφές
st.markdown("<div style='height:150px;'></div>", unsafe_allow_html=True)

# col1, col2 = st.columns(2)
# with col1:
#     st.markdown("⇢ Εκκλησία: [Άγιος Γεράσιμος Ιλισίων](https://share.google/Cs77mCBaMYn2HUTXV)")
# with col2:
#     st.markdown("⇢ Κέντρο: [Pegasus Event Venue](https://share.google/qKdLDqAhLqE8AKYy7)")

st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
lang = st.radio("🌐", ["Ελληνικά", "English"], horizontal=True, label_visibility="collapsed")
st.markdown("</div>", unsafe_allow_html=True)

texts = {
    "Ελληνικά": {
        "church": "⇢ [Εκκλησία](https://share.google/Cs77mCBaMYn2HUTXV)",
        "venue": "⇢ [Κέντρο](https://share.google/qKdLDqAhLqE8AKYy7)",
        "select_name": "Διάλεξε το όνομά σου",
        "adults": "Ενήλικες;",
        "kids_0_3": "Παιδιά 0-3 ετών:",
        "kids_3_plus": "Παιδιά άνω των 3:",
        "upload_photos": "📸 Θες να ανεβάσεις φωτογραφίες από τον γάμο μας;",
        "submit": "✅ Υποβολή",
        "success": "✅ Η υποβολή έγινε με επιτυχία! Ευχαριστούμε πολύ! 💖"
    },
    "English": {
        "church": "⇢ Church: [View on Map](https://share.google/Cs77mCBaMYn2HUTXV)",
        "venue": "⇢ Venue: [View on Map](https://share.google/qKdLDqAhLqE8AKYy7)",
        "select_name": "Choose your name",
        "adults": "Adults",
        "kids_0_3": "Children aged 0-3:",
        "kids_3_plus": "Children over 3:",
        "upload_photos": "📸 Want to upload photos from our wedding?",
        "submit": "✅ Submit",
        "success": "✅ Submitted successfully! Thank you so much! 💖"
    }
}

guest_list = ["Αλέξανδρος Παπαδόπουλος", "Μαρία Κωνσταντίνου", "Γιάννης & Ελένη", "Άλλο..."]
col1, col2 = st.columns(2)
with col1:
    st.markdown(texts[lang]["church"])
with col2:
    st.markdown(texts[lang]["venue"])

name = st.selectbox(texts[lang]["select_name"], guest_list)
adults = st.number_input(texts[lang]["adults"], min_value=1, max_value=10, value=1)
kids_0_3 = st.number_input(texts[lang]["kids_0_3"], min_value=0, max_value=10, value=0)
kids_3_plus = st.number_input(texts[lang]["kids_3_plus"], min_value=0, max_value=10, value=0)

