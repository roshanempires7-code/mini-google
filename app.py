import streamlit as st
from google import genai
from PIL import Image

# Google-like Professional Configuration
st.set_page_config(page_title="Mini Google AI", page_icon="⚡", layout="centered")

# Custom CSS for clean Google look
st.markdown("""
<style>
    .main { text-align: center; }
    div.stButton > button {
        background-color: #f8f9fa;
        color: #3c4043;
        border: 1px solid #f8f9fa;
        border-radius: 4px;
        padding: 8px 16px;
    }
    div.stButton > button:hover {
        border-color: #dadce0;
        color: #202124;
        background-color: #f8f9fa;
    }
</style>
""", unsafe_allow_html=True)

# Main Title
st.title("⚡ Mini Google AI")
st.subheader("Mini google official platform")

# Professional Input Boxes (Same as Google)
user_query = st.text_input("Search or type a URL", placeholder="Ask Mini Google anything...")
uploaded_file = st.file_uploader("Upload an Image to search with visuals", type=["png", "jpg", "jpeg"])

# Image Preview Setup
uploaded_image = None
if uploaded_file is not None:
    uploaded_image = Image.open(uploaded_file)
    st.image(uploaded_image, caption="Visual Input Loaded", use_container_width=True)

# Google Search Buttons Trigger
if st.button("Mini Search"):
    if not user_query and not uploaded_file:
        st.warning("Please enter a query or upload an image first!")
    else:
        with st.spinner("Searching Google AI servers..."):
            try:
                # Backend initialization using Gemini online cloud servers
                client = genai.Client()
                
                # 1. Visual Search + Text Query
                if uploaded_file and user_query:
                    response = client.models.generate_content(
                        model="gemini-1.5-flash",
                        contents=[user_query, uploaded_image]
                    )
                    st.success("Google AI Search Results:")
                    st.write(response.text)
                
                # 2. Pure Visual Search (Image and text Only)
                elif uploaded_file:
                    response = client.models.generate_content(
                        model="gemini-1.5-flash",
                        contents=["Scan this image thoroughly and describe all visible elements and context in detail.", uploaded_image]
                    )
                    st.success("Google Visual Search Results:")
                    st.write(response.text)
                
                # 3. Standard Text Search
                else:
                    response = client.models.generate_content(
                        model="gemini-1.5-flash",
                        contents=[user_query]
                    )
                    st.success("Google Search Results:")
                    st.write(response.text)
                    
            except Exception as e:
                st.error(f"Unable to connect to Google servers. Error: {str(e)}")
