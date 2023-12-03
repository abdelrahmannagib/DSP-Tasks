signalx = []
signaly = []
from tkinter import filedialog
from tkinter import messagebox
from Task7.ConvTest import ConvTest

signalx = []
signaly = []
x = {}

filterx = []
filtery = []
h = {}
def read_signal(flag):
    if flag == "signal":
        signalx.clear()
        signaly.clear()
    elif flag == "filter":
        filtery.clear()
        filterx.clear()

    file_path = filedialog.askopenfilename()
    if file_path:
        signal_file1 = open(file_path)
        for line in signal_file1:
            component = line.strip().split()
            if len(component) == 2:
                if flag == "signal":
                    signalx.append(float(component[0]))
                    signaly.append(float(component[1]))
                    x[int(component[0])] = int(component[1])
                elif flag == "filter":
                    filterx.append(float(component[0]))
                    filtery.append(float(component[1]))
                    h[int(component[0])] = int(component[1])

        signal_file1.close()

    else:
        messagebox.showinfo(title="Error", message="can't read such file")

def convolv():
    mn_index = int(signalx[0] + filterx[0])
    mx_index = int(signalx[-1] + filterx[-1])
    indeces = list(range(mn_index, mx_index+1))
    result = []

    counter = 1
    for n in indeces:
        k = signalx[0]

        tmpAns = 0
        innerCounter = min(counter, len(signalx))
        while innerCounter:
            index2 = n - k
            secondVal = 0
            if index2 in h:
                secondVal = h[index2]

            tmpAns += x[k] * secondVal
            k += 1
            innerCounter -= 1

        result.append(tmpAns)
        counter += 1

    ConvTest(indeces, result)

