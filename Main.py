from tkinter import *
from tkinter import ttk 
from PIL import Image,ImageTk
import os
import tkinter
from time import strftime
from datetime import datetime
from Student import Student
from Train import Train
from Face_Recognition import face_recognition
from Attendance import attendance_system
from Devloper import developer
from Help import helpp 



class Face_Recognition_system:
	def __init__(self,root):
		self.root=root
		self.root.geometry("1360x700+0+0")
		self.root.title("Face Recognition System")



		#First Image
		img=Image.open(r"C:\Users\sejal\Desktop\Attendance_System\Images\Face4.jpg")
		img=img.resize((500,130),Image.ANTIALIAS)
		self.photoimg=ImageTk.PhotoImage(img)

		lbl_img=Label(self.root,image=self.photoimg)
		lbl_img.place(x=0,y=0,width=500,height=130)


		# Second Image
		img1=Image.open(r"C:\Users\sejal\Desktop\Attendance_System\Images\Face.jpg")
		img1=img1.resize((500,130),Image.ANTIALIAS)
		self.photoimg1=ImageTk.PhotoImage(img1)

		lbl_img1=Label(self.root,image=self.photoimg1)
		lbl_img1.place(x=500,y=0,width=500,height=130)


		# Third Image
		img2=Image.open(r"C:\Users\sejal\Desktop\Attendance_System\Images\Face5.jpg")
		img2=img2.resize((500,130),Image.ANTIALIAS)
		self.photoimg2=ImageTk.PhotoImage(img2)

		lbl_img2=Label(self.root,image=self.photoimg2)
		lbl_img2.place(x=1000,y=0,width=500,height=130)


		# Title
		lbl_Title=Label(self.root,text="ATTENDENCE  SYSTEM  USING  FACE  RECOGNITION  SOFTWARE",font=("times new roman",25,"bold"),bg="white",fg="red")
		lbl_Title.place(x=0,y=130,width=1360,height=40)


		# bg Image
		img3=Image.open(r"C:\Users\sejal\Desktop\Attendance_System\Images\BGImg.jpg")
		img3=img3.resize((1360,570),Image.ANTIALIAS)
		self.photoimg3=ImageTk.PhotoImage(img3)

		bg_img=Label(self.root,image=self.photoimg3)
		bg_img.place(x=0,y=170,width=1360,height=570)

