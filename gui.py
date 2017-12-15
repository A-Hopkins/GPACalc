"""
GPACalc
Alex
3/4/2017

This file contains the class that handles the GUI of the program, GPACalc.

Functions included:
	createWidgets -- which handles the creation of all the widgets displayed.
	validateCred -- restricts the credit hour Entry field to only accept numbers from 1 - 10.
	validateGrade -- restricts the grade Entry field to only accept the letters a,b,c,d,f and its caps variants.
	caps -- produces the capitalized entry of the grade Entry field.
	add -- adds the Entry fields of both credText and gradeText to the Listbox.
	delete -- deletes the Listbox entries that are selected.
	calculate -- performs the operations needed to calculate the GPA, total grade points and total credit hours, See Calc
	file for more information on how.
"""

from tkinter import *
import calculate


class GUI:
	"""
	This class has everything related to the GUI of the program is in here.
	"""
	
	def __init__(self, master):
		"""
		The initialization of the main window of the GUI.

		Included in this function, is the size of the window, the title of the window, and the initialization of the
		widgets.

		parameters
		----------
		master: The main window to be initialized to.
		"""
		
		self.master = master
		master.title("GPA Calc")
		
		master.minsize(width=600, height=480)
		self.createWidgets()
	
	def createWidgets(self):
		"""
		This function is in charge of creating all the widgets on the screen.

		The function is segmented by the widgets, labels, texts, buttons, and the listbox included on the screen.
		"""
		
		# Labels ("Text")
		self.master.message = "Enter the class credit hours and your grade earned."
		self.master.label_text = StringVar()
		self.master.label_text.set(self.master.message)
		self.master.label = Label(self.master, textvariable=self.master.label_text)
		self.master.credLabel = Label(self.master, text="Credit hours:")
		self.master.gradeLabel = Label(self.master, text="Grade:")
		self.master.orLabel = Label(self.master, text="or")
		self.master.pointLabel = Label(self.master, text="Grade Points:")
		self.master.creditOutput = Label(self.master, text="Total Credits:")
		self.master.gradePointOutput = Label(self.master, text="Total Grade Points:")
		self.master.gpa = Label(self.master, text="GPA:")
		
		vcmdCred = self.master.register(self.validateCred)
		vcmdPoint = self.master.register(self.validatePoint)
		vcmdGrade = self.master.register(self.validateGrade)
		
		# Texts ("Entry fields")
		self.master.creditText = Entry(self.master, validate="key", validatecommand=(vcmdCred, '%P'), width=5)
		
		self.master.var = StringVar()
		self.master.gradeText = Entry(self.master, textvariable=self.master.var, validate="key",
		                              validatecommand=(vcmdGrade, '%P'), width=5)
		self.master.gradeText.bind("<KeyRelease>", self.caps)
		
		self.master.pointText = Entry(self.master, validate="key", validatecommand=(vcmdPoint, '%P'), width=5)
		
		self.master.creditOutputEntry = Entry(self.master, width=5)
		self.master.gradePointOutputEntry = Entry(self.master, width=5)
		self.master.gpaEntry = Entry(self.master, width=5)
		
		# Buttons
		self.master.addButton = Button(self.master, text="Add")
		self.master.addButton.bind("<Return>", self.add)
		self.master.addButton.bind("<Button-1>", self.add)
		self.master.addButton.lift(aboveThis=self.master.gradeText)
		
		self.master.addCalcButton = Button(self.master, text="Calculate!", command=self.calculate)
		self.master.addDeleteButton = Button(self.master, text='Delete', command=self.delete)
		
		# List Box
		self.master.scrollBar = Scrollbar(self.master)
		self.master.addListBox = Listbox(self.master, selectmode=EXTENDED, yscrollcommand=self.master.scrollBar.set,
		                                 width=50)
		
		# Layout Manager for Labels
		self.master.label.grid(row=0, column=0, columnspan=2)
		self.master.credLabel.grid(row=1, column=0)
		self.master.pointLabel.grid(row=1, column=2)
		self.master.orLabel.grid(row=1, column=4)
		self.master.gradeLabel.grid(row=1, column=5, sticky=W)
		
		self.master.creditOutput.grid(row=12, column=0)
		self.master.gradePointOutput.grid(row=12, column=2)
		self.master.gpa.grid(row=12, column=6)
		
		# Layout Manager for Text Fields
		self.master.creditText.grid(row=1, column=1, sticky=W)
		self.master.pointText.grid(row=1, column=3, sticky=W)
		self.master.gradeText.grid(row=1, column=6, sticky=W)
		
		self.master.creditOutputEntry.grid(row=12, column=1, sticky=W)
		self.master.gradePointOutputEntry.grid(row=12, column=4, sticky=W)
		self.master.gpaEntry.grid(row=12, column=7, sticky=W)
		
		# Layout Manager for Buttons
		self.master.addButton.grid(row=1, column=7, sticky=E)
		self.master.addCalcButton.grid(row=5, column=2)
		self.master.addDeleteButton.grid(row=5, column=0)
		
		# Layout Manager for List Box
		self.master.addListBox.grid(row=3, columnspan=8)
		self.master.scrollBar.grid(row=3, column=5)
	
	def validateCred(self, newText):
		"""
		Function to see if the entry Field of credText is valid numbers from 1 - 240.

		parameters
		----------
		:param newText:
				The text entered in the entry field for the credit hours Text.

		returns
		-------
		:return: True or False, if True entered text will work, if False, won't accept input.
		"""
		
		if not newText:
			self.master.creditHour = None
			return True
		
		try:
			text = int(newText)
			if 1 <= text <= 240:
				self.master.creditHour = text
				return True
			else:
				return False
		except ValueError:
			return False
	
	def validatePoint(self, newText):
		"""
		Function to see if the entry Field of pointText is valid numbers from 1 - 960.

		parameters
		----------
		:param newText:
				The text entered in the entry field for the grade points Text.

		returns
		-------
		:return: True or False, if True entered text will work, if False, won't accept input.
		"""
		
		if self.master.gradeText.get():
			return False
		
		if not newText:
			self.master.point = None
			return True
		
		try:
			text = int(newText)
			if 1 <= text <= 960:
				self.master.point = text
				return True
			else:
				return False
		except ValueError:
			return False
	
	def validateGrade(self, newText):
		"""
		Function to see if the entry Field of gradeText is valid entry.

		Valid entry is included as A, B, C, D, F and all lowercase forms, note: although this function accepts lowercase
		the entry will always be converted to uppercase.

		parameters
		----------
		:param newText:
				The text entered in the entry field for the grade Text.

		returns
		-------
		:return: True or False, if True entered text will work, if False, won't accept input.
		"""
		
		if self.master.pointText.get():
			return False
		
		if not newText:
			self.master.grade = None
			return True
		
		try:
			if newText in calculate.grades:
				self.master.grade = newText.upper()
				
				return True
			
			else:
				return False
		
		except ValueError:
			return False
	
	def caps(self, event):
		"""
		Capitalizes the entries of Entry Fields, of text variable currently used in the gradeText Entry field.

		Parameters
		----------
		:param event:
				scans for the pressed key release event

		returns
		-------
		:return: No returns, but does convert the Entry Field applied to to uppercase entry.
		"""
		self.master.var.set(self.master.var.get().upper())
	
	def add(self, event):
		"""
		Add the text fields of Credit Hours and Grade Entry fields to the List Box
		Note: the weird spacing is due to the Listbox not accepting \t formatting
		"""
		
		if self.master.creditText.get() and self.master.gradeText.get():
			self.master.addListBox.insert(END, "%s hrs                   %s" % (self.master.creditText.get(),
			                                                                    self.master.gradeText.get()))
		elif self.master.creditText.get() and self.master.pointText.get():
			self.master.addListBox.insert(END, "%s hrs                   %s" % (self.master.creditText.get(),
			                                                                    self.master.pointText.get()))
	
	def delete(self):
		"""
		Deletes the selected entries in the listbox.
		"""
		
		items = self.master.addListBox.curselection()
		pos = 0
		
		for i in items:
			idx = int(i) - pos
			self.master.addListBox.delete(idx, idx)
			pos += 1
	
	def calculate(self):
		"""
		Calculates the entirety of the listbox, summing the total credit hrs, the total grade points, and the gpa.

		takes the listbox contents and outputs the results onto the gui. See the calculate module for more information
		on how the gpa and summations are being calculated.
		"""
		
		items = self.master.addListBox.get(0, END)
		
		totalCredits = calculate.totalCredits(items)
		totalGradePoints = calculate.totalGradePoint(items)
		gpa = calculate.gpaCalc(items)
		
		self.master.creditOutputEntry.delete(0, END)
		self.master.gradePointOutputEntry.delete(0, END)
		self.master.gpaEntry.delete(0, END)
		
		self.master.creditOutputEntry.insert(0, totalCredits)
		self.master.gradePointOutputEntry.insert(0, totalGradePoints)
		self.master.gpaEntry.insert(0, gpa)
