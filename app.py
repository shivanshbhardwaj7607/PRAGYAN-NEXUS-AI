import streamlit as st
import time
from datetime import datetime

# ==============================================================================
# 1. PAGE CONFIG
# ==============================================================================
st.set_page_config(
    page_title="PRAGYAN NEXUS AI",
    page_icon="🛰️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================================================================
# 2. SCI-FI UI STYLE
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
    letter-spacing: 6px;
}

.stChatMessage {
    background: rgba(2, 6, 23, 0.9);
    border-radius: 18px;
    padding: 22px;
    border: 1px solid rgba(56,189,248,0.4);
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
# 3. SCHOOL KNOWLEDGE BASE
# ==============================================================================
DATA = {
    "intro": "Pragyan Public School, Jewar is a CBSE-affiliated institution focused on academic excellence, discipline, and holistic development.",

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
        "• Mobile phones are strictly prohibited\n"
        "• 75% attendance is mandatory\n"
        "• Proper uniform is compulsory\n"
        "• Discipline is strictly followed"
    ),

    "facilities": (
        "• Smart Classrooms\n"
        "• Atal Tinkering Lab (ATL)\n"
        "• Science & Computer Labs\n"
        "• Library\n"
        "• Sports Facilities\n"
        "• NCC & Robotics"
    ),

    "contact": (
        "📞 General Enquiry: 7300723901\n"
        "📞 Admission Office: 7300723904\n"
        "📍 Jewar, Gautam Buddha Nagar, UP"
    )
}

# ==============================================================================
# 4. AI QUERY ENGINE (RULE BASED)
# ==============================================================================
def answer_query(query: str) -> str:
    q = query.lower()

    if any(x in q for x in ["about", "school", "pragyan"]):
        return DATA["intro"]

    if "fee" in q:
        for cls in ["6","7","8","9","10","11","12"]:
            if cls in q or f"class {cls}" in q or f"{cls}th" in q or "xii" in q:
                if cls in ["11","12"]:
                    if "science" in q:
                        return f"Fee for Class {cls} (Science): {DATA['fees'][cls]['science']}"
                    if "commerce" in q:
                        return f"Fee for Class {cls} (Commerce): {DATA['fees'][cls]['commerce']}"
                    if "arts" in q:
                        return f"Fee for Class {cls} (Arts): {DATA['fees'][cls]['arts']}"
                    return (
                        f"Fee for Class {cls}:\n"
                        f"Science – {DATA['fees'][cls]['science']}\n"
                        f"Commerce – {DATA['fees'][cls]['commerce']}\n"
                        f"Arts – {DATA['fees'][cls]['arts']}"
                    )
                return f"Fee for Class {cls}: {DATA['fees'][cls]}"
        return "Please mention the class (example: fee of class 9)."

    if any(x in q for x in ["time", "timing"]):
        return DATA["timings"]

    if any(x in q for x in ["rule", "discipline"]):
        return DATA["rules"]

    if any(x in q for x in ["facility", "facilities", "lab", "sports"]):
        return DATA["facilities"]

    if any(x in q for x in ["contact", "number", "phone"]):
        return DATA["contact"]

    return (
        "🔒 Secure AI Core:\n"
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
# 6. SIDEBAR CONTROL PANEL
# ==============================================================================
with st.sidebar:
    st.markdown("## 🛰️ NEXUS CONTROL PANEL")
    st.markdown("""
    **System Status:** 🟢 ONLINE  
    **Security:** 🔐 Encrypted  
    **Network:** 📡 Satellite Linked  
    **AI Core:** 🧠 Rule-Based  
    **Response:** ⚡ Instant  
    """)
    st.divider()
    st.markdown("### 🏫 Pragyan Public School")
    st.markdown("CBSE Affiliated • Jewar, UP")
    st.divider()
    st.progress(100)
    st.caption("© 2026 PRAGYAN NEXUS AI")

# ==============================================================================
# 7. CHAT MEMORY
# ==============================================================================
if "chat" not in st.session_state:
    st.session_state.chat = [
        {"role": "assistant", "content": "🛰️ PRAGYAN NEXUS AI ONLINE.\nAsk me anything about Pragyan Public School."}
    ]

# ==============================================================================
# 8. CHAT DISPLAY
# ==============================================================================
for msg in st.session_state.chat:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ==============================================================================
# 9. INPUT
# ==============================================================================
if user_input := st.chat_input("Ask about fees, rules, facilities, timings..."):
    st.session_state.chat.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    reply = answer_query(user_input)

    with st.chat_message("assistant"):
        box = st.empty()
        text = ""
        for word in reply.split():
            text += word + " "
            time.sleep(0.012)
            box.markdown(text)

    st.session_state.chat.append({"role": "assistant", "content": reply})
