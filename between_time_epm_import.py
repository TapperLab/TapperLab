import sys
import pandas as pd
import pickle

#Import variables from cmd line
file_handle = sys.argv[1]
save_handle = sys.argv[2]

imported_data = {'Start Times': [], 'End Times': [], 'Event Type': [], 'Time': [], '465nm': [], '405nm': [], '405nm Fitted': [], 'DF/F0': []}

for line_num, line in enumerate(open(file_handle)):
	line = line.strip().split(',')
	for item_num, item in enumerate(line):
		if line_num > 0 and item != '':
			if item_num == 0:
				imported_data['Start Times'].append(float(item))
			if item_num == 1:
				imported_data['End Times'].append(float(item))
			if item_num == 2:
				imported_data['Event Type'].append(item)
			if item_num == 3:
				imported_data['Time'].append(float(item))
			if item_num == 4:
				imported_data['465nm'].append(float(item))
			if item_num == 5:
				imported_data['405nm'].append(float(item))
			if item_num == 6:
				imported_data['405nm Fitted'].append(float(item))
			if item_num == 7:
				imported_data['DF/F0'].append(float(item))

pickle.dump(imported_data, open('imported_data.pkl','wb'))