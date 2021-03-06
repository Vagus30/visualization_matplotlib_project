# %load q02_plot_matches_by_team/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')
ipl_df = pd.read_csv('data/ipl_dataset.csv', index_col=None)


# Solution
def plot_matches_by_team():
    plt.plot('batting_team','match_count')
    plt.xlabel('batting_team')
    plt.ylabel('match_count')
    plt.show()

