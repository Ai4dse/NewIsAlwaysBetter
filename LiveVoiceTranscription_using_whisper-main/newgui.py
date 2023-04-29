import tkinter as tk
from tkinter import ttk
import sounddevice as sd
import os
import time
import main
import threading

# Initialize the Tkinter app
root = tk.Tk()
root.geometry('400x400')
root.title('My Application')

# Define a function to read the transcript.txt file and display the last update
def display_update():
    if device != '':
        # Get the last update time of the transcript.txt file
        timestamp = os.path.getmtime('transcript.txt')
        # Convert the timestamp to a human-readable format
        last_update = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))
        # Open the transcript.txt file and read the last line
        with open('transcript.txt', 'r') as f:
            lines = f.readlines()
            last_line = lines[-1].strip()
        # Display the last update and last line in the output field
        output_field.delete('1.0', tk.END)
        output_field.insert(tk.END, f'Last update: {last_update}\n{last_line}')

# Define a function to start the application
def start_app():
    global device
    device = device_list.get()
    print(device)
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)
    t1 = threading.Thread(target=main.start)
    t1.start()


# Define a function to stop the application
def stop_app():
    global device
    device = ''
    stop_button.config(state=tk.DISABLED)
    start_button.config(state=tk.NORMAL)
    #stop()


# Get a list of available audio devices with at least one input channel
devices = sd.query_devices()
input_devices = [d for d in devices if d['max_input_channels'] > 0]

# Define the user interface elements
device_label = ttk.Label(root, text='Select system audio device:')
device_list = ttk.Combobox(root, values=[d['name'] for d in input_devices], state='readonly', width=30)
output_label = ttk.Label(root, text='Output:')
output_field = tk.Text(root, height=10, width=50)
start_button = ttk.Button(root, text='Start', command=start_app)
stop_button = ttk.Button(root, text='Stop', command=stop_app, state=tk.DISABLED)

# Add the user interface elements to the app
device_label.pack(pady=10)
device_list.pack()
output_label.pack(pady=10)
output_field.pack()
start_button.pack(pady=10)
stop_button.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
