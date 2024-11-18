import streamlit as st
import base64
import os
import re

from st_audiorec import st_audiorec

# Todo: Call Files
from DB.create_db import Create_DB
from src.rag_pipeline import RAG_Pipeline
from src.utils.record_audio import record_audio
from src.utils.asr import run_asr
from src.voice.english_voice import *
from src.voice.hindi_voice import *
from src.voice.tamil_voice import *
from src.voice.gujarati_voice import *

# Set the layout to wide
# streamlit code for viewing document
st.set_page_config(layout="wide",
                   page_title="PolyVox",
                   page_icon="🗣️",
                   )

# hide hamburger and customize footer
hide_menu = """
    <style>

    #MainMenu {
        visibility:hidden;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        color: grey;
        text-align: center;
    }

    </style>

    <div class="footer">
        <p>'With 🫶️ from Shubham Shankar.'</p>
    </div>

"""

# Styling ----------------------------------------------------------------------
st.image("icon.jpg", width=85)
st.title("PolyVox")
st.subheader("🎙️ Bridging languages with lifelike voices 🔊.")
st.write("Powered by LLMs.")
st.markdown(hide_menu, unsafe_allow_html=True)

# Intro ----------------------------------------------------------------------

st.write(
    """
    Hi 👋, I'm **:red[Shubham Shankar]**, and welcome to **:green[PolyVox]**! ! :rocket: **PolyVox** leverages cutting-edge technologies like **:blue[Automatic Speech Recognition (ASR)]**, **:orange[Speech-to-Text (STT)]**, :violet[Hybrid Retrieval-Augmented Generation (RAG)], and **:red[advanced voice cloning]** to create truly human-like, multilingual conversations. 
    Whether you speak in English, Hindi, or any other language, **PolyVox** recognizes your language and responds in the same **natural accent**, providing seamless and intuitive interactions. With **PolyVox**, your conversations feel more personal, dynamic, and connected, no matter the language you choose. ✨


    """
)

st.markdown('---')

st.write(
    """
    ### App Interface!!

    :dog: The web app has an easy-to-use interface. 

    1] **:red[Upload File]**: Easily upload your documents to feed into the RAG pipeline for processing.
    
    2] **:green[Choose Chunk Size]**: Select the appropriate chunk size for optimal data processing and retrieval.
    
    3] **:orange[Start Chat or Voice]**: Click on one of the options—Chat for text-based interactions or Voice for voice-based conversations with human-like accents.
    
    4] **:blue[Clear]**: Click Clear to reset the conversation and start fresh.

    """
)

st.markdown('---')

st.error(
    """
    Connect with me on [**Github**](https://github.com/RATHOD-SHUBHAM) and [**LinkedIn**](https://www.linkedin.com/in/shubhamshankar/). ✨
    """,
    icon="🧟‍♂️",
)

st.markdown('---')

HOME = os.getcwd()

# Todo: Creating Object
db_obj = Create_DB()
rag_obj = RAG_Pipeline()


def record_voice():
    # Record Audio
    wav_audio_data = st_audiorec()

    if wav_audio_data is not None:
        # Save the raw audio data to a .wav file
        wav_file_name = f'{HOME}/src/utils/microphone-results.wav'

        with open(wav_file_name, 'wb') as f:
            f.write(wav_audio_data)  # Write raw bytes directly to the file

        st.write("Audio saved as 'recorded_audio.wav'")


# Save the uploaded file
def save_uploadedfile(uploadedfile):
    data_file_dir = f'{HOME}/data_file'
    with open(os.path.join(data_file_dir, "my_docs"), "wb") as f:
        f.write(uploadedfile.getbuffer())
    return st.success("Saved File:{} to data_file_dir".format(uploadedfile.name))


