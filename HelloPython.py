import sys

import datetime
print("Hello world!")
now = datetime.datetime.now()
print ("Current date and time is ")
print (now.strftime("%A, %d-%m-%Y : %H:%M"))
def this_fails():
   x = 1/0
this_fails()

sys.exit(-1)