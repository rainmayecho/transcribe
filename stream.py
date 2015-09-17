import pyaudio
import numpy as np
import scipy
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from pylab import *
from SpectrumAnalyzer import SpectrumAnalyzer

class AudioStream(object):
    def __init__(self):
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44000
        self.CHUNK = 2**12

    def setup(self):
        self.invHz = 1.0/self.RATE
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.FORMAT,
                    channels=self.CHANNELS,
                    rate=self.RATE,
                    input=True,
                    frames_per_buffer=self.CHUNK)

        self.xs = np.arange(self.CHUNK) * self.invHz
        self.ys = None
        self.fft(self.fetch())
        self.SA = SpectrumAnalyzer(self)
        ion()
        self.line, = plot(self.xs, self.ys)

    def close(self):
        """Closes stream and pyaudio"""
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

    def fetch(self):
        """Gets streaming audio data of size CHUNK"""
        audiodata = self.stream.read(self.CHUNK)
        return np.fromstring(audiodata, 'Int16')

    def record(self):
        """Record loop. Updates Freq-Spectrum"""
        try:
            while True:
                self.fft(self.fetch())
                #self.ys = self.SA.filter_spectrum()
                self.line.set_ydata(self.ys)
                plt.pause(.01)
        except KeyboardInterrupt:
            self.stop_record()

    def start_record(self):
        self.record()

    def stop_record(self):
        plt.close()
        self.close()

    def fft(self, data):
        """Returns the Freq-Spectrum"""
        left, right = np.split(abs(scipy.fft(data)),2)
        self.ys = np.add(left, right[::-1])
        self.xs = np.arange(self.CHUNK/2, dtype=float)
        i = int((self.CHUNK/2)/10)
        self.ys = self.ys[:i]
        self.ys = self.ys / (max(np.amax(self.ys), 10**6))
        self.xs = self.xs[:i]* self.RATE/self.CHUNK

        
