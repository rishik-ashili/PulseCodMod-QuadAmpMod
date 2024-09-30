import numpy as np
from functions import record
import matplotlib.pyplot as plt


def PCM():
        
        fs = int(input("Enter the sampling frequency in integers (should be >8000):\n"))
        duration = int(input("Enter the duration of recording in integers (in seconds):\n"))

        pcm_message_signal = record(record_name="pcm_message_signal.wav", fs=fs, duration=duration)

        signal_norm = (pcm_message_signal - np.min(pcm_message_signal)) / (np.max(pcm_message_signal) - np.min(pcm_message_signal))

        bits = int(input("Enter the number of bits per symbol:\n"))
        levels = 2**bits

        quantized_signal = np.round(signal_norm * (levels - 1)) / (levels - 1)

        pcm_signal = np.array([np.binary_repr(int(s * (levels - 1)), width=bits) for s in quantized_signal])

        plt.figure(figsize=(15, 15))
        plt.subplot(2, 1, 1)
        plt.plot(quantized_signal, label='Quantized Audio Signal')
        plt.subplot(2, 1, 2)
        plt.plot(pcm_signal, label='PCM Audio Signal')
        plt.legend()
        plt.show()