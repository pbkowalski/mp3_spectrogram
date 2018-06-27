from tempfile import mktemp
from subprocess import check_call
from scipy.io import wavfile
from numpy import mean
import os


def mp3_read(filename):
    mp3filename = 'XC124158.mp3'
    wname = mktemp('.wav')
    check_call(['ffmpeg','-ac','1', '-i', filename, wname])
    fs, data = wavfile.read(wname)
    if len(data.shape)>1:
        data = mean(data, 1)
    os.unlink(wname)
    return fs, data
