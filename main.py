# imports
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter import IntVar
import numpy as np
import Task3
import Task5.Task5
import Task6.Task6
from Task6 import *

from Task4 import task4
from Task5 import *
# Load GUI
root = Tk()
root.geometry("400x400")
root.title("DSP")


home_page = Frame(root)
task1page = Frame(root)
task1generate_signal_page = Frame(root)
task2page = Frame(root)
task3page = Frame(root)
task4page = Frame(root)
task5page = Frame(root)
task6page = Frame(root)

btn_font = font.Font(size=15)
lbl_font = font.Font(size=25)


x = []
y = []


def pages_initializer():
    home_page.grid(row=0, column=0, sticky="nsew")
    task1page.grid(row=0, column=0, sticky="nsew")
    task1generate_signal_page.grid(row=0, column=0, sticky="nsew")
    task2page.grid(row=0, column=0, sticky="nsew")
    task3page.grid(row=0, column=0, sticky="nsew")
    task4page.grid(row=0, column=0, sticky="nsew")
    task5page.grid(row=0, column=0, sticky="nsew")
    task6page.grid(row=0, column=0, sticky="nsew")


def home_page_gui():
    home_page_lbl = Label(home_page, text="Home Page", font=lbl_font)
    home_page_lbl.pack()
    task1btn = Button(home_page, text="Task 1", command=lambda: task1page.tkraise(), font=btn_font)
    task1btn.pack()
    task2btn = Button(home_page, text="Task 2", command=lambda: task2page.tkraise(), font=btn_font)
    task2btn.pack()
    task3btn = Button(home_page, text="Task 3", command=lambda: task3page.tkraise(), font=btn_font)
    task3btn.pack()
    task4btn = Button(home_page, text="Task 4", command=lambda: task4page.tkraise(), font=btn_font)
    task4btn.pack()
    task5btn = Button(home_page, text="Task 5", command=lambda: task5page.tkraise(), font=btn_font)
    task5btn.pack()
    task6btn = Button(home_page, text="Task 6", command=lambda: task6page.tkraise(), font=btn_font)
    task6btn.pack()

def read_signal():
    try:
        signal_file = open("signal1.txt", "r")

        for line in signal_file:
            component = line.strip().split()
            if len(component) == 2:
                x.append(float(component[0]))
                y.append(float(component[1]))

        signal_file.close()
        messagebox.showinfo(title="Message", message="Signal is Read Successfully")

    except Exception as e:
        messagebox.showerror(title="Error", message="Failed to read the signal file: \n" + str(e))


def task2_add():
    signal1x=[]
    signal1y=[]
    signal2x=[]
    signal2y=[]
    signal3x = []
    signal3y = []
    try:
        signal_file1 = open("task2/Signal1.txt", "r")
        signal_file2 = open("task2/Signal2.txt", "r")
        signal_file3 = open("task2/signal3.txt", "r")

        for line in signal_file1:
            component = line.strip().split()
            if len(component) == 2:
                signal1x.append(float(component[0]))
                signal1y.append(float(component[1]))

        signal_file1.close()

        #messagebox.showinfo(title="Message", message="Signal1and2_task2 is Read Successfully")
        for line in signal_file2:
            component = line.strip().split()
            if len(component) == 2:
                signal2x.append(float(component[0]))
                signal2y.append(float(component[1]))

        signal_file2.close()
        #messagebox.showinfo(title="Message", message="Signal1and2_task2 is Read Successfully")
        for line in signal_file3:
            component = line.strip().split()
            if len(component) == 2:
                signal3x.append(float(component[0]))
                signal3y.append(float(component[1]))

        signal_file2.close()

    except Exception as e:
        messagebox.showerror(title="Error", message="Failed to read the signal file: \n" + str(e))
    sig1_add_sig2= np.add(signal1y,signal2y)
    plt.figure(figsize=(8, 4))
    plt.scatter(signal1x, sig1_add_sig2, label='Discrete Data', color='red', marker='o')
    plt.title('add 1 and 2')
    plt.show()
    ## add 1+3
    sig1_add_sig3 = np.add(signal1y, signal3y)
    plt.figure(figsize=(8, 4))
    plt.scatter(signal1x, sig1_add_sig3, label='Discrete Data', color='red', marker='o')
    plt.title('add 1 and 3')
    plt.show()

