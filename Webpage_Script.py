# PreetyTable module helps you to write HTML script using Python 
# Install PreetyTable Module using the command (Pip install PreetyTable)


import prettytable

with open("/home/ubuntu/logs/new_logs.csv", "r+") as log_data:
    list_data = log_data.readlines()                                            # Obtain list of all rows
    
table = prettytable.PrettyTable(('DATE', ' TIME', ' OWNER', ' LOGS'))           # Name the columns

for line in list_data:                                                          # Iter through list and update the rows
    y = line.split(",")
    table.add_row(y)

html_code = table.get_html_string()                                             # preetytable module creates html scrpit for the table

with open("/home/ubuntu/logs/web_logs.html", "w+") as html_file:
    html_file = html_file.write(html_code)                                      # Writes the script in the HTML file
