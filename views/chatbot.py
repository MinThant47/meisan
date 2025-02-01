import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.bottom_container import bottom
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from audio_recorder_streamlit import audio_recorder
import speech_recognition as sr
from flow import app
from retrieve_firebase import update_data_2_firebase
import os

st.title("Chat with Meisan")
st.write("I'm ready to answer anything related with YTU!")

conversational_memory_length = 5
memory=ConversationBufferWindowMemory(k=conversational_memory_length)

if 'chat_history' not in st.session_state:
        st.session_state.chat_history=[]
else:
    for message in st.session_state.chat_history:
        memory.save_context({'input':message['human']},{'output':message['AI']})

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

if st.session_state.chat_history:
    for msg in st.session_state.chat_history:
        st.chat_message('user').markdown(msg['human'])
        st.chat_message('assistant').markdown(msg['AI'])

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


