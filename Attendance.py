from tkinter import *
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog



mydata=[]

class attendance_system:
	def __init__(self,root):
		self.root=root
		self.root.geometry("1360x700+0+0")
		self.root.title("Attendance_Sheet")


#======== Variables ====================================================================================================		
		self.var_atten_Id=StringVar()
		self.var_atten_roll=StringVar()
		self.var_atten_name=StringVar()
		self.var_atten_dep=StringVar()
		self.var_atten_time=StringVar()
		self.var_atten_date=StringVar()
		self.var_atten_attendance=StringVar()


#======== First image ================================================================================
		img1=Image.open(r"C:\Users\sejal\Desktop\Attendance_System\Images\student3.jpg")
		img1=img1.resize((680,140),Image.ANTIALIAS)
		self.photoimg1=ImageTk.PhotoImage(img1)

		lbl_img1=Label(self.root,image=self.photoimg1)
		lbl_img1.place(x=0,y=0,width=680,height=140)

#======= Second Image =========================================================================================
		img2=Image.open(r"C:\Users\sejal\Desktop\Attendance_System\Images\student2.jpg")
		img2=img2.resize((680,140),Image.ANTIALIAS)
		self.photoimg2=ImageTk.PhotoImage(img2)

		lbl_img2=Label(self.root,image=self.photoimg2)
		lbl_img2.place(x=680,y=0,width=680,height=140)

