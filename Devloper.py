from tkinter import *
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2                          #pip install openvc-python




class developer:
	def __init__(self,root):
		self.root=root
		self.root.geometry("1360x700+0+0")
		self.root.title("Developer")



#======= Title =======================================================================================================================
		lbl_Title=Label(self.root,text="DEVELOPER",font=("times new roman",30,"bold"),bg="white",fg="blue")
		lbl_Title.place(x=0,y=0,width=1360,height=45)


#======== First Image===============================================================================================================
		img=Image.open(r"C:\Users\sejal\Desktop\Attendance_System\Images\Devloper1.png")
		img=img.resize((1360,655),Image.ANTIALIAS)
		self.photoimg=ImageTk.PhotoImage(img)

		lbl_img=Label(self.root,image=self.photoimg)
		lbl_img.place(x=0,y=45,width=1360,height=655)

#====== Main Frame ============================================================================================================================
		Main_Frame=Frame(lbl_img,bd=2,bg="white")
		Main_Frame.place(x=950,y=0,width=400,height=500)


		
		# Frame Image Second ==========================

		img1=Image.open(r"C:\Users\sejal\Desktop\Attendance_System\Images\Help_Deskt.png")
		img1=img1.resize((400,300),Image.ANTIALIAS)
		self.photoimg1=ImageTk.PhotoImage(img1)

		lbl_img1=Label(Main_Frame,image=self.photoimg1)
		lbl_img1.place(x=0,y=200,width=400,height=300)



		# Frame Image First =========================

		img2=Image.open(r"C:\Users\sejal\Desktop\Attendance_System\Images\Sejal_Photo.jpeg")
		img2=img2.resize((150,200),Image.ANTIALIAS)
		self.photoimg2=ImageTk.PhotoImage(img2)

		lbl_img2=Label(Main_Frame,image=self.photoimg2)
		lbl_img2.place(x=250,y=0,width=150,height=200)



		# Information ================================

		lbl_Info=Label(Main_Frame,text="Hello, My Name is",font=("times new roman",18,"bold"),fg="black",bg="white")
		lbl_Info.place(x=0,y=0,width=250,height=50)

		lbl_Info1=Label(Main_Frame,text="Sejal Wadkar,",font=("times new roman",18,"bold"),fg="black",bg="white")
		lbl_Info1.place(x=0,y=60,width=250,height=50)

		lbl_Info1=Label(Main_Frame,text="I am Python Developer.",font=("times new roman",18,"bold"),fg="black",bg="white")
		lbl_Info1.place(x=0,y=120,width=250,height=50)






if __name__ == "__main__":
	root=Tk()
	obj=developer(root)
	root=mainloop()