def task2_subtract():
    signal1x=[]
    signal1y=[]
    signal2x=[]
    signal2y=[]
    signal3x = []
    signal3y = []
    try:
        signal_file1 = open("task2/Signal1.txt", "r")
        signal_file2 = open("task2/Signal2.txt", "r")
        signal_file3 = open("task2/signal3.txt", "r")

        for line in signal_file1:
            component = line.strip().split()
            if len(component) == 2:
                signal1x.append(float(component[0]))
                signal1y.append(float(component[1]))

        signal_file1.close()

        #messagebox.showinfo(title="Message", message="Signal1and2_task2 is Read Successfully")
        for line in signal_file2:
            component = line.strip().split()
            if len(component) == 2:
                signal2x.append(float(component[0]))
                signal2y.append(float(component[1]))

        signal_file2.close()
        #messagebox.showinfo(title="Message", message="Signal1and2_task2 is Read Successfully")
        for line in signal_file3:
            component = line.strip().split()
            if len(component) == 2:
                signal3x.append(float(component[0]))
                signal3y.append(float(component[1]))

        signal_file3.close()

    except Exception as e:
        messagebox.showerror(title="Error", message="Failed to read the signal file: \n" + str(e))
    sig1_subtract_sig2= np.subtract(signal2y,signal1y)
    plt.figure(figsize=(8, 4))
    plt.scatter(signal1x, sig1_subtract_sig2, label='Discrete Data', color='red', marker='o')
    plt.title('add 1 and 2')
    plt.show()
    ## add 1+3
    sig1_subtract_sig3 = np.subtract(signal3y, signal1y)
    plt.figure(figsize=(8, 4))
    plt.scatter(signal1x, sig1_subtract_sig3, label='Discrete Data', color='red', marker='o')
    plt.title('add 1 and 3')
    plt.show()

def task2_multilply(cons):
    signal1x = []
    signal1y = []
    signal2x = []
    signal2y = []
    signal3x = []
    signal3y = []
    cons = float(cons.get())
    try:
        signal_file1 = open("task2/Signal1.txt", "r")
        signal_file2 = open("task2/Signal2.txt", "r")
        signal_file3 = open("task2/signal3.txt", "r")

        for line in signal_file1:
            component = line.strip().split()
            if len(component) == 2:
                signal1x.append(float(component[0]))
                signal1y.append(float(component[1]))

        signal_file1.close()

        # messagebox.showinfo(title="Message", message="Signal1and2_task2 is Read Successfully")
        for line in signal_file2:
            component = line.strip().split()
            if len(component) == 2:
                signal2x.append(float(component[0]))
                signal2y.append(float(component[1]))

        signal_file2.close()
        # messagebox.showinfo(title="Message", message="Signal1and2_task2 is Read Successfully")
        for line in signal_file3:
            component = line.strip().split()
            if len(component) == 2:
                signal3x.append(float(component[0]))
                signal3y.append(float(component[1]))

        signal_file3.close()

    except Exception as e:
        messagebox.showerror(title="Error", message="Failed to read the signal file: \n" + str(e))
    multiply_by_cons =np.array(signal1y)*cons
    plt.figure(figsize=(8, 4))
    plt.scatter(signal1x, multiply_by_cons, label='Discrete Data', color='red', marker='o')
    plt.title('Multiply Signal 1')
    plt.show()
    multiply_by_cons = np.array(signal2y) * cons
    plt.figure(figsize=(8, 4))
    plt.scatter(signal2x, multiply_by_cons, label='Discrete Data', color='red', marker='o')
    plt.title('Multiply Signal 2')
    plt.show()

def task2_squaring():
    signal1x = []
    signal1y = []
    signal2x = []
    signal2y = []
    signal3x = []
    signal3y = []
    try:
        signal_file1 = open("task2/Signal1.txt", "r")
        signal_file2 = open("task2/Signal2.txt", "r")
        signal_file3 = open("task2/signal3.txt", "r")

        for line in signal_file1:
            component = line.strip().split()
            if len(component) == 2:
                signal1x.append(float(component[0]))
                signal1y.append(float(component[1]))

        signal_file1.close()

        # messagebox.showinfo(title="Message", message="Signal1and2_task2 is Read Successfully")
        for line in signal_file2:
            component = line.strip().split()
            if len(component) == 2:
                signal2x.append(float(component[0]))
                signal2y.append(float(component[1]))

        signal_file2.close()
        # messagebox.showinfo(title="Message", message="Signal1and2_task2 is Read Successfully")
        for line in signal_file3:
            component = line.strip().split()
            if len(component) == 2:
                signal3x.append(float(component[0]))
                signal3y.append(float(component[1]))

        signal_file3.close()

    except Exception as e:
        messagebox.showerror(title="Error", message="Failed to read the signal file: \n" + str(e))
    multiply_by_cons =np.array(signal1y)*np.array(signal1y)
    plt.figure(figsize=(8, 4))
    plt.scatter(signal1x, multiply_by_cons, label='Discrete Data', color='red', marker='o')
    plt.title('Squaring signal 1')
    plt.show()

