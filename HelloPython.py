import datetime
rint("Hello world!")
now = datetime.datetime.now()
print ("Current date and time is ")
print (now.strftime("%A, %d-%m-%Y : %H:%M"))
def this_fails():
   x = 1/0

try:
   this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)