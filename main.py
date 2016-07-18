# main.py - run the Bind Maker
import code.classes,code.gui;

print("Spy Bind Maker - configuration creation")
binder = code.classes.BindMaker(raw_input("Enter script output filename: "))
gui = code.gui.mainGui(binder)
gui.run()
