"""

Helper functions for Metis project 1

"""

import pandas as pd

def find_weekend_indices(datetime_array):
    """
    Find the indices for weekends in datetime_array
    """
    indices = []
    for i in range(len(datetime_array)):
        if datetime_array[i].weekday() >= 5:
            indices.append(i)
    return indices

def highlight_datetimes(indices, ax, data):
    """
    Highlight datetime backgrounds for data on ax based on selected indices 
    """
    i = 0
    while i < len(indices)-1:
        ax.axvspan(data.at[data.index[indices[i]], 'DATE'], data.at[data.index[indices[i] + 1], 'DATE'], facecolor='lightblue', edgecolor='none', alpha=.5)
        i += 1
