import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

sample_rate, data = wavfile.read('recording.wav')

if len(data.shape) > 1:
    data = data[:, 0]

n = len(data)
freq_data = np.fft.fft(data)
freq_magnitude = np.abs(freq_data)[:n // 2]  # Take positive frequencies only

freqs = np.fft.fftfreq(n, 1 / sample_rate)[:n // 2]

plt.plot(freqs, freq_magnitude)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Frequency Spectrum')
plt.show()