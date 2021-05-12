# File Name: main.py
# Author: Deniz ASLAN
# Last Modified: 12.05.2021
# Python Version: 3.8

import expyriment as xp
import random

# change these parameters as seen fit:
number_of_blocks = 5
circle_size = 100
circle_color = (255, 255, 255)
beep_duration = 50
duration_of_flash = 50
duration_between_flashes = 50

# do NOT change these parameters unless you know what you are doing:
stimuli = ["11", "12", "13", "14",
           "21", "22", "23", "24",
           "31", "32", "33", "34",
           "41", "42", "43", "44"]
key_values = {49: "1", 50: "2", 51: "3", 52: "4"}

exp = xp.design.Experiment(name="Beeps and Flashes")

# comment out this line to make experiment full-screen:
xp.control.set_develop_mode(True)

xp.control.initialize(exp)

# initialize stimuli and text messages
beep = xp.stimuli.Tone(beep_duration)
disk = xp.stimuli.Circle(circle_size, colour=circle_color, anti_aliasing=10)
blank = xp.stimuli.BlankScreen()

elicit = xp.stimuli.TextScreen("", """How many times did the circle flash? 
Press 1, 2, 3 or 4.""")

title = xp.stimuli.TextScreen("Beeps and Flashes", """In this experiment, 
you will be exposed to two stimuli: a flashing circle, and a beeping tone. 
After each trial, you will be asked to indicate how many times the circle 
has flashed. Press any key to begin. (You can end the experiment at any time by 
pressing Escape.)""")

end = xp.stimuli.TextScreen("The End", """The experiment is now over, your 
answers have been recorded in the csv file with the name or identifier you 
entered. Thank you for your participation. Press any key to exit.""")

ask_name = xp.io.TextInput("Please enter a name or identifier:")

beep.preload()
disk.preload()

# start experiment
xp.control.start()
identity = ask_name.get()
title.present()
exp.keyboard.wait()
blank.present()
exp.clock.wait(1000)

# initialize empty set, randomize and present stimuli for specified
# number of blocks, then collect answers and append to set:
answers = []
for block in range(number_of_blocks):
    random.shuffle(stimuli)
    for key in stimuli:
        exp.clock.wait(400)
        for i in range(4):
            if int(key[0]) > i:
                disk.present()
            if int(key[1]) > i:
                beep.present()
            exp.clock.wait(duration_of_flash)
            blank.present()
            exp.clock.wait(duration_between_flashes)
        exp.clock.wait(400)
        elicit.present()
        answer, time = exp.keyboard.wait([xp.misc.constants.K_1,
                                          xp.misc.constants.K_2,
                                          xp.misc.constants.K_3,
                                          xp.misc.constants.K_4])
        answers.append(key[0])
        answers.append(key[1])
        answers.append(key_values[answer])
        blank.present()
        exp.clock.wait(500)

# create csv file, add header, write experiment results into file
filename = "data_" + identity + ".csv"
file = open(filename, "w")
file.write("number of flashes,number of beeps,perceived flashes")
for index, answer in enumerate(answers):
    if index % 3 == 0:
        file.write("\n")
    file.write(answer)
    if index % 3 != 2:
        file.write(",")
file.close()

end.present()
exp.keyboard.wait()

# end experiment and close window
xp.control.end()
