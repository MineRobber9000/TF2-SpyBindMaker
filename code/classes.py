class BindMaker:
	def __init__(self, filename):
		self.filename = filename
		self.binds = []

	def addBind(self, key, commands):
		self.binds.append(Bind(key,commands))

	def dump(self):
		lines = ["// made with TF2-SpyBindMaker","// https://github.com/MineRobber9000/TF2-SpyBindMaker"]
		for bind in self.binds:
			lines.append(bind.output())
		with open(self.filename,"wb") as f:
			f.write("\r\n".join(lines)+"\r\n")

class Bind:
	def __init__(self,key,commands):
		self.details = [key, "; ".join(commands)]

	def output(self):
		return 'bind "{!s}" "{!s}"'.format(*self.details)
