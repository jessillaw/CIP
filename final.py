import time
from datetime import datetime
import pytz #for timezone

#Timesheet selections 
# 1 - Clock-in
# 2 - Start break
# 3 - End break
# 4 - Clock-out

def clock_in():
    Timecard_file = open('timecard.txt', 'a')
    #print(file)
    tz_LA = pytz.timezone('America/Los_Angeles')
    datetime_LA = datetime.now(tz_LA)
    current_date = datetime_LA.strftime("%Y-%m-%d")
    clock_in = datetime_LA.strftime("%H:%M:%S")
    

    Timecard_file.write(current_date + " ")
    Timecard_file.write(clock_in)

    print("Date:",current_date)
    print("Clocked in at:",clock_in)
    

def start_break():
    Timecard_file = open('timecard.txt', 'a')

    tz_LA = pytz.timezone('America/Los_Angeles')
    datetime_LA = datetime.now(tz_LA)
    current_date = datetime_LA.strftime("%Y-%m-%d")
    start_break = datetime_LA.strftime("%H:%M:%S")

    Timecard_file.write(current_date + " ")
    Timecard_file.write(start_break)

    print("Date:",current_date)
    print("Break started at:",start_break)
    #convert start_break time to seconds to a variable and subtract from it
    # print ("Return to work at")

    Timecard_file.close()

# punch time and countdown to clock_out
def end_break():
    Timecard_file = open('timecard.txt', 'a')

    #print(file)
    tz_LA = pytz.timezone('America/Los_Angeles')
    datetime_LA = datetime.now(tz_LA)
    current_date = datetime_LA.strftime("%Y-%m-%d")
    end_break = datetime_LA.strftime("%H:%M:%S")

    Timecard_file.write(current_date + " ")
    Timecard_file.write(end_break)

    print("Date:",current_date)
    print("Break ended at:",end_break)

    Timecard_file.close() 

def clock_out():
     
    Timecard_file = open('timecard.txt', 'a')
    #print(file)
    tz_LA = pytz.timezone('America/Los_Angeles')
    datetime_LA = datetime.now(tz_LA)
    current_date = datetime_LA.strftime("%Y-%m-%d")
    clock_out = datetime_LA.strftime("%H:%M:%S")
      

    Timecard_file.write(current_date + " ")
    Timecard_file.write(clock_out)

    print("Date:",current_date)
    print("Clocked out at:",clock_out)


print("Enter a selection:")
select = input()


if select == "1":
       clock_in()
elif select == "2":
       start_break()
elif select == "3":
        end_break()
elif select == "4":
        clock_out()
else:
        print("INVALID SELECTION")



# def countdown(t):
#     while t >=0:
#       hour = t * 60
#       mins = t // 60
#       sec = t % 60
#       timer = '{02d}:{02d}:{02d}'.format(hour,mins,secs)
#       time.sleep(1) #waits 1 sec before starts, decrement by 1 each time.
#       t -= 1
#       print("Return to work",)


# ----- OR-----

# while t >=0:
#     # in seconds
#     hour = t * 60 
#     mins = t // 60
#     secs = t % 60
#     countdown = '{:02d}:{:02d}:{:02d}'.format(hour,mins,secs)
#     print(countdown, end="\r") #overwrite previous line?
#     time.sleep(1)
#     t -= 1 
#     print("Return to work at:",start_break)
    #print(file)
