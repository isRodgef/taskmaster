import subprocess
import signal
import sys
import os
import threading


class Task:
	def __init__(self, dic):
		self.attr = dic
		self.prog = dic['prog']
		for i in dic:
			self.i = (dic[i]) 
	def run(self):
		proc = subprocess.Popen([self.prog],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		stdout_value = proc.communicate()
		print ("stdout:", (stdout_value[:len(stdout_value)-1]) , proc.returncode)
	
	

class TaskManager:
	def __init__(self , processes):
			self.processes = processes
	def run(self):
		threads = []
		for i in self.processes:
			if i.attr["autostart"]:
				t = threading.Thread(target=i.run())
				threads.append(t)
				t.start()
	

if __name__ == '__main__':
	a=  TaskManager([Task({"prog" :"ls" ,"autostart" : True }) ,Task({"prog" :"$?", "autostart" : False }) ,Task({"prog" :"pwd","autostart" : True })])
	a.run()
