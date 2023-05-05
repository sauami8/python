import time as t
timenow = t.localtime()
ddate = t.time() + (2*24*60*60)+120
edate = t.localtime(t.time() + (2*24*60*60))
#time() is python clock started from 1970 show time elipsed in second, 
# here add the time in seconds like plus two day and additing additional 120 second

print("Order time ", str(timenow.tm_mday) +'/'+ str(timenow.tm_mon)+'/'+str(timenow.tm_year)
      +' '+ str(timenow.tm_hour) +':'+str(timenow.tm_min),
      " delivery date is +2 day's and expected delivery: ",
      str(edate.tm_mday) +'/'+ str(edate.tm_mon)+'/'+
      str(edate.tm_year)+' '+ str(edate.tm_hour)+':'+str(edate.tm_min))

#Time left from given time
import datetime as dt
#a= '2021-06-01'
a= ['2021-06-01'] #string or list

deadline = dt.datetime.strptime(a, "%Y-%m-%d")
settime = dt.datetime.now()
print(deadline - settime)

#current date and time
print(dt.datetime.now())
print(dt.datetime.today())

--- change in date format and display only the Days by adding another function
a= ['01-06-2021'] #string or list
deadline = dt.datetime.strptime(a[0], "%d-%m-%Y")
settime = dt.datetime.now()
v=deadline - settime
print(f"{v.days}  Days")
