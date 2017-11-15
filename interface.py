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

class Interface:
	def __init__(self,tm):
		self.tm = tm

	def run():
		while 1:
			cmd = input(">>")
			if cmd == "start":
				tm.run()
			else if cmd == "stop":
				tm.kill()

if __name__ == '__main__':
	Interface(Taskmaster([])).run()
