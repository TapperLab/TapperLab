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
	subprocess.call(['python', 'random_time.py', file_handle, save_handle, udf_path])
	
print('Done')