import time,datetime
'''
now = int(time.time())     
timeArray = time.localtime(now)
print(timeArray)
otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
print(otherStyleTime )
'''

timeStamp =  1582427860422/1000 #时间轴
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)   # 2013--10--10 23:40:00
