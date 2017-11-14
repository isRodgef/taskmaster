from ConfigData import *

test = ConfigData("/goinfre/lvan-gen/Documents/WTC/taskmaster/ConfigData/test.json")
print (test.data)
test.load_data("/goinfre/lvan-gen/Documents/WTC/taskmaster/ConfigData/test2.json")
print (test.changed_processes)