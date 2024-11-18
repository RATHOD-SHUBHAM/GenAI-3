# LanguageLLM-PloyVox

LanguageLLM-PloyVox is an advanced AI-powered application designed to provide seamless audio transcription, document processing, and voice synthesis capabilities. The project integrates multiple cutting-edge technologies including automatic speech recognition (ASR), speech-to-text (STT), voice cloning, and large language models (LLMs). It can operate both locally and in the cloud.

## Features

- **Automatic Speech Recognition (ASR) & Speech-to-Text (STT):**
  - The application captures audio from the user and transcribes it into text using the Whisper model by OpenAI. This allows for highly accurate transcription both locally and in the cloud.

- **Document Processing:**
  - Users can provide a document, which is processed through a retrieval-augmented generation (RAG) pipeline. This involves chunking the document based on user input and storing the resulting embeddings in a database for efficient querying.

- **Voice Cloning & Synthesis:**
  - The application allows for the generation of custom voices with different accents using ElevenLabs' voice cloning APIs, enabling a personalized voice experience for output.

- **Large Language Model (LLM) Integration:**
  - OpenAI’s GPT model is used to enhance user interaction and provide intelligent responses based on the processed documents or transcription input.

## Requirements

To run the application locally, you will need to set up a Python virtual environment and install the necessary dependencies.

### Setup Instructions

1. **Create a Virtual Environment:**
   To create and activate a virtual environment, run the following commands:

   ```
   python3 -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate     # For Windows
   ```

2. **Install Dependencies:** After activating the virtual environment, install the required Python libraries using requirements.txt:
  
  ```
  pip install -r requirements.txt
  ```

3. **Run the Application:** Start the Streamlit application by running the following command:

  ```
  streamlit run app.py
  ```

4. **Usage**:

Once the app is running, you can interact with the user interface to:
  * Record audio for transcription (ASR & STT).
  * Upload documents for chunking and embedding storage.
  * Use the voice cloning feature to generate synthetic voices with custom accents.
  * Query and interact with the stored document embeddings via OpenAI's GPT-based LLM.

5. **Technologies Used**
    * Whisper - OpenAI's ASR model for audio transcription.
    * ElevenLabs API - For voice cloning and accent synthesis.
    * OpenAI GPT - For LLM-based processing and responses.
    * Streamlit - For building the interactive web application.
    * Chroma/Pinecone/FAISS (or similar) - For storing and querying document embeddings.


<img width="1403" alt="Screenshot 2024-11-18 at 1 11 08 PM" src="https://github.com/user-attachments/assets/3600616b-4c6e-4264-ba93-b5edf1c5eb05">
