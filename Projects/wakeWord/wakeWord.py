import os

import pvporcupine
from pvrecorder import PvRecorder



from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

access_key = os.getenv('access_key')


def fib(N: int) -> int:
    if N <= 1:
        return N

    cache = [0] * (N + 1)
    cache[1] = 1
    for i in range(2, N + 1):
        cache[i] = cache[i - 1] + cache[i - 2]

    return cache[N]


def wake_work():
    keywords = ['Toothless']

    # Initializing
    porcupine = pvporcupine.create(
            access_key=access_key,
            keyword_paths=['toothless_en_mac_v3_0_0/toothless_en_mac_v3_0_0.ppn']
    )

    devices = PvRecorder.get_available_devices()
    print(devices)
    print(devices[-1])



    recoder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)


    try:
        recoder.start()

        while True:
            keyword_index = porcupine.process(recoder.read())
            if keyword_index >= 0:
                print("Hey, Shubham")
                # print(keywords[keyword_index])

                print("Your fibonacci number is: ",fib(6))


    except KeyboardInterrupt:
        recoder.stop()
    finally:
        porcupine.delete()
        recoder.delete()


if __name__ == '__main__':
    wake_work()