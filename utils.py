import numpy as np
import math
from matplotlib.mlab import find
import scipy
import Image, ImageDraw
"""
--------------------------------------------------
    Utility functions for signal processing
--------------------------------------------------
"""
class Color():
    def __init__(self, r=255, g=255, b=255):
        self.r = r
        self.g = g
        self.b = b
    def scale(self, s):
        return (min(int(self.r * s), 255), min(int(self.g * s), 255), min(int(self.b * s), 255))


def pitch(signal, rate):
    signal = np.fromstring(signal, 'Int16')
    crossing = [math.copysign(1.0, s) for s in signal]
    index = find(np.diff(crossing))
    f0 = round(len(index) * rate / (2*np.prod(len(signal))))
    return f0

def create_spectrograph(name, rate, chunk, spectra):
    g = 1
    f = 11 - g
    width, height = chunk/2/g, len(spectra)
    im = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(im)
    white = Color()
    for j, dt in enumerate(spectra):
        for i, fmag in enumerate(dt):
            c = white.scale(fmag)
            draw.line([i*f,height - j,i*f+f,height -j], c)
    del draw
    im.save('%s.png' %(name), 'PNG')
            
            
                   

            

