import numpy as np
from scipy.io.wavfile import write
from functions import record
import matplotlib.pyplot as plt


def QAM():

        fs = int(input("Enter the sampling frequency in integers (should be >8000):\n"))
        duration = int(input("Enter the duration of recording in integers (in seconds):\n"))

        print("Initiating recording I-channel.")
        I_channel = record(record_name="I_channel.wav", fs=fs, duration=duration)

        print("Initiating recording Q-channel.")
        Q_channel = record(record_name="Q_channel.wav", fs=fs, duration=duration)

        fc = int(input("Enter the carrier frequency:\n"))

        t = np.arange(len(I_channel)) / fs

        I_modulated = I_channel * np.cos(2 * np.pi * fc * t)
        Q_modulated = Q_channel * np.sin(2 * np.pi * fc * t)
        QAM = I_modulated + Q_modulated

        plt.figure(figsize=(15, 50))
        plt.subplot(3, 1, 1)
        plt.plot(np.linspace(0, duration, len(I_modulated)), I_modulated, color="red")
        plt.title('I MODULATED')
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.legend()
        plt.grid()
        plt.subplot(3, 1, 2)
        plt.plot(np.linspace(0, duration, len(Q_modulated)), Q_modulated, color="blue")
        plt.title('Q MODULATED')
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.legend()
        plt.grid()
        plt.subplot(3, 1, 3)
        plt.plot(np.linspace(0, duration, len(QAM)), QAM, color="green")
        plt.title('QAM MODULATED')
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.legend()
        plt.grid()
        plt.show()

        QAM_normalized = QAM / np.max(np.abs(QAM)) * 32767
        write("QAM.wav", fs, np.int16(QAM_normalized))

        I_demodulated = QAM * np.cos(2 * np.pi * fc * t)
        Q_demodulated = QAM * np.sin(2 * np.pi * fc * t)

        I_demodulated_normalized = I_demodulated / np.max(np.abs(I_demodulated)) * 32767
        Q_demodulated_normalized = Q_demodulated / np.max(np.abs(Q_demodulated)) * 32767

        write("I_demodulated.wav", fs, np.int16(I_demodulated_normalized))
        write("Q_demodulated.wav", fs, np.int16(Q_demodulated_normalized))