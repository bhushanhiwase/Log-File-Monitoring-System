import subprocess                  # To run the CLI commands on pyton
import os                          # To change the directory
import time                        # Repeat a  function after an Interva
import sys                         # Exit from Infinite while loop

c = 0 

def myfunc():
    os.chdir("/var/log")           # This takes you to the log file directory
    subprocess.run("cat syslog  > /home/ubuntu/logs/templogs.txt", shell=True)  # Directly runs the command to import the logs in templogs.txt
    print("{}".format(c+1) +". "+"Files copied successfully")

while True:
    if c == 50:                    # Say we want to repeat this finction for 50 times  
        print("Exiting the code...")
        sys.exit()                  # To exit from infinite loop
    else:
        myfunc()
        with open("/home/ubuntu/logs/templogs.txt", "r+") as f:              # Reading the logs from  templogs.txt
            subprocess.run("rm /home/ubuntu/logs/new_logs.csv", shell=True)  # Removes the old logs in the new_logs.csv file so that only new logs are pesent
            for lines in f: 
                string = f.readline()
                k = "{}, {}, {}, {}".format(string[0:6], string[7:16], string[16:27], string[27:])
                with open("/home/ubuntu/logs/new_logs.csv", "a") as g:       # copy/write the latest logs from templogs.txt to new_logs.csv file in logs folder
                    g.writelines(k)
        c = c + 1
        time.sleep(300)              # Repeats the function after every 5 mins



# Doing this prcedure we get our log into new_logs.csv file




