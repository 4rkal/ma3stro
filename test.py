import wave
import numpy as np

samplerate = 44100  # Adjusted the sample rate to 44100 Hz for standard audio quality.

# Define the duration of the beat and silence
beat_duration = 0.5  # Duration of the beat in seconds

# Create time array for the beat
beat_t = np.linspace(0, beat_duration, int(samplerate * beat_duration))

# Generate a sine wave for the beat
beat_channel = 0.5 * np.sin(2 * np.pi * 440.0 * beat_t)

# Combine left and right channels
audio_beat = np.array([beat_channel, beat_channel]).T

# Convert to 16-bit integers
audio_beat = (audio_beat * (2 ** 10 - 1)).astype("<h")

# Define a function to write the beat to a WAV file
def write_beat_to_wav():
    with wave.open("beat.wav", "w") as f:
        f.setnchannels(2)
        f.setsampwidth(2)
        f.setframerate(samplerate)
        f.writeframes(audio_beat.tobytes())

# Write the beat to a WAV file
write_beat_to_wav()

# Flag to track if a beat has been played
beat_played = False

# Simulate beat play
print("Playing beat")
beat_played = True
