import time
from datetime import datetime

#Timesheet selections 
# 1 - Clock-in
# 2 - Start break
# 3 - End break
# 4 - Clock-out

def clock_in():
    Timecard_file = open('timecard.txt', 'a')
    now = datetime.now()
    local = time.localtime()
    #print(file)
    current_date = now.strftime("%Y-%m-%d")
    clock_in = time.strftime("%H:%M:%S",local)
    #clock_in = now.strftime("%H:%M:%S")

    Timecard_file.write(current_date + " ")
    Timecard_file.write(clock_in)

    print("Date:",current_date)
    print("Clocked in at:",clock_in)
    

def start_break():
    Timecard_file = open('timecard.txt', 'a')

    now = datetime.now()
    #print(file)
    current_date = now.strftime("%Y-%m-%d")
    start_break = now.strftime("%H:%M:%S")

    Timecard_file.write(current_date + " ")
    Timecard_file.write(start_break)

    print("Date:",current_date)
    print("Break started at:",start_break)

    Timecard_file.close()

# punch time and countdown to clock_out
def end_break():
    Timecard_file = open('timecard.txt', 'a')

    now = datetime.now()
    #print(file)
    current_date = now.strftime("%Y-%m-%d")
    end_break = now.strftime("%H:%M:%S")

    Timecard_file.write(current_date + " ")
    Timecard_file.write(end_break)

    print("Date:",current_date)
    print("Break ended at:",end_break)

    Timecard_file.close() 

def clock_out():
     
     Timecard_file = open(timecard.txt, 'a')


print("Enter a selection:")
select = input()


if select == "1":
       print("clock_in")
       clock_in()
elif select == "2":
       print("start_break")
       start_break()
elif select == "3":
        print("end_break")
        end_break()
elif select == "4":
        print("clock_out")
        clock_out()
else:
        print("INVALID SELECTION")
