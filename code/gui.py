import menus
class mainGui:
	def __init__(self,bindmaker):
		self.bindmaker = bindmaker

	def run(self):
		while True:
			print("What key do you wish to create a bind to?")
			choice = menus.parenMenu(["Custom","Left Click","Right Click","Wheel Click","Wheel Up","Wheel Down","Leave Bind Maker"])
			if choice == 0:
				key = raw_input("Key name: ")
			elif choice == 1:
				key = "MOUSE1"
			elif choice == 2:
				key = "MOUSE2"
			elif choice == 3:
				key = "MOUSE3"
			elif choice == 4:
				key = "MWHEELUP"
			elif choice == 5:
				key = "MWHEELDOWN"
			elif choice == 6:
				break
			print("Choose a class:")
			choice = menus.parenMenu(["Pyro","Engineer","Medic","Spy","Custom command"])
			if choice == 0:
				choice = menus.parenMenu(["Auto W+M1","Constant attack (useful for flamethrowers)","Cancel"])
				if choice == 0:
					self.bindmaker.addAlias("+autoWM1","+forward; +attack")
					self.bindmaker.addAlias("-autoWM1","-forward; -attack")
					command = "+autoWM1"
				elif choice == 1:
					self.bindmaker.addAlias("+constAttack","+attack; +attack")
					self.bindmaker.addAlias("-constAttack","-attack; -attack")
					command = "+constAttack"
				elif choice == 2:
					continue
			elif choice == 1:
				choice = menus.parenMenu(["Quick Build","Cancel"])
				if choice == 0:
					choice = menus.parenMenu(["Sentry","Dispenser","Teleporter Entrance","Teleporter Exit","Cancel"])
					if choice == 0:
						command = "build 2 0"
					elif choice == 1:
						command = "build 0 0"
					elif choice == 2:
						command = "build 1 0"
					elif choice == 3:
						command = "build 1 1"
					elif choice == 4:
						continue;
				elif choice == 1:
					continue;
			elif choice == 2:
				choice = menus.parenMenu(["Inform your team-mates that you have Uber-Charge","Cancel"])
				if choice == 1:
					continue;
				elif choice == 0:
					command = "say_team UberCharge ready!"
			elif choice == 3:
				choice = menus.parenMenu(["Bind Disguises","Keypad Enemy Disguise Menu (ignores key chosen at start)","Cancel"])
				if choice == 2:
					continue;
				elif choice == 1:
					self.bindmaker.addBind("KP_HOME",["disguise 1 -1"])
					self.bindmaker.addBind("KP_UPARROW",["disguise 3 -1"])
					self.bindmaker.addBind("KP_PGUP",["disguise 7 -1"])
					self.bindmaker.addBind("KP_LEFTARROW",["disguise 4 -1"])
					self.bindmaker.addBind("KP_5",["disguise 6 -1"])
					self.bindmaker.addBind("KP_RIGHTARROW",["disguise 9 -1"])
					self.bindmaker.addBind("KP_END",["disguise 5 -1"])
					self.bindmaker.addBind("KP_DOWNARROW",["disguise 2 -1"])
					self.bindmaker.addBind("KP_PGDN",["disguise 8 -1"])
					self.bindmaker.addBind("KP_INS",["disguise 8 -2"])
					continue
				elif choice == 0:
					print("Which class?")
					classesNums = [1,3,7,4,6,9,5,2,8]
					choice = menus.parenMenu(["Scout","Soldier","Pyro","Demoman","Heavy","Engineer","Medic","Sniper","Spy"])
					c2 = raw_input("Disguise as enemy class?(Y/n): ")
					if len(c2) > 0:
						if c2.lower()[1] == "n":
							command = "disguise {!s} -2".format(classesNums[choice])
						else:
							command = "disguise {!s} -1".format(classesNums[choice])
					else:
						command = "disguise {!s} -1".format(classesNums[choice])
			elif choice == 4:
				command = raw_input("Command: ")
			# TO-DO: Add in most used commands for each class
			self.bindmaker.addBind(key,[command])
		self.bindmaker.dump()
