from tkinter import filedialog
from tkinter import messagebox
import math
import numpy as np

signal1x = []
signal1y = []
x = {}

signal2x = []
signal2y = []
h = {}
def read_signal(flag):
    if flag == "signal":
        signal1x.clear()
        signal1y.clear()
    elif flag == "filter":
        signal2y.clear()
        signal2x.clear()

    file_path = filedialog.askopenfilename()
    if file_path:
        signal_file1 = open(file_path)
        for line in signal_file1:
            component = line.strip().split()
            if len(component) == 2:
                if flag == "signal":
                    signal1x.append(float(component[0]))
                    signal1y.append(float(component[1]))
                    x[int(component[0])] = int(component[1])
                elif flag == "filter":
                    signal2x.append(float(component[0]))
                    signal2y.append(float(component[1]))
                    h[int(component[0])] = int(component[1])

        signal_file1.close()

    else:
        messagebox.showinfo(title="Error", message="can't read such file")

def Dft(Y,i):
    N = len(Y)
    X = np.zeros(N, dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k] += Y[n] * np.exp(-2j * np.pi * k * n / N)
        if i==1:
            X[k]=np.conjugate(X[k])
    # print("harmonic", X, "\n")
    #print(X)
    #amplitude = np.abs(X)
    #phase_shift = np.angle(X)
    #print(X)
    return X
def DoFastCorr():
    signal1yDft= Dft(signal1y,1)
    signal2yDft = Dft(signal2y,2)
    # complex_numbers1 = []
    # complex_numbers2 = []
    complex_numbers3 = []
    N= len(signal2yDft)
    for i in range(N):
        #real_part = amp[i] * np.cos(phase[i])
        # real_part= signal1xDft[i]*np.cos(signal1yDft[i])
        # imag_part = (signal1xDft[i] * np.sin(signal1yDft[i]))
        # complex_numbers1.append(complex(real_part, imag_part))
        # real_part = signal2xDft[i] * np.cos(signal2yDft[i])
        # imag_part = (signal2xDft[i] * np.sin(signal2yDft[i]))*-1
        # complex_numbers2.append(complex(real_part, imag_part))
        complex_numbers3.append((signal1yDft[i]*signal2yDft[i])/N)

    Y = np.zeros(N)
    X = np.zeros(N)
    for n in range(N):
        #print(complex_numbers3[n])
        for k in range(N):
            Y[n] += complex_numbers3[k] * np.exp((2j * np.pi * k * n) / N)
        Y[n] *= 1 / N
        Y[n] = np.round(Y[n], 1)
        X[n] = n
        #Y[n]*= 1/N
        #print(Y[n])
    from task9FastCorr import CompareSignal
    file_name = r'E:\كلية\Dsp\Tasks\DSP Tasks Implementation\task9FastCorr\Corr_Output.txt'
    CompareSignal.Compare_Signals(file_name,X,Y)
