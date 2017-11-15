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
from ConfigData import *


class Interface:
    def __init__(self, config):
        #self.tm = tm
        self.loop = False
        self.config = config

    def exit(self):
        self.loop = False

    def run(self):
        self.loop = True
        while self.loop:
            cmd = input(">>").split(" ")
            if cmd[0] == "start":
                if len(cmd) > 1:
                    print (self.config.data.keys())
                    if str(cmd[1]) in self.config.data.keys():
                        print("running...")
                    else:
                        print ("That is not a known process")
                    # self.tm.run()
            if cmd[0] == "stop":
                print("stopping")
            if cmd[0] == "loadfile":
                if len(cmd) > 1:
                    self.config.load_data(cmd[1])
            if cmd[0] == "exit":
                self.exit()


if __name__ == '__main__':
    configData = ConfigData()
    e_loop = Interface(configData)
    e_loop.run()
