#REV: 9-21-22, TF
#Collects event traces for 465nm and 405nm for all events and between time.
#Response to reviews for Rubing/Susanna rebuttal Paper

import os
import subprocess

#OPTIONS
input_folder = 'C:/Users/Tim/Documents/Python/Rubing/input_folder'
output_folder = 'C:/Users/Tim/Documents/Python/Rubing/output_folder'
udf_path = 'C:/Users/Tim/Documents/Python/UDFs'

#Main wrapper loop
input_files = os.listdir(input_folder)

for file_name in input_files:
	print('Processing: ' + file_name + '...')
	file_handle = input_folder + '/' + file_name
	save_handle = output_folder + '/' + file_name
	subprocess.call(['python', 'between_time_import.py', file_handle, save_handle])
	subprocess.call(['python', 'between_time_extract.py', file_handle, save_handle, udf_path, 'imported_data.pkl'])
	subprocess.call(['python', 'between_time_calc.py', file_handle, save_handle, udf_path, 'extracted_data.pkl', 'imported_data.pkl'])
	subprocess.call(['python', 'between_time_calc_avg_events.py', file_handle, save_handle, udf_path, 'extracted_data.pkl', 'imported_data.pkl'])
print('Done')