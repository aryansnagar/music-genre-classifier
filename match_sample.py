import numpy as np
from scipy.io import wavfile

def get_freq_magnitude(filename):
    sample_rate, data = wavfile.read(filename)
    if len(data.shape) > 1:
        data = data[:, 0]
    n = len(data)
    freq_data = np.fft.fft(data)
    freq_magnitude = np.abs(freq_data)[:n // 2]

    norm = np.linalg.norm(freq_magnitude)
    if norm == 0:
        return freq_magnitude
    return freq_magnitude / norm

def similarity_score(vec1, vec2):

    min_len = min(len(vec1), len(vec2))
    v1 = vec1[:min_len]
    v2 = vec2[:min_len]

    score = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

    return max(0, score) * 100


recorded_file = 'music_file.wav'
reference_file = 'music_sample.wav'

freq1 = get_freq_magnitude(recorded_file)
freq2 = get_freq_magnitude(reference_file)

score = similarity_score(freq1, freq2)
print(f"Similarity score: {score:.2f}%")
