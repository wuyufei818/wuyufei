import re
count=0
filepointer=open("log_files/201811113009.log","r")
for line in filepointer.readlines()
    if(re.split("[0-9]{12}",line)):
        count=count+1
    print(count)
