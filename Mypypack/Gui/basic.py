

from ..Sorting.Allsort import *
from tkinter import *
class initilize():
	def __init__(self):
		self.root=Tk()
		self.root.title("GUI ALL SORTINGS BY Group 1")
		self.c = Canvas(self.root, width=700, height=450, bg='black')
		self.var = IntVar()
		self.R1 = Radiobutton(self.root, text="Bubble", variable=self.var, value=1,command=self.sel,bg="purple",fg="white")
		self.R2 = Radiobutton(self.root, text="Insertion", variable=self.var, value=2,command=self.sel,bg="purple",fg="white")
		self.R3 = Radiobutton(self.root, text="Selection", variable=self.var, value=3,command=self.sel,bg="purple",fg="white")
		self.R4 = Radiobutton(self.root, text="Merge", variable=self.var, value=4,command=self.sel,bg="purple",fg="white")
		self.R5 = Radiobutton(self.root, text="Quick", variable=self.var, value=5,command=self.sel,bg="purple",fg="white")
		self.R6 = Radiobutton(self.root, text="Heap", variable=self.var, value=6,command=self.sel,bg="purple",fg="white")
		# self.R7 = Radiobutton(self.root, text="Linear", variable=self.var, value=7,command=self.sel)
		self.e=Entry(self.root,bg="brown",fg="white",width=100)
		self.mylab=Label(self.root,text="Input Array",bg="#52591F",fg="black")
		self.newlabel=Label(self.root,text="Created with❤️By Group 1",bg="black",fg="#0294A5")
		self.mylabe=Label(self.root,text="Enter the values in the Input array and then Select the technique")
	def packall(self):
		self.c.grid(row =7, column =1,columnspan=6, rowspan = 1,padx=10,pady=10)
		self.R1.grid(row=3,column=1)
		self.R2.grid(row=3,column=2)
		self.R3.grid(row=3,column=3)
		self.R4.grid(row=3,column=4)
		self.R5.grid(row=3,column=5)
		self.R6.grid(row=3,column=6)
		self.newlabel.grid(row=0,column=1,columnspan=6)
		self.e.grid(row=4,column=2,columnspan=5)
		self.mylab.grid(row=4,column=1)
		self.mylabe.grid(row=2,column=1,columnspan=6)
		self.root.mainloop()
	def sel(self):
		try:
			if mylabel34:
				mylabel34.destroy()
		except:
			hji=1
		try:
			if mylabel12:
				mylabel12.destroy()
		except:
			hji=1
		values=self.e.get()
		value=list(map(int,values.split()))
		q=self.var.get()
		type_sort=["",bubblesort,insertionsort,selectionsort,mergesort,quicksort1,heapsort]
		type_sorts=["","Bubble Sort","Insertion Sort","Selection Sort","Merge Sort","Quick Sort","Heap Sort"]
		time_comp=["","O(n^2)","O(n^2)","O(n^2)","O(n log(n))","O(n^2)","O(n log(n))"]
		def visualize(l):
			n = len(l)
			for i in range(n):
				height = l[i] * 500 / max(l)
				self.c.create_rectangle(i * 700 / n, 500 - height, (i + 1) * 700 / n, 500, fill="#824CA7")
				self.c.create_text(i * 700 / n, 0, text=str(l[i]))

		def updatecanvas(type_sort,q,value):
			self.root.update()
			self.c.delete("all")
			visualize(value)
			self.root.update()
			self.root.after(1000)
			gen=type_sort[q](value)
			for w in gen:
				self.c.delete("all")
				visualize(w)
				self.root.update()
				self.root.after(100)
			st="The worst case time complexity of "
			st+=str(type_sorts[q])
			st+="  is  "+time_comp[q]+"."

			mylabel12=Label(self.root,text=st,bg="#2E303E",fg="white")
			mylabel12.grid(row=5,column=1,columnspan=6)


		updatecanvas(type_sort,q,value)
		st="Sorted Output Array is "
		for i in value:
			st+=str(i)
			st+=" "
		mylabel34=Label(self.root,text=st,bg="grey",fg="red")
		mylabel34.grid(row=6,column=1,columnspan=6)


