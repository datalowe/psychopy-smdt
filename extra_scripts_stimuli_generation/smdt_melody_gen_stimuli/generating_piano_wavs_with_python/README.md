PROJECT FOR GENERATING ONE-TONE AUDIO WAV FILES
Using kaleidonkep99's piano soundfont (https://github.com/KaleidonKep99/Steinway-B-211), sforzando (https://www.plogue.com/products/sforzando.html), the SoundFile Python package (https://pysoundfile.readthedocs.io/) and the Python package mido (https://mido.readthedocs.io/).

STEPS
1. Create midi files using 'mido_gen_midi.py'.
2. Open sforzando and drag-and-drop the relevant .sfz file from the presets in KaleidonKep99's soundfont repo. 
2a. If error messages pop up, look at them - you probably need to rename the files in the repo's Extensions folders, for instance 'B-211.hmr' should be '1960 Steinway B-211.hmr'.
3. In sforzando, go to (on Mac) sforzando->'Render offline', or just use Cmd+R.
4. Select one of the MIDI files generated in step 1 as input and specify a name/path for the output file, then run render.
4a. Repeat step 4 with all the MIDI files.
5. Run the 'soundfile_convert_aiff2wav.py' script to convert the AIFF files produced by sforzando into the WAV format, making sure to change the target folder if necessary.
