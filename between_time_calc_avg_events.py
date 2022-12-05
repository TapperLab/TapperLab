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


trim_keys = []
for name in extracted_data.keys():
	if 'Time' not in name:
		trim_keys.append(name)
		
avg_events = {name:[] for name in trim_keys}
events_means = {name:[] for name in trim_keys}

for name in trim_keys:
	df = pd.DataFrame.from_dict(extracted_data[name]).T
	avg_events[name].append(df.mean(axis = 1, skipna = True))
	df2 = pd.DataFrame.from_dict(avg_events[name])
	events_means[name].append(df2.mean(axis = 1, skipna = True))
	



'''
main_output = open(save_handle[:-4] + '_avg_events_calcs_output.csv', 'w')
title_line = ['Event Name', '465nm Mean (V)', '405nm Mean (V)', '405nm Fitted Mean (V)', 'DF/F0 Mean']
main_output.write(','.join(title_line) + '\n')

for item_num, item in enumerate(means_465nm_O):
	current_line = []
	current_line.append('Object ' + str(item_num + 1))
	current_line.append(str(item))
	current_line.append(str(means_405nm_O[item_num]))
	current_line.append(str(means_405nm_fitted_O[item_num]))
	current_line.append(str(means_dff0_O[item_num]))
	main_output.write(','.join(current_line) + '\n')
	
for item_num, item in enumerate(means_465nm_S):
	current_line = []
	current_line.append('Social ' + str(item_num + 1))
	current_line.append(str(item))
	current_line.append(str(means_405nm_S[item_num]))
	current_line.append(str(means_405nm_fitted_S[item_num]))
	current_line.append(str(means_dff0_S[item_num]))
	main_output.write(','.join(current_line) + '\n')
	
for item_num, item in enumerate(means_465nm_I):
	current_line = []
	current_line.append('Interval ' + str(item_num + 1))
	current_line.append(str(item))
	current_line.append(str(means_405nm_I[item_num]))
	current_line.append(str(means_405nm_fitted_I[item_num]))
	current_line.append(str(means_dff0_I[item_num]))
	main_output.write(','.join(current_line) + '\n')
	
df_465nm_O = pd.DataFrame(events_465nm_O).T
cols = ['465nm Object ' + str(x + 1) for x in range(len(events_465nm_O))]
df_465nm_O.columns = cols

df_465nm_S = pd.DataFrame(events_465nm_S).T
cols = ['465nm Social ' + str(x + 1) for x in range(len(events_465nm_S))]
df_465nm_S.columns = cols

df_465nm_I = pd.DataFrame(events_465nm_I).T
cols = ['465nm Interval ' + str(x + 1) for x in range(len(events_465nm_I))]
df_465nm_I.columns = cols

df_405nm_O = pd.DataFrame(events_405nm_O).T
cols = ['405nm Object ' + str(x + 1) for x in range(len(events_405nm_O))]
df_405nm_O.columns = cols

df_405nm_S = pd.DataFrame(events_405nm_S).T
cols = ['405nm Social ' + str(x + 1) for x in range(len(events_405nm_S))]
df_405nm_S.columns = cols

df_405nm_I = pd.DataFrame(events_405nm_I).T
cols = ['405nm Interval ' + str(x + 1) for x in range(len(events_405nm_I))]
df_405nm_I.columns = cols

df_405nm_fitted_O = pd.DataFrame(events_405nm_fitted_O).T
cols = ['405nm Fitted Object ' + str(x + 1) for x in range(len(events_405nm_fitted_O))]
df_405nm_fitted_O.columns = cols

df_405nm_fitted_S = pd.DataFrame(events_405nm_fitted_S).T
cols = ['405nm Fitted Social ' + str(x + 1) for x in range(len(events_405nm_fitted_S))]
df_405nm_fitted_S.columns = cols

df_405nm_fitted_I = pd.DataFrame(events_405nm_fitted_I).T
cols = ['405nm Fitted Interval ' + str(x + 1) for x in range(len(events_405nm_fitted_I))]
df_405nm_fitted_I.columns = cols

df_dff0_O = pd.DataFrame(events_dff0_O).T
cols = ['DF/F0 Object ' + str(x + 1) for x in range(len(events_dff0_O))]
df_dff0_O.columns = cols

df_dff0_S = pd.DataFrame(events_dff0_S).T
cols = ['DF/F0 Social ' + str(x + 1) for x in range(len(events_dff0_S))]
df_dff0_S.columns = cols

df_dff0_I = pd.DataFrame(events_dff0_I).T
cols = ['DF/F0 Interval ' + str(x + 1) for x in range(len(events_dff0_I))]
df_dff0_I.columns = cols

event_df = pd.concat([df_465nm_O, df_465nm_S, df_465nm_I, df_405nm_O, df_405nm_S, df_405nm_I, df_405nm_fitted_O, df_405nm_fitted_S, df_405nm_fitted_I, df_dff0_O, df_dff0_S, df_dff0_I], axis = 1)

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
time_df.columns = ['Time (s)']

event_df2 = pd.concat([time_df, event_df], axis = 1)
event_df2.to_csv(save_handle[:-4] + '_avg_events_output.csv', index = False)
'''