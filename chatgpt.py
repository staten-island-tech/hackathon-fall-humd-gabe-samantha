import pygame
import numpy as np
import time

# Define musical notes and their frequencies (A4 = 440 Hz)
NOTE_FREQS = {
    'C': 261.63,
    'C#': 277.18,
    'D': 293.66,
    'D#': 311.13,
    'E': 329.63,
    'F': 349.23,
    'F#': 369.99,
    'G': 392.00,
    'G#': 415.30,
    'A': 440.00,
    'A#': 466.16,
    'B': 493.88
}

# Duration in seconds for basic note lengths
DURATIONS = {
    'whole': 4,
    'half': 2,
    'quarter': 1,
    'eighth': 0.5,
    'sixteenth': 0.25
}

# Initialize pygame mixer
pygame.mixer.init(frequency=22050, size=-16, channels=2)

# Function to generate a sound for a given note and duration
def generate_sound(frequency, duration, sample_rate=22050):
    # Number of samples based on duration and sample rate
    num_samples = int(sample_rate * duration)
    
    # Generate a sine wave for the note
    t = np.linspace(0, duration, num_samples, endpoint=False)  # Time array
    waveform = np.sin(2 * np.pi * frequency * t)  # Sine wave formula
    
    # Convert to 16-bit PCM format (mono)
    audio_data = np.int16(waveform * 32767)  # Scale to int16
    
    # Convert to stereo by duplicating the mono waveform to both left and right channels
    stereo_data = np.column_stack((audio_data, audio_data))  # Stack columns for stereo
    
    return stereo_data

# Function to play a note for a given duration
def play_note(note, duration):
    if note not in NOTE_FREQS:
        print("Invalid note!")
        return

    frequency = NOTE_FREQS[note]  # Get frequency for the note
    sound_data = generate_sound(frequency, duration)  # Generate sound data
    
    # Ensure pygame mixer is initialized before playing the sound
    if not pygame.mixer.get_init():
        pygame.mixer.init(frequency=22050, size=-16, channels=2)
    
    # Create a pygame sound object from the NumPy array (stereo)
    sound = pygame.sndarray.make_sound(sound_data)  # Create a pygame sound object
    sound.play()  # Play the sound
    time.sleep(duration)  # Wait for the duration of the note

# Function to play a song
def play_song(song):
    for note, duration in song:
        play_note(note, DURATIONS[duration])  # Play each note in the song

# Main function to run the game
def game_loop():
    print("Welcome to the Music Maker Game!")
    print("Available notes: C, D, E, F, G, A, B (with # for sharps like C#, D#...)")
    print("Available durations: whole, half, quarter, eighth, sixteenth")
    
    song = []

    while True:
        note = input("Enter a note (or 'exit' to finish): ").strip()
        if note.lower() == 'exit':
            break

        if note not in NOTE_FREQS:
            print("Invalid note. Try again.")
            continue

        duration = input("Enter duration (whole, half, quarter, eighth, sixteenth): ").strip()
        if duration not in DURATIONS:
            print("Invalid duration. Try again.")
            continue

        song.append((note, duration))
        print(f"Added {note} for {duration} duration.")

    # Play the song
    print("\nPlaying your song...")
    play_song(song)

if __name__ == "__main__":
    game_loop()
