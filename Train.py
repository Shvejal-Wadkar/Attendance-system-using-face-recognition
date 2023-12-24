from tkinter import *
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
	def __init__(self,root):
		self.root=root
		self.root.geometry("1360x700+0+0")
		self.root.title("Train Data")


#====== First Title ========================================================================================================
		lbl_Title=Label(self.root,text="Photo Sample Training",font=("times new roman",30,"bold"),bg="white",fg="red")
		lbl_Title.place(x=0,y=0,width=1360,height=40)


#====== First Img ==========================================================================================================
		img1=Image.open(r"C:\Users\sejal\Desktop\Attendance_System\Images\Face.jpg")
		img1=img1.resize((1360,200),Image.ANTIALIAS)
		self.photoimg1=ImageTk.PhotoImage(img1)

		bg_img=Label(self.root,image=self.photoimg1)
		bg_img.place(x=0,y=40,width=1360,height=200)

#========= Button ============================================================================================================
		btn_TrainData=Button(self.root,text="TRAIN  DATA",command=self.Train_Classifier,cursor="hand2",font=("time new roman",30,"bold"),bg="red",fg="white")
		btn_TrainData.place(x=0,y=240,width=1360,height=50)

#======== second Img =========================================================================================================
		img2=Image.open(r"C:\Users\sejal\Desktop\Attendance_System\Images\Face6.jpg")
		img2=img2.resize((1360,590),Image.ANTIALIAS)
		self.photoimg2=ImageTk.PhotoImage(img2)

		bg_img=Label(self.root,image=self.photoimg2)
		bg_img.place(x=0,y=290,width=1360,height=590)


#====== Function ======================================================================================================================

	def Train_Classifier(self):
		data_dir=("Data")
		path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

		faces=[]
		ids=[]

		for image in path:
			img=Image.open(image).convert('L')             # Gray scale image
			imageNp=np.array(img,'uint8')
			id=int(os.path.split(image)[1].split('.')[1])

			faces.append(imageNp)
			ids.append(id)
			cv2.imshow("Training",imageNp)
			cv2.waitKey(1)==13

		ids=np.array(ids)

	#========== Train the classifier And save ================
		clf=cv2.face.LBPHFaceRecognizer_create()
		clf.train(faces,ids)
		clf.write("classifier.xml")
		cv2.destroyAllWindows()
		messagebox.showinfo("Result","Training Datasets Completed")



if __name__ == "__main__":
	root=Tk()
	obj=Train(root)
	root.mainloop()