# Wake word
import os
import pvporcupine
from pvrecorder import PvRecorder


# Whisper
import time
import whisper

# LLM
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

access_key = os.getenv('access_key')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Todo: Audio Processing ---------------------------------------------------------------------------------------------------


import pyaudio
import wave

def audio_processing():
    # Parameters
    FRAMES_PER_BUFFER = 3200 # play around with this
    FORMAT = pyaudio.paInt16
    CHANNEL = 1
    RATE = 16000

    # Instantiate PyAudio and initialize PortAudio system resources (1)
    p = pyaudio.PyAudio()

    # Open stream
    stream = p.open(
                    format=FORMAT,
                    channels=CHANNEL,
                    rate=RATE,
                    input = True)

    print("* Recording Started")

    # the number of seconds our machine should listen
    seconds = 8
    frames = []
    for i in range(0, int(RATE / FRAMES_PER_BUFFER * seconds)):
        data = stream.read(FRAMES_PER_BUFFER)
        frames.append(data)

    print("* done recording")

    # Close stream (4)
    stream.stop_stream()
    stream.close()

    # Release PortAudio system resources (5)
    p.terminate()


    # Todo: save the frames in wav file

    obj = wave.open('audio/my_recording.wav', mode='wb')


    obj.setnchannels(CHANNEL)
    obj.setsampwidth(p.get_sample_size(FORMAT))
    obj.setframerate(RATE)

    # write this as a binary
    obj.writeframes(b"".join(frames))

    obj.close()

# Todo: ASR ---------------------------------------------------------------------------------------------------

def ASR():
    model = whisper.load_model("base")
    result = model.transcribe("audio/my_recording.wav")
    return result['text']

# Todo: LLM ---------------------------------------------------------------------------------------------------

def LLM_Call(query):

    # Todo: Using an example set
    # create our examples set
    examples = [
        {
            "query": "Don’t turn left here instead take the next right?",
            "answer": "next right."
        },
        {
            "query": "Can you stop behind the vehicle",
            "answer": "Stop."
        },
        {
            "query": "Don’t go straight, instead take the second left?",
            "answer": "Second Left."
        },
        {
                "query": "I feel a little dizzy today, Stop at the nearest coffee shop",
                "answer": "Stop at Coffee Shop."
            },
        {
            "query": "You are running out of fuel, Stop at the nearest gas station",
            "answer": "Stop at Gas Station."
        },
        {
            "query": "I feel like going to Club, Can you go to the nearest club",
            "answer": "Stop at Club."
        },

        {
                "query": "I need to reach early, drive a bit faster",
                "answer": "Increase speed."
            },
        {
            "query": "Stop at coffee shop first and then go the bank",
            "answer": "Coffee Shop and Bank."
        }
    ]

    # Todo: Create a formatter for the few-shot examples
    # create a example template
    example_template = """
    Input: {query}
    AI: {answer}
    """

    # create a prompt example from above template
    example_prompt = PromptTemplate(
        input_variables=["query", "answer"],
        template=example_template
    )


    # Todo: Feed examples and formatter to FewShotPromptTemplate

    # now break our previous prompt into a prefix and suffix
    # the prefix is our instructions
    prefix = """
    Context: [Turn Left, Coffee Shop, Turn Right, Second Left, Stop, increase speed, Decrease Speed, 
    stop at the sign, Don’t Stop, Stop at the next signal, Stop after 5 minutes, Third Left, Third Right.]
    
    Extract the information from the input based on the above context.
    Here are some examples
    """

    # and the suffix our user input and output indicator
    suffix = """
    Input: {query}
    AI: """

    # now create the few shot prompt template
    prompt = FewShotPromptTemplate(
        examples=examples,
        example_prompt=example_prompt,
        prefix=prefix,
        suffix=suffix,
        input_variables=["query"],
        example_separator="\n\n"
    )

    # Query the prompt
    # query = "Dont take left hear, take the third right"
    # query = "Me and my friend want to go clubbing, take me to the nearest club"
    # query = "Road seems super busy, so take the next left"
    query = query
    # print(prompt.format(query=query))

    # Todo: Passing prompt to LLM

    model = ChatOpenAI()

    chain = LLMChain(llm=model, prompt=prompt)

    result = chain.run(query)

    print(result)



# Todo: Wake Word Detection ---------------------------------------------------------------------------------------------------
def wake_work():
    keywords = ['Toothless']

    # Initializing
    porcupine = pvporcupine.create(
            access_key=access_key,
            keyword_paths=['toothless_en_mac_v3_0_0/toothless_en_mac_v3_0_0.ppn']
    )


    recoder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)


    try:
        recoder.start()

        while True:
            keyword_index = porcupine.process(recoder.read())
            if keyword_index >= 0:
                print("Hey, Shubham. How can I help you?")
                # print(keywords[keyword_index])

                # Wait for 1 second and perform audio processing
                time.sleep(1)
                audio_processing()

                print("Audio Ready")

                # Perform ASR
                query = ASR()
                # print(query)
                # print(type(query))

                # LLM - Extract Result.
                extracted_word = LLM_Call(query)



    except KeyboardInterrupt:
        recoder.stop()
    finally:
        porcupine.delete()
        recoder.delete()


if __name__ == '__main__':
    wake_work()