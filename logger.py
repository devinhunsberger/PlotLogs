from datetime import datetime

while(True):
    fname = input('File Name: ') + '.txt'
    try:
        with open(fname) as f:
            break
    except:
        print('File Not Found')


# Create 2d matrix
datum = []
with open(fname) as f:
    last = 0
    next(f)
    for i in f.readlines()[1:]:
        grp = i.split('\t')
        if last < int(grp[0]):
            datum.append(grp)
            last = int(grp[0])
        else:
            print(last)
            print(grp[0])
            break

# Create 1d matrix for temperature
i = 0
temp = []
while i < len(datum):
    temp.append(float(datum[i][2]))
    i += 1

# Get Max Temp
max = temp[0]
for i in temp:
    if i > max:
        max = i
maxTempDatum = 'Maximum Temp: ' + str(max)

# Get Average Temp
avgMax = 0
for i in temp:
     avgMax += i
avgMax = avgMax / (len(temp) + 1)
avgTempDatum = 'Average Temp: ' + str(avgMax)

# Create 1d time matrix
i = 0
duration = []
while i < len(datum):
    duration.append(datum[i][1])
    i += 1

# Get Video Duration
start = datetime.strptime(duration[0], '%Y-%m-%d %H:%M:%S.%f')
end = datetime.strptime(duration[len(duration)-1], '%Y-%m-%d %H:%M:%S.%f')
timeDelta = end - start
durationDatum = 'Video Duration: ' + str(timeDelta.total_seconds())

with open('LOG.txt', 'a') as f:
    f.write(fname + '\n')
    f.write(maxTempDatum + '\n')
    f.write(avgTempDatum + '\n')
    f.write(durationDatum + '\n')
    f.write('\n\n')