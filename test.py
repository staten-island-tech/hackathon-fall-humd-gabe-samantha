# Example file showing a basic pygame "game loop"
import pygame
import time
import numpy as np
import sounddevice as sd


NOTE_LIBRARY = {
    'C4': 261.63,
    'C#4': 277.18,
    'D4': 293.66,
    'D#4': 311.13,
    'E4': 329.63,
    'F4': 349.23,
    'F#4': 369.99,
    'G4': 392.00,
    'G#4': 415.30,
    'A4': 440.00,
    'A#4': 466.16,
    'B4': 493.88
}

NOTE_DURATIONS = {
    'whole': 4,
    'half': 2,
    'quarter': 1,
    'eighth': 0.5,
    'sixteenth': 0.25
}


def game_loop():
    print("Welcome to the Music Maker Game!")
    print("Notes: C, D, E, F, G, A, B, and the sharp(#) form of each note")
    print("Available durations: whole, half, quarter, eighth, sixteenth")
    
    song = []

    while True:
        note = input("Enter a note from our note Library", (NOTE_LIBRARY))

