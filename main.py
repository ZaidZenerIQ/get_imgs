# حط خيار للاسم
#حط خيار للpath

from tkinter import *
from get_im import get_imgs
root = Tk()
root.geometry("400x300")
output_l = Label(root, text="...")

def get_value():
	s:str = ""
	name = i1.get()
	number = i2.get()
	name_img = i3.get()
	path = i4.get()
	s = get_imgs(name,number,name_img,path)
	output_l.config(text=s)

l1 = Label(root, text="enter the name")
i1 = Entry(root, bd =5)
l2 = Label(root, text="enter the number")
i2 = Entry(root, bd =5)
l3 = Label(root, text="name of images")
i3 = Entry(root, bd =5)
l4 = Label(root, text="path to save")
i4 = Entry(root, bd =5)
button = Button(root, text="Submit",command=get_value)

#__________
l1.grid(row=0,column=0,padx=10,pady=10,ipadx=1,ipady=1)
i1.grid(row=0,column=1,padx=10,pady=10,ipadx=1,ipady=1)
l2.grid(row=1,column=0,padx=10,pady=10,ipadx=1,ipady=1)
i2.grid(row=1,column=1,padx=10,pady=10,ipadx=1,ipady=1)
l3.grid(row=2,column=0,padx=10,pady=10,ipadx=1,ipady=1)
i3.grid(row=2,column=1,padx=10,pady=10,ipadx=1,ipady=1)
l4.grid(row=3,column=0,padx=10,pady=10,ipadx=1,ipady=1)
i4.grid(row=3,column=1,padx=10,pady=10,ipadx=1,ipady=1)
button.grid(row=4,column=0,padx=10,pady=10,ipadx=1,ipady=1)
output_l.grid(row=4,column=1,padx=10,pady=10,ipadx=1,ipady=1)
root.mainloop()
