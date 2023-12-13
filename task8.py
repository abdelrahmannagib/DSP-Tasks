signalx = []
signaly = []
from tkinter import filedialog
from tkinter import messagebox
import math


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


def do_task8():
    N= len(signaly)
    S1 = 0
    S2 =0
    Ans=[]
    for i in range(N):
        S1 += (signaly[i]*signaly[i])
        S2 += (filtery[i]*filtery[i])

    F2 = filtery
    Div = (1 / N) * (math.sqrt(S1 * S2))


    for i in range(N):
        sum1 =0
        for j in range(N):
            #print(signaly[i])
            #print(F2[j])
            sum1 += signaly[j]*F2[j]


        sum1*=1/N
        #print(sum1)
        Ans.append(sum1/Div)
        #  Move the first list item to the back
        F2 = F2[1:] + F2[:1]
        #print(Ans[i])'
    from Task8.Point1_Correlation.CompareSignal import Compare_Signals
    test_path="Task8/Point1_Correlation/CorrOutput.txt"
    Compare_Signals(test_path,signalx,Ans)

