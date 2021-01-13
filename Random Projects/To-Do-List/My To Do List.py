from tkinter import*
from random import*
from PIL import ImageTk,Image
from tkinter import messagebox

# root window
root=Tk()

# root window size
root.geometry('445x505')

# disable maximise button
root.resizable(0,0)

# root window title
root.title("My To-Do-Licon.ico")

# root window color
root.config(bg="#ECA58F")

# Title inside window
title=Label(root,text="My To-Do-List",bg="#ECA58F",font=("helvatica",18,"italic bold"))
title.pack(pady=5)

# lists for tasks and favorites
tasks=[]

fav=[]

# my_var
d=IntVar()
d.set(0)

# dark mode
def dark():
	global title
	get_value=d.get()
	if get_value==0:
		title.config(bg="#ECA58F",fg="black")
		root.config(bg="#ECA58F")
		f.config(bg="#ECA58F",fg="black")
		f1.config(bg="#ECA58F",fg="black")
		f2.config(bg="#ECA58F",fg="black")
		dark_mode.config(text="Dark Mode Off",bg="#ECA58F",fg="black")
	else:
		root.config(bg="#2B2B2B")
		title.config(fg="#BCB2B8",bg="#2B2B2B")
		f.config(bg="#2B2B2B")
		f1.config(bg="#2B2B2B",fg="#BCB2B8")
		f2.config(bg="#2B2B2B",fg="#BCB2B8")
		dark_mode.config(text="Dark Mode On",bg="#2B2B2B",fg="#BCB2B8")

# update listboxes
def update_listbox():
	clear_listbox()
	for i,j in enumerate(tasks,1):
		data=i,".", j
		listbox.insert(END,data)

def update_favorites():
	clear_favorites()
	for i in fav:
		data=chr(10084),i
		favorites.insert(END,data)

def clear_listbox():
	listbox.delete(0,END)

def clear_favorites():
	favorites.delete(0,END)

# add functionality to buttons
def add():
	global tasks
	task=str(e1.get()).capitalize()
	if (task!="") and (task not in tasks) and (task not in fav) and (len(task)<=19):
		tasks.append(str(task))
		e1.delete(0,END)
		update_listbox()
	elif task in tasks:
		messagebox.showerror("OOPS","Already exists in Tasks")
		e1.delete(0,END)
	elif task in fav:
		messagebox.showerror("OOPS","Already exists in Favorites")
		e1.delete(0,END)
	elif len(task)>19:
		messagebox.showerror("OOPS","Entry shouldn't exceed 19 characters")
	else:
		pass

def delete():
	global fav
	global tasks

	if listbox.curselection():
		active=listbox.get("active")
		active1=active[2]
		tasks.remove(active1)
		update_listbox()
	if favorites.curselection():
		active2=favorites.get("active")
		active3=active2[1]
		fav.remove(active3)
		update_favorites()


def add_to_fav():
	global fav
	task=str(e1.get()).capitalize()
	if (task!="") and (task not in tasks) and (task not in fav) and (len(task)<=19):
		fav.append(task)
		e1.delete(0,END)
	elif task in tasks:
		messagebox.showerror("OOPS","Already exists in Tasks")
		e1.delete(0,END)
	elif task in fav:
		messagebox.showerror("OOPS","Already exists in Favorites")
		e1.delete(0,END)
	elif len(task)>19:
		messagebox.showerror("OOPS","Entry shouldn't exceed 19 characters")
	else:
		pass
	update_favorites()

def delete_all_in_task():
	global tasks
	tasks=[]
	update_listbox()

def delete_all_in_fav():
	global fav
	fav=[]
	clear_favorites()

# image for buttons
myimg1=ImageTk.PhotoImage(Image.open("Add.png"))
myimg2=ImageTk.PhotoImage(Image.open("Delete.png"))
myimg3=ImageTk.PhotoImage(Image.open("fav on.png"))
#myimg4=ImageTk.PhotoImage(Image.open("Number Of Tasks.png"))
myimg5=ImageTk.PhotoImage(Image.open("exit.png"))
myimg6=ImageTk.PhotoImage(Image.open("Delete All.png"))

# Frame 1 for Buttons and Entry
f=LabelFrame(root,bg="#ECA58F",pady=14)
f.place(x=30,y=50)

# Entry widget
e1=Entry(f,width=30,bd=2,font=("helvatica",8,"bold"))
e1.grid(row=1,column=0,padx=15,pady=23)

# buttons
b1=Button(f,image=myimg1,text ="Add to Tasks",font=("helvatica",8,"bold"),compound="left",padx=20,command=add)
b1.grid(row=2,column=0,pady=10,padx=20)

b2=Button(f,image=myimg2,text ="Delete Task",font=("helvatica",8,"bold"),compound="left",padx=22,command=delete)
b2.grid(row=3,column=0,pady=10,padx=20)

b3=Button(f,image=myimg3,text ="Add to favorites",font=("helvatica",8,"bold"),compound="left",padx=15,command=add_to_fav)
b3.grid(row=4,column=0,pady=10,padx=20)

b5=Button(f,image=myimg5,text ="Exit",font=("helvatica",8,"bold"),compound="left",padx=10,command=exit)
b5.grid(row=7,column=0,pady=10,padx=20)

b6=Button(f,image=myimg6,text ="Delete All in Tasks",font=("helvatica",8,"bold"),compound="left",padx=10,command=delete_all_in_task)
b6.grid(row=5,column=0,pady=10,padx=20)

b7=Button(f,image=myimg6,text ="Delete All in Favorites",font=("helvatica",8,"bold"),compound="left",padx=5,command=delete_all_in_fav)
b7.grid(row=6,column=0,pady=10,padx=20)

# Frame for Listbox
f1=LabelFrame(root,text="Tasks",font=("helvatica",12,"bold"),bg="#ECA58F",pady=5)
f1.place(x=265,y=40)

# Listbox
listbox=Listbox(f1,font=("helvatica",10))
listbox.pack(padx=2,pady=2)

# Frame for favorites
f2=LabelFrame(root,text="Favorites",font=("helvatica",12,"bold"),bg="#ECA58F",pady=5)
f2.place(x=265,y=250)

# Listbox
favorites=Listbox(f2,font=("helvatica",10))
favorites.pack(padx=2,pady=2)

# Dark mode Button
dark_mode=Checkbutton(root,variable=d,text="Dark Mode Off",font=("helvatica",8,"bold"),bg="#ECA58F",command=dark)
dark_mode.pack()
dark_mode.place(x=290,y=465)

# mainloop()
root.mainloop()
