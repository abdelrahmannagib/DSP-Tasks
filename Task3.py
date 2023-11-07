import math
from QuanTest1 import  *
from QuanTest2 import  *
import numpy as np
from tkinter import filedialog
from tkinter import messagebox
from decimal import Decimal
signal1x = []
signal1y = []
signal_file1 = 0

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

encoding = []

def encoding_algorithm(levels_num, n_bits):
    for i in range(0, levels_num):
        # Convert the integer to binary string and remove the '0b' prefix
        binary_str = bin(i)[2:]

        # Calculate the number of bits to pad
        padding = max(0, int(n_bits) - len(binary_str))

        # Create the binary representation with the specified number of bits
        binary_representation = '0' * padding + binary_str
        encoding.append(binary_representation)




def task3_work(no_level, no_bit):
    lvls = 0
    bits = 0
    if not no_level.get():
        bits = int(no_bit.get())
        lvls = pow(2, bits)

    if not no_bit.get():
        lvls = int(no_level.get())
        bits = math.ceil(np.log(lvls) / np.log(2))

    encoding_algorithm(lvls, bits)
    mn = np.min(signal1y)
    mx = np.max(signal1y)

    delta = (mx - mn) / lvls


    ranges = []
    interval_index = {}
    mid_points = []
    last_val = mn
    for i in range(0, int(lvls)):
        b = round(last_val + delta, 3)
        ranges.append((last_val, b))
        last_val = round ( last_val + delta, 3)

    index = 0
    mid_mapping = {}
    for item in ranges:
        mid = round((item[1] + item[0]) / 2, 3)
        mid_points.append(mid)

        mid_mapping[mid] = encoding[index]
        interval_index[mid] = index + 1
        index += 1

    # quantize
    final_mapping = []
    encod = []
    quantized_signal = []

    indces = []
    error = []
    for amp in signal1y:
        index = 0
        for comp in ranges:
            if amp >= comp[0] and amp <= comp[1]:
                mid = mid_points[index]
                mapping = mid_mapping[mid]
                final_mapping.append((mapping, mid))
                encod.append(mapping)
                quantized_signal.append(mid)
                print(str(index + 1) + " " +str(mapping) + " " +str(mid) +" " + str(round(mid - amp, 3)))
                indces.append(index + 1)
                error.append(round(mid - amp, 3))
                break
            index += 1


    QuantizationTest1("Quan1_Out.txt", encod, quantized_signal)
    QuantizationTest2("Quan2_Out.txt", indces, encod, quantized_signal, error)

    return