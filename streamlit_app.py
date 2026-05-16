# import streamlit as st
# import requests

# # ----------------------
# # App title
# # ---------------------
# st.set_page_config(page_title="Chennai House Predictor", layout="centered")
# st.title("🏠Chennai House Price Predictor")

# st.markdown(
#     "Enter property details below and click **Predict Price** to get an estimate."
# )

# # -----------------------
# # Input fields
# # -----------------------
# int_sqft = st.number_input("Interior Area(sqft)", min_value=300, max_value=10000, value=1000)
# n_room = st.number_input("Number of Rooms", min_value=1, max_value=10, value=3)
# house_age = st.number_input("House Age (years)", min_value=0, max_value=100, value=10)

# area = st.selectbox(
#     "Area",
#     [
#         "Anna Nagar",
#         "Adyar",
#         "Velachery",
#         "Karapakkam",
#         "Chrompet",
#         "KK Nagar",
#         "T Nagar"
#     ]
# )

# build_type = st.selectbox(
#     "Building Type",
#     ["House", "Commercial", "Other"]
# )

# park_facl = st.checkbox("Parking Facility Available")

# # ------------------------
# # Prepare input for API
# # ------------------------
# payload = {
#     "data" : {
#         "INT_SQFT": int_sqft,
#         "N_ROOM" : n_room,
#         "HOUSE_AGE" : house_age,
#         f"AREA_{area}" : 1,
#         f"BUILDTYPE_{build_type}" : 1,
#         "PARK_FACIL_Yes" : 1 if park_facl else 0
#     }
# }

# # ------------------------
# # Predict button
# # ------------------------
# if st.button("💰Predict Price"):
#     try:
#         response = requests.post(
#             "http://127.0.0.1:8000/predict",
#             json=payload,
#             timeout=10
#         )

#         if response.status_code == 200:
#             price = response.json()["predicted_price"]
#             st.success(f"✅Estimated House Price: ₹{price:,.2f}")
#         else:
#             st.error("❌API Error. Please check server.")
#     except Exception as e:
#         st.error("❌Unable to connect to prediction API.")
#         st.error(str(e))


import streamlit as st

# ------------------------------
# App Config
# ------------------------------
st.set_page_config(page_title="Real Estate App", layout="centered")

# ------------------------------
# Session State Init
# ------------------------------
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "page" not in st.session_state:
    st.session_state["page"] = "Home"

# ------------------------------
# Navigation (TOP menu)
# ------------------------------
st.markdown(
    "<h1 style='white-space: nowrap;'>🏠 Real Estate Price Prediction System</h1>",
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Home"):
        st.session_state["page"] = "Home"

if not st.session_state["logged_in"]:
    with col2:
        if st.button("Login"):
            st.session_state["page"] = "Login"

if st.session_state["logged_in"]:
    with col2:
        if st.button("Predict"):
            st.session_state["page"] = "Predict"

    with col3:
        if st.button("Logout"):
            st.session_state["logged_in"] = False
            st.session_state["page"] = "Home"

# ------------------------------
# Page Routing
# ------------------------------
page = st.session_state["page"]

# ------------------------------
# HOME PAGE
# ------------------------------
if page == "Home":
    st.markdown("---")
    st.subheader("Welcome")

    st.write("""
    This application predicts house prices using Machine Learning.

    ✅ Accurate predictions
    ✅ Clean user interface
    ✅ Real-time API results
    """)

    st.markdown("---")

    st.write("""
    This application predicts house prices using Machine Learning.

    It uses advanced algorithms like Gradient Boosting to provide accurate predictions based on:
    - Area
    - Number of Rooms
    - House Age
    - Location
    - Building Type
    """)

    st.markdown("---")

    st.subheader("How to Use")

    st.write("""
    1. Go to the Login page
    2. Login with your credentials
    3. Navigate to Predict page
    4. Enter property details
    5. Get price prediction instantly
    """)

# ------------------------------
# LOGIN PAGE
# ------------------------------
elif page == "Login":
    st.markdown("---")
    st.subheader("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login Now"):
        if username == "admin" and password == "admin":
            st.session_state["logged_in"] = True
            st.session_state["page"] = "Predict"  # ✅ redirect
            st.success("✅ Login successful")

            st.rerun()  # ✅ FORCE UI REFRESH (IMPORTANT)

        else:
            st.error("❌ Invalid credentials")

    st.caption("Demo: admin / admin")

# ------------------------------
# PREDICT PAGE (Protected)
# ------------------------------
elif page == "Predict":

    if not st.session_state["logged_in"]:
        st.warning("⚠️ Please login first")
        st.stop()

    import requests

    st.markdown("---")
    st.subheader("🏠 Price Prediction")

    # Inputs
    int_sqft = st.number_input("Interior Area", 300, 10000, 1000)
    n_room = st.number_input("Rooms", 1, 10, 3)
    house_age = st.number_input("House Age", 0, 100, 10)

    area = st.selectbox(
        "Area",
        ["Anna Nagar", "Adyar", "Velachery", "Karapakkam", "Chrompet", "KK Nagar", "T Nagar"]
    )

    build_type = st.selectbox(
        "Building Type",
        ["House", "Commercial", "Other"]
    )

    parking = st.checkbox("Parking Available")

    # Payload
    payload = {
        "data": {
            "INT_SQFT": int_sqft,
            "N_ROOM": n_room,
            "HOUSE_AGE": house_age,
            f"AREA_{area}": 1,
            f"BUILDTYPE_{build_type}": 1,
            "PARK_FACIL_Yes": 1 if parking else 0
        }
    }

    # Predict
    if st.button("🪙 Predict Price"):
        try:
            response = requests.post(
                "http://127.0.0.1:8000/predict",
                json=payload,
                timeout=10
            )

            if response.status_code == 200:
                price = response.json()["predicted_price"]
                st.success(f"✅ Estimated Price: ₹ {price:,.2f}")
            else:
                st.error("❌ API Error")

        except Exception as e:
            st.error("❌ API connection failed")