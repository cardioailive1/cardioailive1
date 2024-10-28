import numpy as np
import time
from scipy.stats import skew, kurtosis
from joblib import Parallel, delayed

# Simulated ECG data (e.g., 1000 segments of 1-second ECG data sampled at 500 Hz)
num_segments = 1000
sampling_rate = 500  # Hz
segment_length = sampling_rate  # 1-second segments
ecg_data = np.random.rand(num_segments, segment_length)  # Dummy data for demonstration

# Define feature extraction function
def extract_features(ecg_segment):
    features = {
        "mean": np.mean(ecg_segment),
        "std_dev": np.std(ecg_segment),
        "skewness": skew(ecg_segment),
        "kurtosis": kurtosis(ecg_segment),
        "max": np.max(ecg_segment),
        "min": np.min(ecg_segment)
    }
    return features

# Optimized feature extraction using parallel processing
start_time = time.time()
features = Parallel(n_jobs=-1)(delayed(extract_features)(segment) for segment in ecg_data)
end_time = time.time()

# Time taken
total_time = end_time - start_time
average_time_per_segment = total_time / num_segments

print(f"Total time: {total_time:.2f} seconds")
print(f"Average time per segment: {average_time_per_segment:.2f} seconds")
