# PsychoPy implementation of the Swedish Musical Discrimination Test: Melody
This is a [PsychoPy](https://psychopy.org/) experiment implementing the "Melody" subtest of the [Swedish Musical Discrimination Test](https://www.sciencedirect.com/science/article/pii/S0191886914000841)(SMDT) in Swedish.

Each experiment trial first plays two sequences of tones for the participant. The participant is then to respond, with a mouse, by indicating which tone differed between the two sequences. The sequences increase in length, from 4 tones up to 9 tones, where each 'difficulty level' includes 3 trials. In total, there are 18 trials.

## Running the experiment
1. Install [Standalone PsychoPy](https://www.psychopy.org/download.html).
2. Download this project, by either using the green 'code' button and selecting 'Download ZIP', or by using `git clone` if you know Git.
3. Open up 'smdt_melody.psyexp' with PsychoPy.
4. Click the cogwheel ('Edit experiment settings') icon, go to the 'Screen' tab, and insert specifications appropriate for your monitor (if you haven't already, you also need to set up a monitor in Monitor Center).
5. Click the Play ('Run experiment') icon.

## Translating the experiment
In PsychoPy, click the Text Components in the 'instructions' and 'end_message' routines, e.g. the component 'text_instructions'. In the window that pops up, edit the 'Text' field. It's recommended that you copy and paste the Swedish text snippets into e.g. Google Translate as a start. Once you've finished translating the experiment, save it ('Save current experiment file' in main window toolbar) and try running it again.

## Stimuli
The sound files in this project were produced using KaleidonKep99's Steinway B-211 sound library: https://github.com/KaleidonKep99/Steinway-B-211

## Output data
The most relevant output data files are the 'CSV'/'.csv' files, saved to the 'data' directory. The most important columns in these files are as follows:
* correct_name: Indicate frequency of first/second tone played.
* correct_name: Indicate correct response ('pitch_rect_higher' or 'pitch_rect_lower').
* response_correct: 0 if response was incorrect, 1 if response was correct.

## Differences from original test
The original test was written in Adobe Flash and used exactly the same melodies/sound files for all participants, in the same sequence. The PsychoPy version automatically generates, while adhering to the restrictions specified by the original article (e.g. sequences are atonal), melodies for each experiment run. Generating new sequences means that:
* The experiment can be rerun with participants without the risk of learning effects being specific for the exact sequence being used.
* There is virtually no risk of any findings being specific to the particular melodies used, improving generalizability.
* There is likely to be somewhat more noise in inter-individual differences, as some participants might happen to be played 'easier' sequences. Note though that this risk should be relatively low, since all melodies are atonal etc. which makes them not easily memorable, and there is a relatively large number of trials.

## (not) Running the experiment online
This experiment was only developed for local use, i.e. not with online use in mind. Since it uses much custom Python code, it is unlikely that one could easily convert it to JavaScript for being run online. You are very welcome to try, but you might find it easier to rewrite the experiment from scratch.

## Attribution
The SMDT was developed at Karolinska Institutet's Department of Neuroscience by a research group led by Prof. Fredrik Ullén. This PsychoPy implementation was created by Lowe Wilsson.

You are free to use and modify this experiment for non-commercial purposes (e.g. research is OK) __with attribution__. If you publish articles or share other work based on this project (e.g. if you share a modified version of it), you are required to include the following two articles as references:
* Ullén, F, Mosing, MA, Holm, L, Eriksson, H, Madison, G (2014). Psychometric properties and heritability of a new online test for musicality, the Swedish Musical Discrimination Test. _Personality and Individual Differences 63_, 87-93. [https://doi.org/10.1016/j.paid.2014.01.057](https://doi.org/10.1016/j.paid.2014.01.057)
* Mosing, MA, Madison, G, Pedersen, NL, Kuja-Halkola, R, Ullén, F. (2014). Practice does not make perfect: No causal effect of musical practice on musical ability. _Psychological Science 25(9)_, pp. 1795-803. [https://doi.org/10.1177/0956797614541990](https://doi.org/10.1177/0956797614541990)

It's not required, but it's appreciated if you also share a link to this project's parent code repository [https://github.com/datalowe/psychopy-smdt](https://github.com/datalowe/psychopy-smdt) in order to help spread the word.
