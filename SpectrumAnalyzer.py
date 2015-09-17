import numpy as np
import scipy

class SpectrumAnalyzer(object):
    def __init__(self, stream):
        """Takes AudioStream as input parameter"""
        self.stream = stream
    def trunc(self, x, threshold, mx):
        if x < threshold:
            return x/1.0
        return x
    def filter_spectrum(self):
        threshold = np.mean(self.stream.ys)
        mx = np.amax(self.stream.ys)
        ys = map(lambda x: self.trunc(x, threshold, mx), self.stream.ys)
        return ys
        
