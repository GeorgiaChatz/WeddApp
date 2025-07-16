# # import streamlit as st
# # import pandas as pd
# # import os
# # from datetime import datetime
# # import base64
# #
# # # st.set_page_config(page_title="Γ & Ν - Πρόσκληση", layout="centered")
# # # Κλήση με το όνομα του αρχείου εικόνας σου
# #
# # # -- CSS για background εικόνα
# # def set_background(png_file):
# #     with open(png_file, "rb") as f:
# #         data = f.read()
# #         encoded = base64.b64encode(data).decode()
# #
# #     css = f"""
# #     <style>
# #     .stApp {{
# #         background-image: url("data:image/png;base64,{encoded}");
# #         background-size: cover;
# #         background-position: center;
# #         background-repeat: no-repeat;
# #         background-attachment: fixed;
# #     }}
# #     </style>
# #     """
# #     st.markdown(css, unsafe_allow_html=True)
# #
# # set_background("Nikolis.png")
# #
# # # Κενό για να "κατέβουν" οι χάρτες πιο κάτω από τις υπογραφές
# # st.markdown("<div style='height:150px;'></div>", unsafe_allow_html=True)
# #
# # st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
# # lang = st.radio("🌐", ["Ελληνικά", "English"], horizontal=True, label_visibility="collapsed")
# # st.markdown("</div>", unsafe_allow_html=True)
# #
# # texts = {
# #     "Ελληνικά": {
# #         "church": "⇢ [Εκκλησία](https://share.google/Cs77mCBaMYn2HUTXV)",
# #         "venue": "⇢ [Κέντρο](https://share.google/qKdLDqAhLqE8AKYy7)",
# #         "select_name": "Διάλεξε το όνομά σου",
# #         "adults": "Ενήλικες;",
# #         "kids_0_3": "Παιδιά 0-3 ετών:",
# #         "kids_3_plus": "Παιδιά άνω των 3:",
# #         "upload_photos": "📸 Θες να ανεβάσεις φωτογραφίες από τον γάμο μας;",
# #         "submit": "✅ Υποβολή",
# #         "success": "✅ Η υποβολή έγινε με επιτυχία! Ευχαριστούμε πολύ! 💖"
# #     },
# #     "English": {
# #         "church": "⇢ Church: [View on Map](https://share.google/Cs77mCBaMYn2HUTXV)",
# #         "venue": "⇢ Venue: [View on Map](https://share.google/qKdLDqAhLqE8AKYy7)",
# #         "select_name": "Choose your name",
# #         "adults": "Adults",
# #         "kids_0_3": "Children aged 0-3:",
# #         "kids_3_plus": "Children over 3:",
# #         "upload_photos": "📸 Want to upload photos from our wedding?",
# #         "submit": "✅ Submit",
# #         "success": "✅ Submitted successfully! Thank you so much! 💖"
# #     }
# # }
# #
# # guest_list = ["Αλέξανδρος Παπαδόπουλος", "Μαρία Κωνσταντίνου", "Γιάννης & Ελένη", "Άλλο..."]
# # col1, col2 = st.columns(2)
# # with col1:
# #     st.markdown(texts[lang]["church"])
# # with col2:
# #     st.markdown(texts[lang]["venue"])
# #
# # name = st.selectbox(texts[lang]["select_name"], guest_list)
# # adults = st.number_input(texts[lang]["adults"], min_value=1, max_value=10, value=1)
# # kids_0_3 = st.number_input(texts[lang]["kids_0_3"], min_value=0, max_value=10, value=0)
# # kids_3_plus = st.number_input(texts[lang]["kids_3_plus"], min_value=0, max_value=10, value=0)
# #
# import streamlit as st
# import pandas as pd
# import os
# from datetime import datetime
# import base64
# import requests
#
# def upload_to_github(file_content, file_path, commit_message, token, repo_owner, repo_name):
#     """Upload a file to a GitHub repository."""
#     api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"
#     response = requests.get(api_url, headers={"Authorization": f"token {token}"})
#     sha = response.json()["sha"] if response.status_code == 200 else None
#
#     encoded_content = base64.b64encode(file_content).decode("utf-8")
#
#     payload = {
#         "message": commit_message,
#         "content": encoded_content,
#         "sha": sha,
#     }
#
#     upload_response = requests.put(api_url, json=payload, headers={"Authorization": f"token {token}"})
#     if upload_response.status_code in [200, 201]:
#         return upload_response.json()["content"]["html_url"]
#     else:
#         st.error(f"Error uploading file to GitHub: {upload_response.json()}")
#         return None
#
# GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]
# REPO_OWNER = "GeorgiaChatz"
# REPO_NAME = "WeddApp"
# # Background image function
# # def set_background(png_file):
# #     with open(png_file, "rb") as f:
# #         data = f.read()
# #         encoded = base64.b64encode(data).decode()
# #
# #     css = f"""
# #     <style>
# #     .stApp {{
# #         background-image: url("data:image/png;base64,{encoded}");
# #         background-size: cover;
# #         background-position: center;
# #         background-repeat: no-repeat;
# #         background-attachment: fixed;
# #     }}
# #     a {{
# #         color: #586c82 !important;  /* Custom pink color */
# #         font-weight: bold;
# #         font-size: 18px;
# #         text-decoration: none;
# #     }}
# #     </style>
# #     """
# #     st.markdown(css, unsafe_allow_html=True)
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
#
#     a {{
#         color: #586c82 !important;
#         font-weight: bold;
#         font-size: 18px;
#         text-decoration: none;
#     }}
#
#     /* ✅ Custom checkbox styling */
#     input[type="checkbox"] + div[data-testid="stMarkdownContainer"] > label::before {{
#         border-color: #586c82;  /* outline color */
#     }}
#
#     input[type="checkbox"]:checked + div[data-testid="stMarkdownContainer"] > label::before {{
#         background-color: #586c82;  /* custom checked color */
#         border-color: #586c82;
#     }}
#     </style>
#     """
#     st.markdown(css, unsafe_allow_html=True)
# set_background("tzo.png")
#
# # Add spacing
# st.markdown("<div style='height:150px;'></div>", unsafe_allow_html=True)
#
# # Center language selection
# # st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
# # lang = st.checkbox("🌐", ["Ελληνικά", "English"], horizontal=True, label_visibility="collapsed")
# # st.markdown("</div>", unsafe_allow_html=True)
# st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
# lang = st.radio("🌐", ["Ελληνικά", "English"], horizontal=True, label_visibility="collapsed")
# st.markdown("</div>", unsafe_allow_html=True)
#
#
# guest_list = ["Αλέξανδρος Παπαδόπουλος", "Μαρία Κωνσταντίνου", "Γιάννης & Ελένη", "Άλλο..."]
# def get_base64_image(image_path):
#     with open(image_path, "rb") as image_file:
#         return base64.b64encode(image_file.read()).decode()
#
# leaf_base64 = get_base64_image("leaf-removebg-preview.png")
# leaf_img = f'<img src="data:image/png;base64,{leaf_base64}" width="20" style="vertical-align: middle; margin-right: 4px;"/>'
#
# texts = {
#     "Ελληνικά": {
#         "church": f'{leaf_img}<a href="https://share.google/Cs77mCBaMYn2HUTXV" target="_blank">⇢ Εκκλησία</a>',
#         "venue": f'{leaf_img}<a href="https://share.google/qKdLDqAhLqE8AKYy7" target="_blank">⇢ Κέντρο</a>',
#         "select_name": "Διάλεξε το όνομά σου",
#         "adults": "Ενήλικες;",
#         "kids_0_3": "Παιδιά 0-3 ετών:",
#         "kids_3_plus": "Παιδιά άνω των 3:",
#         "upload_photos": "📸 Θες να ανεβάσεις φωτογραφίες από τον γάμο μας;",
#         "submit": "Υποβολή",
#         "success": "Ευχαριστούμε πολύ, ανυπομονούμε!!"
#     },
#     "English": {
#         "church": '<a href="https://share.google/GFpw6TkvB1dCoJOIP" target="_blank">⇢ Church: View on Map</a>',
#         "venue": '<a href="https://share.google/h0IKsQ0Srz0cUvfJy" target="_blank">⇢ Venue: View on Map</a>',
#         "select_name": "Choose your name",
#         "adults": "Adults",
#         "kids_0_3": "Children aged 0-3:",
#         "kids_3_plus": "Children over 3:",
#         "upload_photos": "📸 Want to upload photos from our wedding?",
#         "submit": "Submit",
#         "success": "Can't wait for this day!!"
#     }
# }
#
# # Centered links
# st.markdown(f"<div style='text-align: center;'>{texts[lang]['church']} &nbsp;&nbsp;&nbsp; {texts[lang]['venue']}</div>", unsafe_allow_html=True)
#
# # Form layout
# with st.form("attendance_form"):
#     name = st.selectbox(texts[lang]["select_name"], guest_list)
#     adults = st.number_input(texts[lang]["adults"], min_value=1, max_value=10, value=1)
#     kids_0_3 = st.number_input(texts[lang]["kids_0_3"], min_value=0, max_value=10, value=0)
#     kids_3_plus = st.number_input(texts[lang]["kids_3_plus"], min_value=0, max_value=10, value=0)
#
#     submitted = st.form_submit_button(texts[lang]["submit"])
#
#     if submitted:
#         # Ensure the wedding_table directory exists
#         os.makedirs("wedding_table", exist_ok=True)
#
#         # Define the file path
#         filename = os.path.join("wedding_table", "guest_responses.csv")
#
#         # Create new row of data
#         new_data = pd.DataFrame([{
#             "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#             "Name": name,
#             "Adults": adults,
#             "Kids_0_3": kids_0_3,
#             "Kids_3_plus": kids_3_plus
#         }])
#
#         # Save or append to CSV
#         if os.path.exists(filename):
#             existing = pd.read_csv(filename)
#             combined = pd.concat([existing, new_data], ignore_index=True)
#         else:
#             combined = new_data
#         combined.to_csv(filename, index=False)
#         custom_message = texts[lang]["success"]
#
#         st.markdown(
#             f"""
#             <div style='
#                 background-color: #586c82;
#                 padding: 1em;
#                 border-left: 5px solid #586c82;
#                 border-radius: 5px;
#                 color: #586c82;
#                 font-weight: bold;
#                 font-size: 16px;
#                 margin-top: 1em;
#             '>
#                 {custom_message}
#             </div>
#             """,
#             unsafe_allow_html=True
#         )
#
#         # Upload to GitHub
#         with open(filename, "rb") as f:
#             file_bytes = f.read()
#
#         upload_url = upload_to_github(
#             file_content=file_bytes,
#             file_path="wedding_table/guest_responses.csv",  # path in the GitHub repo
#             commit_message="Update guest responses",
#             token=GITHUB_TOKEN,
#             repo_owner=REPO_OWNER,
#             repo_name=REPO_NAME
#         )
#
import streamlit as st
import pandas as pd
import os
from datetime import datetime
import base64
import requests

