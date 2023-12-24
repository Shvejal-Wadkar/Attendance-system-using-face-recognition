from tkinter import *
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np



class face_recognition:
	def __init__(self,root):
		self.root=root
		self.root.geometry("1360x700+0+0")
		self.root.title("Face Recognition")


#======= First Title ==============================================================================================
		lbl_Title=Label(self.root,text="FACE  RECOGNITION",font=("times new roman",30,"bold"),fg="blue")
		lbl_Title.place(x=0,y=0,width=1360,height=40)


#======= First Image ===========================================================================================
		img1=Image.open(r"C:\Users\sejal\Desktop\Attendance_System\Images\Face_Reconition1.png")
		img1=img1.resize((600,660),Image.ANTIALIAS)
		self.photoimg1=ImageTk.PhotoImage(img1)

		bg_img=Label(self.root,image=self.photoimg1)
		bg_img.place(x=0,y=40,width=600,height=660)


#======= Second Image ============================================================================================================

		img2=Image.open(r"C:\Users\sejal\Desktop\Attendance_System\Images\Face_Reconition.png")
		img2=img2.resize((760,660),Image.ANTIALIAS)
		self.photoimg2=ImageTk.PhotoImage(img2)

		bg_img=Label(self.root,image=self.photoimg2)
		bg_img.place(x=600,y=40,width=760,height=660)

#========= Button ============================================================================================================
		btn_TrainData=Button(self.root,text="face Fecognition",command=self.face_recognition,cursor="hand2",font=("time new roman",15,"bold"),bg="green",fg="white")
		btn_TrainData.place(x=880,y=630,width=200,height=30)



#====== Attendance Function and csv,excel file =======================================================================================
	def mark_attendance(self,i,r,n,d):
		with open("sejal.csv","r+",newline="\n") as f:
			myDataList=f.readlines()
			name_list=[]
			for line in myDataList:
				entry=line.split((","))
				name_list.append(entry[0])
			if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
				now=datetime.now()
				d1=now.strftime("%d/%m/%Y")
				dtString=now.strftime("%H:%M:%S")
				f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")


#======== Function ==================================================================================================================

	def face_recognition(self):
		def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
			gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
			features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

			coord=[]

			for (x,y,w,h) in features:
				cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
				id,predict=clf.predict(gray_image[y:y+h,x:x+w])
				confidence=int((100*(1-predict/300)))


		#===== Data Base Create ======================================
				conn=mysql.connector.connect(host="localhost",username="root",password="Sejal@1999",database="attendance_system")
				my_Cursor=conn.cursor()

				my_Cursor.execute("select Student_name from student where id="+str(id))
				n=my_Cursor.fetchone()
				n="+".join(n)

				my_Cursor.execute("select roll from student where id="+str(id))
				r=my_Cursor.fetchone()
				r="+".join(r)

				my_Cursor.execute("select dep from student where id="+str(id))
				d=my_Cursor.fetchone()
				d="+".join(d)

				my_Cursor.execute("select id from student where id="+str(id))
				i=my_Cursor.fetchone()
				i="+".join(i)


				if confidence>77:
					cv2.putText(img,f"id: {i}",(x,y-125),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
					cv2.putText(img,f"Student Name: {n}",(x,y-95),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
					cv2.putText(img,f"Roll: {r}",(x,y-65),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
					cv2.putText(img,f"dep: {d}",(x,y-35),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,0,0),3)
					self.mark_attendance(i,r,n,d)

				else:
					cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
					cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

				coord=[x,y,w,y]
			return coord


		def recognize(img,clf,faceCascade):
			coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
			return img

		faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
		clf=cv2.face.LBPHFaceRecognizer_create()
		clf.read("classifier.xml")

		video_cap=cv2.VideoCapture(0)

		while True:
			ret,img=video_cap.read()
			img=recognize(img,clf,faceCascade)
			cv2.imshow("Wecome To Face Recognition",img)

			if cv2.waitKey(1)==13:
				break
		video_cap.release()
		cv2.destroyAllWindows()





if __name__ == "__main__":
	root=Tk()
	obj=face_recognition(root)
	root.mainloop()