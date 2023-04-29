import sounddevice as sd
import wavio as wv
import datetime

class AudioRecorder:
    def __init__(self, freq=44100, duration=5, device=None):
        self.freq = freq
        self.duration = duration
        self.recording = None
        self.device = device

    def record(self):
        if self.recording is not None:
            print('Recording is already in progress')
            return

        print('Recording')
        if self.device is None:
            self.recording = sd.rec(int(self.duration * self.freq), samplerate=self.freq, channels=2)
        else:
            self.recording = sd.rec(int(self.duration * self.freq), samplerate=self.freq, channels=2, device=self.device)

        # Wait for the recording to finish
        sd.wait()

        return self.recording
