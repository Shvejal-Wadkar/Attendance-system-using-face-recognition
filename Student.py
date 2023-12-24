from tkinter import *
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2                          #pip install openvc-python



class Student:
	def __init__(self,root):
		self.root=root
		self.root.geometry("1360x700+0+0")
		self.root.title("Student Detail")


#======== Variables ====================================================================================================		
		self.var_dep=StringVar()
		self.var_course=StringVar()
		self.var_year=StringVar()
		self.var_sem=StringVar()
		self.var_id=StringVar()
		self.var_name=StringVar()
		self.var_roll=StringVar()
		self.var_gender=StringVar()
		self.var_phone=StringVar()
		self.var_dob=StringVar()
		self.var_email=StringVar()
		self.var_address=StringVar()


#======== First Image===============================================================================================================
		img=Image.open(r"C:\Users\sejal\Desktop\Attendance_System\Images\student3.jpg")
		img=img.resize((480,130),Image.ANTIALIAS)
		self.photoimg=ImageTk.PhotoImage(img)

		lbl_img=Label(self.root,image=self.photoimg)
		lbl_img.place(x=0,y=0,width=480,height=130)


		# Second Image
		img1=Image.open(r"C:\Users\sejal\Desktop\Attendance_System\Images\student1.jpg")
		img1=img1.resize((400,130),Image.ANTIALIAS)
		self.photoimg1=ImageTk.PhotoImage(img1)

		lbl_img1=Label(self.root,image=self.photoimg1)
		lbl_img1.place(x=480,y=0,width=400,height=130)


		# Third Image
		img2=Image.open(r"C:\Users\sejal\Desktop\Attendance_System\Images\student2.jpg")
		img2=img2.resize((480,130),Image.ANTIALIAS)
		self.photoimg2=ImageTk.PhotoImage(img2)

		lbl_img2=Label(self.root,image=self.photoimg2)
		lbl_img2.place(x=880,y=0,width=480,height=130)


#======= Title =======================================================================================================================
		lbl_Title=Label(self.root,text="STUDENT  MANAGEMENT  SYSTEM",font=("times new roman",30,"bold"),bg="red",fg="white")
		lbl_Title.place(x=0,y=130,width=1360,height=40)


#======= bg Image ====================================================================================================================
		img3=Image.open(r"C:\Users\sejal\Desktop\Attendance_System\Images\BGImg.jpg")
		img3=img3.resize((1360,570),Image.ANTIALIAS)
		self.photoimg3=ImageTk.PhotoImage(img3)

		bg_img=Label(self.root,image=self.photoimg3)
		bg_img.place(x=0,y=170,width=1360,height=570)


#====== Main Frame ============================================================================================================================
		Main_Frame=Frame(self.root,bd=5)
		Main_Frame.place(x=5,y=175,width=1350,height=520)


#======= left Label Frame =========================================================================================================================
		Left_Frame=LabelFrame(Main_Frame,bd=2,relief=RIDGE,bg="white",text="Student Information",font=("times new roman",12,"bold"),fg="red")
		Left_Frame.place(x=3,y=5,width=655,height=510)


		# left Frame first Image
		img4=Image.open(r"C:\Users\sejal\Desktop\Attendance_System\Images\Present_Mam.jpg")
		img4=img4.resize((645,130),Image.ANTIALIAS)
		self.photoimg4=ImageTk.PhotoImage(img4)

		lbl_img4=Label(Left_Frame,image=self.photoimg4)
		lbl_img4.place(x=5,y=0,width=645,height=130)


