# File Name: grapher.py
# Author: Deniz ASLAN
# Last Modified: 12.05.2021
# Python Version: 3.8

import pandas as pd
import matplotlib.pyplot as plt

# read csv, turn into pandas dataframe, split into two, turn into numpy arrays:
filename = input("Which csv file would you like to visualize? e.g. data.csv")
df = pd.read_csv(filename)
df_audio = df.drop(["number of flashes"], 1)
df_visual = df.drop(["number of beeps"], 1)
array_visual = df_visual.to_numpy()
array_audio = df_audio.to_numpy()

# initialize dictionary, sum values and divide by rows to get means:
audio_responses = {1: 0, 2: 0, 3: 0, 4: 0}
visual_responses = {1: 0, 2: 0, 3: 0, 4: 0}

for i in range(1, 5):
    for row in array_audio:
        if row[0] == i:
            audio_responses[i] += row[1]
    audio_responses[i] = audio_responses[i] / (len(array_audio) / 4)

for i in range(1, 5):
    for row in array_visual:
        if row[0] == i:
            visual_responses[i] += row[1]
    visual_responses[i] = visual_responses[i] / (len(array_visual) / 4)

# visualize dictionaries into two graphs, save as png file:
graph_name = filename[:len(filename) - 4] + "_graph.png"

visual_keys = visual_responses.keys()
visual_values = visual_responses.values()

plt.subplot(1, 2, 1)
plt.plot(visual_keys, visual_values, marker="o")
plt.xlabel("Number of flashes")
plt.ylabel("Number of perceived flashes")
plt.grid()

audio_keys = audio_responses.keys()
audio_values = audio_responses.values()

plt.subplot(1, 2, 2)
plt.plot(audio_keys, audio_values, marker="o")
plt.xlabel("Number of beeps")
plt.ylabel("Number of perceived flashes")
plt.grid()
plt.tight_layout()
plt.xticks([1, 2, 3, 4])
plt.show()
plt.savefig(graph_name)
