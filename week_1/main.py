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
		print(styles.yellow + styles.bold + "====================" + styles.end)
		print(styles.yellow + styles.bold + "  The Oregon Trail  " + styles.end)
		print(styles.yellow + styles.bold + "====================" + styles.end)
		# print()
		print("What about supplies? Well, if you're")
		print("low on food you can hunt. You might")
		print("get a buffalo... you might. And there")
		print("are bear in the mountains.")
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
		print("At the Dalles, you can try navigating")
		print("the Columbia River, but if running the")
		print("rapids with a makeshift raft makes you")
		print("queasy, better take the Barlow Road.")
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
		print("If for some reason you don't survive -- your")
		print("wagon burns, or thieves steal your oxen, or")
		print("you run out of provisions, or you die of")
		print("cholera -- don't give up! Try again... and")
		print("again... until your name is up with the others")
		print("on The Oregon Top Ten.")
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
		print("The software team responsible for")
		print("creation of this product includes:")
		print("Idea: Constant pressure for 17 hours of not even knowing where to start and procrastination")
		print("Guiding and new fren across this event: Pratik#6965")
		print("Actual coding: EntropicBlackhole and Google, \"a bit\" of StackOverflow, TabNine too, as Copilot is dead to me")
		print("Main Supporters: My girlfriend, my girlfriend, Pratik, and my girlfriend, Tabnine kept helping so who's a good little AI?")
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