# ==============================================================================
# PRAGYAN AI — COMPLETE SCHOOL INFORMATION CHATBOT
# Class 12 AI Practical Project (Final Version)
# ==============================================================================

import streamlit as st

# ------------------------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="PRAGYAN AI • School Assistant",
    page_icon="🤖",
    layout="centered"
)

# ------------------------------------------------------------------------------
# UI STYLE (FAST & CLEAN)
# ------------------------------------------------------------------------------
st.markdown("""
<style>
body { background-color:#0e1117; }
.chat {
    padding:14px 18px;
    border-radius:10px;
    margin-bottom:10px;
    max-width:85%;
    font-size:15px;
}
.user {
    background:#1f2937;
    margin-left:auto;
    border-left:4px solid #ef4444;
}
.bot {
    background:#020617;
    border-left:4px solid #38bdf8;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# COMPLETE SCHOOL DATA
# ------------------------------------------------------------------------------
SCHOOL_DETAILS = {
    "name": "Pragyan Public School",
    "location": "Jewar, Gautam Buddha Nagar, Uttar Pradesh",
    "board": "CBSE",
    "vision": (
        "To provide quality education with discipline, moral values, "
        "and holistic development of students."
    ),
    "management": {
        "principal": "Mrs. Deepti Sharma",
        "chairman": "Sh. Harish Kumar Sharma"
    },
    "timings": {
        "summer": "07:50 AM to 02:10 PM",
        "winter": "08:20 AM to 02:20 PM",
        "office": "08:30 AM to 04:00 PM"
    },
    "rules": [
        "75% attendance is compulsory",
        "Mobile phones are strictly prohibited",
        "School uniform is mandatory",
        "Discipline and punctuality are required",
        "Medical leave requires a certificate"
    ],
    "facilities": [
        "Smart Classrooms",
        "Science Laboratories",
        "Computer Laboratory",
        "Atal Tinkering Lab (ATL)",
        "Library",
        "Sports Ground",
        "NCC",
        "Robotics & Coding",
        "Cultural Activities"
    ],
    "contacts": {
        "office": "7300723901",
        "admission": "7300723904",
        "transport": "7300723906"
    }
}

FEES = {
    "class 6": "₹32,500 per year",
    "class 7": "₹32,500 per year",
    "class 8": "₹32,500 per year",
    "class 9": "₹35,000 per year",
    "class 10": "₹35,000 per year",
    "class 11 science": "₹43,600 per year",
    "class 11 arts": "₹39,200 per year",
    "class 12 science": "₹43,600 per year",
    "class 12 arts": "₹39,200 per year"
}

# ------------------------------------------------------------------------------
# SESSION STATE
# ------------------------------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        ("bot", "Hello! I am PRAGYAN AI. Ask me anything about Pragyan Public School.")
    ]

# ------------------------------------------------------------------------------
# AI LOGIC ENGINE (RULE-BASED)
# ------------------------------------------------------------------------------
def get_reply(query: str) -> str:
    q = query.lower()

    # Fees
    if "fee" in q:
        for cls, fee in FEES.items():
            if cls in q:
                return f"📘 Fee for {cls.upper()} is {fee}."
        return "📘 Fee depends on class. Please mention the class."

    # Facilities
    if "facility" in q or "facilities" in q:
        return "🏫 Facilities:\n• " + "\n• ".join(SCHOOL_DETAILS["facilities"])

    # Rules
    if "rule" in q or "discipline" in q:
        return "⚖️ School Rules:\n• " + "\n• ".join(SCHOOL_DETAILS["rules"])

    # Timings
    if "time" in q or "timing" in q:
        t = SCHOOL_DETAILS["timings"]
        return (
            "⏰ School Timings:\n"
            f"Summer: {t['summer']}\n"
            f"Winter: {t['winter']}\n"
            f"Office: {t['office']}"
        )

    # Management
    if "principal" in q or "chairman" in q:
        m = SCHOOL_DETAILS["management"]
        return (
            f"👤 Principal: {m['principal']}\n"
            f"👤 Chairman: {m['chairman']}"
        )

    # Contact
    if "contact" in q or "phone" in q:
        c = SCHOOL_DETAILS["contacts"]
        return (
            "📞 Contact Numbers:\n"
            f"Office: {c['office']}\n"
            f"Admission: {c['admission']}\n"
            f"Transport: {c['transport']}"
        )

    # About school
    if "school" in q or "about" in q:
        return (
            f"🏫 {SCHOOL_DETAILS['name']}\n"
            f"Location: {SCHOOL_DETAILS['location']}\n"
            f"Board: {SCHOOL_DETAILS['board']}\n\n"
            f"{SCHOOL_DETAILS['vision']}"
        )

    return "I can answer only verified questions related to Pragyan Public School."

# ------------------------------------------------------------------------------
# UI
# ------------------------------------------------------------------------------
st.title("🤖 PRAGYAN AI")
st.caption("Complete School Information Assistant")

chat_area = st.container()

with chat_area:
    for role, msg in st.session_state.messages[-20:]:
        css = "user" if role == "user" else "bot"
        st.markdown(f"<div class='chat {css}'>{msg}</div>", unsafe_allow_html=True)

user_input = st.chat_input("Ask about fees, rules, facilities, timings, contacts...")

if user_input:
    st.session_state.messages.append(("user", user_input))
    response = get_reply(user_input)
    st.session_state.messages.append(("bot", response))
    st.rerun()
