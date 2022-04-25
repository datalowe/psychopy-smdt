# PsychoPy implementation of Swedish Musical Discrimination Test: Pitch
This is a [PsychoPy](https://psychopy.org/) experiment implementing the "Pitch" subtest of the [Swedish Musical Discrimination Test](https://www.sciencedirect.com/science/article/pii/S0191886914000841)(SMDT) in Swedish.

Each experiment trial first plays two tones for the participant. The participant is then to respond, with a keyboard, by indicating whether the second tone was higher (pitch-wise) or lower than the first of the two tones. There are 27 trials, with progressively decreasing difference in frequency between the first and second tone as follows:
* 17Hz difference (e.g. 500Hz/517Hz), 3 trials
* 12Hz difference, 3 trials
* 8Hz difference, 3 trials
* 5Hz difference, 4 trials
* 4Hz difference, 4 trials
* 3Hz difference, 4 trials
* 2Hz difference, 4 trials
* 1Hz difference, 2 trials

## Running the experiment
1. Install [Standalone PsychoPy](https://www.psychopy.org/download.html).
2. Download this project, by either using the green 'code' button and selecting 'Download ZIP', or by using `git clone` if you know Git.
3. Open up 'smdt_rhythm.psyexp' with PsychoPy.
4. Click the cogwheel ('Edit experiment settings') icon, go to the 'Screen' tab, and insert specifications appropriate for your monitor (if you haven't already, you also need to set up a monitor in Monitor Center).
5. Click the Play ('Run experiment') icon.

## Translating the experiment
In PsychoPy, click the Text Components in the 'instructions', 'trial', 'inter_trial_500ms_highlight', 'inter_trial_500ms_grey', and 'end_screen' routines, e.g. the component 'text_instructions'. In the window that pops up, edit the 'Text' field. It's recommended that you copy and paste the Swedish text snippets into e.g. Google Translate as a start. Once you've finished translating the experiment, save it ('Save current experiment file' in main window toolbar) and try running it again.

## Stimuli
The sound files in this project were generated, based on the descriptions in the original SMDT article, with Python (especially the `wave` module). The names of the sound files indicate the frequencies of the first/second tones, so e.g. 'smdtpitch_500_501.wav' holds a sound file that first plays a 500Hz tone, then a 501Hz tone.

### Stimuli generation scripts
If you're interested and know Python well, The jupyter notebooks which include the scripts for stimuli generation can be found in the 'extra_scripts_stimuli_generation' folder of the code repository at [https://github.com/datalowe/psychopy-smdt](https://github.com/datalowe/psychopy-smdt).

## Output data
The most relevant output data files are the 'CSV'/'.csv' files, saved to the 'data' directory. The most important columns in these files are as follows:
* first_freq/second_freq: Indicates frequency of first/second tone played.
* correct_name: Indicates which 'box' in PsychoPy the participant needed to click to produce a correct response, e.g. 'tone_square_4', and thus which tone (4th) differed between the two melodies.
* clicked_name: Indicates which 'box' in PsychoPy the participant actually clicked, e.g. 'tone_square_5' would mean the participant thought the fifth tone differed between the two melodies.
* response_correct: 0 if response was incorrect, 1 if response was correct.
* first_melody/second_melody: Describe what sequences of tones were played for the first and second melody, e.g. '['A5', 'F#5', 'G#5', 'G5']' means the tones A5, F#5, G#5 and then G5 were played.

## Differences from original test
The original test was written in Adobe Flash and used a different set of sound stimuli, while the ones used here were newly generated according to the original article's description. The original test always used the same sequence of sound files, meaning the sequence of correct responses was also the same. This PsychoPy implementation ensures that there are as equal amounts of 'second-tone-higher'/'second-tone-lower' trials as possible (e.g. 13/14 for a total of 27 trials), but otherwise the sequence of 'higher'/'lower' correct responses is randomly generated for each experiment run. This means that:
* The experiment can be rerun with participants without the risk of learning effects being specific for the exact sequence being used.
* There is likely to be somewhat more noise in inter-individual differences, since not all participants go through exactly the same experiment. Note though that this risk should be relatively low since there is a relatively large number of trials and the amounts of 'second-tone-higher'/'-lower' trials being the same.

## (not) Running the experiment online
This experiment was only developed for local use, i.e. not with online use in mind. Since it uses much custom Python code, it is unlikely that one could easily convert it to JavaScript for being run online. You are very welcome to try, but you might find it easier to rewrite the experiment from scratch.

## Attribution
The SMDT was developed at Karolinska Institutet's Department of Neuroscience by a research group led by Prof. Fredrik Ullén. This PsychoPy implementation was created by Lowe Wilsson.

You are free to use and modify this experiment for non-commercial purposes (e.g. research is OK) __with attribution__. If you publish articles or share other work based on this project (e.g. if you share a modified version of it), you are required to include the following two articles as references:
* Ullén, F, Mosing, MA, Holm, L, Eriksson, H, Madison, G (2014). Psychometric properties and heritability of a new online test for musicality, the Swedish Musical Discrimination Test. _Personality and Individual Differences 63_, 87-93. [https://doi.org/10.1016/j.paid.2014.01.057](https://doi.org/10.1016/j.paid.2014.01.057)
* Mosing, MA, Madison, G, Pedersen, NL, Kuja-Halkola, R, Ullén, F. (2014). Practice does not make perfect: No causal effect of musical practice on musical ability. _Psychological Science 25(9)_, pp. 1795-803. [https://doi.org/10.1177/0956797614541990](https://doi.org/10.1177/0956797614541990)

It's not required, but it's appreciated if you also share a link to this project's parent code repository [https://github.com/datalowe/psychopy-smdt](https://github.com/datalowe/psychopy-smdt) in order to help spread the word.
