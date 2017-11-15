from ConfigData import *

test = ConfigData("C:\\Users\\User\\Documents\\WTC\\taskmaster\ConfigData\\test.json")
#print (test.data)
test.load_data("C:\\Users\\User\\Documents\WTC\\taskmaster\ConfigData\\test2.json")
print ("differences: ")
print (test.changed_processes)