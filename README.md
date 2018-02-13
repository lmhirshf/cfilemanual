# Preface / Resources:

The information in this manual has been culled from both personal experience as well as from various reference manuals for the sensors generally used in the MIND lab – if there is a question that you have that you find not addressed in this manual feel free to look over the following resources to see if you question can be answered, or feel free to contact this manual’s author, Trevor Grant, at tjgran01@syr.edu.

# Creating Conditions Files.

## What is a conditions file?

The code used for analysis needs more than just a raw data file in order to do the type of analysis needed in many of our experiments. During data collection <em>marks</em> are received by the various sensors at various times to help us keep track of what sections of the data reflect the participant undergoing various tasks. A conditions file is used by the analysis code to look at only the sections of data we are interested in analyzing at a given time.

For example – say you were viewing a participant’s heart rate during periods of stressful stimuli vs. periods of non-stressful stimuli. In order to perform an accurate analysis, you would need to view all of the times the participant was exposed to stressful stimuli and compare it against the times in which they were exposed to a non-stressful stimuli, and then analyze the data file to see if there was a significant difference in their physiological response (in this case in their heart rate).

In order to perform the above analysis, you will need three things – the <em><strong>onset</strong> of the stimulus</em>, the <em><strong>duration</strong> of the stimulus</em> and, something to identify <em>what the stimulus (<strong>stim</strong>) was</em>. The three bolded words in the prior sentence are needed in every conditions file, and as a result will be the first three rows generated in every conditions file made.

The other data included in a conditions file are generated by the participant’s self-reports which may have been administered throughout an experiment or after the physiological data has been collected. Typically, these data are in the form of survey questions, though they can take other forms. We will first discuss how to generate the onset, duration and stim rows of a conditions file, after we will discuss how to include the participant’s self-report in the file.

## Example Conditions File:

![Figure1-1](https://github.com/tjgran01/cfilemanual/blob/master/cfilemanual/img/cfilesample1.png)
