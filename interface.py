#!/goinfre/rfrancis/.brew/bin
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    interface.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rfrancis <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/11/15 15:40:13 by rfrancis          #+#    #+#              #
#    Updated: 2017/11/18 14:54:30 by rfrancis         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
from ConfigDataSources.ConfigData import *
import subprocess as sp
import sys
import task 

def create_tasks(dictions):
	tasks = []
	for i in dictions:
		tasks.append(task.Task(dictions[i]))
	return tasks


class Interface:
	def __init__(self, config=ConfigData()):
		
		tmp = sp.call("clear", shell=True)
		print ("TASKMASTER!!")
		self.loop = False
	#	print (config.data)
		self.task_list = task.TaskManager(create_tasks(config.data))
		self.config = config
		for process in config.data:
			if config.data[process]["AUTO_S"] == "true":
				self.start(process)
	def exit(self):
		self.stop_all()
		self.loop = False

	def start(self, cmd):
		if str(cmd) in self.config.data.keys():
			self.task_list.start(cmd)
		else:
			print ("That is not a known process")

	def stop(self, cmd, flag):
		if str(cmd) in self.config.data.keys():
			self.task_list.stop(cmd)
		else:
			print ("That is not a known process")

	def restart(self, cmd):
		if str(cmd) in self.config.data.keys():
			self.stop(cmd)
			self.start(cmd)
		else:
			print ("That is not a known process")

	def status(self):
		if not self.config.data:
			print ("No config file loaded, no process info to display")
		else:
			self.task_list.status()

	def loadfile(self, cmd):
		self.config.load_data(cmd)
		for diff in self.config.changed_processes:
			self.stop(diff, True)

	def stop_all(self):
		for process in self.config.data:
			self.stop(process, False)
	
	def help(self):
		print ("The commands that this shell can run are:" +
				"\nstart process_name \nstop process_name \nstop_all" +
				"\nrestart process_name" +
				"\nloadfile file_name \nstatus \nexit")

	def run(self):
		self.loop = True
		while self.loop:
			cmd = str(input(">>")).split(" ")
			if cmd[0] == "start":
				if len(cmd) > 1:
					self.start(cmd[1])
				else:
					print ("No process specified!")
			elif cmd[0] == "stop":
				if len(cmd) > 1:
					self.stop(cmd[1], False)
				else:
					print ("No process specified!")
			elif cmd[0] == "restart":
				if len(cmd) > 1:
					self.restart(cmd[1])
				else:
					print ("No process specified!")
			elif cmd[0] == "status":
				self.status()
			elif cmd[0] == "loadfile":
				if len(cmd) > 1:
					self.loadfile(cmd[1])
				else:
					print ("No config file specified!")
			elif cmd[0] == "help":
				self.help()
			elif cmd[0] == "clear" and len(cmd) == 1:
				tmp = sp.call("clear", shell=True)
				print ("TASKMASTER!!")
			elif cmd[0] == "stop_all" and len(cmd) == 1:
				self.stop_all()
			elif cmd[0] == "exit" and len(cmd) == 1:
				self.exit()
			else:
				print ("Command not found!\nType help for a list of available" +
						 " commands")


if __name__ == '__main__':
	inter_loop = None
	if (len(sys.argv) > 1):
		inter_loop = Interface(config=ConfigData(sys.argv[1]))
	else:
		inter_loop = Interface()
	inter_loop.run()
