from tkinter import filedialog
from tkinter import messagebox
import math


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

def DoFastCorr():
    print("REad")
