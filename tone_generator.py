import numpy as np
import sounddevice as sd
import sys
import threading

# Global variables
frequency = 440.0  # Initial frequency in Hz
sampling_rate = 44100  # Sampling rate in Hz

def generate_tone(frequency):
    t = np.arange(0, 1.0, 1.0 / sampling_rate)
    tone = 0.5 * np.sin(2 * np.pi * frequency * t)
    return tone

def play_tone():
    while True:
        tone = generate_tone(frequency)
        sd.play(tone, samplerate=sampling_rate)
        sd.wait()

def change_frequency(key):
    global frequency
    step = 10  # Frequency change step in Hz

    if key == 'U':
        frequency += step
    elif key == 'D':
        frequency -= step

    print(f"Frequency: {frequency} Hz")

def main():
    print("Tone Generator CLI (Press 'U' to increase frequency, 'D' to decrease)")

    # Start the tone generation thread
    tone_thread = threading.Thread(target=play_tone)
    tone_thread.daemon = True
    tone_thread.start()

    while True:
        key = input()
        if key.upper() in ['U', 'D']:
            change_frequency(key.upper())
        elif key.upper() == 'Q':
            # Press 'Q' to quit the program
            sys.exit()
        else:
            print("Invalid input. Press 'U' to increase, 'D' to decrease, 'Q' to quit.")

if __name__ == "__main__":
    main()
