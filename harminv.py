import numpy as np
import tempfile
import os
from scipy.constants import c as c0

def harminv(delta_t, wavelength_min, wavelength_max, data):
    freq_max = c0/wavelength_min
    freq_min = c0/wavelength_max
    temp_result = tempfile.mktemp()
    cmd = "harminv -t %e %e-%e < %s > %s" % (delta_t, freq_min, freq_max, data, temp_result)
    os.system(cmd)
    temp_f = file(temp_result, 'r')
    result_data = ''
    for l, line in enumerate(temp_f.readlines()):
        if l > 0:
            words = line.split(',')
            words[0] = "%e" % (c0/float(words[0]))
            newline = ''
            for word in words:
                if word[-1] != '\n':
                    word += ','
                newline += word
        else:
            newline = line.replace('frequency', 'wavelength')
        result_data += newline
    temp_f.close()
    return result_data

if __name__ == '__main__':
    nm = 1.e-9
    dt = 4.16955e-18
    wave_min = 500*nm
    wave_max = 1000*nm
    harminv_data = harminv(dt, wave_min, wave_max, 'Input4Harminv.txt')
    print harminv_data

    
