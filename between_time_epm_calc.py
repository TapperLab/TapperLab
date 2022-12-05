import sys
import pandas as pd
import pickle
sys.path.append(sys.argv[3])
from signal_udfs import unpickle
import statistics

file_handle = sys.argv[1]
save_handle = sys.argv[2]

extracted_data = unpickle([sys.argv[4]])[0]
imported_data = unpickle([sys.argv[5]])[0]

means_465nm_J = []
events_465nm_J = []
means_465nm_O = []
events_465nm_O = []
means_465nm_C= []
events_465nm_C = []
means_465nm_I = []
events_465nm_I = []

means_405nm_J = []
events_405nm_J = []
means_405nm_O = []
events_405nm_O = []
means_405nm_C = []
events_405nm_C = []
means_405nm_I = []
events_405nm_I = []

means_405nm_fitted_J = []
events_405nm_fitted_J = []
means_405nm_fitted_O = []
events_405nm_fitted_O = []
means_405nm_fitted_C = []
events_405nm_fitted_C = []
means_405nm_fitted_I = []
events_405nm_fitted_I = []

means_dff0_J = []
events_dff0_J = []
means_dff0_O = []
events_dff0_O = []
means_dff0_C = []
events_dff0_C = []
means_dff0_I = []
events_dff0_I = []

for item in extracted_data['465nm J']:
	means_465nm_J.append(statistics.mean(item))
	events_465nm_J.append(item)
for item in extracted_data['465nm O']:
	means_465nm_O.append(statistics.mean(item))
	events_465nm_O.append(item)
for item in extracted_data['465nm C']:
	means_465nm_C.append(statistics.mean(item))
	events_465nm_C.append(item)
for item in extracted_data['465nm I']:
	means_465nm_I.append(statistics.mean(item))
	events_465nm_I.append(item)
	

for item in extracted_data['405nm J']:
	means_405nm_J.append(statistics.mean(item))
	events_405nm_J.append(item)
for item in extracted_data['405nm O']:
	means_405nm_O.append(statistics.mean(item))
	events_405nm_O.append(item)
for item in extracted_data['405nm C']:
	means_405nm_C.append(statistics.mean(item))
	events_405nm_C.append(item)
for item in extracted_data['405nm I']:
	means_405nm_I.append(statistics.mean(item))
	events_405nm_I.append(item)

for item in extracted_data['405nm Fitted J']:
	means_405nm_fitted_J.append(statistics.mean(item))
	events_405nm_fitted_J.append(item)
for item in extracted_data['405nm Fitted O']:
	means_405nm_fitted_O.append(statistics.mean(item))
	events_405nm_fitted_O.append(item)
for item in extracted_data['405nm Fitted C']:
	means_405nm_fitted_C.append(statistics.mean(item))
	events_405nm_fitted_C.append(item)
for item in extracted_data['405nm Fitted I']:
	means_405nm_fitted_I.append(statistics.mean(item))
	events_405nm_fitted_I.append(item)

for item in extracted_data['DF/F0 J']:
	means_dff0_J.append(statistics.mean(item))
	events_dff0_J.append(item)	
for item in extracted_data['DF/F0 O']:
	means_dff0_O.append(statistics.mean(item))
	events_dff0_O.append(item)
for item in extracted_data['DF/F0 C']:
	means_dff0_C.append(statistics.mean(item))
	events_dff0_C.append(item)
for item in extracted_data['DF/F0 I']:
	means_dff0_I.append(statistics.mean(item))
	events_dff0_I.append(item)	
	
main_output = open(save_handle[:-4] + '_calcs_output.csv', 'w')
title_line = ['Event Name', '465nm Mean (V)', '405nm Mean (V)', '405nm Fitted Mean (V)', 'DF/F0 Mean']
main_output.write(','.join(title_line) + '\n')

for item_num, item in enumerate(means_465nm_J):
	current_line = []
	current_line.append('Junction ' + str(item_num + 1))
	current_line.append(str(item))
	current_line.append(str(means_405nm_J[item_num]))
	current_line.append(str(means_405nm_fitted_J[item_num]))
	current_line.append(str(means_dff0_J[item_num]))
	main_output.write(','.join(current_line) + '\n')

for item_num, item in enumerate(means_465nm_O):
	current_line = []
	current_line.append('Open ' + str(item_num + 1))
	current_line.append(str(item))
	current_line.append(str(means_405nm_O[item_num]))
	current_line.append(str(means_405nm_fitted_O[item_num]))
	current_line.append(str(means_dff0_O[item_num]))
	main_output.write(','.join(current_line) + '\n')
	
for item_num, item in enumerate(means_465nm_C):
	current_line = []
	current_line.append('Closed ' + str(item_num + 1))
	current_line.append(str(item))
	current_line.append(str(means_405nm_C[item_num]))
	current_line.append(str(means_405nm_fitted_C[item_num]))
	current_line.append(str(means_dff0_C[item_num]))
	main_output.write(','.join(current_line) + '\n')
	
