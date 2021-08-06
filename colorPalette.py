import tkinter
from tkinter import *
from random import sample


def refreshing():
	colors=color_generator(66, 6)

	row=0

	for _ in range(6):
		column=0

		for _ in range(11):
			current=next(colors)
			Button(colorContainer, bg=f"#{current}", width=10, height=4, activebackground=f"#{current}").grid(row=row, column=column, padx=4, pady=4)
			Label(colorContainer, text=f"#{current}", background=f"#{current}").grid(row=row, column=column, sticky="s")
			column+=1

		row+=1

def color_generator(n0_color:int, lenghtOf:int):
	numbers="1234567890"
	alpha="ABCDEF"

	Tnumber, Talpha = True, True
	combined=""


	if Tnumber:
		combined+=numbers
	if Talpha:
		combined+=alpha


	for _ in range(n0_color):
		color="".join(sample(combined, lenghtOf))
		yield color



mainwindow = Tk()
mainwindow.resizable(False, False)
mainwindow.geometry("1000x640")
mainwindow.title("Color Generator")
#mainwindow.iconbitmap("")




title = Label(mainwindow, text="Colors", font=("", 40)).place(x=400, y=2)


colorContainer = LabelFrame(mainwindow, width=980, height=550, bd=5, borderwidth=5)
colorContainer.place(x=10, y=60)

colors=color_generator(66, 6)

row=0

for _ in range(6):
	column=0

	for _ in range(11):
		current=next(colors)
		Button(colorContainer, bg=f"#{current}", width=10, height=4, activebackground=f"#{current}").grid(row=row, column=column, padx=4, pady=4)
		Label(colorContainer, text=f"#{current}", background=f"#{current}").grid(row=row, column=column, sticky="s")
		column+=1

	row+=1


refreshBtn = Button(colorContainer, text="Refresh", command=refreshing)
refreshBtn.grid(row=row+1, column=0, columnspan=11, pady=8)





mainwindow.mainloop()
