import time
from datetime import date

for i in range(977745600,977918400,86400):
	print str(int(time.mktime(date.fromtimestamp(i).timetuple())))

