# imports
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter import IntVar
import numpy as np

# Load GUI
root = Tk()
root.geometry("400x400")
root.title("DSP")


home_page = Frame(root)
task1page = Frame(root)
task1generate_signal_page = Frame(root)

btn_font = font.Font(size=15)
lbl_font = font.Font(size=25)


x = []
y = []


def pages_initializer():
    home_page.grid(row=0, column=0, sticky="nsew")
    task1page.grid(row=0, column=0, sticky="nsew")
    task1generate_signal_page.grid(row=0, column=0, sticky="nsew")


def home_page_gui():
    home_page_lbl = Label(home_page, text="Home Page", font=lbl_font)
    home_page_lbl.pack()

    task1btn = Button(home_page, text="Task 1", command=lambda: task1page.tkraise(), font=btn_font)
    task1btn.pack()


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



pages_initializer()
home_page_gui()
task1page_gui()
task1generate_signal_page_gui()

home_page.tkraise()
root.mainloop()
