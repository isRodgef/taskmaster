# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    interface.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rfrancis <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/11/15 15:40:13 by rfrancis          #+#    #+#              #
#    Updated: 2017/11/15 15:46:29 by rfrancis         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
from ConfigDataSources.ConfigData import *
import subprocess as sp
import sys

class Interface:
    def __init__(self, config=ConfigData()):
        # self.tm = tm
        tmp = sp.call("clear", shell=True)
        print ("TASKMASTER!!")
        self.loop = False
        self.config = config
        for process in config.data:
            if config.data[process]["AUTO_S"] == "true":
                self.start(process)

    def exit(self):
        self.stop_all()
        self.loop = False

    def start(self, cmd):
            if str(cmd) in self.config.data.keys():
                print("running " + cmd + "...")
            else:
                print ("That is not a known process")

    def stop(self, cmd, flag):
            if str(cmd) in self.config.data.keys():
                print("stopping " + cmd + "...")
            else:
                print ("That is not a known process")

    def restart(self, cmd):
            if str(cmd) in self.config.data.keys():
                self.stop(cmd)
                self.start(cmd)
            else:
                print ("That is not a known process")

    def status(self):
        print ("program status")

    def loadfile(self, cmd):
        self.config.load_data(cmd)
        for diff in self.config.changed_processes:
            self.stop(diff, False)

    def stop_all(self):
        for process in self.config.data:
            self.stop(process, False)

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
                    self.stop(cmd[1], True)
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
            elif cmd[0] == "clear" and len(cmd) == 1:
                tmp = sp.call("clear", shell=True)
                print ("TASKMASTER!!")
            elif cmd[0] == "stopall" and len(cmd) == 1:
                self.stop_all()
            elif cmd[0] == "exit" and len(cmd) == 1:
                self.exit()
            else:
                print ("Command not found!")


if __name__ == '__main__':
    inter_loop = None
    if (len(sys.argv) > 1):
        inter_loop = Interface(config=ConfigData(sys.argv[1]))
    else:
        inter_loop = Interface()
    inter_loop.run()
