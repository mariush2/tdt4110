import pyaudio
import numpy as np

p = pyaudio.PyAudio()

CONCERT_PITCH = 440  # kammertonen
HALF_INTERVAL = 2**(1 / 12)
C_FREQUENCY = CONCERT_PITCH * HALF_INTERVAL**(-9)


def play_tone(frequency, duration, volume=0.3):
    """
    Kode funnet på SO: https://stackoverflow.com/questions/8299303/generating-sine-wave-sound-in-python
    Se også: http://en.wikipedia.org/wiki/Bit_rate#Audio
    """
    sampling_rate = 44100
    global stream
    # generate samples, note conversion to float32 array
    samples = (np.sin(2 * np.pi * np.arange(sampling_rate * duration) * frequency / sampling_rate)).astype(np.float32)
    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=sampling_rate, output=True)
    # play. May repeat with different volume values (if done interactively)
    stream.write(volume * samples)


def close():
    global stream
    stream.stop_stream()
    stream.close()
    p.terminate()


def get_scale_frequencies(scale, start_frequency):
    global CONCERT_PITCH
    list = []
    for amount in scale:
        if(amount >= 1):
            start_frequency = start_frequency*HALF_INTERVAL**(amount)
            list.append(round(start_frequency, 3))
        else:
            list.append(round(start_frequency, 3))
    return list


def play_song(frequencies, lengths):
    [play_tone(frequencies[i], lengths[i]) for i in range(0, len(lengths))]


def frequency_from_note(note):
    global C_FREQUENCY, HALF_INTERVAL
    main_notes = ["C", "D", "E", "F", "G", "A", "B"]
    note = note.upper()
    if(len(note) >= 1):
        if(len(note) == 1):
            #Enkel note
            amount = 0
            for index, test in enumerate(main_notes):
                if(test == note):
                    amount = index
                    break
            return C_FREQUENCY*HALF_INTERVAL**amount
        else:
            amount = 0
            for index, test in enumerate(main_notes):
                if(test == note[0]):
                    amount = index
                    break

            if(note[1] == "B" or note[1] == "#"):
                if(note[1] == "B"):
                    amount -= 1
                else:
                    amount += 1
            else:
                if(note[1] == "+"):
                    #Octave up
                    amount += 7
                else:
                    amount -= 7

            return C_FREQUENCY*HALF_INTERVAL**amount
    return "Error!"


def transpose(frequencies, steps):
    global HALF_INTERVAL
    return [round(freq*HALF_INTERVAL**steps, 3) for freq in frequencies]


def frequencies_from_notes(notes):
    return [round(frequency_from_note(note), 3) for note in notes]


def read_sheet(path):
    notes = []
    lengths = []
    try:
        with open(path, "r") as f:
            for line in f:
                current = line.split(" ")
                notes.append(current[0])
                lengths.append(int(current[1][0]))

            return notes, lengths
    except:
        return "Error!"

play_song(transpose(frequencies_from_notes(read_sheet("song.txt")[0]), 5), read_sheet("song.txt")[1])
