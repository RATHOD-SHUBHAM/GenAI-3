# Todo 1: Wake Word

# Todo 2: Respond back with a greeting
'''
    1. Respond back to the user.
    2. Play the Audio
'''

# Todo 3: Take user input and perform audio to speech
'''
    1. Record User Command.
    2. Perform Audio To Speech
'''


# Todo 4: Use the user command from ASR to invoke agent

# Todo 5: Respond back to the user with answer
'''
    1. Respond back to the user.
    2. Play the Audio
'''


from Project.src.wakeword import WakeWord
from Project.src.greetings import Greeting
if __name__ == '__main__':
    greeting_obj = Greeting()
    greeting_obj.greet()
    obj = WakeWord()
    obj.wake_work()