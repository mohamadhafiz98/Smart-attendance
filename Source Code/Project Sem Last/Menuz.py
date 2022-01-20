import os
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from Studentz import student
from Trainz import Train
from Face_recognitionz import Face_recognition
from Attendancez import Attendance

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        #image besar
        img4=Image.open(r"C:\Users\hafiz\THE CODE\Project redesign\clg_img\img\backg.png")
        img4=img4.resize((1530,790),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(width=1530, height=790)

        #tajuk
        title_lbl=Label(self.root,text="FACE RECOGNITION ATTENDANCE SYSTEM" ,font=("Arial",35,"bold"),fg="Black")        
        title_lbl.place(width=1530,height=45)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details, cursor="hand2",font=("Arial",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=550,y=100,width=400,height=60)

        b1_1=Button(bg_img,text="Take Attendance", cursor="hand2",command=self.face_data,font=("Arial",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=550,y=200,width=400,height=60)

        b1_1=Button(bg_img,text="Attendance Details", cursor="hand2",command=self.attendance_data,font=("Arial",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=550,y=300,width=400,height=60)

        b1_1=Button(bg_img,text="Train Image", cursor="hand2",command=self.train_data,font=("Arial",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=550,y=400,width=400,height=60)

        b1_1=Button(bg_img,text="Photo", cursor="hand2",command=self.open_img, font=("Arial",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=550,y=500,width=400,height=60)

        b1_1=Button(bg_img,text="Exit",command=self.return_login, cursor="hand2",font=("Arial",15,"bold"),bg="blue",fg="white")
        b1_1.place(x=550,y=600,width=400,height=60)


    def open_img(self):
        os.startfile("data")


#fuctions button
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def return_login(self):
        self.root.destroy()


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()