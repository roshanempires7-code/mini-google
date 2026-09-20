import streamlit as st
from google import genai

# Page Configuration
st.set_page_config(page_title="Mini Google", page_icon="🔍", layout="centered")

# UI Styling
st.markdown("""
    <style>
    .main { text-align: center; }
    div.stButton > button {
        background-color: #303134;
        color: #e8eaed;
        border: 1px solid #5f6368;
        border-radius: 4px;
        padding: 8px 16px;
    }
    div.stButton > button:hover {
        border-color: #8ab4f8;
        color: #8ab4f8;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🔍 Mini Google")

# Search Input
query = st.text_input("", placeholder="Search anything here...", label_visibility="collapsed")

if st.button("Google Search"):
    if query:
        with st.spinner("Searching..."):
            try:
                # Retrieve API Key from Streamlit Secrets
                api_key = st.secrets["GEMINI_API_KEY"]
                client = genai.Client(api_key=api_key)
                
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=query
                )
                
                st.write("### Results:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a query to search.")