# GitHub setup
GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]
REPO_OWNER = "GeorgiaChatz"
REPO_NAME = "WeddApp"

def upload_to_github(file_content, file_path, commit_message, token, repo_owner, repo_name):
    api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"
    response = requests.get(api_url, headers={"Authorization": f"token {token}"})
    sha = response.json()["sha"] if response.status_code == 200 else None

    encoded_content = base64.b64encode(file_content).decode("utf-8")

    payload = {
        "message": commit_message,
        "content": encoded_content,
        "sha": sha,
    }

    upload_response = requests.put(api_url, json=payload, headers={"Authorization": f"token {token}"})
    if upload_response.status_code in [200, 201]:
        return upload_response.json()["content"]["html_url"]
    else:
        st.error(f"Error uploading file to GitHub: {upload_response.json()}")
        return None

# Set background and styles
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
        color: #586c82 !important;
        font-weight: bold;
        font-size: 18px;
        text-decoration: none;
    }}

    /* Style radio buttons like checkboxes */
    div[role="radiogroup"] > label > div:first-child {{
        border: 2px solid #586c82 !important;
        border-radius: 3px !important;
        background-color: white !important;
        width: 20px !important;
        height: 20px !important;
    }}

    div[role="radiogroup"] > label > div:first-child > div {{
        background-color: #586c82 !important;
        width: 10px !important;
        height: 10px !important;
        border-radius: 2px !important;
        margin: auto;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

set_background("tzo.png")



# Load leaf image as base64
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

leaf_base64 = get_base64_image("leaf-removebg-preview.png")
leaf_img = f'<img src="data:image/png;base64,{leaf_base64}" width="30" style="vertical-align: middle; margin-right: 6px;"/>'

# Language-specific texts
texts = {
    "Ελληνικά": {
        "church": f'{leaf_img}<a href="https://share.google/Cs77mCBaMYn2HUTXV" target="_blank">Εκκλησία</a>',
        "venue": f'{leaf_img}<a href="https://share.google/qKdLDqAhLqE8AKYy7" target="_blank">Κέντρο</a>',
        "select_name": "Διάλεξε το όνομά σου",
        "adults": "Ενήλικες:",
        "kids_0_3": "Παιδιά 0-3 ετών:",
        "kids_3_plus": "Παιδιά 3-10 ετών:",
        "submit": "Υποβολή",
        "success": "Ευχαριστούμε πολύ, ανυπομονούμε!!"
    },
    "English": {
        "church": f'{leaf_img}<a href="https://share.google/GFpw6TkvB1dCoJOIP" target="_blank">Church</a>',
        "venue": f'{leaf_img}<a href="https://share.google/h0IKsQ0Srz0cUvfJy" target="_blank">Venue</a>',
        "select_name": "Choose your name",
        "adults": "Adults:",
        "kids_0_3": "Children aged 0-3:",
        "kids_3_plus": "Children aged 3-10:",
        "submit": "Submit",
        "success": "Can't wait for this day!!"
    }
}

# Show links centered
# st.markdown(f"<div style='text-align: center;'>{texts[lang]['church']} &nbsp;&nbsp;&nbsp; {texts[lang]['venue']}</div>", unsafe_allow_html=True)
st.markdown("<div style='height:180px;'></div>", unsafe_allow_html=True)

# ✅ Language toggle aligned with form width
st.markdown("""
<div style='max-width: 400px; margin: 0 auto; text-align: center;'>
""", unsafe_allow_html=True)
lang = st.radio("🌐", ["Ελληνικά", "English"], horizontal=True, label_visibility="collapsed")
st.markdown("</div>", unsafe_allow_html=True)

# Leave some space between language and links
st.markdown("<div style='height:15px;'></div>", unsafe_allow_html=True)

# ✅ Church / Venue links aligned with form
st.markdown(f"""
<div style='max-width: 400px; margin: 0 auto; text-align: center; margin-left: -20 px; margin-bottom: 30px;'>
    {texts[lang]['church']} &nbsp;&nbsp;&nbsp; {texts[lang]['venue']}
</div>
""", unsafe_allow_html=True)
# Form
guest_list = ["Κοσμάς Κουβαράς", "Βασίλης Γεωργακόπουλος", "Αναστάσης Τσέλιος", "Χαράλαμπος Τσαφάς", "Αντώνης Καπογιαννάτος", "Φιλοθέη Κόσσυφα", "Ειρήνη Τζανέτου", "Γιώργος Μαρτζούκος", "Αθηνά Καμηλέλλη", "Θάλεια Λαμπίδη", "Ντίνα Τίτση", "Τατιάνα Γιαννούλη", "Πάνος Σαλτερής", "Δημήτρης Χριστόπουλος", "Στέφανος Γιώτης", "Μαρία Τσαρδίκου", "Μηνάς Καλωσυνάκης", "Κωσταντίνα", "Ελευθερία Κούρσαρη", "Άννα Μπουρλή", "Ιωάννα Μπουρλή", "Luca Canalini", "Sylvia Andaloro", "Lucia Cordoba-Esteban", "Βάγια Ξεβγένη", "Βασιλίνα Σωτηροπούλου", "Παναγιώτα Χάιδα", "Αλέξανδρος Βέρρας", "Πάολα Μερτίρι", "Σπυριδούλα Βλατάκη", "Αλέξης Σουρτζής", "Ανθή Χατζηιωάννου", "Άννα Μπουργανού", "Αναστάσης Χαλδούπης", "Γιούλα Κωσταντοπούλου", "Αλεξία Καλαντζή", "Ντόρα Καλαντζή", "Γιώργος Καλαντζής", "Παναγιώτης Καλαντζής", "Δημήτρης Καλαντζής", "Άννα Κούσουλα", "Χρήστος Σκουφαρίδης", "Δημήτρης Μποιντάς", "Μιχάλης Αλεξόπουλος", "Θοδωρής Θεοδωρίδης", "Δημήτρης Παπαδημητρίου", "Ιφιγένεια Ισαμπάλογλου", "Γιάννης Μπόσκοβιτς", "Λάζαρος Γιάβρο"
]
with st.form("attendance_form"):
    name = st.selectbox(texts[lang]["select_name"], guest_list)
    adults = st.number_input(texts[lang]["adults"], min_value=1, max_value=10, value=1)
    kids_0_3 = st.number_input(texts[lang]["kids_0_3"], min_value=0, max_value=10, value=0)
    kids_3_plus = st.number_input(texts[lang]["kids_3_plus"], min_value=0, max_value=10, value=0)

    submitted = st.form_submit_button(texts[lang]["submit"])

    if submitted:
        os.makedirs("wedding_table", exist_ok=True)
        filename = os.path.join("wedding_table", "guest_responses.csv")

        new_data = pd.DataFrame([{
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Name": name,
            "Adults": adults,
            "Kids_0_3": kids_0_3,
            "Kids_3_plus": kids_3_plus
        }])

        if os.path.exists(filename):
            existing = pd.read_csv(filename)
            combined = pd.concat([existing, new_data], ignore_index=True)
        else:
            combined = new_data
        combined.to_csv(filename, index=False)

        st.markdown(
            f"""
            <div style='
                background-color: #586c82;
                padding: 1em;
                border-left: 5px solid #586c82;
                border-radius: 5px;
                color: #fff;
                font-weight: bold;
                font-size: 16px;
                margin-top: 1em;
                text-align: center;
            '>
                {texts[lang]["success"]}
            </div>
            """,
            unsafe_allow_html=True
        )

        with open(filename, "rb") as f:
            file_bytes = f.read()

        upload_url = upload_to_github(
            file_content=file_bytes,
            file_path="wedding_table/guest_responses.csv",
            commit_message="Update guest responses",
            token=GITHUB_TOKEN,
            repo_owner=REPO_OWNER,
            repo_name=REPO_NAME
        )
