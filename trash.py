import time
import warnings
import numpy as np

ts = 0.01  # Sample period in seconds
session_duration = 10.0  # Session duration in seconds
cycles = int(np.floor(session_duration / ts)) + 1

for k in range(cycles):

    st = time.time()

    # All code, like one work with nidaqmx, should be inside this loop

    print(f"Iteration: {k} of {cycles - 1}")

    # Getting end time
    et = time.time()

    try:
        time.sleep(ts + (st - et))
    except BaseException:
        warnings.warn(
            "Time spent to append data and update interface was greater than ts. "
            "You CANNOT trust time.dat"
        )
