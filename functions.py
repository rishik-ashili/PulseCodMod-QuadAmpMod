import sounddevice as sd
import numpy as np
from scipy.io import wavfile
from scipy.io.wavfile import write
import matplotlib.pyplot as plt


def record(record_name, fs, duration):

    print("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    print("Recording finished")

    write(record_name, fs, np.int16(audio * 32767))

    plt.figure(figsize=(15, 5))
    plt.plot(np.linspace(0, duration, len(audio)), audio)
    plt.title("AUDIO WAVEFORM")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.show()

    return audio.flatten()