import streamlit as st
import ollama
from PIL import Image
import io

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
                # 1. Agar user ne Photo aur Text dono diye hain
                if uploaded_file and user_query:
                    # Photo ko bytes mein convert karna local AI ke liye
                    img_byte_arr = io.BytesIO()
                    uploaded_image.save(img_byte_arr, format=uploaded_image.format)
                    img_bytes = img_byte_arr.getvalue()
                    
                    # Local Llava model ko call karna jo text aur photo dono samajhta hai
                    response = ollama.chat(
                        model='llava',
                        messages=[{
                            'role': 'user',
                            'content': user_query,
                            'images': [img_bytes]
                        }]
                    )
                    st.success("Results:")
                    st.write(response['message']['content'])
                
                # 2. Agar user ne sirf Photo di hai bina text ke
                elif uploaded_file:
                    img_byte_arr = io.BytesIO()
                    uploaded_image.save(img_byte_arr, format=uploaded_image.format)
                    img_bytes = img_byte_arr.getvalue()
                    
                    response = ollama.chat(
                        model='llava',
                        messages=[{
                            'role': 'user',
                            'content': 'Is tasveer ko scan karo aur batao isme kya kya cheezein mojud hain detail mein.',
                            'images': [img_bytes]
                        }]
                    )
                    st.success("Results:")
                    st.write(response['message']['content'])
                
                # 3. Agar user ne sirf Text likha hai
                else:
                    response = ollama.chat(
                        model='llama3', # Ya jo bhi local text model aap chalana chahein
                        messages=[{
                            'role': 'user',
                            'content': user_query
                        }]
                    )
                    st.success("Results:")
                    st.write(response['message']['content'])
                    
            except Exception as e:
                st.error(f"AI Model connect nahi ho saka. Error: {str(e)}")
                st.info("Tip: Apne laptop ke terminal mein 'ollama run llava' command chala kar check karein.")

            
