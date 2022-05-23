import numpy as np
import statistics
my_list = [1, 1, 2, 3, 4, 1, 2, 3, 3, 3, 3, 3]#Type your sample data here
mode1 = statistics.mode(my_list)
mode2 = np.argmax(np.bincount(my_list))
print(mode1)
print(mode2)