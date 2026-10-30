import streamlit as st
from redactor import redact_text
from detector import detect_private_info

st.set_page_config(
    page_title="BharatShield AI",
    page_icon="🛡️"
)

st.title("🛡️ BharatShield AI")
st.subheader("Privacy protection for Indian documents")

st.write(
    "Paste your text below. "
    "We'll detect and hide sensitive information."
)

user_text = st.text_area(
    "Enter your text here:",
    height=200,
    placeholder="Example: Contact me at example@gmail.com"
)

if st.button("Protect My Text"):

    if user_text.strip():

        safe_text = redact_text(user_text)
        findings = detect_private_info(user_text)

        # Privacy Risk Score
        total_items = len(findings)
        risk_score = min(total_items * 20, 100)

        st.subheader("🔐 Privacy Risk Score")
        st.metric("Risk Score", f"{risk_score}/100")

        if risk_score <= 20:
            st.success("Low Risk")

        elif risk_score <= 60:
            st.warning("Medium Risk")

        else:
            st.error("High Risk")

        # Privacy Summary
        st.success("Privacy scan completed!")
        st.subheader("Privacy Summary")

        st.metric(
            "Total sensitive items detected",
            len(findings)
        )

        counts = {}

        for item in findings:
            category = item["type"]
            counts[category] = counts.get(category, 0) + 1

        for category, count in counts.items():
            st.write(f"{category}: {count}")

        # Protected Text
        st.subheader("Protected Text")
        st.code(safe_text)

        # Download
        st.download_button(
            "Download protected text",
            data=safe_text,
            file_name="protected_text.txt",
            mime="text/plain"
        )

    else:
        st.warning("Please enter some text first.")