def main():
    # Initialize Sessions
    # Initialize state for toggling between chat modes
    if "voice_chat_history" not in st.session_state:
        st.session_state.voice_chat_history = []

    if "text_chat_history" not in st.session_state:
        st.session_state.text_chat_history = []

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "create_embedding_mode" not in st.session_state:
        st.session_state.create_embedding_mode = ""

    # Start Application
    datafile = st.file_uploader("Upload PDF", type=['pdf'])
    if datafile is not None:
        file_details = {"FileName": datafile.name, "FileType": datafile.type}
        save_uploadedfile(datafile)

        st.subheader("Create Database")
        chunk_size = st.slider("Chunk Size", 1000, 10000, 4000)
        chunk_overlap = st.slider("Chunk Overlap", 300, 1000, 800)

        if st.button("💬 Create Embeddings"):  # Text chat button
            st.session_state.create_embedding_mode = "Create Embeddings"

        if st.session_state.create_embedding_mode == "Create Embeddings":
            db_done = db_obj.create_embeddings(chunk_size, chunk_overlap)

            if db_done:
                st.success("DB Create Successfully!!")

                st.subheader("Start Conversation")

                col1, col2, col3 = st.columns(3)

                # Initialize state for toggling between chat modes
                if "chat_mode" not in st.session_state:
                    st.session_state.chat_mode = ""  # Default mode

                with col1:
                    if st.button("💬 Chat"):  # Text chat button
                        st.session_state.chat_mode = "text"

                with col2:
                    if st.button("🎙️ Voice Input"):  # Voice chat button
                        st.session_state.chat_mode = "voice"

                with col3:
                    if st.button("🔄 Clear"):  # Voice chat button
                        st.session_state.chat_mode = "clear"

                # Todo: Onclick

                # Todo: Chat Column
                # Display the corresponding chat interface based on the selected mode
                if st.session_state.chat_mode == "text":
                    st.write("*Text Chat Interface*")

                    if prompt := st.chat_input("Ask Anything: "):
                        # Store and display the current prompt.
                        st.session_state.messages.append({"role": "user", "content": prompt})

                        input_text, message = rag_obj.run_rag_pipeline(st.session_state.text_chat_history, prompt)

                        st.session_state.text_chat_history.extend(message)

                        # Regular expression to split text before and after the colon
                        match = re.match(r"([^:]+):\s*(.*)", input_text)

                        if match:
                            language = match.group(1)  # Text before the colon
                            result = match.group(2)  # Text after the colon

                            print(f"Language = {language}")
                            print(f"result = {result}")

                            # Add assistant response to chat history
                            st.session_state.messages.append({"role": "assistant", "content": result})

                            # Generate Audio File
                            if language == "English":
                                english_voice_file_path = english_text_to_speech_file(result)
                                st.audio(english_voice_file_path)

                            if language == "Hindi":
                                hindi_voice_file_path = hindi_text_to_speech_file(result)
                                st.audio(hindi_voice_file_path)

                            if language == "Tamil":
                                tamil_voice_file_path = tamil_text_to_speech_file(result)
                                st.audio(tamil_voice_file_path)

                            if language == "Gujarati":
                                gujarati_voice_file_path = gujarati_text_to_speech_file(result)
                                st.audio(gujarati_voice_file_path)
                        else:
                            print("No match found")

                        # Display the existing chat messages via `st.chat_message`.
                        for message in st.session_state.messages:
                            with st.chat_message(message["role"]):
                                st.markdown(message["content"])


                # Todo: Audio File Column
                elif st.session_state.chat_mode == "voice":
                    st.subheader("Voice Recording")

                    # Record Audio
                    audio_file_path = record_voice()
                    print(audio_file_path)

                    if st.button('Run'):
                        # Perform ASR
                        user_input = run_asr()

                        st.success(user_input)

                        # st.write(st.session_state.voice_chat_history)

                        input_text, message = rag_obj.run_rag_pipeline(st.session_state.voice_chat_history, user_input)

                        st.session_state.voice_chat_history.extend(message)

                        # Regular expression to split text before and after the colon
                        match = re.match(r"([^:]+):\s*(.*)", input_text)

                        if match:
                            language = match.group(1)  # Text before the colon
                            result = match.group(2)  # Text after the colon

                            print(f"Language = {language}")
                            print(f"result = {result}")

                            if language == "English":
                                english_voice_file_path = english_text_to_speech_file(result)
                                st.audio(english_voice_file_path)

                            if language == "Hindi":
                                hindi_voice_file_path = hindi_text_to_speech_file(result)
                                st.audio(hindi_voice_file_path)

                            if language == "Tamil":
                                tamil_voice_file_path = tamil_text_to_speech_file(result)
                                st.audio(tamil_voice_file_path)

                            if language == "Gujarati":
                                gujarati_voice_file_path = gujarati_text_to_speech_file(result)
                                st.audio(gujarati_voice_file_path)


                elif st.session_state.chat_mode == "clear":
                    st.session_state.voice_chat_history = []
                    st.session_state.text_chat_history = []
                    st.session_state.messages = []


if __name__ == '__main__':
    main()
