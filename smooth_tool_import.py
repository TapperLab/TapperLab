import sys
import pandas as pd
import numpy as np
sys.path.append(sys.argv[3])
from signal_udfs import lowpass

file_handle = sys.argv[1]
save_handle = sys.argv[2]

names = []
signals = []

for line_num, line in enumerate(open(file_handle)):
	line = line.strip().split(',')
	if line_num == 0:
		for point in line:
			if point != '' and point != []:
				names.append(point)
signals = [[] for x in range(len(names))]
		   
for line_num, line in enumerate(open(file_handle)):
	line = line.strip().split(',')
	if line_num > 0:
		for point_num, point in enumerate(line):
			if point != '' and point != []:
				signals[point_num].append(float(point))

time = signals[0]
raw_signals = signals[1:]

smooth_events = lowpass(raw_signals, 10, 242, 2)
	
smooth_df = pd.DataFrame(smooth_events).T
smooth_df.columns = names[1:]
time_df = pd.DataFrame(time)
time_df.columns = ['Time']
output_df = pd.concat([time_df, smooth_df], axis = 1)
output_df.to_csv(save_handle[:-4] + '_smoothed_events.csv', index = False)