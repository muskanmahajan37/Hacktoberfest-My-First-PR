from tkinter import *
root = Tk()
root.title("menus")
root.geometry("300x300")
menu1 = Menu(root)
root.config(menu =menu1)
submenu= Menu(menu1)
menu1.add_cascade(label ="file", menu =submenu)
submenu= Menu(menu1)
submenu.add_command(label = "filename")
submenu.add_command(label= "filename")
submenu.add_command(label = "new project")
submenu.add_command(label = "save as")
submenu.add_command(label= "save")
submenu.add_command(label = "settings")
submenu.add_command(label= "Exit")
root.mainloop()

