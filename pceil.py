import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import dates
from datetime import datetime


f = open('/Users/laufers/data/ceilo/test.dat', 'r')
data = [x.strip() for x in f.readlines()]
araw = []
for line in data:
   if ('Logfile' not in line) and ('created' not in line) and ('DAT' not in line) and ('File Closed' not in line):
        araw.append( line )
f.close()

times = araw[::8]
cloudsRaw = araw[2::8]
info = araw[4::8]
backscatterRaw = araw[5::8]


# Clean up timestamp of when the observation was recorded. 
format1 = "-%Y-%m-%d %H:%M:%S"
obsTime = []

for t in times:
	obsTime.append(datetime.strptime(t, format1))

# Now check for clouds which can have up to three layers?
clouds = [] ; base1 = [] ; base2 = [] ; base3 = []

for line in cloudsRaw:
    c, b1, b2, b3, junk  = line.replace('/////','NaN').split(' ')
    clouds = clouds + [c]
    base1 = base1 + [b1]
    base2 = base2 + [b2]
    base3 = base3 + [b3]

# Plot cloud base (Right now plot all three.)
fig = plt.figure(figsize=(12,10))
plt.plot(obsTime, base1, 'ro')
plt.plot(obsTime, base2, 'bd')
plt.plot(obsTime, base3, 'gs')
plt.show()

# Now lets work on backscatterRaw
scale = [] ; resolution = [] ; profLen = [] ; energyPulse = []
laserTemp = [] ; windowTrans = [] ; tilt = [] ; background = []
parms = [] ; sumBackscatter = []

for line in info:
	p1, p2, p3, p4, p5, p6, p6, p7, p8, p9 = line.split(' ')
	scale = scale + [p1]
	resolution = resolution +[p2]
	profLen = profLen + [p3]
	energyPulse = energyPulse + [p4]
	windowTrans = windowTrans +[p5]
	tilt = tilt + [p6]
	background = background + [p7]
	parms = parms + [p8]
	sumBackscatter = sumBackscatter + [p9]


