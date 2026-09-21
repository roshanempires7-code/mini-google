import streamlit as st
import openai
from PIL import Image
import base64
import io

# Roshan Empires Professional Configuration
st.set_page_config(page_title="Roshan Empires AI", page_icon="⚡", layout="centered")

# Custom CSS for clean Premium look
st.markdown("""
<style>
    .main { text-align: center; }
    div.stButton > button {
        background-color: #f8f9fa;
        color: #3c4043;
        border: 1px solid #dadce0;
        border-radius: 4px;
        padding: 8px 16px;
    }
    div.stButton > button:hover {
        border-color: #8ab4f8;
        color: #1a73e8;
        background-color: #f8f9fa;
    }
</style>
""", unsafe_allow_html=True)

# Main Title
st.title("⚡ Roshan Empires AI")
st.subheader("Mini google official platform - Powered by OpenAI")

# Input Boxes
user_query = st.text_input("Search or ask anything...", placeholder="Ask Roshan Empires AI...")
uploaded_file = st.file_uploader("Upload an Image for visual analysis", type=["png", "jpg", "jpeg"])

# Image Preview Setup & Base64 Encoder
uploaded_image = None
base64_image = None

if uploaded_file is not None:
    uploaded_image = Image.open(uploaded_file)
    st.image(uploaded_image, caption="Visual Input Loaded", use_container_width=True)
    
    # Image ko OpenAI format (Base64) mein badalna
    buffered = io.BytesIO()
    # Handle transparent PNGs or JPEGs automatically
    img_format = uploaded_image.format if uploaded_image.format else "JPEG"
    uploaded_image.save(buffered, format=img_format)
    base64_image = base6464encode(buffered.getvalue()).decode('utf-8')

# Mini Search Button Trigger
if st.button("Mini Search"):
    if not user_query and not uploaded_file:
        st.warning("Please enter a query or upload an image first!")
    else:
        with st.spinner("Searching OpenAI secure servers..."):
            try:
                # Automatic initialization (Background secret se openai_api_key khud utha lega)
                client = openai.OpenAI()
                
                # 1. Visual Search + Text Query (Both image and text)
                if uploaded_file and user_query:
                    response = client.chat.completions.create(
                        model="gpt-4o",  # Stable Multimodal Model
                        messages=[{
                            "role": "user",
                            "content": [
                                {"type": "text", "text": user_query},
                                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                            ]
                        }]
                    )
                    st.success("OpenAI Intelligence Results:")
                    st.write(response.choices[0].message.content)
                
                # 2. Pure Visual Search (Image Only)
                elif uploaded_file:
                    response = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[{
                            "role": "user",
                            "content": [
                                {"type": "text", "text": "Scan this image thoroughly and describe it in full detail."},
                                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                            ]
                        }]
                    )
                    st.success("OpenAI Visual Results:")
                    st.write(response.choices[0].message.content)
                
                # 3. Standard Text Search (Text Only)
                else:
                    response = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[{
                            "role": "user",
                            "content": user_query
                        }]
                    )
                    st.success("OpenAI Search Results:")
                    st.write(response.choices[0].message.content)
                    
            except Exception as e:
                st.error(f"OpenAI server connection issue. Error: {str(e)}")
