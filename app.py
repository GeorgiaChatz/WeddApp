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

col1, col2 = st.columns(2)
with col1:
    st.markdown("⇢ Εκκλησία: [Δες στον Χάρτη](https://www.google.com/maps)")
with col2:
    st.markdown("⇢ Κέντρο: [Δες στον Χάρτη](https://www.google.com/maps)")

st.markdown("---")

# -- Λίστα Καλεσμένων
guest_list = ["Αλέξανδρος Παπαδόπουλος", "Μαρία Κωνσταντίνου", "Γιάννης & Ελένη", "Άλλο..."]
name = st.selectbox("Διάλεξε το όνομά σου", guest_list)

# -- Αριθμός Ατόμων
adults = st.number_input("Πόσοι ενήλικες θα έρθουν (μαζί με εσένα);", min_value=1, max_value=10, value=1)
kids_0_3 = st.number_input("Παιδιά 0-3 ετών:", min_value=0, max_value=10, value=0)
kids_3_plus = st.number_input("Παιδιά άνω των 3:", min_value=0, max_value=10, value=0)

st.markdown("---")

# -- Φωτογραφίες
st.markdown("📸 Θες να ανεβάσεις φωτογραφίες από τον γάμο μας;")
st.markdown("➡️ [Ανέβασε στο Google Drive εδώ](https://drive.google.com/drive/folder/xxx)")

uploaded_files = st.file_uploader("Ή ανέβασε εδώ (προαιρετικά):", accept_multiple_files=True)

# -- Υποβολή
if st.button("✅ Υποβολή"):
    # Αποθήκευση στοιχείων σε CSV
    submission = {
        "Όνομα": name,
        "Ενήλικες": adults,
        "Παιδιά 0-3": kids_0_3,
        "Παιδιά 3+": kids_3_plus,
        "Ημερομηνία": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    df = pd.DataFrame([submission])
    if not os.path.exists("responses.csv"):
        df.to_csv("responses.csv", index=False)
    else:
        df.to_csv("responses.csv", mode='a', header=False, index=False)

    # Αποθήκευση φωτογραφιών
    if uploaded_files:
        os.makedirs("uploaded_photos", exist_ok=True)
        for file in uploaded_files:
            with open(os.path.join("uploaded_photos", file.name), "wb") as f:
                f.write(file.getbuffer())

    st.success("✅ Η υποβολή έγινε με επιτυχία! Ευχαριστούμε πολύ! 💖")