for item_num, item in enumerate(means_465nm_I):
	current_line = []
	current_line.append('Interval ' + str(item_num + 1))
	current_line.append(str(item))
	current_line.append(str(means_405nm_I[item_num]))
	current_line.append(str(means_405nm_fitted_I[item_num]))
	current_line.append(str(means_dff0_I[item_num]))
	main_output.write(','.join(current_line) + '\n')
	
df_465nm_J = pd.DataFrame(events_465nm_J).T
cols = ['465nm Junction ' + str(x + 1) for x in range(len(events_465nm_J))]
df_465nm_J.columns = cols

df_465nm_O = pd.DataFrame(events_465nm_O).T
cols = ['465nm Open ' + str(x + 1) for x in range(len(events_465nm_O))]
df_465nm_O.columns = cols

df_465nm_C = pd.DataFrame(events_465nm_C).T
cols = ['465nm Closed ' + str(x + 1) for x in range(len(events_465nm_C))]
df_465nm_C.columns = cols

df_465nm_I = pd.DataFrame(events_465nm_I).T
cols = ['465nm Interval ' + str(x + 1) for x in range(len(events_465nm_I))]
df_465nm_I.columns = cols

df_405nm_J = pd.DataFrame(events_405nm_J).T
cols = ['405nm Junction ' + str(x + 1) for x in range(len(events_405nm_J))]
df_405nm_J.columns = cols

df_405nm_O = pd.DataFrame(events_405nm_O).T
cols = ['405nm Open ' + str(x + 1) for x in range(len(events_405nm_O))]
df_405nm_O.columns = cols

df_405nm_C = pd.DataFrame(events_405nm_C).T
cols = ['405nm Closed ' + str(x + 1) for x in range(len(events_405nm_C))]
df_405nm_C.columns = cols

df_405nm_I = pd.DataFrame(events_405nm_I).T
cols = ['405nm Interval ' + str(x + 1) for x in range(len(events_405nm_I))]
df_405nm_I.columns = cols

df_405nm_fitted_J = pd.DataFrame(events_405nm_fitted_J).T
cols = ['405nm Fitted Junction ' + str(x + 1) for x in range(len(events_405nm_fitted_J))]
df_405nm_fitted_J.columns = cols

df_405nm_fitted_O = pd.DataFrame(events_405nm_fitted_O).T
cols = ['405nm Fitted Open ' + str(x + 1) for x in range(len(events_405nm_fitted_O))]
df_405nm_fitted_O.columns = cols

df_405nm_fitted_C = pd.DataFrame(events_405nm_fitted_C).T
cols = ['405nm Fitted Closed ' + str(x + 1) for x in range(len(events_405nm_fitted_C))]
df_405nm_fitted_C.columns = cols

df_405nm_fitted_I = pd.DataFrame(events_405nm_fitted_I).T
cols = ['405nm Fitted Interval ' + str(x + 1) for x in range(len(events_405nm_fitted_I))]
df_405nm_fitted_I.columns = cols

df_dff0_J = pd.DataFrame(events_dff0_J).T
cols = ['DF/F0 Junction ' + str(x + 1) for x in range(len(events_dff0_J))]
df_dff0_J.columns = cols

df_dff0_O = pd.DataFrame(events_dff0_O).T
cols = ['DF/F0 Open ' + str(x + 1) for x in range(len(events_dff0_O))]
df_dff0_O.columns = cols

df_dff0_C = pd.DataFrame(events_dff0_C).T
cols = ['DF/F0 Closed ' + str(x + 1) for x in range(len(events_dff0_C))]
df_dff0_C.columns = cols

df_dff0_I = pd.DataFrame(events_dff0_I).T
cols = ['DF/F0 Interval ' + str(x + 1) for x in range(len(events_dff0_I))]
df_dff0_I.columns = cols

event_df = pd.concat([df_465nm_J, df_465nm_O, df_465nm_C, df_465nm_I, df_405nm_J, df_405nm_O, df_405nm_C, df_405nm_I, df_405nm_fitted_J, df_405nm_fitted_O, df_405nm_fitted_C, df_405nm_fitted_I, df_dff0_J, df_dff0_O, df_dff0_C, df_dff0_I], axis = 1)

time = imported_data['Time'][:event_df.size]
norm_time = []
for point in time:
	norm_time.append(point - 1)

max_len = 0
for name in extracted_data.keys():
	for item in extracted_data[name]:
		temp_len = len(item)
		if temp_len > max_len:
			max_len = temp_len
		
norm_time = norm_time[0:max_len]
time_df = pd.DataFrame(norm_time)

event_df2 = pd.concat([time_df, event_df], axis = 1)
event_df2.to_csv(save_handle[:-4] + '_events_output.csv', index = False)