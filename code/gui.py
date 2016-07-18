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
			choice = menus.parenMenu(["Scout","Soldier","Pyro","Demoman","Heavy","Engineer","Medic","Sniper","Spy","Basic commands","Custom command"])
			if choice == 10:
				command = raw_input("Command: ")
			# TO-DO: Add in most used commands for each class
			self.bindmaker.addBind(key,[command])
		self.bindmaker.dump()
