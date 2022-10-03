import os
import time
import keyboard

class styles:
	end = '\033[0m'
	bold = '\033[1m'
	transparent = '\033[2m'
	italics = '\033[3m'
	understrike = '\033[4m'
	throughstrike = '\033[9m'
	underline = '\033[21m'
	gray = '\033[30m'
	red = '\033[31m'
	green = '\033[32m'
	yellow = '\033[33m'
	blue = '\033[34m'
	purple = '\033[35m'
	cyan = '\033[36m'
	brown = '\033[37m'

class start:
	def start():
		print(styles.yellow + styles.bold + "====================" + styles.end)
		print(styles.yellow + styles.bold + "  The Oregon Trail  " + styles.end)
		print(styles.yellow + styles.bold + "====================" + styles.end)
		print("You may:")
		print("	1. Travel the trail")
		print("	2. Learn about the trail")
		print("	3. End")
		print("What is your choice?")
		# while True:
		# 	if keyboard.is_pressed("a"):
		# 		print('a')
		startInput = input()
		if (startInput.find("1") != -1):
			game.startNewGame()
		elif (startInput.find("2") != -1):
			start.learn()
		elif (startInput.find("3") != -1):
			exit()
		else:
			print("That is not a valid choice, please choose through 1 and 4")
			time.sleep(2.5)
			os.system('cls')
			start.start()
	def learn():
		print(styles.yellow + styles.bold + "====================" + styles.end)
		print(styles.yellow + styles.bold + "  The Oregon Trail  " + styles.end)
		print(styles.yellow + styles.bold + "====================" + styles.end)
		# print()
		print("Try taking a journey by covered wagon across 2000 miles")
		print("of plains, rivers, and mountains. Try! On the plains,")
		print("will you slosh your oxen through mud and water-filled")
		print("ruts or will you plod through dust six inches deep?")
		# print()
		print(styles.yellow + styles.bold + "====================" + styles.end)
		print(styles.bold + "Press SPACE BAR to continue")
		spaceCheck = True
		time.sleep(2)
		while spaceCheck:
			if keyboard.is_pressed(" "):
				spaceCheck = False
				os.system('cls')
				break
		print(styles.yellow + styles.bold + "====================" + styles.end)
		print(styles.yellow + styles.bold + "  The Oregon Trail  " + styles.end)
		print(styles.yellow + styles.bold + "====================" + styles.end)
		# print()
		print("How will you cross the rivers? If you have money,")
		print("you might take a ferry (if there is a ferry). Or,")
		print("you can ford the river and hope you and your wagon")
		print("aren't swallowed alive!")
		# print()
		print(styles.yellow + styles.bold + "====================" + styles.end)
		print(styles.bold + "Press SPACE BAR to continue")
		spaceCheck = True
		time.sleep(2)
		while spaceCheck:
			if keyboard.is_pressed(" "):
				spaceCheck = False
				os.system('cls')
				break
		start.start()

class game:
	def startNewGame():
		print("Starting!")
start.start()