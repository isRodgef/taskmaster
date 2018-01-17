import subprocess
import signal
import sys
import os
import threading
import multiprocessing


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
	def start(self):
		rerun = True
		while int(self.attr['NUM']) > 0:
			print ("working")
			self.proc = subprocess.Popen([self.attr['CMD']],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,cwd =self.attr['DIR'])
			self.attr['NUM'] =  str(int(self.attr['NUM']) - 1)
		t = [self.proc] * int(self.attr['NUM'])
		STDOUT_value = str(self.proc.communicate()[0])
		rerun = False
		print (STDOUT_value)
		#print (self.attr["RESTART_NUM"], "ll")
		while int(self.attr["RESTART_NUM"]) == 0:
			if	self.attr["OUT"] == "stdout":
				print ("STDOUT:", (STDOUT_value[:len(STDOUT_value)-1]))
			else :
				fi = open(self.attr["OUT"], "w+")
				fi.write(STDOUT_value)
				fi.close()
			for i in t:
				if i.returncode != self.attr["RET_CODE"]:
					i = subprocess.Popen([self.attr['CMD']],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE ,cwd = self.attr['DIR'])
			self.attr["RESTART_NUM"] = str(int(self.attr['RESTART_NUM']) - 1)
		#print (self.attr["RESTART_NUM"])


class TaskManager:
	def __init__(self , processes):
		self.processes = processes
		self.threadList = []
		for i in self.processes:
			if i.attr["AUTO_S"]:
				threads = threading.Thread(target=i.start())
				self.threadList.append(threads)
				threads.start()

	def status(self):
		for i in self.processes:
			if i.proc.poll() == None:
			#	print (i.attr['CMD'])
				print ("alive",i.proc.pid) 
			else:
				print ("dead",i.proc.pid)
	def start(self,pname):
		for j in self.threadList:
			#if j.attr['CMD'] == pname:
			j.start()
	def stop(self,pname):
		for j in self.processes:
			if j.attr['CMD'] == pname:
				print ("POES")
				print (pname)
				j.proc.terminate()
				#os.killpg(int(j.proc.pid),signal.SIGTERM)


#class Task:
#	def __init__(self, dic):
#		self.attr = dic 
#		self.proc = None 
#		self.attr["ENV_VARS"] = str_to_dic(self.attr["ENV_VARS"])
#		self.lst = []
#		pass
#	def status(self):
#		if self.proc.poll():
#			print ("dead", self.proc.pid)
#		else :	
#			print ("alive", self.proc.pid)
#
#		pass
#	def start(self):
#		self.proc = subprocess.Popen([self.attr["CMD"], shell =True, stdout=subprocess.PIPE, stderr= subprocess.PIPE, cwd = self.attr['DIR'])
#		self.attr['NUM'] =  str(int(self.attr['NUM']) - 1)
#		while  int(self.attr["RESTART_NUM"]) >= 0:
##			
#			self.attr["RESTART_NUM"] = str(int(self.attr['RESTART_NUM']) - 1)
#		pass
#	def stop(self):
#		self.proc.kill()
#		pass

#class TaskManager:
#	def __init__(self,processes):
#		pass
#	def status(self):
#		#pass
#	def start(self):
#		pass
#	def stop(self):
#		pass