def task2_shifting(cons):
    signal1x = []
    signal1y = []
    signal2x = []
    signal2y = []
    signal3x = []
    signal3y = []
    cons = float(cons.get())
    try:
        signal_file1 = open("task2/Input Shifting.txt", "r")
        signal_file2 = open("task2/Signal2.txt", "r")
        signal_file3 = open("task2/signal3.txt", "r")

        for line in signal_file1:
            component = line.strip().split()
            if len(component) == 2:
                signal1x.append(float(component[0]))
                signal1y.append(float(component[1]))

        signal_file1.close()

        # messagebox.showinfo(title="Message", message="Signal1and2_task2 is Read Successfully")
        for line in signal_file2:
            component = line.strip().split()
            if len(component) == 2:
                signal2x.append(float(component[0]))
                signal2y.append(float(component[1]))

        signal_file2.close()
        # messagebox.showinfo(title="Message", message="Signal1and2_task2 is Read Successfully")
        for line in signal_file3:
            component = line.strip().split()
            if len(component) == 2:
                signal3x.append(float(component[0]))
                signal3y.append(float(component[1]))

        signal_file3.close()

    except Exception as e:
        messagebox.showerror(title="Error", message="Failed to read the signal file: \n" + str(e))
    shiftx =np.array(signal1x)-cons
    plt.figure(figsize=(8, 4))
    plt.scatter(shiftx, signal1y, label='Discrete Data', color='red', marker='o')
    plt.title('Multiply Signal 1')
    plt.show()

def task2_normalize(cons1,cons2):
    signal1x = []
    signal1y = []
    signal2x = []
    signal2y = []
    signal3x = []
    signal3y = []
    cons1 = float(cons1.get())
    cons2 = float(cons2.get())

    try:
        signal_file1 = open("task2/Signal1.txt", "r")
        signal_file2 = open("task2/Signal2.txt", "r")
        signal_file3 = open("task2/signal3.txt", "r")

        for line in signal_file1:
            component = line.strip().split()
            if len(component) == 2:
                signal1x.append(float(component[0]))
                signal1y.append(float(component[1]))

        signal_file1.close()

        # messagebox.showinfo(title="Message", message="Signal1and2_task2 is Read Successfully")
        for line in signal_file2:
            component = line.strip().split()
            if len(component) == 2:
                signal2x.append(float(component[0]))
                signal2y.append(float(component[1]))

        signal_file2.close()
        # messagebox.showinfo(title="Message", message="Signal1and2_task2 is Read Successfully")
        for line in signal_file3:
            component = line.strip().split()
            if len(component) == 2:
                signal3x.append(float(component[0]))
                signal3y.append(float(component[1]))

        signal_file3.close()

    except Exception as e:
        messagebox.showerror(title="Error", message="Failed to read the signal file: \n" + str(e))
    ## (x-min)/(max-min)
    ## * (b-a)+a
    #shiftx =np.array(signal1x)+cons
    st1= (np.array(signal1y)-np.min(signal1y))/(np.max(signal1y)-np.min(signal1y))
    signal1y_after= st1* (cons2-cons1)+cons1
    plt.figure(figsize=(8, 4))
    plt.scatter(signal1x, signal1y_after, label='signal 1', color='red', marker='o')
    plt.title('signal 1')
    plt.show()

    st2 = (np.array(signal2y) - np.min(signal2y)) / (np.max(signal2y) - np.min(signal2y))
    signal2y_after = st2 * (cons2 - cons1) + cons1
    plt.figure(figsize=(8, 4))
    plt.scatter(signal2x, signal2y_after, label='signal 2', color='red', marker='o')
    plt.title('signal 2')
    plt.show()

