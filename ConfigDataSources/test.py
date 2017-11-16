from ConfigData import *

test = ConfigData("/goinfre/lvan-gen/Documents/WTC/taskmaster/ConfigDataSources/test.json")
#print (test.data)
test.load_data("/goinfre/lvan-gen/Documents/WTC/taskmaster/ConfigDataSources/test.json")
print ("differences: ")
print (test.changed_processes)