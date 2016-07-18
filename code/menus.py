def parenMenu(choices,prompt="> "):
	i = 0
	for item in choices:
		i += 1
		print("{!s}) {!s}".format(i,item))
	while True:
		try:
			choice = int(raw_input(prompt))
			choice -= 1
			if choice in [x for x in range(0,len(choices))]:
				return choice
		except:
			continue