#======= Title =======================================================================================================================
		lbl_Title=Label(self.root,text="STUDENT ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="WHITE",fg="GREEN")
		lbl_Title.place(x=0,y=140,width=1360,height=40)


		

#======== Main Frame =================================================================================================================
		Main_Frame=Frame(self.root,bd=5)
		Main_Frame.place(x=10,y=190,width=1340,height=500)

#======= left Label Frame =========================================================================================================================
		Left_Frame=LabelFrame(Main_Frame,bd=2,relief=RIDGE,bg="white",text="Student Attendance Details",font=("times new roman",12,"bold"),fg="red")
		Left_Frame.place(x=3,y=3,width=655,height=485)

		# left Frame first Image
		img3=Image.open(r"C:\Users\sejal\Desktop\Attendance_System\Images\student_Presenty.webp")
		img3=img3.resize((645,130),Image.ANTIALIAS)
		self.photoimg3=ImageTk.PhotoImage(img3)

		lbl_img3=Label(Left_Frame,image=self.photoimg3)
		lbl_img3.place(x=5,y=0,width=645,height=130)

		#======= Inside Frame
		Left_Inside_Frame=Frame(Left_Frame,bd=2,relief=RIDGE,bg="white")
		Left_Inside_Frame.place(x=3,y=135,width=645,height=325)


#====== Label and entry =========================================================================================================================
		
		# Attendance_Id
		lbl_Attendance_Id=Label(Left_Inside_Frame,text="Attendance Id: ",font=("times new roman",12,"bold"),bg="white")
		lbl_Attendance_Id.grid(row=0,column=0,padx=2,sticky=W)

		txt_Attendance_Id=ttk.Entry(Left_Inside_Frame,textvariable=self.var_atten_Id,width=20,font=("times new roman",12,"bold"))
		txt_Attendance_Id.grid(row=0,column=1,padx=2,pady=10,sticky=W)

		# Attendance_RollNo
		lbl_RollNo=Label(Left_Inside_Frame,text="Roll No: ",font=("times new roman",12,"bold"),bg="white")
		lbl_RollNo.grid(row=0,column=2,sticky=W)

		txt_Date=ttk.Entry(Left_Inside_Frame,textvariable=self.var_atten_roll,width=20,font=("times new roman",12,"bold"))
		txt_Date.grid(row=0,column=3,padx=2,pady=10,sticky=W)

		# Attendance_Name
		lbl_Name=Label(Left_Inside_Frame,text="Name: ",font=("times new roman",12,"bold"),bg="white")
		lbl_Name.grid(row=1,column=0,padx=2,sticky=W)

		txt_Name=ttk.Entry(Left_Inside_Frame,textvariable=self.var_atten_name,width=20,font=("times new roman",12,"bold"))
		txt_Name.grid(row=1,column=1,padx=2,pady=10,sticky=W)

		# Attendance_Department
		lbl_Dep=Label(Left_Inside_Frame,text="Department: ",font=("times new roman",12,"bold"),bg="white")
		lbl_Dep.grid(row=1,column=2,sticky=W)

		txt_Dep=ttk.Entry(Left_Inside_Frame,textvariable=self.var_atten_dep,width=20,font=("times new roman",12,"bold"))
		txt_Dep.grid(row=1,column=3,padx=2,pady=10,sticky=W)

		# Attendance_Time
		lbl_Time=Label(Left_Inside_Frame,text="Time: ",font=("times new roman",12,"bold"),bg="white")
		lbl_Time.grid(row=2,column=0,sticky=W)

		txt_Time=ttk.Entry(Left_Inside_Frame,textvariable=self.var_atten_time,width=20,font=("times new roman",12,"bold"))
		txt_Time.grid(row=2,column=1,padx=2,pady=10,sticky=W)

		# Attendance_Date
		lbl_Date=Label(Left_Inside_Frame,text="Date: ",font=("times new roman",12,"bold"),bg="white")
		lbl_Date.grid(row=2,column=2,sticky=W)

		txt_Date=ttk.Entry(Left_Inside_Frame,textvariable=self.var_atten_date,width=20,font=("times new roman",12,"bold"))
		txt_Date.grid(row=2,column=3,padx=2,pady=10,sticky=W)

		# Attendance
		lbl_Attendance=Label(Left_Inside_Frame,text="Attendance: ",font=("times new roman",12,"bold"),bg="white")
		lbl_Attendance.grid(row=3,column=0,sticky=W)

		combo_Gender=ttk.Combobox(Left_Inside_Frame,textvariable=self.var_atten_attendance,width=20,font=("times new roman",12,"bold"),state="readonly")
		combo_Gender["values"]=("Status","Present","Absent")
		combo_Gender.current(0)
		combo_Gender.grid(row=3,column=1,padx=2,pady=10,sticky=W)

#======= Button Left Frame1 
		btn_Frame1=Frame(Left_Inside_Frame,bd=2,relief=RIDGE)
		btn_Frame1.place(x=80,y=250,width=480,height=35)


		# Import Button
		btn_Import=Button(btn_Frame1,text="Import Csv",command=self.importCsv,width=15,font=("time new roman",12,"bold"),bg="blue",fg="white")
		btn_Import.grid(row=0,column=0,padx=1)


		# Export Button
		btn_Export=Button(btn_Frame1,text="Export Csv",command=self.exportCsv,width=15,font=("time new roman",12,"bold"),bg="blue",fg="white")
		btn_Export.grid(row=0,column=1,padx=1)


		# Update Button
		#btn_Update=Button(btn_Frame1,text="Update",width=15,font=("time new roman",12,"bold"),bg="blue",fg="white")
		#btn_Update.grid(row=0,column=2,padx=1)


		# Reset Button
		btn_Reset=Button(btn_Frame1,text="Reset",command=self.Reset_Data,width=15,font=("time new roman",12,"bold"),bg="blue",fg="white")
		btn_Reset.grid(row=0,column=3,padx=1)


#======= Right Label Frame ============================================================================================================================
		Right_Frame=LabelFrame(Main_Frame,bd=2,relief=RIDGE,bg="white",text="Attendance Details",font=("times new roman",12,"bold"),fg="red")
		Right_Frame.place(x=660,y=3,width=670,height=485)

		#===== Inside Frame
		Table_Frame=Frame(Right_Frame,bd=2,relief=RIDGE,bg="white")
		Table_Frame.place(x=5,y=5,width=660,height=455)


#====== Scrol Bar Table ==================================================================================================================================
		
		Scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
		Scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

		self.AttendanceReportTabel=ttk.Treeview(Table_Frame,column=("id","roll","name","dep","time","date","attendance"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)

		Scroll_x.pack(side=BOTTOM,fill=X)
		Scroll_y.pack(side=RIGHT,fill=Y)
		
		Scroll_x.config(command=self.AttendanceReportTabel.xview)
		Scroll_y.config(command=self.AttendanceReportTabel.yview)

		self.AttendanceReportTabel.heading("id",text="Attendance Id")
		self.AttendanceReportTabel.heading("roll",text="Roll No")
		self.AttendanceReportTabel.heading("name",text="Name")
		self.AttendanceReportTabel.heading("dep",text="Department")
		self.AttendanceReportTabel.heading("time",text="Time")
		self.AttendanceReportTabel.heading("date",text="Date")
		self.AttendanceReportTabel.heading("attendance",text="Attendance")
	
		self.AttendanceReportTabel["show"]="headings"

		self.AttendanceReportTabel.column("id",width=100)
		self.AttendanceReportTabel.column("roll",width=100)
		self.AttendanceReportTabel.column("name",width=100)
		self.AttendanceReportTabel.column("dep",width=100)
		self.AttendanceReportTabel.column("time",width=100)
		self.AttendanceReportTabel.column("date",width=100)
		self.AttendanceReportTabel.column("attendance",width=100)
		
		self.AttendanceReportTabel.pack(fill=BOTH,expand=1)

		self.AttendanceReportTabel.bind("<ButtonRelease>",self.get_cursor)


#======== Fetch data Import Button ====================================================================================================
	def FetchData(self,rows):
		self.AttendanceReportTabel.delete(*self.AttendanceReportTabel.get_children())
		for i in rows:
			self.AttendanceReportTabel.insert("",END,values=i)

		# Import Csv==================
	def importCsv(self):
		global mydata
		mydata.clear()
		fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
		
		with open(fln) as myfile:
			csvread=csv.reader(myfile,delimiter=",")
			for i in csvread:
				mydata.append(i)
			self.FetchData(mydata)

#========= Export Button ==========================================================================================================================
	
		# Export Csv ======================
	def exportCsv(self):
		try:
			if len(mydata)<1:
				messagebox.showerror("No Data","No Data Found to Export",parent=self.root)
				return False
			fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
		
			with open(fln,mode="w",newline="") as myfile:
				exp_write=csv.writer(myfile,delimiter=",")
				for i in mydata:
					exp_write.writerow(i)
				messagebox.showinfo("Data Export","Your Data is Exported to " +os.path.basename(fln) +" Successfully")
		except Exception as es:
				messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)



	def get_cursor(self,event=""):
		cursor_row=self.AttendanceReportTabel.focus()
		content=self.AttendanceReportTabel.item(cursor_row)
		rows=content["values"]

		self.var_atten_Id.set(rows[0])
		self.var_atten_roll.set(rows[1])
		self.var_atten_name.set(rows[2])
		self.var_atten_dep.set(rows[3])
		self.var_atten_time.set(rows[4])
		self.var_atten_date.set(rows[5])
		self.var_atten_attendance.set(rows[6])


#========= Reset ================================================================================================================================================================================
	
	def Reset_Data(self):
		self.var_atten_Id.set("")
		self.var_atten_roll.set("")
		self.var_atten_name.set("")
		self.var_atten_dep.set("")
		self.var_atten_time.set("")
		self.var_atten_date.set("")
		self.var_atten_attendance.set("")


if __name__ == "__main__":
	root=Tk()
	obj=attendance_system(root)
	root.mainloop()