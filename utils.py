import numpy as np
import math
from matplotlib.mlab import find
import scipy
"""
--------------------------------------------------
    Utility functions for signal processing
--------------------------------------------------
"""

def pitch(signal, rate):
    signal = np.fromstring(signal, 'Int16')
    crossing = [math.copysign(1.0, s) for s in signal]
    index = find(np.diff(crossing))
    f0 = round(len(index) * rate / (2*np.prod(len(signal))))
    return f0



