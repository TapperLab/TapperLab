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

means_465nm_O = []
events_465nm_O = []
means_465nm_S = []
events_465nm_S = []
means_465nm_I = []
events_465nm_I = []

means_405nm_O = []
events_405nm_O = []
means_405nm_S = []
events_405nm_S = []
means_405nm_I = []
events_405nm_I = []

means_405nm_fitted_O = []
events_405nm_fitted_O = []
means_405nm_fitted_S = []
events_405nm_fitted_S = []
means_405nm_fitted_I = []
events_405nm_fitted_I = []

means_dff0_O = []
events_dff0_O = []
means_dff0_S = []
events_dff0_S = []
means_dff0_I = []
events_dff0_I = []

for item in extracted_data['465nm O']:
	means_465nm_O.append(statistics.mean(item))
	events_465nm_O.append(item)
for item in extracted_data['465nm S']:
	means_465nm_S.append(statistics.mean(item))
	events_465nm_S.append(item)
for item in extracted_data['465nm I']:
	means_465nm_I.append(statistics.mean(item))
	events_465nm_I.append(item)
	

for item in extracted_data['405nm O']:
	means_405nm_O.append(statistics.mean(item))
	events_405nm_O.append(item)
for item in extracted_data['405nm S']:
	means_405nm_S.append(statistics.mean(item))
	events_405nm_S.append(item)
for item in extracted_data['405nm I']:
	means_405nm_I.append(statistics.mean(item))
	events_405nm_I.append(item)
	
for item in extracted_data['405nm Fitted O']:
	means_405nm_fitted_O.append(statistics.mean(item))
	events_405nm_fitted_O.append(item)
for item in extracted_data['405nm Fitted S']:
	means_405nm_fitted_S.append(statistics.mean(item))
	events_405nm_fitted_S.append(item)
for item in extracted_data['405nm Fitted I']:
	means_405nm_fitted_I.append(statistics.mean(item))
	events_405nm_fitted_I.append(item)
	
for item in extracted_data['DF/F0 O']:
	means_dff0_O.append(statistics.mean(item))
	events_dff0_O.append(item)
for item in extracted_data['DF/F0 S']:
	means_dff0_S.append(statistics.mean(item))
	events_dff0_S.append(item)
for item in extracted_data['DF/F0 I']:
	means_dff0_I.append(statistics.mean(item))
	events_dff0_I.append(item)	
	
main_output = open(save_handle[:-4] + '_calcs_output.csv', 'w')
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

event_df2 = pd.concat([time_df, event_df], axis = 1)
event_df2.to_csv(save_handle[:-4] + '_events_output.csv', index = False)