#======= Current Course Information Frame 
		Curent_Course_Frame=LabelFrame(Left_Frame,bd=2,relief=RIDGE,bg="white",text="Current Course Information",font=("times new roman",12,"bold"),fg="green")
		Curent_Course_Frame.place(x=5,y=130,width=646,height=100)


		# Department Label
		lbl_Department=Label(Curent_Course_Frame,text="Department: ",font=("times new roman",12,"bold"),bg="white")
		lbl_Department.grid(row=0,column=0,padx=2,pady=10,sticky=W)

		combo_Department=ttk.Combobox(Curent_Course_Frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
		combo_Department["values"]=("Select Department","IT","Civil","Mechanical")
		combo_Department.current(0)
		combo_Department.grid(row=0,column=1,padx=2,pady=10,sticky=W)


		# Course
		lbl_Course=Label(Curent_Course_Frame,text="Course: ",font=("times new roman",12,"bold"),bg="white")
		lbl_Course.grid(row=0,column=2,padx=2,pady=10,sticky=W)

		combo_Course=ttk.Combobox(Curent_Course_Frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
		combo_Course["values"]=("Select Course","B.CA","B.CS","MCA","BE")
		combo_Course.current(0)
		combo_Course.grid(row=0,column=3,padx=2,pady=10,sticky=W)


		# Year
		lbl_Year=Label(Curent_Course_Frame,text="Year: ",font=("times new roman",12,"bold"),bg="white")
		lbl_Year.grid(row=1,column=0,padx=2,sticky=W)

		combo_Year=ttk.Combobox(Curent_Course_Frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
		combo_Year["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
		combo_Year.current(0)
		combo_Year.grid(row=1,column=1,padx=2,sticky=W)


		# Semester
		lbl_Semester=Label(Curent_Course_Frame,text="Semester: ",font=("times new roman",12,"bold"),bg="white")
		lbl_Semester.grid(row=1,column=2,padx=2,sticky=W)

		combo_Semester=ttk.Combobox(Curent_Course_Frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),state="readonly")
		combo_Semester["values"]=("Select Semester","Sem-I","Sem-II")
		combo_Semester.current(0)
		combo_Semester.grid(row=1,column=3,padx=2,sticky=W)



#====== Class Student Information Frame
		Class_Student_Frame=LabelFrame(Left_Frame,bd=2,relief=RIDGE,bg="white",text="Class Student Information",font=("times new roman",12,"bold"),fg="green")
		Class_Student_Frame.place(x=5,y=230,width=646,height=258)


		# Student Id 
		lbl_Student_Id=Label(Class_Student_Frame,text="Student Id:",font=("times new roman",12,"bold"),bg="white")
		lbl_Student_Id.grid(row=0,column=0,padx=2,sticky=W)

		txt_Student_Id=ttk.Entry(Class_Student_Frame,textvariable=self.var_id,width=20,font=("times new roman",12,"bold"))
		txt_Student_Id.grid(row=0,column=1,padx=2,pady=10,sticky=W)


		# Student Name 
		lbl_Student_Name=Label(Class_Student_Frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
		lbl_Student_Name.grid(row=0,column=2,padx=2,sticky=W)

		txt_Student_Name=ttk.Entry(Class_Student_Frame,textvariable=self.var_name,width=28,font=("times new roman",12,"bold"))
		txt_Student_Name.grid(row=0,column=3,padx=2,pady=10,sticky=W)


		# Roll Number
		lbl_Roll_No=Label(Class_Student_Frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
		lbl_Roll_No.grid(row=1,column=0,padx=2,sticky=W)

		txt_Roll_No=ttk.Entry(Class_Student_Frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
		txt_Roll_No.grid(row=1,column=1,padx=2,sticky=W)


		# Gender
		lbl_Gender=Label(Class_Student_Frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
		lbl_Gender.grid(row=1,column=2,padx=2,sticky=W)

		combo_Gender=ttk.Combobox(Class_Student_Frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"),state="readonly")
		combo_Gender["values"]=("Select Gender","Male","Female","Other")
		combo_Gender.current(0)
		combo_Gender.grid(row=1,column=3,padx=2,sticky=W)


		# Phone No
		lbl_Phone_No=Label(Class_Student_Frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
		lbl_Phone_No.grid(row=2,column=0,padx=2,sticky=W)

		txt_Phone_No=ttk.Entry(Class_Student_Frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
		txt_Phone_No.grid(row=2,column=1,padx=2,pady=10,sticky=W)


		# Date of Birth
		lbl_DOB=Label(Class_Student_Frame,text="Date Of Birth:",font=("times new roman",12,"bold"),bg="white")
		lbl_DOB.grid(row=2,column=2,padx=2,sticky=W)

		txt_DOB=ttk.Entry(Class_Student_Frame,textvariable=self.var_dob,width=28,font=("times new roman",12,"bold"))
		txt_DOB.grid(row=2,column=3,padx=2,sticky=W)


		# Emil
		lbl_Email=Label(Class_Student_Frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
		lbl_Email.grid(row=3,column=0,padx=2,sticky=W)

		txt_Email=ttk.Entry(Class_Student_Frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
		txt_Email.grid(row=3,column=1,padx=2,sticky=W)


		# Address
		lbl_Address=Label(Class_Student_Frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
		lbl_Address.grid(row=3,column=2,padx=2,sticky=W)

		txt_Address=ttk.Entry(Class_Student_Frame,textvariable=self.var_address,width=28,font=("times new roman",12,"bold"))
		txt_Address.grid(row=3,column=3,padx=2,sticky=W)


		# Radio Buuton
		self.var_radio1=StringVar()
		radiobtn1=ttk.Radiobutton(Class_Student_Frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
		radiobtn1.grid(row=5,column=0,padx=2,pady=10)

		radiobtn2=ttk.Radiobutton(Class_Student_Frame,variable=self.var_radio1,text="No Photo Sample",value="No")
		radiobtn2.grid(row=5,column=1,padx=2,pady=10)


#======= Button Left Frame1 
		btn_Frame1=Frame(Class_Student_Frame,bd=2,relief=RIDGE)
		btn_Frame1.place(x=0,y=170,width=640,height=35)


		# Save Button
		btn_Save=Button(btn_Frame1,text="Save",command=self.Add_Data,width=15,font=("time new roman",12,"bold"),bg="blue",fg="white")
		btn_Save.grid(row=0,column=0,padx=1)


		# Update Button
		btn_Update=Button(btn_Frame1,text="Update",command=self.Update_Data,width=14,font=("time new roman",12,"bold"),bg="blue",fg="white")
		btn_Update.grid(row=0,column=1,padx=1)


		# Delete Button
		btn_Delete=Button(btn_Frame1,text="Delete",command=self.Delete_Data,width=15,font=("time new roman",12,"bold"),bg="blue",fg="white")
		btn_Delete.grid(row=0,column=2,padx=1)


		# Reset Button
		btn_Reset=Button(btn_Frame1,text="Reset",command=self.Reset_Data,width=15,font=("time new roman",12,"bold"),bg="blue",fg="white")
		btn_Reset.grid(row=0,column=3,padx=1)


#======= Button Left Frame2 
		btn_Frame2=Frame(Class_Student_Frame,bd=2,relief=RIDGE)
		btn_Frame2.place(x=0,y=205,width=640,height=30)


		# Take Photo Sample Button
		btn_Take_Photo_Sample=Button(btn_Frame2,command=self.Generte_DataSet,text="Take Photo Sample",width=31,font=("time new roman",12,"bold"),bg="blue",fg="white")
		btn_Take_Photo_Sample.grid(row=0,column=0,padx=1)

		# Update Photo Sample Button
		btn_Update_Photo_Sample=Button(btn_Frame2,text="Update Photo Sample",width=31,font=("time new roman",12,"bold"),bg="blue",fg="white")
		btn_Update_Photo_Sample.grid(row=0,column=1,padx=1)



#======= Right Label Frame ============================================================================================================================
		Right_Frame=LabelFrame(Main_Frame,bd=2,relief=RIDGE,bg="white",text="Student Details",font=("times new roman",12,"bold"),fg="red")
		Right_Frame.place(x=660,y=5,width=680,height=510)


		# Right Frame first Image
		img5=Image.open(r"C:\Users\sejal\Desktop\Attendance_System\Images\student_Presenty.webp")
		img5=img5.resize((670,130),Image.ANTIALIAS)
		self.photoimg5=ImageTk.PhotoImage(img5)

		lbl_img5=Label(Right_Frame,image=self.photoimg5)
		lbl_img5.place(x=5,y=0,width=670,height=130)


#======== Search System Frame 
		Search_Frame=LabelFrame(Right_Frame,bd=2,relief=RIDGE,bg="white",text="View Student Details & Search System",font=("times new roman",12,"bold"),fg="green")
		Search_Frame.place(x=5,y=130,width=670,height=60)


		# search By Label
		lbl_Search=Label(Search_Frame,text="Search By:",font=("times new roman",12,"bold"),bg="red",fg="white")
		lbl_Search.grid(row=0,column=0,padx=4,sticky=W)


		# Search By Combo Box
		combo_Gender=ttk.Combobox(Search_Frame,width=10,font=("times new roman",12,"bold"),state="readonly")
		combo_Gender["values"]=("Select","Roll no","Phone No")
		combo_Gender.current(0)
		combo_Gender.grid(row=0,column=1,padx=4,sticky=W)


		# Searching Entry
		txt_Search=ttk.Entry(Search_Frame,width=25,font=("times new roman",12,"bold"))
		txt_Search.grid(row=0,column=2,padx=4,sticky=W)


		# Search Button
		btn_Search=Button(Search_Frame,text="Search",width=10,font=("time new roman",12,"bold"),bg="blue",fg="white")
		btn_Search.grid(row=0,column=3,padx=4)


		# Show All Button
		btn_Show_All=Button(Search_Frame,text="Show All",width=10,font=("time new roman",12,"bold"),bg="blue",fg="white")
		btn_Show_All.grid(row=0,column=4,padx=4)



# ======= Tabel Frame
		Table_Frame=Frame(Right_Frame,bd=2,relief=RIDGE,bg="white")
		Table_Frame.place(x=5,y=190,width=670,height=300)


		# ScrollBar
		Scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
		Scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

		self.Student_Table=ttk.Treeview(Table_Frame,column=("dep","course","year","sem","id","name","roll","gender","phone","dob","email","address","photo"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)

		Scroll_x.pack(side=BOTTOM,fill=X)
		Scroll_y.pack(side=RIGHT,fill=Y)

		Scroll_x.config(command=self.Student_Table.xview)
		Scroll_y.config(command=self.Student_Table.yview)

		self.Student_Table.heading("dep",text="Department")
		self.Student_Table.heading("course",text="Course")
		self.Student_Table.heading("year",text="Year")
		self.Student_Table.heading("sem",text="Semester")
		self.Student_Table.heading("id",text="StudentId")
		self.Student_Table.heading("name",text="Name")
		self.Student_Table.heading("roll",text="RollNo")
		self.Student_Table.heading("gender",text="Gender")
		self.Student_Table.heading("phone",text="Phone")
		self.Student_Table.heading("dob",text="DOB")
		self.Student_Table.heading("email",text="Email")
		self.Student_Table.heading("address",text="Address")
		self.Student_Table.heading("photo",text="PhotoSampleStatus")
		self.Student_Table["show"]="headings"


		self.Student_Table.column("dep",width=100)
		self.Student_Table.column("course",width=70)
		self.Student_Table.column("year",width=70)
		self.Student_Table.column("sem",width=80)
		self.Student_Table.column("id",width=70)
		self.Student_Table.column("name",width=150)
		self.Student_Table.column("roll",width=70)
		self.Student_Table.column("gender",width=70)
		self.Student_Table.column("phone",width=100)
		self.Student_Table.column("dob",width=100)
		self.Student_Table.column("email",width=200)
		self.Student_Table.column("address",width=200)
		self.Student_Table.column("photo",width=150)
		
		self.Student_Table.pack(fill=BOTH,expand=1)
		self.Student_Table.bind("<ButtonRelease>",self.Get_Cursor)
		self.Fetch_Data()


# ========== Function Deaclation.......Database Connect and Show the data in Saved data in database table ====================================================================================================================

	def Add_Data(self):
		if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_sem.get()=="Select Semester" or self.var_id.get()=="" or self.var_name.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="Select Gender" or self.var_phone.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_address.get()=="" :
			messagebox.showerror("Error","All Field are Required",parent=self.root)
		else:
			try:	
				conn=mysql.connector.connect(host="localhost",username="root",password="Sejal@1999",database="attendance_system")
				my_Cursor=conn.cursor()
				my_Cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
																										self.var_dep.get(),
																										self.var_course.get(),
																										self.var_year.get(),
																										self.var_sem.get(),
																										self.var_id.get(),
																										self.var_name.get(),
																										self.var_roll.get(),
																										self.var_gender.get(),
																										self.var_phone.get(),
																										self.var_dob.get(),
																										self.var_email.get(),
																										self.var_address.get(),
																										self.var_radio1.get()
																									))
				conn.commit()
				self.Fetch_Data()
				conn.close()
				messagebox.showinfo("Success","Student details has been added Successfully!",parent=self.root)
			except Exception as es:
				messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)


#======== Fetch Data and Display the data in greedview table ====================================================================================================================================================================

	def Fetch_Data(self):
		conn=mysql.connector.connect(host="localhost",username="root",password="Sejal@1999",database="attendance_system")
		my_Cursor=conn.cursor()
		my_Cursor.execute("select * from Student")
		data=my_Cursor.fetchall()

		if len(data)!=0:
			self.Student_Table.delete(*self.Student_Table.get_children())
			for i in data:
				self.Student_Table.insert("",END,values=i)
			conn.commit()
		conn.close()


#====== get cursor And display the data taskbar ========================================================================================================================================
	
	def Get_Cursor(self,event=""):
		Cursor_focus=self.Student_Table.focus()
		content=self.Student_Table.item(Cursor_focus)
		data=content["values"]

		self.var_dep.set(data[0]),
		self.var_course.set(data[1]),
		self.var_year.set(data[2]),
		self.var_sem.set(data[3]),
		self.var_id.set(data[4]),
		self.var_name.set(data[5]),
		self.var_roll.set(data[6]),
		self.var_gender.set(data[7]),
		self.var_phone.set(data[8]),
		self.var_dob.set(data[9]),
		self.var_email.set(data[10]),
		self.var_address.set(data[11]),
		self.var_radio1.set(data[12])


#======= Update Function ======================================================================================================================

	def Update_Data(self):
		if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_sem.get()=="Select Semester" or self.var_id.get()=="" or self.var_name.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="Select Gender" or self.var_phone.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_address.get()=="" :
			messagebox.showerror("Error","All Field are Required",parent=self.root)
		else:
			try:
				Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
				if Update > 0:
					conn=mysql.connector.connect(host="localhost",username="root",password="Sejal@1999",database="attendance_system")
					my_Cursor=conn.cursor()
					my_Cursor.execute("Update student set dep=%s,course=%s,course_year=%s,sem=%s,Student_name=%s,roll=%s,gender=%s,phone=%s,dob=%s,email=%s,address=%s,photosample=%s where id=%s",(

																																											self.var_dep.get(),
																																											self.var_course.get(),
																																											self.var_year.get(),
																																											self.var_sem.get(),
																																											self.var_name.get(),
																																											self.var_roll.get(),
																																											self.var_gender.get(),
																																											self.var_phone.get(),
																																											self.var_dob.get(),
																																											self.var_email.get(),
																																											self.var_address.get(),
																																											self.var_radio1.get(),
																																											self.var_id.get()
																																										))

				else:
					if not Update:
						return
				messagebox.showinfo("Success","Student Details Successfully Update Complete",parent=self.root)
				conn.commit()
				self.Fetch_Data()
				conn.close()

			except Exception as es:
				messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

#======== Delete Function ========================================================================================================================================================================================

	def Delete_Data(self):
		if self.var_id.get()=="":
			messagebox.showerror("Error","Student Id Must be Required", parent=self.root)
		else:
			try:
				delete=messagebox.askyesno("Student Delete Page","Do you Want to Delete this Student",parent=self.root)
				if delete > 0:
					conn=mysql.connector.connect(host="localhost",username="root",password="Sejal@1999",database="attendance_system")
					my_Cursor=conn.cursor()
					sql="Delete from Student where id=%s"
					val=(self.var_id.get(),)
					my_Cursor.execute(sql,val)
				else:
					if not delete:
						return
				conn.commit()
				self.Fetch_Data()
				conn.close()
				messagebox.showinfo("Delete","Successfully Deleted Student Details",parent=self.root)

			except Exception as es:
				messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


#========= Reset ================================================================================================================================================================================
	
	def Reset_Data(self):
		self.var_dep.set("Select Department"),
		self.var_course.set("Select Course"),
		self.var_year.set("Select Year"),
		self.var_sem.set("Select Semester"),
		self.var_id.set(""),
		self.var_name.set(""),
		self.var_roll.set(""),
		self.var_gender.set("Select Gender"),
		self.var_phone.set(""),
		self.var_dob.set(""),
		self.var_email.set(""),
		self.var_address.set(""),
		self.var_radio1.set("")


#======== Genereate Data set or Take Photo Samples =========================================================================================================================

	def Generte_DataSet(self):
		if self.var_dep.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_sem.get()=="Select Semester" or self.var_id.get()=="" or self.var_name.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="Select Gender" or self.var_phone.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_address.get()=="" :
			messagebox.showerror("Error","All Field are Required",parent=self.root)
		else:
			try:				
				conn=mysql.connector.connect(host="localhost",username="root",password="Sejal@1999",database="attendance_system")
				my_Cursor=conn.cursor()
				my_Cursor.execute("Select * from student")
				myresult=my_Cursor.fetchall()
				id=0				
				for x in myresult:
					id += 1
				my_Cursor.execute("Update student set dep=%s,course=%s,course_year=%s,sem=%s,Student_name=%s,roll=%s,gender=%s,phone=%s,dob=%s,email=%s,address=%s,photosample=%s where id=%s",(

																																												self.var_dep.get(),
																																												self.var_course.get(),
																																												self.var_year.get(),
																																												self.var_sem.get(),
																																												self.var_name.get(),
																																												self.var_roll.get(),
																																												self.var_gender.get(),
																																												self.var_phone.get(),
																																												self.var_dob.get(),
																																												self.var_email.get(),
																																												self.var_address.get(),
																																												self.var_radio1.get(),
																																												self.var_id.get()==id+1
																																											))

				conn.commit()
				self.Fetch_Data()
				self.Reset_Data()
				conn.close()


				#======= Load predifined data on face frontals from opencv

				face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

				def face_cropped(img):
					gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
					faces=face_classifier.detectMultiScale(gray,1.3,5)

					# Scaling factor=1.3
					# Minimum Neighbor=5

					for (x,y,w,h) in faces:
						face_cropped=img[y:y+h,x:x+w]
						return face_cropped


				capture=cv2.VideoCapture(0)
				img_id=0
				while True:
					ret,my_frame=capture.read()
					if face_cropped(my_frame) is not None:
						img_id+=1
						face=cv2.resize(face_cropped(my_frame),(450,450))
						face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
						File_Name_Path="Data/user."+str(id)+"."+str(img_id)+".jpg"
						cv2.imwrite(File_Name_Path,face)
						cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255,0),2)
						cv2.imshow("Crooped Face",face)

					if cv2.waitKey(1)==13 or int(img_id)==100:
						break
				capture.release()
				cv2.destroyAllWindows()
				messagebox.showinfo("Result","Generating data sets compled !")
			except Exception as es:
					messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)






if __name__ == "__main__":
	root=Tk()
	obj=Student(root)
	root.mainloop()