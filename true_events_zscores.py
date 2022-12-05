import sys
import random
import pandas as pd
import statistics
sys.path.append(sys.argv[3])

file_handle = sys.argv[1]
save_handle = sys.argv[2]

#Import data from .csv (ROW1 = COL Titles, COL1 = Time (s), COL2-END =  Event DF/F0)
time = []
col_titles = []
for line_num, line in enumerate(open(file_handle)):
    line = line.strip().split(',')
    if line_num == 0:
        events = [[] for i in range(len(line)-1)]
        for point_num, point in enumerate(line):
            if point_num > 0:
                col_titles.append(point)
    else:
        if line[0] != '':
            time.append(float(line[0]))
        for point_num, point in enumerate(line):
            if point_num != 0 and point != '':
                events[point_num - 1].append(float(point))
                
#Output raw data for events
df = pd.DataFrame(events).T
df.columns = col_titles
df.to_csv(save_handle[:-4] + ' raw event traces.csv', index = False)

#Calculate Zscores for random sample traces
dff_zscores = [[] for i in range(len(events))]
dff_prepost_zscores = [[],[],[]]

for line_num, line in enumerate(events):
    temp_base = []
    temp_avg = []
    temp_stdev = []
    temp_pre = []
    temp_post = []
    for point_num, point in enumerate(time):
        if point < 0:
            temp_base.append(line[point_num])
    temp_avg = statistics.mean(temp_base)
    temp_stdev = statistics.stdev(temp_base)
    for point in line:
        dff_zscores[line_num].append((point - temp_avg)/temp_stdev)
    for point_num, point in enumerate(dff_zscores[line_num]):
        if time[point_num] < 0:
            temp_pre.append(point)
        if time[point_num] >= 0 and time[point_num] <= 3:
            temp_post.append(point)
    dff_prepost_zscores[0].append(col_titles[line_num])
    dff_prepost_zscores[1].append(statistics.mean(temp_pre))
    dff_prepost_zscores[2].append(statistics.mean(temp_post))

#Output event zscore traces and means
df = pd.DataFrame(dff_zscores).T
df.columns = col_titles
df.to_csv(save_handle[:-4] + ' event dff0 zscores.csv', index = False)
df = pd.DataFrame(dff_prepost_zscores).T
df.columns = ['Event ID', 'Baseline Mean DF/F0 Zscore', 'Event Mean DF/F0 Zscore']
df.to_csv(save_handle[:-4] + ' pre-post zscore calcs.csv', index = False)
