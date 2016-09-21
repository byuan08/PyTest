import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
style.use('ggplot')

LARGE_FONT = ('Verdana', 12)

f = Figure(figsize=(5,4), dpi=100)
a = f.add_subplot(111)
def animate(i):
    pullData = open('sampleText.txt','r').read()
    dataArray = pullData.split('\n')
    xar=[]
    yar=[]
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar.append(int(x))
            yar.append(int(y))
    a.clear()
    a.plot(xar,yar)

class MyTkinterApplication(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		#tk.Tk.iconbitmap(self, default='clienticon.ico')
		tk.Tk.wm_title(self, "Application Client")


		container = tk.Frame(self)
		container.pack(side='top', fill='both', expand=True)
		container.grid_rowconfigure(0,weight=1)
		container.grid_columnconfigure(0,weight=1)

		# self.frame will be packed with a bunch of frames, with the 'top' frame being the current one
		self.frames = {}

		# instantiate objecs with for loop		
		for F in (StartPage, PageOne, PageTwo, PageThree):
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

		button = ttk.Button(self, text='Visit Page1', command=lambda: controller.show_frame(PageOne))
		button.pack()

		button2 = ttk.Button(self, text='Visite Page2', command=lambda: controller.show_frame(PageTwo))
		button2.pack()

		button3 = tk.Button(self, text='Visit Page3', command=lambda:controller.show_frame(PageThree))
		button3.pack()

class PageOne(tk.Frame):
	''' Page one'''
	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text='This is the first page', font=LARGE_FONT)

		label.pack(pady=10, padx=10)
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

class PageThree(tk.Frame):

	def __init__(self, parent, controller):

		tk.Frame.__init__(self, parent)
		label = tk.Label(self,text='Graph Page', font=LARGE_FONT)
		label.pack(pady=10, padx=10)
		button1 = ttk.Button(self,text='Back to Home', command=lambda:controller.show_frame(StartPage))
		button1.pack()
		self.create_figure()

	def create_figure(self):
		'''Create figure along with its toolbar'''

		# Figure is the actual plot
		# f = Figure(figsize=(5,5),dpi=100)
		# a = f.add_subplot(111)
		# a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

		# Canvas is the frame of the plot, it needs the frame and page to initialize
		canvas = FigureCanvasTkAgg(f,self)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

		# create toolbar that is associated with the canvas rather than the figure
		toolbar = NavigationToolbar2TkAgg(canvas, self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


if __name__ == '__main__':
	app = MyTkinterApplication()
	ani = animation.FuncAnimation(f, animate, interval=1000)
	app.mainloop()




