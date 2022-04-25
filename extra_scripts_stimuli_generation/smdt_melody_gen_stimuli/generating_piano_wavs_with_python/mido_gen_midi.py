from mido import Message, MidiFile, MidiTrack
note_names = [
  "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", 
  "G#4", "A4", "A#4", "B4", "C5", "C#5", "D5", "D#5", 
  "E5", "F5", "F#5", "G5", "G#5", "A5", "A#5"
]

note_numbers = [x for x in range(72, 95)]

for i in range(len(note_numbers)):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    track.append(Message('program_change', program=12, time=0))
    track.append(Message('note_on', note=note_numbers[i], velocity=64, time=0))
    track.append(Message('note_off', note=note_numbers[i], velocity=127, time=0))

    mid.save(f'gen_midis/{note_names[i]}.mid')
