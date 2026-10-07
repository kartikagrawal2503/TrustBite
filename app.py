import streamlit as st
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="TrustBite | Curated Dining",
    page_icon="🍽️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        font-weight: bold;
    }
    .card {
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        background-color: #f9f9fb;
    }
    .critical-consensus {
        background-color: #fff3cd;
        color: #856404;
        padding: 10px;
        border-radius: 5px;
        border-left: 4px solid #ffeeba;
        font-size: 0.9em;
        margin-top: 10px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- APP HEADER ---
st.title("🍽️ TrustBite")
st.markdown("*Skip the endless scrolling. Find the perfect spot based on real verified diners.*")
st.divider()

# --- TABS FOR USER JOURNEYS ---
tab1, tab2 = st.tabs(["🔍 Find a Restaurant", "✍️ Leave a Review"])

# ==========================================
# JOURNEY 1: DISCOVERING & CHOOSING
# ==========================================
with tab1:
    st.markdown("### Quick Shortcut Scenarios")
    # Quick launch chips for high-intent use cases
    scenario = st.radio(
        "Select a pre-configured mood:",
        ["None (Custom Search)", "👨‍👩‍👧 Family Dinner (Quiet + Valet)", "🍟 Quick Bite with Friends", "🌙 Reliable Late-Night Craving"],
        horizontal=True,
        label_visibility="collapsed"
    )

    st.markdown("### Or customize your filters")
    # Contextual Quick-Filter Bar with Granular Fields
    col1, col2 = st.columns(2)
    with col1:
        diet = st.selectbox("Dietary Needs", ["100% Pure Vegetarian", "Separate Jain Kitchen Available", "Vegan-Friendly Options", "No Restrictions"])
        parking = st.selectbox("Parking & Access", ["Dedicated Valet", "Easy On-Site Parking", "Street Parking Only", "Any"])
    with col2:
        ambiance = st.selectbox("Ambiance Profile", ["Quiet & Intimate", "Bustling / Family-Friendly", "Lively & High Energy", "Any"])
        budget = st.selectbox("True Bill for Two (Expected)", ["Under ₹1000", "₹1000 - ₹2500", "₹2500+"])

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Single-Action Trigger
    discover_btn = st.button("🚀 Get My Top 3 Matches", type="primary", use_container_width=True)

    if discover_btn:
        with st.spinner("Curating based on real, verified diner receipts..."):
            time.sleep(1.5) 
            
        st.success("Found 3 matches that fit your vibe and dietary needs perfectly!")
        st.markdown("---")

        # Result 1: Featuring all new attributes
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("1. Swati Snacks")
        st.markdown("**📍 Law Garden** | 🌟 *#1 for Consistent Quality*")
        
        c1, c2, c3, c4 = st.columns(4)
        c1.metric(label="Trust Score", value="98/100", delta="Top 1%")
        c2.metric(label="Live Wait", value="~15 mins", delta="Walk-in Ready", delta_color="normal")
        c3.metric(label="Consistency", value="High", delta="Wknd/Wkday Match")
        c4.metric(label="True Bill (2 pax)", value="₹850")
        
        st.markdown("🌱 **100% Pure Veg & Separate Jain Menu** | 🅿️ **Dedicated Valet** | 🗣️ **Bustling**")
        
        # Critical Consensus Block
        st.markdown("""
        <div class='critical-consensus'>
            <b>⚖️ Critical Consensus:</b> Consistently praised for authentic taste and hygiene. The main downside reported is tight seating and 25+ min waits on Sunday evenings.
        </div>
        """, unsafe_allow_html=True)

        st.info("✅ **Must Order:** Panki Chatni \n\n ⛔ **Overhyped / Skip:** Standard Pizzas (stick to regional dishes)")
        
        bc1, bc2 = st.columns(2)
        bc1.button("📍 Get Directions", key="dir1")
        bc2.button("📅 Join Live Waitlist", key="res1", type="primary")
        st.markdown("</div>", unsafe_allow_html=True)


# ==========================================
# JOURNEY 2: LEAVING A REVIEW
# ==========================================
with tab2:
    st.markdown("### Drop an Honest Review (15 Seconds)")
    st.write("Help the community avoid bad meals by sharing the real experience.")
    
    restaurant_name = st.selectbox(
        "Which restaurant did you visit?", 
        ["Type or select...", "Swati Snacks", "Little French House", "Agashiye", "Manek Chowk Ratri Bazar", "Other"]
    )

    if restaurant_name != "Type or select...":
        with st.form("review_form"):
            
            # --- MANDATORY QUICK TAPS ---
            st.markdown("#### 1. The Context")
            c1, c2 = st.columns(2)
            visit_time = c1.selectbox("When did you go?", ["Weekday Lunch", "Weekday Dinner", "Weekend Lunch", "Weekend Dinner (Peak Rush)"])
            visit_group = c2.selectbox("Who with?", ["Family", "Friends", "Date", "Solo"])

            st.markdown("#### 2. The Verdict")
            verdict = st.radio(
                "Overall Experience", 
                ["Disappointed 😞", "Met Expectations 😐", "Exceeded Expectations 🤩"], 
                horizontal=True
            )

            # Conditional Anti-Rant Guardrail for Negative Reviews
            if verdict == "Disappointed 😞":
                st.warning("What went wrong? (Select all that apply)")
                issues = st.multiselect("Specific Issues", ["Food was bland / cold", "Slow service", "Poor hygiene / washrooms", "Misleading prices", "Too loud / cramped"])

            st.markdown("#### 3. Dish Breakdown")
            c3, c4 = st.columns(2)
            c3.text_input("👍 Must-Order Dish", placeholder="e.g., Truffle Fries")
            c4.text_input("👎 Skip / Overhyped Dish", placeholder="e.g., Red Sauce Pasta")

            # --- OPTIONAL DEEP DIVE (PROGRESSIVE DISCLOSURE) ---
            with st.expander("Detailed Reality Check & Verification (Optional)"):
                st.markdown("Help establish the *True Cost* and *Actual Wait Times*.")
                
                ec1, ec2 = st.columns(2)
                ec1.select_slider("Did you have to wait?", ["No Wait", "10-20 mins", "30+ mins"])
                ec2.select_slider("Food Delivery Speed", ["Quick", "Normal", "Unusually Slow"])
                
                ec3, ec4 = st.columns(2)
                ec3.select_slider("Hygiene & Cleanliness", ["Questionable", "Acceptable", "Spotless"], value="Acceptable")
                actual_bill = ec4.number_input("Actual Total Bill Amount (₹)", min_value=0, step=100)
                pax = ec4.number_input("For how many people?", min_value=1, step=1)
                
                st.markdown("**Get the 'Verified Diner' Badge 🏆**")
                st.file_uploader("Upload receipt / bill photo", type=['jpg', 'png'])

            st.markdown("<br>", unsafe_allow_html=True)
            submit_btn = st.form_submit_button("Submit Anonymous Review 🚀", use_container_width=True)

            if submit_btn:
                st.success("Review published! Thanks for keeping it real. 🏆 Your feedback instantly updates the Trust Score.")
                st.balloons()
