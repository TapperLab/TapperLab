import sys
import random
import pandas as pd
import statistics
sys.path.append(sys.argv[3])

file_handle = sys.argv[1]
save_handle = sys.argv[2]

#Import data from .csv (COL1 = Time (s), COL2 = DF/F0)
raw_signal = []
time = []


for line_num, line in enumerate(open(file_handle)):
	if line_num > 0:
		line = line.strip().split(',')
		time.append(float(line[0]))
		raw_signal.append(float(line[1]))

#Generate timestamps for random sample times
random_start = []
for i in range(10):
	random_start.append(random.uniform(5, 149.999))
	random_start.append(random.uniform(150, 294.999))
random_start.sort()	

dff_random_signal = [[] for x in range(len(random_start))]
dff_random_time = [[] for x in range(len(random_start))]

#Extract events based on random sample times
for num_num, num in enumerate(random_start):
    temp_signal = []
    temp_time = []
    for point_num, point in enumerate(time):
        if point >= num - 1 and point <= num + 3:
            dff_random_time[num_num].append(point - num)
            dff_random_signal[num_num].append(raw_signal[point_num])

#Export random sample event data
names_df1 = ['Random Event Time ' + str(i + 1) for i in range(len(dff_random_time))]
names_df2 = ['Random Event DF/F0 ' + str(i + 1) for i in range(len(dff_random_time))]

df1 = pd.DataFrame(dff_random_time).T
df1.columns = names_df1
df2 = pd.DataFrame(dff_random_signal).T
df2.columns = names_df2
raw_output_df = pd.concat([df1, df2], axis = 1)
raw_output_df.to_csv(save_handle[:-4] + ' raw event data.csv', index = False)

#Calculate Zscores for random sample traces
dff_random_zscores = [[] for i in range(len(dff_random_time))]
dff_prepost_zscores = [[],[],[]]

for line_num, line in enumerate(dff_random_time):
    temp_base = []
    temp_avg = []
    temp_stdev = []
    temp_pre = []
    temp_post = []
    for point_num, point in enumerate(line):
        if point < 0:
            temp_base.append(dff_random_signal[line_num][point_num])
    temp_avg = statistics.mean(temp_base)
    temp_stdev = statistics.stdev(temp_base)
    for point in dff_random_signal[line_num]:
        dff_random_zscores[line_num].append((point - temp_avg)/temp_stdev)
    for point_num, point in enumerate(line):
        if point < 0:
            temp_pre.append(dff_random_zscores[line_num][point_num])
        if point >= 0:
            temp_post.append(dff_random_zscores[line_num][point_num])     
    dff_prepost_zscores[0].append('Random Event ' + str(line_num + 1))
    dff_prepost_zscores[1].append(statistics.mean(temp_pre))
    dff_prepost_zscores[2].append(statistics.mean(temp_post))

names = ['Random Event DF/F0 Zscore ' + str(i + 1) for i in range(len(dff_random_zscores))]
df = pd.DataFrame(dff_random_zscores).T
df.columns = names
df.to_csv(save_handle[:-4] + ' raw event data normalized.csv', index = False)
df = pd.DataFrame(dff_prepost_zscores).T
df.columns = ['Event Number', 'Baseline Zscore', 'Event Zscore']
df.to_csv(save_handle[:-4] + ' pre-post event zscores.csv', index = False)
