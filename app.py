import streamlit as st
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="TrustBite | Curated Dining",
    page_icon="🍽️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS FOR CLEANER UI ---
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        font-weight: bold;
    }
    .primary-btn>button {
        background-color: #FF4B4B;
        color: white;
    }
    .card {
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        background-color: #f9f9fb;
    }
    </style>
""", unsafe_allow_html=True)

# --- APP HEADER ---
st.title("🍽️ TrustBite")
st.markdown("*Skip the endless scrolling. Find the perfect spot.*")
st.divider()

# --- TABS FOR USER JOURNEYS ---
tab1, tab2 = st.tabs(["🔍 Find a Restaurant (Journey 1)", "✍️ Leave a Review (Journey 2)"])

# ==========================================
# JOURNEY 1: DISCOVERING & CHOOSING
# ==========================================
with tab1:
    st.markdown("### What are you in the mood for?")
    
    # Contextual Quick-Filter Bar
    col1, col2, col3 = st.columns(3)
    with col1:
        occasion = st.selectbox("Occasion", ["Casual Meal", "Quick Bite", "Celebration", "Late Night Craving"])
    with col2:
        diet = st.selectbox("Dietary Needs", ["Pure Veg", "Jain Options Available", "No Restrictions", "Vegan Friendly"])
    with col3:
        group = st.selectbox("Dining With", ["Friends", "Family", "Solo", "Date"])

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Single-Action Trigger
    discover_btn = st.button("🚀 Get My 3 Best Matches", type="primary", use_container_width=True)

    if discover_btn:
        with st.spinner("Curating based on real, trusted reviews..."):
            time.sleep(1.5) # Simulate API call/ranking logic
            
        st.success("Found 3 matches that fit your vibe perfectly today!")
        st.markdown("---")

        # Result 1 (Mock Data naturally styled for Ahmedabad)
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("1. Swati Snacks")
        st.markdown("**📍 Law Garden** | 🌟 *#1 for Consistent Quality*")
        
        c1, c2, c3 = st.columns(3)
        c1.metric(label="Verified Trust Score", value="98/100", delta="Top 1%")
        c2.metric(label="Weekend Service", value="Fast", delta="Consistent")
        c3.metric(label="Live Wait Time", value="~15 mins", delta="-5 mins usual", delta_color="inverse")
        
        st.markdown("🌱 **Strictly Pure Veg & Jain** | 🅿️ Valet Available")
        st.info("✅ **Must Order:** Panki Chatni & Baked Macaroni \n\n ⚠️ **Heads-up:** Can get very noisy during peak family hours.")
        
        bc1, bc2 = st.columns(2)
        bc1.button("📍 Get Directions", key="dir1")
        bc2.button("📅 Join Waitlist", key="res1", type="primary")
        st.markdown("</div>", unsafe_allow_html=True)

        # Result 2
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("2. Little French House")
        st.markdown("**📍 Navrangpura** | 🥐 *Great for Casual Friend Hangouts*")
        
        c1, c2, c3 = st.columns(3)
        c1.metric(label="Verified Trust Score", value="89/100")
        c2.metric(label="Weekend Service", value="Average")
        c3.metric(label="Live Wait Time", value="0 mins", delta="Walk-in")
        
        st.markdown("🌱 **Pure Veg** | 🛵 Street Parking")
        st.info("✅ **Must Order:** Mushroom Crepes \n\n ⚠️ **Heads-up:** Portions are slightly on the smaller side for the price.")
        
        bc1, bc2 = st.columns(2)
        bc1.button("📍 Get Directions", key="dir2")
        bc2.button("📅 Reserve Table", key="res2", type="primary")
        st.markdown("</div>", unsafe_allow_html=True)


# ==========================================
# JOURNEY 2: LEAVING A REVIEW
# ==========================================
with tab2:
    st.markdown("### Drop an Honest Review")
    st.write("Help the community by sharing the real experience, minus the hype.")
    
    # Step 1: Search-to-Review
    restaurant_name = st.selectbox(
        "Which restaurant did you visit?", 
        ["Type or select...", "Swati Snacks", "Little French House", "Agashiye", "Manek Chowk Ratri Bazar", "Other"]
    )

    if restaurant_name != "Type or select...":
        with st.form("review_form"):
            # Step 1: Overall Verdict
            st.markdown("#### 1. The Verdict")
            verdict = st.radio(
                "Overall Experience", 
                ["Disappointed 😞", "Met Expectations 😐", "Exceeded Expectations 🤩"], 
                horizontal=True
            )

            # Step 2: Attribute Chips (using select sliders for ease of use)
            st.markdown("#### 2. The Details")
            c1, c2 = st.columns(2)
            c1.select_slider("Food Quality", ["Poor", "Average", "Excellent"], value="Average")
            c2.select_slider("Hygiene & Cleanliness", ["Questionable", "Average", "Spotless"], value="Average")
            c1.select_slider("Weekend Rush/Service", ["Slow", "Manageable", "Quick"], value="Manageable")
            c2.select_slider("Value for Money", ["Overpriced", "Fair", "Worth it"], value="Fair")

            # Step 3: Specific Recommendations
            st.markdown("#### 3. Community Tips")
            st.text_input("What dish should someone definitely order here?", placeholder="e.g., The truffle fries are amazing")
            st.text_area("Any heads-up before going?", placeholder="e.g., Parking is a nightmare, take an auto.", max_chars=140)

            # Step 4: Anti-Hype Verification
            st.markdown("#### 4. Verification (Anti-Hype Anchor)")
            st.file_uploader("Upload receipt/bill to get a 'Verified Diner' badge (Optional)", type=['jpg', 'png', 'pdf'])

            st.markdown("<br>", unsafe_allow_html=True)
            submit_btn = st.form_submit_button("Submit Review 🚀", use_container_width=True)

            if submit_btn:
                st.success("Review published! Thanks for keeping it real. 🏆 Your feedback updates the Trust Score instantly.")
                st.balloons()
