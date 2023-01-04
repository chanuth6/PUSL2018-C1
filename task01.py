import random

# Number of simulations
num_simulations = 500

# Durations for each activity
durations = {
    "A": (8, 10, 12),
    "B": (10, 12, 14),
    "C": (12, 14, 16),
}

# Initialize the frequency table for each duration range
duration_ranges = {
    "30-35": 0,
    "36-38": 0,
    "39-42": 0,
}

# Perform the simulations
for i in range(num_simulations):
    total_duration = 0
    for activity, duration_range in durations.items():
        duration = random.triangular(*duration_range)
        total_duration += duration
    if total_duration >= 30 and total_duration <= 35:
        duration_ranges["30-35"] += 1
    elif total_duration >= 36 and total_duration <= 38:
        duration_ranges["36-38"] += 1
    elif total_duration >= 39 and total_duration <= 42:
        duration_ranges["39-42"] += 1

# Calculate the likelihood of completion for each duration range
for duration_range, frequency in duration_ranges.items():
    likelihood = frequency / num_simulations
    print(f"{duration_range}: {likelihood:.2f}")
