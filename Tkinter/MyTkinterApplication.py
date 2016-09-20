import tkinter as tk

LARGE_FONT = ('Verdana', 12)

class MyTkinterApplication(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		container = tk.Frame(self)
		container.pack(side='top', fill='both', expand=True)
		container.grid_rowconfigure(0,weight=1)
		container.grid_columnconfigure(0,weight=1)

		# self.frame will be packed with a bunch of frames, with the 'top' frame being the current one
		self.frames = {}

		# instantiate objecs with for loop		
		for F in (StartPage, PageOne, PageTwo):
			frame = F(container, self)

			# add each frame to self.frames dictionary
			self.frames[F] = frame
			# "nsew" corresponds to directions (north, south, east, west).
			# The idea of sticky is like alignment, with a slight change of stretching. 
			# So if you aligned something e, then the widget would be to the right. 
			#If you said sticky="ew," then the widget would stretch from the left to right side. 
			#If you sticky "nsew" like we have, then the widget will be encouraged to fill the entire space allotted.
			frame.grid(row=0,column=0,sticky='nsew')
		
		self.show_frame(StartPage)


	def show_frame(self, controller):
		frame = self.frames[controller]

		# Bring the frame to the top for user to see
		frame.tkraise()

class StartPage(tk.Frame):
	''' Start Page class which inherits from tk.Frame'''
	def __init__(self, parent, controller):

		# other ways to invoke super class constructor???
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text='This is the start page', font=LARGE_FONT)

		# padding on x and y to add empty space on the edge of things to look not cluttered
		label.pack(pady=10,padx=10)

		button = tk.Button(self, text='Visit Page1', command=lambda: controller.show_frame(PageOne))
		button.pack()

		button2 = tk.Button(self, text='Visite Page2', command=lambda: controller.show_frame(PageTwo))
		button2.pack()

class PageOne(tk.Frame):
	''' Page one'''
	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text='This is the first page', font=LARGE_FONT)

		label.pack()
		button = tk.Button(self,text='Visit Start Page', command=lambda: controller.show_frame(StartPage))
		button.pack()

		button2 = tk.Button(self,text = 'Visit Page Two', command=lambda:controller.show_frame(PageTwo))
		button2.pack()

class PageTwo(tk.Frame):
	''' Page two'''
	def __init__(self, parent, controller):

		#tk.Frame.__init__(self, parent)
		tk.Frame.__init__(self, parent)
		label = tk.Label(self,text='This is the second page', font=LARGE_FONT)
		label.pack()

		button = tk.Button(self,text='Visit StartPage',command=lambda:controller.show_frame(StartPage))
		button.pack()

		button2 = tk.Button(self, text = 'Visit Page Two', command=lambda:controller.show_frame(PageTwo))
		button2.pack()

if __name__ == '__main__':
	app = MyTkinterApplication()
	app.mainloop()




