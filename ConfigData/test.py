from ConfigData import *

test = ConfigData("/goinfre/lvan-gen/Documents/WTC/taskmaster/test.json")
print (test.data)
test.load_data("/goinfre/lvan-gen/Documents/WTC/taskmaster/test2.json")
print (test.changed_processes)