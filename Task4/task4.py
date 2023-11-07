from tkinter import filedialog
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
from Task4 import signalcompare
signal1x = []
signal1y = []

file_path = ""
def read_signal():
    signal1x.clear()
    signal1y.clear()
    file_path = filedialog.askopenfilename()
    if file_path:
        signal_file1 = open(file_path)
        for line in signal_file1:
            component = line.strip().split()
            if len(component) == 2:
                signal1x.append(float(component[0]))
                signal1y.append(float(component[1]))

        signal_file1.close()

    else:
        messagebox.showinfo(title="Error", message="can't read such file")


def dft(fs_ent):
    read_signal()
    fs = int(fs_ent.get())

    N = len(signal1y)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += signal1y[n] * np.exp(-2j * np.pi * k * n / N)

    # print("harmonic", X, "\n")
    amplitude = np.abs(X)
    phase_shift = np.angle(X)
    # print(amplitude)
    # print(phase_shift)

    with open('frequencyDomainComponents.txt', 'w') as file:
        print("0\n1",file=file)
        print(N,  file=file)
        for i in range(N):
            print(amplitude[i], phase_shift[i], file=file)


    # generate fundamental frequency
    fund_freq = fs / N
    freqs = []
    for i in range(N):
        freqs.append(fund_freq * (i + 1))

    test(amplitude, phase_shift)
    plot_dft(amplitude, phase_shift, freqs)


def plot_dft(amplitude, phase_shift, freqs):
    plt.figure(figsize=(8, 6))
    plt.stem(freqs, amplitude, linefmt='-b', markerfmt='ob', basefmt=" ")
    plt.title("Frequency vs. Amplitude [Frequency Domain]")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()

    plt.stem(freqs, phase_shift, linefmt='-b', markerfmt='ob', basefmt=" ")
    plt.title("Frequency vs. Phase Shift [Frequency Domain]")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Phase Shift")
    plt.grid(True)
    plt.show()


def test(amplitude, phase_shift):
    testpath = "Task4/DFT/Output_Signal_DFT_A,Phase.txt"
    file = open(testpath)
    testAmp = []
    testPhase = []
    for line in file:
        component = line.strip().split()
        if len(component) == 2:
            if component[0].endswith('f'):
                component[0] = component[0][:-1]
            if component[1].endswith('f'):
                component[1] = component[1][:-1]

            testAmp.append(float(component[0]))
            testPhase.append(float(component[1]))

    file.close()

    t1 = signalcompare.SignalComapreAmplitude(amplitude, testAmp)
    t2 = signalcompare.SignalComaprePhaseShift(phase_shift, testPhase)
    if t1 and t2:
        print("over all passed !!")


def read_IDFT(amp, phase):
    file_path = filedialog.askopenfilename()
    if file_path:
        file = open(file_path)
        for line in file:
            component = line.strip().split(',')
            if len(component) == 2:
                if component[0].endswith('f'):
                    component[0] = component[0][:-1]
                if component[1].endswith('f'):
                    component[1] = component[1][:-1]

                amp.append(float(component[0]))
                phase.append(float(component[1]))

        file.close()
    else:
        messagebox.showinfo(title="Error", message="can't read such file")



def idft():
    amp = []
    phase = []
    read_IDFT(amp, phase)
    N = len(amp)
    complex_numbers = []

    for i in range(N):
        real_part = amp[i] * np.cos(phase[i])
        imag_part = amp[i] * np.sin(phase[i])
        complex_numbers.append(complex(real_part, imag_part))

    X = np.zeros(N, dtype = complex)
    # change=0
    # if change==1:
    #     ind=3

    #print(complex_numbers[3].imag)
    for n in range(N):
        for k in range(N):
            X[n] += complex_numbers[k] * np.exp((2j * np.pi * k * n) / N)
        X[n]*= 1/N
        X[n]= np.round(X[n],1)
        print(X[n].real)


def modifyIDFT(index, newAmp, newPhase):