#======Buttons ===================================================================================================

		# Student Button
		img4=Image.open(r"C:\Users\sejal\Desktop\Attendance_System\Images\Student_btn.jpg")
		img4=img4.resize((250,220),Image.ANTIALIAS)
		self.photoimg4=ImageTk.PhotoImage(img4)

		button1=Button(bg_img,image=self.photoimg4,command=self.Student_Details,cursor="hand2")
		button1.place(x=100,y=20,width=250,height=200)

		button1=Button(bg_img,text="Student Details",command=self.Student_Details,font=("times new roman",15,"bold"),bg="dark blue",fg="white",cursor="hand2")
		button1.place(x=100,y=220,width=250,height=30)


		# face_Recognition Button
		img5=Image.open(r"C:\Users\sejal\Desktop\Attendance_System\Images\Face_detector.jpg")
		img5=img5.resize((250,220),Image.ANTIALIAS)
		self.photoimg5=ImageTk.PhotoImage(img5)

		button2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_recignition)
		button2.place(x=390,y=20,width=250,height=200)

		button2=Button(bg_img,text="Face Recognition",command=self.face_recignition,font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2")
		button2.place(x=390,y=220,width=250,height=30)


		# Attendance Button
		img6=Image.open(r"C:\Users\sejal\Desktop\Attendance_System\Images\Atendance.jpg")
		img6=img6.resize((250,220),Image.ANTIALIAS)
		self.photoimg6=ImageTk.PhotoImage(img6)

		button3=Button(bg_img,image=self.photoimg6,command=self.attendance_system,cursor="hand2")
		button3.place(x=680,y=20,width=250,height=200)

		button3=Button(bg_img,text="Attendance",command=self.attendance_system,font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2")
		button3.place(x=680,y=220,width=250,height=30)


		# Help Button
		img7=Image.open(r"C:\Users\sejal\Desktop\Attendance_System\Images\Help1.jpg")
		img7=img7.resize((250,220),Image.ANTIALIAS)
		self.photoimg7=ImageTk.PhotoImage(img7)

		button4=Button(bg_img,image=self.photoimg7,command=self.helpp,cursor="hand2")
		button4.place(x=970,y=20,width=250,height=200)

		button4=Button(bg_img,text="Help",command=self.helpp,font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2")
		button4.place(x=970,y=220,width=250,height=30)


		# Train Data Button
		img8=Image.open(r"C:\Users\sejal\Desktop\Attendance_System\Images\TrainData.jpg")
		img8=img8.resize((250,220),Image.ANTIALIAS)
		self.photoimg8=ImageTk.PhotoImage(img8)

		button5=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
		button5.place(x=100,y=270,width=250,height=200)

		button5=Button(bg_img,text="Train Data",command=self.train_data,font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2")
		button5.place(x=100,y=470,width=250,height=30)



		# Photos Button
		img9=Image.open(r"C:\Users\sejal\Desktop\Attendance_System\Images\Photos.jpg")
		img9=img9.resize((250,220),Image.ANTIALIAS)
		self.photoimg9=ImageTk.PhotoImage(img9)

		button6=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
		button6.place(x=390,y=270,width=250,height=200)

		button6=Button(bg_img,text="Photos",command=self.open_img,font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2")
		button6.place(x=390,y=470,width=250,height=30)
		


		# Developer Button
		img10=Image.open(r"C:\Users\sejal\Desktop\Attendance_System\Images\Devloper.jpg")
		img10=img10.resize((250,220),Image.ANTIALIAS)
		self.photoimg10=ImageTk.PhotoImage(img10)

		button7=Button(bg_img,image=self.photoimg10,command=self.developer,cursor="hand2")
		button7.place(x=680,y=270,width=250,height=200)

		button7=Button(bg_img,text="Developer",command=self.developer,font=("times new roman",15,"bold"),bg="dark blue",fg="white",cursor="hand2")
		button7.place(x=680,y=470,width=250,height=30)

		# Exit Button
		img11=Image.open(r"C:\Users\sejal\Desktop\Attendance_System\Images\Exit.jpg")
		img11=img11.resize((250,220),Image.ANTIALIAS)
		self.photoimg11=ImageTk.PhotoImage(img11)

		button8=Button(bg_img,image=self.photoimg11,command=self.iExit,cursor="hand2")
		button8.place(x=970,y=270,width=250,height=200)

		button8=Button(bg_img,text="Exit",command=self.iExit,font=("times new roman",15,"bold"),bg="blue",fg="white",cursor="hand2")
		button8.place(x=970,y=470,width=250,height=30)



#====== Time ===========================================================================================
		def time():
			string = strftime('%H:%M:%S %p')
			lbl.config(text = string)
			lbl.after(1000, time)

		lbl = Label(lbl_Title, font=('times new roman',14,'bold'),background="white",foreground="blue")
		lbl.place(x=0,y=0,width=110,height=50)
		time()








#========= Photo Button Function =====================================================================================================================
	def open_img(self):
		os.startfile("Data")


#========= Student Datail Buttons Function ===========================================================================================================
	def Student_Details(self):
		self.New_Window=Toplevel(self.root)
		self.app=Student(self.New_Window)

#========= Train Dataset Button Function ============================================================================================================
	def train_data(self):
		self.New_Window=Toplevel(self.root)
		self.app=Train(self.New_Window)

#======= Face Recognition Button function ===========================================================================================================
	def face_recignition(self):
		self.New_Window=Toplevel(self.root)
		self.app=face_recognition(self.New_Window)

#====== Attendance Button Funtion ===================================================================================================================
	def attendance_system(self):
		self.New_Window=Toplevel(self.root)
		self.app=attendance_system(self.New_Window)

#====== Developer Button Funtion ===================================================================================================================
	def developer(self):
		self.New_Window=Toplevel(self.root)
		self.app=developer(self.New_Window)


#====== Help Button Funtion ===================================================================================================================
	def helpp(self):
		self.New_Window=Toplevel(self.root)
		self.app=helpp(self.New_Window)


#====== Exit Button Function ==================================================================================================
	def iExit(self):
		self.iExit=tkinter.messagebox.askyesno("Exit","Are You sure exit this Project",parent=self.root)
		if self.iExit >0:
			self.root.destroy()
		else:
			return 






		


if __name__ == "__main__":
	root=Tk()
	obj=Face_Recognition_system(root)
	root.mainloop()

