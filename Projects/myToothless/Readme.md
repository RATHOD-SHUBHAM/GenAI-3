# EchoAI 🎙️✨
Welcome to EchoAI, the next-generation voice-driven AI that listens, understands, and fulfills your requests—all powered by advanced generative AI technologies.

# Overview
EchoAI is designed to take your voice commands and transform them into actions seamlessly. Whether it's setting a reminder, fetching information, or controlling smart devices, EchoAI has you covered. 
This app leverages state-of-the-art AI frameworks and tools to deliver an intuitive and efficient user experience.

# Key Features
  * Voice-Activated Commands: Trigger EchoAI using a custom wake word and speak your request naturally.
  * Automated Speech Recognition (ASR): Powered by OpenAI's Whisper, ensuring accurate voice-to-text conversion.
  * Text-to-Speech (TTS): EchoAI responds in a clear, natural voice, making interaction smooth and engaging.
  * Intelligent Agents: Agents powered by OpenAI's Language Model (LLM) analyze your requests and choose the best tools from a versatile toolkit to fulfill them.
  * Multi-Tool Support: EchoAI’s agents have access to a wide array of tools, ensuring the right solution for every request.
  * Langchain Framework: The backbone of EchoAI, providing a robust and scalable structure for managing complex voice interactions.

# Technology Stack
  * Langchain Framework: For handling complex interactions and integrating various components seamlessly.
  * Porcupine: Used for the wake word detection, making sure EchoAI is always ready to listen.
  * Whisper (OpenAI): For precise and reliable speech recognition.
  * OpenAI LLM: Powers the intelligent agents that process commands and fulfill requests.
  * Text-to-Speech (TTS): Converts the response back to spoken language.

# Getting Started
## Prerequisites
  1. Python 3.10 or later
  2. Required Python packages (listed in requirements.txt)

## Installation
Clone this repository:
```
  $git clone https://github.com/yourusername/myToothless.git
  $cd myToothless
```

## Install the required dependencies:

```
  $pip install -r requirements.txt
```

## Set up your environment variables for OpenAI API keys, Porcupine access keys, etc.
Run the application:
```
  $python main.py
```

# Usage
Once the application is running, Toothless will be in a listening state. Use your designated wake word to activate Toothless and start giving commands.

WakeWord
```
  Toothless
```

# Configuration
You can configure EchoAI to suit your needs by modifying the py file. 
Here, you can customize:
>> Wake word - Change the weights in model file
>> Greeting - Response voice settings
>> Agent behavior and tool preferences

# Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any improvements or feature additions. 
For major changes, please open an issue first to discuss what you would like to change.

# Acknowledgements
Langchain for providing a robust framework.
OpenAI for Whisper and LLM integration.
Porcupine for reliable wake word detection.