from mp3_read import mp3_read
import matplotlib.pyplot as plt
from subprocess import check_call


def mp3_2_spectrogram(audio_in, img_out):
    fs, signal = mp3_read(audio_in)
    plt.specgram(x = signal, Fs = fs, cmap = 'gray')
    plt.axis('off')
    plt.savefig(img_out)
    plt.close('all')
    check_call(['mogrify', '-trim', img_out]) #bbox tight does not trim fully