def task2_accum():
    signal1x = []
    signal1y = []
    signal2x = []
    signal2y = []
    signal3x = []
    signal3y = []


    try:
        signal_file1 = open("task2/Signal1.txt", "r")
        signal_file2 = open("task2/Signal2.txt", "r")
        signal_file3 = open("task2/signal3.txt", "r")

        for line in signal_file1:
            component = line.strip().split()
            if len(component) == 2:
                signal1x.append(float(component[0]))
                signal1y.append(float(component[1]))

        signal_file1.close()

        # messagebox.showinfo(title="Message", message="Signal1and2_task2 is Read Successfully")
        for line in signal_file2:
            component = line.strip().split()
            if len(component) == 2:
                signal2x.append(float(component[0]))
                signal2y.append(float(component[1]))

        signal_file2.close()
        # messagebox.showinfo(title="Message", message="Signal1and2_task2 is Read Successfully")
        for line in signal_file3:
            component = line.strip().split()
            if len(component) == 2:
                signal3x.append(float(component[0]))
                signal3y.append(float(component[1]))

        signal_file3.close()

    except Exception as e:
        messagebox.showerror(title="Error", message="Failed to read the signal file: \n" + str(e))
    ## (x-min)/(max-min)
    ## * (b-a)+a
    #shiftx =np.array(signal1x)+cons
    signal1y_after= np.add.accumulate(signal1y)
    plt.figure(figsize=(8, 4))
    plt.scatter(signal1x, signal1y_after, label='signal 1', color='red', marker='o')
    plt.title('signal 1')
    plt.show()


def display_discrete_signal(x,y):
    # Display Discrete Signal
    plt.figure(figsize=(8, 4))
    plt.scatter(x, y,  label='Discrete Data', color='red', marker='o')
    plt.title('Discrete Signal')
    plt.show()


def display_continues_signal(x,y):
    # Display Continues Signal
    plt.figure(figsize=(8, 4))
    plt.plot(x, y, label='Continuous Data', color='red', marker='o')
    plt.title('Continues Signal')
    plt.show()


def task1page_gui():
    task1lbl = Label(task1page, text="Task 1", font=lbl_font)
    task1lbl.pack()

    read_signal_btn = Button(task1page, text="Read Signal", command=read_signal, font=btn_font)
    read_signal_btn.pack()

    display_discrete_signal_btn = Button(task1page, text="Display Discrete Signal", command=lambda:display_discrete_signal(x,y), font=btn_font)
    display_discrete_signal_btn.pack()

    display_continues_signal_btn = Button(task1page, text="Display Continues Signal", command=lambda:display_continues_signal(x,y), font=btn_font)
    display_continues_signal_btn.pack()

    generate_signal_btn = Button(task1page, text="Generate Signal",  command=lambda:task1generate_signal_page.tkraise(), font=btn_font)
    generate_signal_btn.pack()

    home_page_btn = Button(task1page, text="Home Page", command=lambda: home_page.tkraise(), font=btn_font)
    home_page_btn.pack()

def task2page_gui():
    task2lbl = Label(task2page, text="Task 2", font=lbl_font)
    task2lbl.pack()
    ## add 1 2 , 1,3
    read_signal_btn1 = Button(task2page, text="add 1+2 then add 1+3", command=task2_add, font=btn_font)
    read_signal_btn1.pack()
    # subtract
    read_signal_btn2 = Button(task2page, text="subtract 1+2 then subtact 1+3", command=task2_subtract, font=btn_font)
    read_signal_btn2.pack()
    #multiply by cons
    cons = Label(task2page, text="Amplitude")
    cons.pack()
    cons_ent = Entry(task2page)
    cons_ent.pack()

    read_signal_btn3 = Button(task2page, text="Multiply signal 1 and 2", command=lambda :task2_multilply(cons_ent), font=btn_font)
    read_signal_btn3.pack()

    read_signal_btn4 = Button(task2page, text="Squaing signal 1", command=task2_squaring, font=btn_font)
    read_signal_btn4.pack()

    cons2 = Label(task2page, text="Shift")
    cons2.pack()
    cons_ent2 = Entry(task2page)
    cons_ent2.pack()

    read_signal_btn5 = Button(task2page, text="Shift signal 1", command=lambda: task2_shifting(cons_ent2),
                              font=btn_font)
    read_signal_btn5.pack()

    ## Normalize
    cons3 = Label(task2page, text="a")
    cons3.pack()
    cons_ent3 = Entry(task2page)
    cons_ent3.pack()

    cons4 = Label(task2page, text="b")
    cons4.pack()
    cons_ent4 = Entry(task2page)
    cons_ent4.pack()

    read_signal_btn6 = Button(task2page, text="Normalize", command=lambda: task2_normalize(cons_ent3,cons_ent4),
                              font=btn_font)
    read_signal_btn6.pack()
    ## acc
    read_signal_btn7 = Button(task2page, text="Accumlate", command=lambda: task2_accum(),
                              font=btn_font)
    read_signal_btn7.pack()

    home_page_btn = Button(task2page, text="Home Page", command=lambda: home_page.tkraise(), font=btn_font)
    home_page_btn.pack()

