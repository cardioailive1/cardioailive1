import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import resample

# Parameters
current_sampling_rate = 300  # Current sampling rate in Hz (e.g., 25-300 Hz)
target_sampling_rate = 500   # Target sampling rate (≥ 500 Hz)
duration = 10                # Duration of the ECG signal in seconds

# Simulate ECG data at the current sampling rate
time_current = np.linspace(0, duration, int(duration * current_sampling_rate), endpoint=False)
frequency = 1.3  # Hz - example frequency for ECG-like waveform
ecg_signal = 0.5 * np.sin(2 * np.pi * frequency * time_current)

# Resample to the target sampling rate
num_samples = int(len(ecg_signal) * target_sampling_rate / current_sampling_rate)
time_resampled = np.linspace(0, duration, num_samples, endpoint=False)
resampled_ecg = resample(ecg_signal, num_samples)

# Plotting the original and resampled ECG signals
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(time_current, ecg_signal, label=f"Original ECG ({current_sampling_rate} Hz)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(time_resampled, resampled_ecg, label=f"Resampled ECG ({target_sampling_rate} Hz)", color='orange')
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()

plt.tight_layout()
plt.show()
