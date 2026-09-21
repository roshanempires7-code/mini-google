import streamlit as st
from google import genai
from PIL import Image

# Roshan Empires Theme & Logo Setup
st.set_page_config(page_title="Roshan Empires AI", page_icon="🔍")
st.title("🔍 Roshan Empires - Mini Google AI")
st.subheader("Mera Apna Custom Multimodal AI Platform")

# User input text aur photo uploader box
user_query = st.text_input("Ameer Hamza ke AI se kuch bhi poochein...", placeholder="E.g., Is photo mein kya hai?")
uploaded_file = st.file_uploader("Koi bhi Photo upload karein (PNG/JPG)", type=["png", "jpg", "jpeg"])

# Agar user photo upload kare
uploaded_image = None
if uploaded_file is not None:
    uploaded_image = Image.open(uploaded_file)
    st.image(uploaded_image, caption="Aapki Uploaded Photo", use_container_width=True)

# Main Button trigger
if st.button("AI Search"):
    if not user_query and not uploaded_file:
        st.warning("Meharbani kar ke kuch likhein ya photo upload karein!")
    else:
        with st.spinner("Roshan Empires AI processing kar raha hai..."):
            try:
                # Client automatic background secrets se key utha lega
                client = genai.Client()
                
                # 1. Agar user ne Photo aur Text dono diye hain
                if uploaded_file and user_query:
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=[user_query, uploaded_image]
                    )
                    st.success("Results:")
                    st.write(response.text)
                
                # 2. Agar user ne sirf Photo di hai bina text ke
                elif uploaded_file:
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=["Is tasveer ko scan karo aur batao isme kya kya cheezein mojud hain detail mein.", uploaded_image]
                    )
                    st.success("Results:")
                    st.write(response.text)
                
                # 3. Agar user ne sirf Text likha hai
                else:
                    response = client.models.generate_content(
                        model="gemini-2.5-flash",
                        contents=[user_query]
                    )
                    st.success("Results:")
                    st.write(response.text)
                    
            except Exception as e:
                st.error(f"AI Model connect nahi ho saka. Error: {str(e)}")