def task3page_gui():
    cons2 = Label(task3page, text="Levels Number ?")
    cons2.pack()
    cons_ent2 = Entry(task3page)
    cons_ent2.pack()

    cons3 = Label(task3page, text="Number of Bits ?")
    cons3.pack()
    cons_ent3 = Entry(task3page)
    cons_ent3.pack()

    read_signal_btn = Button(task3page, text="Read Signal", command=Task3.read_signal, font=btn_font)
    read_signal_btn.pack()

    read_signal_btn5 = Button(task3page, text="Do Work", command=lambda: Task3.task3_work(cons_ent2, cons_ent3), font=btn_font)
    read_signal_btn5.pack()

    home_page_btn = Button(task3page, text="Home Page", command=lambda: home_page.tkraise(), font=btn_font)
    home_page_btn.pack()

def task4page_gui():
    fs_lbl = Label(task4page, text="Fs")
    fs_lbl.pack()
    fs_ent = Entry(task4page)
    fs_ent.pack()

    dft_btn = Button(task4page, text="DFT", command=lambda:task4.dft(fs_ent), font=btn_font)
    dft_btn.pack()

    # idft_btn = Button(task4page, text="IDFT", command=task4.idft, font=btn_font)
    # idft_btn.pack()

    home_page_btn = Button(task4page, text="Home Page", command=lambda: home_page.tkraise(), font=btn_font)
    home_page_btn.pack()



    modification_lbl = Label(task4page, text="Modify Amplitude and Phase Shift")
    modification_lbl.pack()

    index_lbl = Label(task4page, text="index")
    index_lbl.pack()

    index_ent = Entry(task4page)
    index_ent.pack()

    newAmp_lbl = Label(task4page, text="New Amplitude")
    newAmp_lbl.pack()

    newAmp_ent = Entry(task4page)
    newAmp_ent.pack()

    newphase_lbl = Label(task4page, text="New phase")
    newphase_lbl.pack()

    newphase_ent = Entry(task4page)
    newphase_ent.pack()

    modify_btn = Button(task4page, text="Idft", command=lambda:task4.idft(index_ent,newAmp_ent,newphase_ent) , font=btn_font)
    modify_btn.pack()
def task5page_gui():
    cons55 = Label(task5page, text="Choose coff")
    cons55.pack()
    cons_ent55 = Entry(task5page)
    cons_ent55.pack()

    Dct_btn = Button(task5page, text="Compute Dct", command=lambda: Task5.dct(cons_ent55), font=btn_font)
    Dct_btn.pack()

    Remove_Btn = Button(task5page, text="Remove Dct", command=lambda: Task5.remove_dc(), font=btn_font)
    Remove_Btn.pack()

    home_page_btn = Button(task5page, text="Home Page", command=lambda: home_page.tkraise(), font=btn_font)
    home_page_btn.pack()

def task6page_gui():
    ws_lbl = Label(task6page, text="Window Size")
    ws_lbl.pack()
    ws_ent = Entry(task6page)
    ws_ent.pack()

    # read_signal_btn = Button(task6page, text="Read Signal", command=Task6.read_signal, font=btn_font)
    # read_signal_btn.pack()

    moving_avg_btn = Button(task6page, text="Moving Average", command=lambda: Task6.moving_avg(ws_ent), font=btn_font)
    moving_avg_btn.pack()

    space_label = Label(task6page, text="", height=1)
    space_label.pack()

    folding_btn = Button(task6page, text="Folding Signal", command=Task6.folding_signal, font=btn_font)
    folding_btn.pack()

    space_label = Label(task6page, text="", height=1)
    space_label.pack()

    steps_lbl = Label(task6page, text="Steps")
    steps_lbl.pack()
    steps_ent = Entry(task6page)
    steps_ent.pack()

    delay_advance_btn = Button(task6page, text="Delay/Advance Folded Signal", command=lambda:Task6.delay_advance_folded(steps_ent), font=btn_font)
    delay_advance_btn.pack()

    space_label = Label(task6page, text="", height=1)
    space_label.pack()

    from Task6.Derivative_Updated import DerivativeSignal

    Drev_btn = Button(task6page, text="Drev", command=lambda: DerivativeSignal.DerivativeSignal(), font=btn_font)
    Drev_btn.pack()

    home_page_btn = Button(task6page, text="Home Page", command=lambda: home_page.tkraise(), font=btn_font)
    home_page_btn.pack()
