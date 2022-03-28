# ##########################
# data_gen.py
# Anthony Luo, Elina Zheng
# March 2022
# --------------------------
# generates random data that should "look" like temperature
# ##########################

import numpy as np

# Steps:
# 1. Create a -cos wave with period of 365 days.
# 2. Superipmose another wave that's shifted by a random amount and at a frequency of a random amount.
# 2. Generate data with some variance along the curve at fairly regular intervals.
# 3. Return data as a txt file

"""Notes:
- Use numpy data types for maximus precision
"""

def generate_bigcos(x):
    """
    Generates the large cosine wave, returns the value at point x
    :return:
    """
    return

def generate_smallsin(x):
    """
    Generates the small sin wave that is not in sync with the larger one. Returns value at point x
    :param x:
    :return:
    """
    return

def add_variance(val):
    """
    adds some +/- variance onto our value. Returns the new value
    :param val:
    :return:
    """
    return

def generate(num_days, spacing):
    """
    generates num_days worth of data, with spacing minutes in between each sample point?
    Saves to csv.
    Basically each value is variance(bigcos(x) + smallsin(x))
    :return:
    """
    return

if __name__ == "__main__":
    DAYS_OF_DATA = 365
    MINUTES_BETWEEN_SAMPLES = 60 # (once an hour)
    generate(num_days=DAYS_OF_DATA, spacing=MINUTES_BETWEEN_SAMPLES)