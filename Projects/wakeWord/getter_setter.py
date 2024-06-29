# Understanding Getter and Setter with wav file

import wave

# Todo: Getter Example

obj = wave.open('audio/dummy.wav', mode='rb')

print("Number of channel: ", obj.getnchannels())
print("Sample Width: ", obj.getsampwidth())
print("Frame Rate: ", obj.getframerate())
print("Number of Frame: ", obj.getnframes())
print("Parameters: ", obj.getparams())

# todo: Calculate the time for audio
# We can use frame rate and number of sample for this

t_audio = obj.getnframes() / obj.getframerate()
print("Time in seconds: ",t_audio)

# todo: Get the frames
frames = obj.readframes(-1) # -1 to read all frames

print("Number of frames for all sample: ",len(frames)) # this is for both the sample
# our sample width is 2

print("Number of actual frames for all sample: ",len(frames) / 2)
# this will be equal to the number of frames

obj.close()

# Todo: Setter Example

obj_new = wave.open('audio/dummy_dup.wav', mode='wb')


obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(44100)


obj_new.writeframes(frames)

obj_new.close()
