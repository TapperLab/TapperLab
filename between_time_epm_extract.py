import sys
import pickle
sys.path.append(sys.argv[3])
from signal_udfs import unpickle

file_handle = sys.argv[1]
save_handle = sys.argv[2]

imported_data = unpickle([sys.argv[4]])[0]

extracted_data = {'Time J': [], 'Time O':[], 'Time C': [], 'Time I': [], '465nm J': [], '465nm O': [], '465nm C': [], '465nm I': [], '405nm J': [], '405nm O': [], '405nm C': [], '405nm I': [], '405nm Fitted J': [], '405nm Fitted O': [], '405nm Fitted C': [], '405nm Fitted I': [], 'DF/F0 J': [], 'DF/F0 O': [], 'DF/F0 C': [], 'DF/F0 I': []}

len_check = len(imported_data['Start Times'])
for item_num, item in enumerate(imported_data['Start Times']):
	temp_time_J = []
	temp_time_O = []
	temp_time_C = []
	temp_time_I1 = []
	temp_time_I2 = []
	temp_465nm_J = []
	temp_465nm_O = []
	temp_465nm_C = []
	temp_465nm_I1 = []
	temp_465nm_I2 = []
	temp_405nm_J = []
	temp_405nm_O = []
	temp_405nm_C = []
	temp_405nm_I1 = []
	temp_405nm_I2 = []
	temp_405nm_fitted_J = []
	temp_405nm_fitted_O = []
	temp_405nm_fitted_C = []
	temp_405nm_fitted_I1 = []
	temp_405nm_fitted_I2 = []
	temp_dff0_J = []
	temp_dff0_O = []
	temp_dff0_C = []
	temp_dff0_I1 = []
	temp_dff0_I2 = []
	if item_num + 1 < len_check:
		start_ts = item
		end_ts = imported_data['End Times'][item_num]
		next_ts = imported_data['Start Times'][item_num + 1]
	else:
		start_ts = item
		end_ts = imported_data['End Times'][item_num]
		next_ts = 9999
	for point_num, point in enumerate(imported_data['Time']):
		if item_num == 0:
			if point < (start_ts - 1) and point <= 3:
				temp_time_I1.append(point)
				temp_465nm_I1.append(imported_data['465nm'][point_num])
				temp_405nm_I1.append(imported_data['405nm'][point_num])
				temp_405nm_fitted_I1.append(imported_data['405nm Fitted'][point_num])
				temp_dff0_I1.append(imported_data['DF/F0'][point_num])
			if point >= (start_ts - 1) and point <= end_ts and (point - start_ts <= 3):
				if imported_data['Event Type'][item_num] == 'J':
					temp_time_J.append(point)
					temp_465nm_J.append(imported_data['465nm'][point_num])
					temp_405nm_J.append(imported_data['405nm'][point_num])
					temp_405nm_fitted_J.append(imported_data['405nm'][point_num])
					temp_dff0_J.append(imported_data['DF/F0'][point_num])
				if imported_data['Event Type'][item_num] == 'O':
					temp_time_O.append(point)
					temp_465nm_O.append(imported_data['465nm'][point_num])
					temp_405nm_O.append(imported_data['405nm'][point_num])
					temp_405nm_fitted_O.append(imported_data['405nm'][point_num])
					temp_dff0_O.append(imported_data['DF/F0'][point_num])
				if imported_data['Event Type'][item_num] == 'C':
					temp_time_C.append(point)
					temp_465nm_C.append(imported_data['465nm'][point_num])
					temp_405nm_C.append(imported_data['405nm'][point_num])
					temp_405nm_fitted_C.append(imported_data['405nm Fitted'][point_num])
					temp_dff0_C.append(imported_data['DF/F0'][point_num])
			if point > end_ts and point < (next_ts - 1) and (point - start_ts <= 3):
				temp_time_I2.append(point)
				temp_465nm_I2.append(imported_data['465nm'][point_num])
				temp_405nm_I2.append(imported_data['405nm'][point_num])
				temp_405nm_fitted_I2.append(imported_data['405nm Fitted'][point_num])
				temp_dff0_I2.append(imported_data['DF/F0'][point_num])
		if item_num > 0:
			if point >= (start_ts - 1) and point <= end_ts and (point - start_ts <= 3):
				if imported_data['Event Type'][item_num] == 'J':
					temp_time_J.append(point)
					temp_465nm_J.append(imported_data['465nm'][point_num])
					temp_405nm_J.append(imported_data['405nm'][point_num])
					temp_405nm_fitted_J.append(imported_data['405nm Fitted'][point_num])
					temp_dff0_J.append(imported_data['DF/F0'][point_num])
				if imported_data['Event Type'][item_num] == 'O':
					temp_time_O.append(point)
					temp_465nm_O.append(imported_data['465nm'][point_num])
					temp_405nm_O.append(imported_data['405nm'][point_num])
					temp_405nm_fitted_O.append(imported_data['405nm Fitted'][point_num])
					temp_dff0_O.append(imported_data['DF/F0'][point_num])
				if imported_data['Event Type'][item_num] == 'C':
					temp_time_C.append(point)
					temp_465nm_C.append(imported_data['465nm'][point_num])
					temp_405nm_C.append(imported_data['405nm'][point_num])
					temp_405nm_fitted_C.append(imported_data['405nm Fitted'][point_num])
					temp_dff0_C.append(imported_data['DF/F0'][point_num])
			if point > end_ts and point < (next_ts - 1) and (point - start_ts <= 3):
				temp_time_I2.append(point)
				temp_465nm_I2.append(imported_data['465nm'][point_num])
				temp_405nm_I2.append(imported_data['405nm'][point_num])
				temp_405nm_fitted_I2.append(imported_data['405nm Fitted'][point_num])
				temp_dff0_I2.append(imported_data['DF/F0'][point_num])
	if temp_465nm_J != [] and (temp_time_J[-1] - temp_time_J[0]) >= 3:
		extracted_data['465nm J'].append(temp_465nm_J)
	if temp_465nm_O != [] and (temp_time_O[-1] - temp_time_O[0]) >= 3:
		extracted_data['465nm O'].append(temp_465nm_O)
	if temp_465nm_C != [] and (temp_time_C[-1] - temp_time_C[0]) >= 3:
		extracted_data['465nm C'].append(temp_465nm_C)
	if temp_465nm_I1 != [] and (temp_time_I1[-1] - temp_time_I1[0]) >= 3:
		extracted_data['465nm I'].append(temp_465nm_I1)
	if temp_465nm_I2 != [] and (temp_time_I2[-1] - temp_time_I2[0]) >= 3:
		extracted_data['465nm I'].append(temp_465nm_I2)
	if temp_405nm_J != [] and (temp_time_J[-1] - temp_time_J[0]) >= 3:
		extracted_data['405nm J'].append(temp_405nm_J)
	if temp_405nm_O != [] and (temp_time_O[-1] - temp_time_O[0]) >= 3:
		extracted_data['405nm O'].append(temp_405nm_O)
	if temp_405nm_C != [] and (temp_time_C[-1] - temp_time_C[0]) >= 3:
		extracted_data['405nm C'].append(temp_405nm_C)
	if temp_405nm_I1 != [] and (temp_time_I1[-1] - temp_time_I1[0]) >= 3:
		extracted_data['405nm I'].append(temp_405nm_I1)
	if temp_405nm_I2 != [] and (temp_time_I2[-1] - temp_time_I2[0]) >= 3:
		extracted_data['405nm I'].append(temp_405nm_I2)
	if temp_405nm_fitted_J != [] and (temp_time_J[-1] - temp_time_J[0]) >= 3:
		extracted_data['405nm Fitted J'].append(temp_405nm_fitted_J)
	if temp_405nm_fitted_O != [] and (temp_time_O[-1] - temp_time_O[0]) >= 3:
		extracted_data['405nm Fitted O'].append(temp_405nm_fitted_O)
	if temp_405nm_fitted_C != [] and (temp_time_C[-1] - temp_time_C[0]) >= 3:
		extracted_data['405nm Fitted C'].append(temp_405nm_fitted_C)
	if temp_405nm_fitted_I1 != [] and (temp_time_I1[-1] - temp_time_I1[0]) >= 3:
		extracted_data['405nm Fitted I'].append(temp_405nm_fitted_I1)
	if temp_405nm_fitted_I2 != [] and (temp_time_I2[-1] - temp_time_I2[0]) >= 3:
		extracted_data['405nm Fitted I'].append(temp_405nm_fitted_I2)
	if temp_dff0_J != [] and (temp_time_J[-1] - temp_time_J[0]) >= 3:
		extracted_data['DF/F0 J'].append(temp_dff0_J)
	if temp_dff0_O != [] and (temp_time_O[-1] - temp_time_O[0]) >= 3:
		extracted_data['DF/F0 O'].append(temp_dff0_O)
	if temp_dff0_C != [] and (temp_time_C[-1] - temp_time_C[0]) >= 3:
		extracted_data['DF/F0 C'].append(temp_dff0_C)
	if temp_dff0_I1 != [] and (temp_time_I1[-1] - temp_time_I1[0]) >= 3:
		extracted_data['DF/F0 I'].append(temp_dff0_I1)
	if temp_dff0_I2 != [] and (temp_time_I2[-1] - temp_time_I2[0]) >= 3:
		extracted_data['DF/F0 I'].append(temp_dff0_I2)	
	if temp_time_J != [] and (temp_time_J[-1] - temp_time_J[0]) >= 3:
		extracted_data['Time J'].append(temp_time_J)	
	if temp_time_O != [] and (temp_time_O[-1] - temp_time_O[0]) >= 3:
		extracted_data['Time O'].append(temp_time_O)
	if temp_time_C != [] and (temp_time_C[-1] - temp_time_C[0]) >= 3:
		extracted_data['Time C'].append(temp_time_C)
	if temp_time_I1 != [] and (temp_time_I1[-1] - temp_time_I1[0]) >= 3:
		extracted_data['Time I'].append(temp_time_I1)
	if temp_time_I2 != [] and (temp_time_I2[-1] - temp_time_I2[0]) >= 3:
		extracted_data['Time I'].append(temp_time_I2)
		
pickle.dump(extracted_data,open('extracted_data.pkl','wb'))