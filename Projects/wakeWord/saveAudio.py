'''

    Audio file format
    1] .mp3 - Famous but may lose information during compression.
    2] .flac - Compress data - but also reconstructs data
    3] .wav - Uncompressed format. :
    Audio quality is the best - but file size is largest among all

    Waveform Audio “WAVE” (or “WAV”) file format
'''

'''
    :parameters
    1. Number of channels: 
        1 - mono, 2- stereo
        Mono has one channel
        Stereo has 2 independent channel
        This will give an impression that sound is coming from 2 different directions
    
    2. Sample width:
        Number of bytes per sample
    
    3. Frame rate / sample rate / Sample Frequency :
        The number of samples for each second
        
        eg : 44,100 HZ
        this is 44,100 sample value in each second
    
    4. Number of Frames: 
        Total number of frames we get
        
    5. Value of Frames:
        This will be a binary
        
'''
import pyaudio
import wave

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
seconds = 5
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
