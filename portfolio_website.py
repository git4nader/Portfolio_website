import streamlit as st
import google.generativeai as genai

api_key = st.secrets["GOOGLE_API_KEY"]

# genai.configure(api_key="AIzaSyAnKSYdWGMxFC6Imw6cxST5fVll9uPTsvo")

genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

col1, col2 = st.columns(2)

with col1:
    st.subheader("Hi :wave:")
    st.title("I am Nader Farr")


# Terminal >>> command propmpt to get (venv) D:\Documents\python related\PycharmProjects\240703_CVzone_Bootcamp>
# type streamlit run portfolio_website.py >>> result: new tab opens in browser with url: http://localhost:8501/
# and display I am Nader Farr

with col2:
    st.image("images/WIN_20210929_08_21_00_Pro (2).jpg")

st.title(" ")

persona = """
        You are Nader AI bot. You help people answer questions about your self (i.e Murtaza)
        Answer as if you are responding . dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret"
        Here is more info about Nader: 

        Nader Hassan is an Educator/Youtuber/Entrepreneur in the field of Computer Vision and Robotics.
        He runs one of the largest YouTube channels in the field of Computer Vision,
        educating over 3 Million developers,
        hobbyists and students. Nader earned his Bachelor’s degree from SJSU (San Jose State University)
        Majoring EE (Electrical Engineering) and later obtained his Master's degree from
        CSUS (California State University Sacramento). He is also a serial entrepreneur having launched several
        successful ventures including CVZone, which is a one stop solution for learning 
        and building vision projects. Prior to starting his entrepreneurial career, 
        Nader worked as a university lecturer and a design engineer, evaluating 
        and developing rapid prototypes of US patents.

        Nader's Youtube Channel: https://www.youtube.com/channel/UCYUjYU5FveRAscQ8V21w81A
        Nader's Email: contact@Naderhassan.com 
        Nader's Facebook: https://www.facebook.com/Nadersworkshop
        Nader's Instagram: https://www.instagram.com/Nadersworkshop/
        Nader's Linkdin: https://www.linkedin.com/in/Nader-hassan-8045b38a/
        Nader's Github :https://github.com/Naderhassan
        """

st.title("Nader's AI Bot")

# st.write("Ask anything about me")
user_question = st.text_input("Ask anything about me")
if st.button("ASK", use_container_width=400):
    prompt = persona + user_question
    response = model.generate_content(prompt)
    st.write(response.text)




col1, col2 = st.columns(2)

with col1:
    st.subheader("Youtube Channel")
    # st.title("Largest Computer Vision Channel in the world")
    # st.subheader("Largest Computer Vision Channel in the world")
    st.write("- Largest Computer Vision Channel in the world")
    st.write("- 400 subscribers")
    st.write("- 150 free tutorials")
    st.write("- 15 million view")
    st.write("- 1.5 million Hours+ Watch time")

with col2:
    st.video("https://www.youtube.com/@golestaan2259")

st.title(" ")
# st.subheader(" ")
# st.write(" ")

st.title("My Setup")

st.image("images/setup.jpg")

# st.title(" ")
# st.subheader(" ")
st.write(" ")
st.title("My Skills")

st.slider("Programming", 0, 100, 70)
st.slider("teaching", 0, 100, 85)
st.slider("Robotics", 0, 100, 75)

# st.file_uploader("Upload a file")

st.write(" ")
st.title("Gallery")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/g1.jpg")
    st.image("images/g2.jpg")
    st.image("images/g3.jpg")

with col2:
    st.image("images/g4.jpg")
    st.image("images/g5.jpg")
    st.image("images/g6.jpg")

with col3:
    st.image("images/g7.jpg")
    st.image("images/g8.jpg")
    st.image("images/g9.jpg")

st.subheader(" ")
st.write("CONTACT")
st.title("For any inquiries, email at:")
st.subheader("nader.farr@gmail.com")