def generate_signal(selected_function, amplitude_entry, phase_shift_entry, analog_frequency_entry, sampling_frequency_entry):
    selected_function = selected_function.get()
    amplitude = float(amplitude_entry.get())
    phase_shift = float(phase_shift_entry.get())
    analog_frequency = float(analog_frequency_entry.get())
    sampling_frequency = float(sampling_frequency_entry.get())

    if sampling_frequency < 2 * analog_frequency:
        messagebox.showinfo(title="Error", message=f'Error: sampling frequancy should be greater than or equal to {2 * analog_frequency}')
        return


    # time_values = np.linspace(0, 1.0, sampling_frequency)
    time_values = np.arange(0, sampling_frequency)
    mp = {1: "Sin", 2: "Cos"}

    if selected_function == 1:  # sin wave
        signal = amplitude * np.sin(2 * np.pi * analog_frequency / sampling_frequency * time_values + phase_shift)

    elif selected_function == 2:  # cos wave
        signal = amplitude * np.cos(2 * np.pi * analog_frequency / sampling_frequency * time_values + phase_shift)

    with open(f'{mp[selected_function]}wave.txt', "w") as file:
        file.write("0\n0\n")
        file.write(str(sampling_frequency) + "\n")
        for i in range(int(sampling_frequency)):
            file.write(f"{i} {signal[i]}\n")

    file.close()

    # Test
    from comparesignals import SignalSamplesAreEqual
    response = SignalSamplesAreEqual(f'{mp[selected_function]}Output.txt', time_values, samples=signal)
    if response == 1:
        messagebox.showinfo(title="Message", message="Signal is generated successfully")

    # else:
    #     messagebox.showinfo(title="Error", message="Error in generating signal")

    display_discrete_signal(time_values, signal)
    display_continues_signal(time_values, signal)


def task1generate_signal_page_gui():
    generate_signal_lbl = Label(task1generate_signal_page, text="Generate Signal", font=lbl_font)
    generate_signal_lbl.pack()

    # Signal Type
    sin_cos_lbl = Label(task1generate_signal_page, text="Signal Type")
    sin_cos_lbl.pack()

    selected_function = IntVar()
    sine_radio = Radiobutton(task1generate_signal_page, text="Sine", variable=selected_function, value=1)
    sine_radio.pack()
    cosine_radio = Radiobutton(task1generate_signal_page, text="Cosine", variable=selected_function, value=2)
    cosine_radio.pack()

    # Amplitude
    amplitude_lbl = Label(task1generate_signal_page, text="Amplitude")
    amplitude_lbl.pack()
    amplitude_entry = Entry(task1generate_signal_page)
    amplitude_entry.pack()

    # Phase Shift Theta
    phase_shift_lbl = Label(task1generate_signal_page, text="Phase Shift Theta")
    phase_shift_lbl.pack()
    phase_shift_entry = Entry(task1generate_signal_page)
    phase_shift_entry.pack()

    # Analog Frequency
    analog_frequency_lbl = Label(task1generate_signal_page, text="Analog Frequency")
    analog_frequency_lbl.pack()
    analog_frequency_entry = Entry(task1generate_signal_page)
    analog_frequency_entry.pack()

    # Sampling Frequency
    sampling_frequency_lbl = Label(task1generate_signal_page, text="Sampling Frequency")
    sampling_frequency_lbl.pack()
    sampling_frequency_entry = Entry(task1generate_signal_page)
    sampling_frequency_entry.pack()

    # Generate Button
    generate_signal_btn = Button(task1generate_signal_page, text="Generate Signal",
                                 command=lambda: generate_signal(selected_function, amplitude_entry, phase_shift_entry,
                                                                 analog_frequency_entry, sampling_frequency_entry), font=btn_font)
    generate_signal_btn.pack()


#task2_add()
pages_initializer()
home_page_gui()
task1page_gui()
task1generate_signal_page_gui()
task2page_gui()
task3page_gui()
task4page_gui()
task5page_gui()
task6page_gui()

home_page.tkraise()



root.mainloop()
