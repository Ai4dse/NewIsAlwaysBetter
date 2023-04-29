import os
import time
import threading
import numpy as np
import sounddevice as sd
import recorder2
import wavio as wv
import datetime
import transcriber2
import grammarcheck
from queue import Queue
import torch

device = None
model = 'base'

def audio_thread(q, device):
    while True:
        recorder = recorder2.AudioRecorder(device=device)
        recording = recorder.record()
        q.put(recorder)

def transcribe_thread(TranscriptQ):
    while True:
        file = TranscriptQ.get()
        if file != None:
            transcriber2.transcribe(file)


def save_thread(q,TranscriptQ):
    recordings = []
    while True:
        recordings.append(q.get())
        if len(recordings) == 2:
            os.makedirs("./recordings", exist_ok=True)

            filename = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S.wav")
             # Get the number of samples in the first 2 seconds of the second recording
            num_samples = int(recordings[0].freq * 2)

            # Truncate the second recording to the first 2 seconds
            truncated_recording = recordings[1].recording[:num_samples]

            combined_recording = np.concatenate([recordings[0].recording, truncated_recording], axis=0)
            wv.write(f"./recordings/{filename}", combined_recording, recordings[0].freq, sampwidth=2)
            TranscriptQ.put(f"./recordings/{filename}")
            print(f'Saved recording to {filename}')
            del recordings[0]

def start():
    print('Hello')
    print('CUDA enabled:', torch.cuda.is_available())
    print('Pytorch CUDA Version is', torch.version.cuda)
    devices = sd.query_devices()
    print(devices)

    system_audio_device_index = None
    for i, device in enumerate(devices):
        if "TONOR" in device['name']:
            print(f"System audio device found at index {i}")
            system_audio_device_index = i
            break
    print(system_audio_device_index)
    q = Queue()
    TranscriptQ = Queue()
    t1 = threading.Thread(target=audio_thread, args=(q, system_audio_device_index))
    t1.daemon = True
    t1.start()

    t2 = threading.Thread(target=save_thread, args=(q,TranscriptQ))
    t2.daemon = True
    t2.start()

    t3 = threading.Thread(target=transcribe_thread, args=(TranscriptQ,))
    t3.daemon = True
    t3.start()

    print("Lets Gooooooo")
    while True:
        if not t3.is_alive:
            break
        time.sleep(1)

def setDevice(input):
    global device 
    device = input

#def stop():

if __name__ == "__main__":
    start()
