# Log-File-Monitoring-System
A system to parse logs in the system and display it on a Web page


Aim of the project : 
- Import the system logs in a redable CSV file after every 5-mins
- Upload the Logs in the csv file on a webpage

Implementation:
1. Run the Import_system_log.py script -> This imports the system logs after defined period of time into a csv file named, new_logs.csv
2. Run the scipt Webpage_Script.py -> This reads the data in new_logs.csv file and uploads the data table to a webpage creating an HTML script

Required Installation:
- Ubuntu OS on Virtul Machine
- Install PreetyTable module in python using command (pip install PreetyTable)


--> You may see an example of imported first few logs and the obtained HTML file, after running both the scripts, in the Logs folder on the <>code page.


