import numpy as np
def task3_work(no_levels):
    no_levels = float(no_levels.get())
    signal1x = []
    signal1y = []
    try:
        signal_file1 = open("task3/Test 1/Quan1_input.txt", "r")

        for line in signal_file1:
            component = line.strip().split()
            if len(component) == 2:
                signal1x.append(float(component[0]))
                signal1y.append(float(component[1]))

        signal_file1.close()
    except Exception as e:
        messagebox.showerror(title="Error", message="Failed to read the signal file: \n" + str(e))

    Min= np.min(signal1y)
    Max = np.max(signal1y)
    delta= (Max-Min)/no_levels
    ranges1= np.arange(Min, Max+delta, delta)
    ranges1=(ranges1[1:] +ranges1[:-1]) / 2
    for x in ranges1:
        print(x)

    return 0