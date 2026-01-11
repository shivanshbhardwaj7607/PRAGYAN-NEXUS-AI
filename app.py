import streamlit as st
import time
from datetime import datetime

# ==============================================================================
# 1. PAGE CONFIGURATION
# ==============================================================================
st.set_page_config(
    page_title="PRAGYAN NEXUS AI",
    page_icon="🛰️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================================================================
# 2. SCI-FI UI + CYBER THEME
# ==============================================================================
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top, #020617, #000000);
    color: #e5e7eb;
    font-family: 'Inter', sans-serif;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020617, #020617);
    border-right: 2px solid #38bdf8;
}

h1 {
    text-align: center;
    color: #38bdf8;
    font-weight: 900;
    letter-spacing: 8px;
}

.stChatMessage {
    background: rgba(2, 6, 23, 0.9);
    border-radius: 18px;
    padding: 24px;
    border: 1px solid rgba(56,189,248,0.4);
    box-shadow: 0 0 30px rgba(56,189,248,0.15);
}

.badge {
    display: inline-block;
    padding: 6px 16px;
    border-radius: 999px;
    border: 1px solid #38bdf8;
    color: #38bdf8;
    font-size: 12px;
    margin: 4px;
}
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 3. SCHOOL KNOWLEDGE CORE (DATABASE)
# ==============================================================================
SCHOOL_DATA = {
    "school_intro": (
        "Pragyan Public School, Jewar is a CBSE-affiliated institution focused on "
        "academic excellence, discipline, and holistic development."
    ),

    "fees": {
        "6": "₹32,500 per year",
        "7": "₹32,500 per year",
        "8": "₹32,500 per year",
        "9": "₹35,000 per year",
        "10": "₹35,000 per year",
        "11": {
            "science": "₹43,600 per year",
            "commerce": "₹39,200 per year",
            "arts": "₹39,200 per year"
        },
        "12": {
            "science": "₹43,600 per year",
            "commerce": "₹39,200 per year",
            "arts": "₹39,200 per year"
        }
    },

    "timings": (
        "Summer: 7:50 AM – 2:10 PM\n"
        "Winter: 8:20 AM – 2:20 PM\n"
        "Office: 8:30 AM – 4:00 PM"
    ),

    "rules": (
        "• Mobile phones are strictly prohibited.\n"
        "• 75% attendance is mandatory.\n"
        "• Proper school uniform is compulsory.\n"
        "• Discipline and punctuality are mandatory."
    ),

    "facilities": (
        "• Smart Classrooms\n"
        "• Atal Tinkering Lab (ATL)\n"
        "• Science & Computer Labs\n"
        "• Library\n"
        "• Sports Complex\n"
        "• NCC & Robotics"
    ),

    "contact": (
        "📞 General Enquiry: 7300723901\n"
        "📞 Admission Office: 7300723904\n"
        "📍 Jewar, Gautam Buddha Nagar, UP"
    )
}

# ==============================================================================
# 4. INTELLIGENT QUERY ENGINE (RULE-BASED AI)
# ==============================================================================
def process_query(query: str) -> str:
    q = query.lower()

    # SCHOOL INTRO
    if any(word in q for word in ["school", "about", "introduction"]):
        return SCHOOL_DATA["school_intro"]

    # FEES LOGIC
    if "fee" in q:
        for cls in ["6","7","8","9","10","11","12"]:
            if cls in q or f"class {cls}" in q or f"{cls}th" in q or f"xii" in q:
                if cls in ["11","12"]:
                    if "science" in q:
                        return f"Fee for Class {cls} (Science): {SCHOOL_DATA['fees'][cls]['science']}"
                    if "commerce" in q:
                        return f"Fee for Class {cls} (Commerce): {SCHOOL_DATA['fees'][cls]['commerce']}"
                    if "arts" in q:
                        return f"Fee for Class {cls} (Arts): {SCHOOL_DATA['fees'][cls]['arts']}"
                    return (
                        f"Fee for Class {cls}:\n"
                        f"Science – {SCHOOL_DATA['fees'][cls]['science']}\n"
                        f"Commerce – {SCHOOL_DATA['fees'][cls]['commerce']}\n"
                        f"Arts – {SCHOOL_DATA['fees'][cls]['arts']}"
                    )
                return f"Fee for Class {cls}: {SCHOOL_DATA['fees'][cls]}"
        return "Please mention the class (e.g., fee of class 6)."

    # TIMINGS
    if any(word in q for word in ["time", "timing", "schedule"]):
        return SCHOOL_DATA["timings"]

    # RULES
    if any(word in q for word in ["rule", "discipline"]):
        return SCHOOL_DATA["rules"]

    # FACILITIES
    if any(word in q for word in ["facility", "facilities", "labs", "sports"]):
        return SCHOOL_DATA["facilities"]

    # CONTACT
    if any(word in q for word in ["contact", "phone", "number"]):
        return SCHOOL_DATA["contact"]

    return (
        "🔒 Secure AI Core Response:\n"
        "I can answer only verified questions related to Pragyan Public School."
    )

# ==============================================================================
# 5. HEADER
# ==============================================================================
st.markdown("<h1>PRAGYAN NEXUS AI</h1>", unsafe_allow_html=True)
st.markdown("""
<div class="badge">END-TO-END ENCRYPTED</div>
<div class="badge">SATELLITE CONNECTED</div>
<div class="badge">SCHOOL-LOCKED AI</div>
<div class="badge">REAL-TIME RESPONSE</div>
""", unsafe_allow_html=True)

# ==============================================================================
# 6. SESSION MEMORY
# ==============================================================================
if "chat" not in st.session_state:
    st.session_state.chat = [
        {
            "role": "assistant",
            "content": "🛰️ PRAGYAN NEXUS AI ONLINE.\nAsk me anything about Pragyan Public School."
        }
    ]

# ==============================================================================
# 7. CHAT DISPLAY
# ==============================================================================
for msg in st.session_state.chat:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ==============================================================================
# 8. INPUT
# ==============================================================================
if user_input := st.chat_input("Ask about fees, rules, facilities, timings, contacts..."):
    st.session_state.chat.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    response = process_query(user_input)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        text = ""
        for word in response.split():
            text += word + " "
            time.sleep(0.015)
            placeholder.markdown(text)

    st.session_state.chat.append({"role": "assistant", "content": response})
