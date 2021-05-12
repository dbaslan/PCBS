Final Project: "Audiovisual Illusion"
===========================

- Github Page:  <https://dbaslan.github.io/PCBS-project/>
- Github Repository: <https://github.com/dbaslan/PCBS-project>

This repository contains the script and the data for a project meant to be 
validated for the class "Programming for the Cognitive and Brain Sciences". 
The aim of the project is to replicate the experimental set-up created in 
[Shams et al. (2000)](https://www.nature.com/articles/35048669) 
"What you see is what you hear", investigating an audiovisual illusion.

The experiment consists of a group of trials in which a combination of 
audio and visual stimuli are presented to the participant either once or 
multiple times in quick succession. The visual stimulus is a flashing 
circle while tha audio stimulus is a simple beeping tone. The participant 
must then indicate how many times the visual stimulus appeared. However, 
the audio and visual stimuli do not match each other most of the time. 
Interestingly, the audio stimulus affects perception of the visual 
stimulus, leading to an audiovisual illusion.

Running the Experiment
----------------------

The experiment can be started by running the script 
[main.py](../PCBS-project/main/main.py). By default, it will launch in 
windowed mode. It can be launched in full-screen mode by commenting out 
the relevant piece of code in the script (line 27):
```python
xp.control.set_develop_mode(True)
```

All parameters, such as the timing or the size and color of the visual 
stimulus, can be adjusted by changing the values at the top of the script:
```python
number_of_blocks = 5
circle_size = 100
circle_color = (255, 255, 255)
beep_duration = 50
duration_of_flash = 50
duration_between_flashes = 50
```
Each block consists of 16 trials.

Accessing the Results
----------------------

Once the experiment is finished, the results are automatically saved into 
a csv file. The results from a previous test run can be found in 
[data.csv](../PCBS-project/main/data.csv).

Visualizing the Data
----------------------

Run the script [grapher.py](../PCBS-project/main/grapher.py) and 
specify which csv file to work on when prompted, in order to visualize the 
data and save the results as a png file. The visualization of 
[data.csv](../PCBS-project/main/data.csv) is available in 
[data_graph.png](../PCBS-project/main/data_graph.png) as an example.

Technical Information
----------------------

The scripts were written in Python 3.8.8, they have been 
tested on Windows 10, and run without issue. 
[main.py](../PCBS-project/main/main.py) uses the 
[expyriment](https://www.expyriment.org/) and 
[random](https://docs.python.org/3/library/random.html) modules, while 
[grapher.py](../PCBS-project/main/grapher.py) uses the 
[pandas](https://pandas.pydata.org/) and 
[matplotlib](https://matplotlib.org/) modules. 

In case the experiment fails to start, try to restart Python and run the 
script once more.

Last updated: 12.05.2021