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
                    model="gemini-3.6-flash",
                    contents=query
                )
                
                st.write("### Results:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a query to search.")
import streamlit as st
from google import genai
from google.genai import types

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
                api_key = st.secrets["GEMINI_API_KEY"]
                client = genai.Client(api_key=api_key)
                
                # System Instruction se AI ko bataya gaya hai ki creator Ameer Hamza hain
                system_prompt = "Aapka naam Mini Google hai. Aapko Ameer Hamza ne banaya aur design kiya hai. Jab bhi koi aapke creator ya naam ke baare mein pooche, hamesha kahein ki aap Mini Google hain aur aapko Ameer Hamza ne banaya hai."
                
                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=query,
                    config=types.GenerateContentConfig(
                        system_instruction=system_prompt
                    )
                )
                
                st.write("### Results:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a query to search.")
