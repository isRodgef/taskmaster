import subprocess
import signal
import sys
import os
import threading


def str_to_dic(dic):
	d = {}
	for b in dic:
		i = b.split('=')
		d[i[0]] = i[1]
	return d
				

class Task:
	def __init__(self, dic):
		self.attr = dic
		self.proc = None
		self.attr["ENV_VARS"] = str_to_dic(self.attr["ENV_VARS"])
		print (self.attr["ENV_VARS"])
	def start(self):
		rerun = True
		while self.attr['NUM'] > 0:
			self.proc = subprocess.Popen([self.attr['CMD']],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,cwd =self.attr['DIR'])
			self.attr['NUM'] -= 1
		t = [self.proc] * self.attr['NUM']
		STDOUT_value = str(self.proc.communicate()[0])
		while rerun and self.attr["RESTART_NUM"] >= 0:
			if	self.attr["STDOUT"] == "STDOUT":
				print ("STDOUT:", (STDOUT_value[:len(STDOUT_value)-1]))
			else :
				fi = open(self.attr["STDOUT"], "w+")
				fi.write(STDOUT_value)
				fi.close()
			for i in t:
				if i.returncode != self.attr["RET_CODE"]:
					i = subprocess.Popen([self.attr['CMD']],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE ,cwd = self.attr['DIR'])
			self.attr["RESTART_NUM"] -= 1
					

class TaskManager:
	def __init__(self , processes):
		self.processes = processes
		self.threadList = []
		for i in self.processes:
			if i.attr["autostart"]:
				self.threadList = threading.Thread(target=i.start())
				self.threads.append(threadList)
				self.threadList.start()
	def status():
		for i in self.threadList:
			if self.threadList.poll():
				print ("alive",i.proc.pid) 
			else:
				print ("dead",i.proc,pid)
	def start(pname):
		for j in self.threadList:
			if j.attr['CMD'] == pname:
				j.start()
	def end(pname):
		for j in self.threadList:
			if j.attr['CMD'] == pname:
				j.proc.terminate()



