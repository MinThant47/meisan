import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.bottom_container import bottom
# from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from audio_recorder_streamlit import audio_recorder
import speech_recognition as sr
from flow import app
from retrieve_firebase import update_data_2_firebase
import os

st.set_page_config(page_title="YTU Chatbot", layout="wide")


# conversational_memory_length = 5
# memory=ConversationBufferWindowMemory(k=conversational_memory_length)

if 'chat_history' not in st.session_state:
        st.session_state.chat_history=[]
# else:
#     for message in st.session_state.chat_history:
#         memory.save_context({'input':message['human']},{'output':message['AI']})

st.markdown("<h1 style='text-align: center;'> Meisan (မေစံ)</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'> Explore YTU like never before with our smart chatbot! You can ask about the following topics: </p>", unsafe_allow_html=True)

card_style = """
<div style="
    border-radius: 10px; 
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); 
    padding: 20px; 
    background-color: #f9f9f9; 
    text-align: center;
">
    <h5 style="color: #333;">{title}</h5>
    <ul style="list-style-type: disc; text-align: left; color: #555;">
        {items}
    </ul>
</div>
"""

faq,student_affair, instruction = st.columns(3, gap="medium")

faq_items = ["What is YTU?", "About the majors", "Scholarship Info", "....."]
faq_list = "".join(f"<li>{item}</li>" for item in faq_items)

student_affair_items = ["How can I enroll?", "How to apply for hostel?", "How to suspend uni?","....."]
student_affair_list = "".join(f"<li>{item}</li>" for item in student_affair_items)

instruction_items = ["Move Forward", "Move Backward", "Make smiley face", "....."]
instruction_list = "".join(f"<li>{item}</li>" for item in instruction_items)

# Render the card
faq.markdown(card_style.format(title="FAQ ❓", items=faq_list), unsafe_allow_html=True)
student_affair.markdown(card_style.format(title="Student Affairs ☎️", items=student_affair_list), unsafe_allow_html=True)
instruction.markdown(card_style.format(title="Instructions 📜", items=instruction_list), unsafe_allow_html=True)

st.write("")

final_text = ""

with bottom():
    with stylable_container(
        key = "chat_input",
        css_styles="""
        [data-testid="stHorizontalBlock"] { 
     padding-right: 1rem;
     flex-wrap: nowrap;
 }   
        """
    ):
        col1, col2 = st.columns([0.9, 0.1])
        with col1:
            chat_text=st.chat_input("🙍🏻‍♂️ Enter Your Question...")
        with col2:
            audio_record = audio_recorder(
                text="",
                recording_color="#e8b62c",
                neutral_color="#8a8e9c",
                icon_size="2x",
                auto_start=False)
# Record audio
audio_file_path = "audio_input.wav"


if audio_record:
    with open(audio_file_path, "wb") as f:
        f.write(audio_record)
        f.close()

recognizer = sr.Recognizer()

if audio_record:
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)

        try:
            # Recognize the speech
            with st.spinner("Analysing audio file..."):
                recog_text = recognizer.recognize_google(audio_data)
                final_text = recog_text

    
        except sr.UnknownValueError:
            st.warning("Speech recognition could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from service; {e}")

if  os.path.exists(audio_file_path):
    os.remove(audio_file_path)
    print("Temp audio file removed")

if chat_text:
    final_text = chat_text

if final_text:
    st.chat_message('user').markdown(final_text)
    with st.spinner("Thinking..."):
        response = app.invoke({'question': final_text})
        # response = app.invoke({
        #     'question': "".join(
        #         [msg['human'] + " " for msg in st.session_state.chat_history] 
        #     ) + "Just use for your memory. Please only answer the below question without considering the above sentences. " + final_text
        # })

    if response:
        st.chat_message('ai').markdown(response['documents']['answer'])
        message = {'human': final_text, 'AI': response['documents']['answer']}
        st.session_state.chat_history.append(message)
        
        # update_data_2_firebase(final_text, response['documents']['answer'], response['command'])
    # if len(st.session_state.chat_history) >= 6:
    #     st.session_state.chat_history.pop(0)
