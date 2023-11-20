from tkinter import filedialog
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

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
    #print(len(signal1y))

def dct(m):
    read_signal()
    m = int(m.get())

    N = len(signal1y)
    X = np.zeros(N)
    for k in range(N):
        for n in range(N):
            X[k] += signal1y[n]*(np.cos((np.pi/(4*N))*(2*n-1)*(2*k-1)))
        X[k]*= np.sqrt(2/N)
    # print("harmonic", X, "\n")


    with open('T5_DCT_Done.txt', 'w') as file:
        print("0\n1",file=file)
        print(N,  file=file)
        for i in range(m):
            print(0, X[i], file=file)

def remove_dc():
    read_signal()
    N = len(signal1y)
    Avg= np.average(signal1y)
    with open('T5_Delete.txt', 'w') as file:
        print("0\n1",file=file)
        print(N,  file=file)
        for i in range(N):
            print(i,signal1y[i]-Avg , file=file)
