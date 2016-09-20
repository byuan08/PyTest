import tkinter

LARGE_FONT = ('Verdana', 12)

class StartPage(tk.Frame):
	''' Start Page class which inherits from tk.Frame'''
	def __init__(self, parent, controller):

		# other ways to invoke super class constructor???
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text='This is the start page', font=LARGE_FONT)

		# padding on x and y to add empty space on the edge of things to look not cluttered
		label.pack(pady=10,padx=10)


