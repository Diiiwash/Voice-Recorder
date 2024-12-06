import sounddevice
from scipy.io.wavfile import write

fs = 44100

Time = int(input("Enter the recording time (In Seconds): "))
print("Recording......\n")

voice_record = sounddevice.rec(int(Time * fs), samplerate = fs, channels=2)
sounddevice.wait()
write("MyRecording.wav",fs,voice_record)
print("Recording is complete. Please check your folder for the records !!!")







