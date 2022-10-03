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

class jobs: 
	Banker = {
		"job": 'Banker',
		"money": 1600.00,
		"from": 'Boston',
		"party": [],
		"leader": "",
		"month": ""
	}
	Carpenter = {
		"job": 'Carpenter',
		"money": 800.00,
		"from": 'Ohio',
		"party": [],
		"leader": "",
		"month": ""
	}
	Farmer = {
		"job": 'Farmer',
		"money": 400.00,
		"from": 'Illinois',
		"party": [],
		"leader": "",
		"month": ""
	}

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
		os.system('cls')
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
		os.system('cls')
		print("Many kinds of people made the trip to Oregon.")
		print("You may:")
		print("	1. Be a banker from Boston")
		print("	2. Be a carpenter from Ohio")
		print("	3. Be a farmer from Illinois")
		print("	4. Find out the differences between these choices")
		choice = input("What is your choice? ")
		if (choice.find("1") != -1):
			player = jobs.Banker
		elif (choice.find("2") != -1):
			player = jobs.Carpenter
		elif (choice.find("3") != -1):
			player = jobs.Farmer
		elif (choice.find("4") != -1):
			os.system('cls')
			print(styles.yellow + styles.bold + "====================" + styles.end)
			print(styles.yellow + styles.bold + "  The Oregon Trail  " + styles.end)
			print(styles.yellow + styles.bold + "====================" + styles.end)
			print("Traveling to Oregon isn't easy! But if you're")
			print("a banker, you'll have more money for supplies")
			print("and services than a carpenter or a farmer.")
			print("")
			print("However, the harder you have to try, the more")
			print("points you deserve! Therefore, the farmer earns")
			print("the greatest number of points and the banker")
			print("earns the least.")
			print(styles.yellow + styles.bold + "====================" + styles.end)
			print(styles.bold + "Press SPACE BAR to continue")
			spaceCheck = True
			time.sleep(2)
			while spaceCheck:
				if keyboard.is_pressed(" "):
					spaceCheck = False
					os.system('cls')
					return game.startNewGame()
					break
		else:
			print("That is not a valid choice, please choose through 1 and 4")
			time.sleep(2.5)
			os.system('cls')
			game.startNewGame()
		wagonLeader = input("What is the first name of the wagon leader? ")
		os.system('cls')
		print("What are the first names of the four")
		print("other members in your party?")
		print("1. " + wagonLeader)
		wagonSecond = input("2. ")
		wagonThird = input("3. ")
		wagonFourth = input("4. ")
		wagonFifth = input("5. ")
		player["party"].append(wagonLeader)
		player["party"].append(wagonSecond)
		player["party"].append(wagonThird)
		player["party"].append(wagonFourth)
		player["party"].append(wagonFifth)
		player["leader"] = wagonLeader
		game.start2(player)

	def start2(player):
		print("It is 1848. Your jumping off place for Oregon")
		print("is Independence, Missouri. You must decide which")
		print("month to leave Independence.")
		print("	1. March")
		print("	2. April")
		print(" 3. May")
		print(" 4. June")
		print(" 5. July")
		print(" 6. Ask for advice")
		choice = input("What is your choice? ")
		if (choice.find("1") != -1):
			month = "March"
		elif (choice.find("2") != -1):
			month = "April"
		elif (choice.find("3") != -1):
			month = "May"
		elif (choice.find("4") != -1):
			month = "June"
		elif (choice.find("5") != -1):
			month = "July"
		elif (choice.find("6") != -1):
			os.system('cls')
			print("You attend a public meeting held for \"folks")
			print("with the California-Oregon fever.\" You're told:")
			print("If you leave too early, there won't be any grass")
			print("for your oxen to eat. If you leave too late,")
			print("you may not get to Oregon before winter comes.")
			print("If you leave at just the right time, there will")
			print("be green grass and the weather will still be cool.")
			print(styles.yellow + styles.bold + "====================" + styles.end)
			print(styles.bold + "Press SPACE BAR to continue")
			spaceCheck = True
			time.sleep(2)
			while spaceCheck:
				if keyboard.is_pressed(" "):
					spaceCheck = False
					os.system('cls')
					return game.start2()
					break
		else:
			print("That is not a valid choice, please choose through 1 and 6")
			time.sleep(2.5)
			os.system('cls')
			return game.start2(player)
		player["month"] = month
		print("Before leaving Independence you should")
		print("buy equipment and supplies. You have $" + str(player["money"] + "in"))
		print("cash, but you don't have to spend it all now.")
		print(styles.yellow + styles.bold + "====================" + styles.end)
		print(styles.bold + "Press SPACE BAR to continue")
		spaceCheck = True
		time.sleep(2)
		while spaceCheck:
			if keyboard.is_pressed(" "):
				spaceCheck = False
				os.system('cls')
				break
		print("You can buy whatever you need at Matt's General Store.")
		print(styles.yellow + styles.bold + "====================" + styles.end)
		print(styles.bold + "Press SPACE BAR to continue")
		spaceCheck = True
		time.sleep(1)
		while spaceCheck:
			if keyboard.is_pressed(" "):
				spaceCheck = False
				os.system('cls')
				break
		print("Hello, I'm Matt. So you're going to Oregon! I can fix")
		print("you up with what you need:")
		print("	-a team of oxen to pull your wagon")
		print("	-clothing for both summer and winter")
		print(styles.yellow + styles.bold + "====================" + styles.end)
		print(styles.bold + "Press SPACE BAR to continue")
		spaceCheck = True
		time.sleep(2)
		while spaceCheck:
			if keyboard.is_pressed(" "):
				spaceCheck = False
				os.system('cls')
				break
		print("Hello, I'm Matt. So you're going to Oregon! I can fix")
		print("you up with what you need:")
		print("	-plenty of food for the trip")
		print("	-ammunition for your rifles")
		print("	-spare parts for your wagon")
		print(styles.yellow + styles.bold + "====================" + styles.end)
		print(styles.bold + "Press SPACE BAR to continue")
		spaceCheck = True
		time.sleep(2)
		while spaceCheck:
			if keyboard.is_pressed(" "):
				spaceCheck = False
				os.system('cls')
				break
	def mattStore(player):
		print(styles.red + "=================================" + styles.end)
		print(styles.blue + "Matt's General Store\nIndependence, Missouri" + styles.end)
		print(styles.bold + player.month + " 1, 1848" + styles.end)
		print(styles.red + "=================================" + styles.end)
		print("1. Oxen			$0.00")
		print("2. Food			$0.00")
		print("3. Clothing		$0.00")
		print("4. Ammunition	$0.00")
		print("5. Spare parts	$0.00")
		print(styles.red + "=================================" + styles.end)
		print("		Total bill: $0.00")
		print("Amount you have: $" + player["money"])
		print(styles.yellow + styles.bold + "====================" + styles.end)
		item = input("Which item would you like to buy? ")
		main = styles.red + "=================================" + styles.end + styles.blue +"\nMatt's General Store\nIndependence, Missouri" + styles.end + styles.red + "\n=================================" + styles.end
		if (item.find("1") != -1):
			desc = "I recommend you take at least 200 pounds\nof food for each person in your family.\nI see that you have " + str(len(player["party"])) + " people in all.\nYou'll need flour, sugar, bacon, and coffee. My price\nis 20 cents a pound."
			descInput = "How many pounds of food do you want? "
	def buyItem(description, input, bill):
		print(description)
		print("Bill so far:" + bill)
		return input(input)

		
start.start()