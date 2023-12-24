from tkinter import *
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2                          #pip install openvc-python




class helpp:
	def __init__(self,root):
		self.root=root
		self.root.geometry("1360x700+0+0")
		self.root.title("Help desk")


#======= Title =======================================================================================================================
		lbl_Title=Label(self.root,text="HELP  DESK",font=("times new roman",30,"bold"),bg="white",fg="blue")
		lbl_Title.place(x=0,y=0,width=1360,height=45)


#======== First Image===============================================================================================================
		img=Image.open(r"C:\Users\sejal\Desktop\Attendance_System\Images\Help_Deskt.png")
		img=img.resize((1360,655),Image.ANTIALIAS)
		self.photoimg=ImageTk.PhotoImage(img)

		lbl_img=Label(self.root,image=self.photoimg)
		lbl_img.place(x=0,y=45,width=1360,height=655)


# email info
		lbl_email=Label(lbl_img,text="Email: sejalwadkar0210@gmail.com",font=("times new roman",18,"bold"),bg="white", fg="blue")
		lbl_email.place(x=0,y=0)

# email contact
		lbl_contact=Label(lbl_img,text="Contact: 7350761375",font=("times new roman",18,"bold"),bg="white", fg="blue")
		lbl_contact.place(x=40,y=40)



if __name__ == "__main__":
	root=Tk()
	obj=helpp(root)
	root=mainloop()