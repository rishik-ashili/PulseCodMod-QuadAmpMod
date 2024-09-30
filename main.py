from PCM import PCM
from QAM import QAM

while True:
        modulation = int(input("Enter the number corresponding to the modulation you want to perform:\n1. Pulse Coded Modulation\n2. Quadrature Amplitude Modulation\n"))

        if modulation == 1:
                PCM()
        elif modulation == 2:
                QAM()
        else:
                print("Invalid number.")