from tkinter import filedialog
from tkinter import messagebox
from Task6.comparesignal2 import SignalSamplesAreEqual
from Task6.Shift_Fold_Signal import Shift_Fold_Signal

import matplotlib.pyplot as plt
import numpy as np
signalx = []
signaly = []

def read_signal():
    signalx.clear()
    signaly.clear()
    file_path = filedialog.askopenfilename()
    if file_path:
        signal_file1 = open(file_path)
        for line in signal_file1:
            component = line.strip().split()
            if len(component) == 2:
                signalx.append(float(component[0]))
                signaly.append(float(component[1]))

        signal_file1.close()

    else:
        messagebox.showinfo(title="Error", message="can't read such file")
    #print(len(signal1y))


def moving_avg(window_size_ent):
    read_signal()
    window_size = int(window_size_ent.get())

    n_size = len(signaly) - window_size + 1
    new_signal = []

    # 2 pointers
    sum = 0
    for i in range(window_size):
        sum += signaly[i]

    new_signal.append(sum / window_size)

    ptr1 = 0
    for i in range(window_size, len(signaly)):
        sum -= signaly[ptr1]
        sum += signaly[i]
        new_signal.append(sum / window_size)
        ptr1 += 1

    reference_result = "F:\Projects Hosted On Githup\main.py\Task6\Moving Average\OutMovAvgTest2.txt"
    SignalSamplesAreEqual(reference_result, new_signal)

def folding_signal():
    read_signal()
    folded = signaly
    folded.reverse()

    reference_path = "F:\Projects Hosted On Githup\main.py\Task6\Shifting and Folding\Output_fold.txt"
    SignalSamplesAreEqual(reference_path, folded)



def delay_advance_folded(ent):
    read_signal()
    steps = int(ent.get())

    new_signal = signaly
    new_signal.reverse()

    new_indices = [x + steps for x in signalx]

    reference_path = "F:\Projects Hosted On Githup\main.py\Task6\Shifting and Folding\Output_ShiftFoldedby-500.txt"
    Shift_Fold_Signal(reference_path, new_indices, new_signal)

