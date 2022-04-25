import soundfile as sf
import os

TARGET_DIRECTORY = 'ENTER/DIRECTORY/PATH/HERE'

sound_filenames = [x for x in os.listdir(TARGET_DIRECTORY) if not x.startswith('.')]

for fname in sound_filenames:
    # import the data, including the audio's sample rate
    in_fpath = os.path.join(TARGET_DIRECTORY, fname)
    data, samplerate = sf.read(fname)
    # only keep audio data for the first 650ms
    nsamples_650ms = int(0.65 * samplerate)
    data_650ms = data[:nsamples_650ms]
    # export the data
    target_fpath = os.path.join(
        TARGET_DIRECTORY, 
        fname.replace('aiff', 'wav')
    )
    sf.write(target_fpath, data_650ms, samplerate)
